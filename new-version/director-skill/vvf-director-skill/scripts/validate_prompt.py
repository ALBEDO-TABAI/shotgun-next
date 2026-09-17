#!/usr/bin/env python3
"""检查生成提示词的结构：字段、镜头编号、句柄声明与数量、字数与占比。只查结构，不评价创作。

用法：
  python3 scripts/validate_prompt.py prompt.txt
  python3 scripts/validate_prompt.py prompt.txt --max-chars 1500 --per-shot --max-handles 3
  python3 scripts/validate_prompt.py prompt.txt --shot-fields "画面：,机位与运动：,动作：,出口状态：" \
      --global-fields "[空间布局],[全局风格]" --handle-pattern "@image\\d+"

默认硬字段是骨架字段的子集：画面、机位与运动、动作、出口状态；表演为软字段（缺失只警告）；其余骨架字段按需。
--max-chars 默认 0 表示不限制，只报告字数；--per-shot 按“资产 + 空间布局 + 该镜 + 全局风格”计算每个单元的提交量，
适用于逐单元调用的工具。上限与参考数量都是带日期的当期参数，由命令行传入。退出码 1 表示有错误；警告不影响退出码。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_SHOT_FIELDS = "画面：,机位与运动：,动作：,出口状态："
DEFAULT_SOFT_SHOT_FIELDS = "表演："
DEFAULT_GLOBAL_FIELDS = "[空间布局],[全局风格]"
DEFAULT_SHOT_PATTERN = r"【镜头(\d+)】"
DEFAULT_TOTAL_PATTERN = r"镜头总数[：:]\s*(\d+)"
DEFAULT_HANDLE_PATTERN = r"@image\d+"
# 只提示，不判错：这些词本身不描述可执行的画面关系。
VAGUE_WORDS = ("电影感", "高级感", "史诗感", "大片感", "8K", "4K画质")


def strip_fence(text: str) -> str:
    stripped = text.strip()
    match = re.match(r"\A```[a-zA-Z]*\n(.*)\n```\Z", stripped, re.S)
    return match.group(1).strip() if match else stripped


def effective_chars(text: str) -> int:
    return sum(1 for ch in text if not ch.isspace())


def split_list(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("prompt_file", type=Path)
    parser.add_argument("--max-chars", type=int, default=0, help="非空白字符上限；0 表示只报告不限制")
    parser.add_argument("--per-shot", action="store_true", help="按每个单元的提交量（资产+空间+该镜+全局）检查上限")
    parser.add_argument("--max-handles", type=int, default=0, help="参考句柄数量上限；0 表示不限制")
    parser.add_argument("--shot-fields", default=DEFAULT_SHOT_FIELDS, help="每镜必含字段，逗号分隔")
    parser.add_argument("--soft-shot-fields", default=DEFAULT_SOFT_SHOT_FIELDS, help="每镜缺失时只警告的字段")
    parser.add_argument("--global-fields", default=DEFAULT_GLOBAL_FIELDS, help="全局必含字段，逗号分隔")
    parser.add_argument("--shot-pattern", default=DEFAULT_SHOT_PATTERN, help="镜头标题正则，含一个数字分组")
    parser.add_argument("--total-pattern", default=DEFAULT_TOTAL_PATTERN, help="镜头总数声明正则，可选")
    parser.add_argument("--handle-pattern", default=DEFAULT_HANDLE_PATTERN, help="参考句柄正则；空字符串跳过检查")
    parser.add_argument("--preamble-warn", type=float, default=0.25, help="资产与空间占比超过此值时警告")
    parser.add_argument("--shot-warn", type=float, default=0.55, help="逐镜内容占比低于此值时警告")
    args = parser.parse_args()

    try:
        prompt = strip_fence(args.prompt_file.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        print(f"INVALID: 无法读取 UTF-8 文件: {exc}", file=sys.stderr)
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    count = effective_chars(prompt)

    if not prompt:
        errors.append("提示词为空")
    if args.max_chars and not args.per_shot and count > args.max_chars:
        errors.append(f"整包非空白字符 {count}，超过本次上限 {args.max_chars}")

    for marker in split_list(args.global_fields):
        if marker not in prompt:
            errors.append(f"缺少全局字段: {marker}")

    shot_re = re.compile(args.shot_pattern)
    matches = list(shot_re.finditer(prompt))
    numbers = [int(m.group(1)) for m in matches]
    declared_handles: set[str] = set()
    if not numbers:
        errors.append("未找到镜头标题；检查 --shot-pattern")
    else:
        if numbers != list(range(1, len(numbers) + 1)):
            errors.append(f"镜头编号必须从 1 连续且不重复，当前为 {numbers}")
        if args.total_pattern:
            declared = re.search(args.total_pattern, prompt)
            if declared and int(declared.group(1)) != len(numbers):
                errors.append(f"声明 {declared.group(1)} 镜，实际 {len(numbers)} 镜")

        first = matches[0].start()
        preamble = prompt[:first]
        handle_re = re.compile(args.handle_pattern) if args.handle_pattern else None
        if handle_re:
            declared_handles = set(handle_re.findall(preamble))
            if args.max_handles and len(declared_handles) > args.max_handles:
                errors.append(f"已声明 {len(declared_handles)} 个句柄，超过本次上限 {args.max_handles}")

        global_start = None
        for marker in split_list(args.global_fields):
            pos = prompt.find(marker, first)
            if pos >= 0 and (global_start is None or pos < global_start):
                global_start = pos
        shot_end = global_start if global_start is not None else len(prompt)
        global_text = prompt[global_start:] if global_start is not None else ""

        hard_fields = split_list(args.shot_fields)
        soft_fields = split_list(args.soft_shot_fields)
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else shot_end
            block = prompt[match.start():end]
            label = f"镜头{numbers[index]}"
            for field in hard_fields:
                if field not in block:
                    errors.append(f"{label}缺少字段: {field}")
            for field in soft_fields:
                if field not in block:
                    warnings.append(f"{label}没有字段 {field}；无人物时可写“{field}无人物”")
            if handle_re:
                for handle in sorted(set(handle_re.findall(block)) - declared_handles):
                    errors.append(f"{label}引用了未在参考资产中声明的句柄 {handle}")
            if args.per_shot:
                submission = effective_chars(preamble) + effective_chars(block) + effective_chars(global_text)
                note = f"{label} 单独提交量 {submission}"
                if args.max_chars and submission > args.max_chars:
                    errors.append(f"{note}，超过本次上限 {args.max_chars}")
                else:
                    print(f"INFO: {note}")

        if count:
            preamble_ratio = effective_chars(preamble) / count
            shot_ratio = effective_chars(prompt[first:shot_end]) / count
            if preamble_ratio > args.preamble_warn:
                warnings.append(f"资产与空间占整包 {preamble_ratio:.0%}，通常可再压缩")
            if shot_ratio < args.shot_warn:
                warnings.append(f"逐镜内容占整包 {shot_ratio:.0%}，通常应把更多字数留给镜头")

    for word in VAGUE_WORDS:
        if word in prompt:
            warnings.append(f"出现“{word}”：它不描述可执行的画面关系，确认是否已落成具体条件")

    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"INVALID: {error}", file=sys.stderr)
        return 1

    limit = f"/{args.max_chars}" if args.max_chars else "（本次未设上限）"
    mode = "逐单元" if args.per_shot else "整包"
    print(f"VALID: {mode}检查；整包 {count}{limit} 非空白字符；{len(numbers)} 镜；{len(declared_handles)} 个已声明句柄")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
