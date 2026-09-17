# Generated Protocol Reference

Static declarations and actual handler branches from the pinned bundle. Parameter names below are direct `p.field` reads, not complete schemas; helper validation and defaults remain authoritative in the linked handler. Availability may depend on feature flags and supplied dependencies.

Declared methods: **232**; handler cases: **232**; declared events: **41**.

| Method | Handler | Direct parameter reads (partial) |
|---|---|---|
| `workspace.list` | [L103706](../extracted/neo-agent.fmt.js#L103706) |  |
| `workspace.create` | [L103737](../extracted/neo-agent.fmt.js#L103737) | `cyberpunkAddress`, `description`, `emailAddress`, `emailAddressSuggestion`, `focusDomainSlugs`, `integrationSlugs`, `name`, `onboardingObjective`, `preferredWorkerRuntimes`, `workspacePurpose`, `worldTemplate` |
| `workspace.onboardingDraft.create` | [L103773](../extracted/neo-agent.fmt.js#L103773) | `cyberpunkAddress`, `departments`, `emailAddress`, `emailAddressSuggestion`, `focusDomainSlugs`, `inputFingerprint`, `integrationSlugs`, `name`, `onboardingObjective`, `preferredWorkerRuntimes`, `revision`, `workspacePurpose`, `worldTemplate` |
| `workspace.onboardingDraft.update` | [L103858](../extracted/neo-agent.fmt.js#L103858) | `id`, `inputFingerprint`, `worldTemplate` |
| `workspace.onboardingDraft.finalize` | [L103875](../extracted/neo-agent.fmt.js#L103875) | `cyberpunkAddress`, `departments`, `emailAddress`, `emailAddressSuggestion`, `focusDomainSlugs`, `id`, `inputFingerprint`, `integrationSlugs`, `name`, `onboardingObjective`, `preferredWorkerRuntimes`, `responseLanguage`, `workspacePurpose`, `worldTemplate` |
| `workspace.onboardingDraft.discard` | [L103991](../extracted/neo-agent.fmt.js#L103991) | `id`, `inputFingerprint` |
| `workspace.runtimeOnboarding.apply` | [L103944](../extracted/neo-agent.fmt.js#L103944) | `cyberpunkAddress`, `departments`, `description`, `emailAddress`, `emailAddressSuggestion`, `focusDomainSlugs`, `integrationSlugs`, `name`, `onboardingObjective`, `preferredWorkerRuntimes`, `responseLanguage`, `workspacePurpose`, `worldTemplate` |
| `workspace.blueprint.suggestOptions` | [L103823](../extracted/neo-agent.fmt.js#L103823) | `companyAttributes`, `departments`, `existingDraft`, `generationMode`, `locale`, `selectedName`, `sessionId`, `stage`, `vision`, `workspace` |
| `workspace.switch` | [L103723](../extracted/neo-agent.fmt.js#L103723) | `id` |
| `workspace.rename` | [L104019](../extracted/neo-agent.fmt.js#L104019) | `id`, `name` |
| `workspace.delete` | [L104031](../extracted/neo-agent.fmt.js#L104031) | `id`, `permanent` |
| `workspace.restore` | [L104052](../extracted/neo-agent.fmt.js#L104052) | `id` |
| `workspace.prepareAcquisitionHandover` | [L104064](../extracted/neo-agent.fmt.js#L104064) | `acquisition`, `waitForDepartmentWelcome`, `waitForPrimaryWelcome` |
| `workspace.dispatchOnboardingOpening` | [L104097](../extracted/neo-agent.fmt.js#L104097) | `department`, `force`, `sessionId` |
| `workspace.activationChecklist.get` | [L104112](../extracted/neo-agent.fmt.js#L104112) |  |
| `workspace.activationChecklist.completeTask` | [L104115](../extracted/neo-agent.fmt.js#L104115) | `taskId` |
| `workspace.activationChecklist.markEmailGreetingSent` | [L104130](../extracted/neo-agent.fmt.js#L104130) |  |
| `workspace.email.get` | [L104133](../extracted/neo-agent.fmt.js#L104133) |  |
| `workspace.email.set` | [L104138](../extracted/neo-agent.fmt.js#L104138) | `address` |
| `wallet.link.get` | [L104147](../extracted/neo-agent.fmt.js#L104147) |  |
| `wallet.link.configure` | [L104151](../extracted/neo-agent.fmt.js#L104151) | `clientName` |
| `social.accounts.list` | [L104163](../extracted/neo-agent.fmt.js#L104163) |  |
| `social.account.connect` | [L104173](../extracted/neo-agent.fmt.js#L104173) | `provider` |
| `social.account.remove` | [L104190](../extracted/neo-agent.fmt.js#L104190) |  |
| `composio.installs.list` | [L104193](../extracted/neo-agent.fmt.js#L104193) |  |
| `composio.installs.upsert` | [L104196](../extracted/neo-agent.fmt.js#L104196) | `record` |
| `composio.installs.patch` | [L104213](../extracted/neo-agent.fmt.js#L104213) | `groupId`, `patch` |
| `composio.installs.remove` | [L104230](../extracted/neo-agent.fmt.js#L104230) | `groupId` |
| `matrixBrowser.userProfileProcess.open` | [L104246](../extracted/neo-agent.fmt.js#L104246) | `url` |
| `workspace.fs.list` | [L104253](../extracted/neo-agent.fmt.js#L104253) | `path` |
| `workspace.fs.search` | [L104325](../extracted/neo-agent.fmt.js#L104325) | `department`, `limit`, `query` |
| `workspace.fs.metadata` | [L104347](../extracted/neo-agent.fmt.js#L104347) | `fileID`, `path` |
| `workspace.fs.departmentAssociations` | [L104366](../extracted/neo-agent.fmt.js#L104366) | `fileID`, `path` |
| `workspace.fs.departmentAssociations.confirm` | [L104391](../extracted/neo-agent.fmt.js#L104391) | `departmentID`, `fileID` |
| `workspace.fs.summaries` | [L104414](../extracted/neo-agent.fmt.js#L104414) | `paths`, `relatedWorkDepartmentID` |
| `workspace.fs.collaboration.list` | [L104441](../extracted/neo-agent.fmt.js#L104441) | `cursor`, `limit`, `projection` |
| `workspace.fs.history` | [L104541](../extracted/neo-agent.fmt.js#L104541) | `cursor`, `fileID`, `limit`, `path` |
| `workspace.fs.access` | [L104570](../extracted/neo-agent.fmt.js#L104570) | `fileID`, `limit`, `path` |
| `workspace.fs.access.record` | [L104597](../extracted/neo-agent.fmt.js#L104597) | `_localActor`, `accessID`, `accessType`, `path`, `source` |
| `workspace.fs.lineage` | [L104626](../extracted/neo-agent.fmt.js#L104626) | `fileID`, `limit`, `path` |
| `workspace.fs.revision.diff` | [L104801](../extracted/neo-agent.fmt.js#L104801) | `afterRevisionID`, `beforeRevisionID`, `fileID` |
| `workspace.fs.revision.restore` | [L104831](../extracted/neo-agent.fmt.js#L104831) | `_localActor`, `expectedCurrentRevisionID`, `fileID`, `operationID`, `revisionID`, `source` |
| `workspace.fs.revision.pins` | [L104653](../extracted/neo-agent.fmt.js#L104653) | `fileID`, `includeRemoved`, `revisionID` |
| `workspace.fs.revision.pin` | [L104679](../extracted/neo-agent.fmt.js#L104679) | `_localActor`, `fileID`, `kind`, `label`, `pinID`, `referenceID`, `revisionID`, `source` |
| `workspace.fs.revision.unpin` | [L104712](../extracted/neo-agent.fmt.js#L104712) | `_localActor`, `pinID`, `source` |
| `workspace.fs.directory.pins` | [L104733](../extracted/neo-agent.fmt.js#L104733) | `directoryID`, `includeRemoved` |
| `workspace.fs.directory.pin` | [L104757](../extracted/neo-agent.fmt.js#L104757) | `_localActor`, `path`, `pinID`, `source` |
| `workspace.fs.directory.unpin` | [L104780](../extracted/neo-agent.fmt.js#L104780) | `_localActor`, `pinID`, `source` |
| `workspace.fs.workerConflicts` | [L104868](../extracted/neo-agent.fmt.js#L104868) | `includeResolved` |
| `workspace.fs.workerConflicts.resolve` | [L104879](../extracted/neo-agent.fmt.js#L104879) | `_localActor`, `conflictID`, `operationID`, `resolution`, `source` |
| `department.list` | [L105781](../extracted/neo-agent.fmt.js#L105781) | `mode` |
| `department.message.thread` | [L105830](../extracted/neo-agent.fmt.js#L105830) | `includeBodyFor`, `messageId` |
| `department.status` | [L105859](../extracted/neo-agent.fmt.js#L105859) | `department` |
| `department.activity` | [L105877](../extracted/neo-agent.fmt.js#L105877) |  |
| `department.create` | [L105941](../extracted/neo-agent.fmt.js#L105941) | `coordinator`, `description`, `id`, `model`, `name`, `parentDepartmentId`, `profile` |
| `department.rename` | [L105991](../extracted/neo-agent.fmt.js#L105991) | `department`, `name` |
| `department.delete` | [L105973](../extracted/neo-agent.fmt.js#L105973) | `department` |
| `department.prepareMarketplaceHandoff` | [L105929](../extracted/neo-agent.fmt.js#L105929) | `department` |
| `department.skills.refresh` | [L105935](../extracted/neo-agent.fmt.js#L105935) | `department` |
| `department.config.get` | [L106009](../extracted/neo-agent.fmt.js#L106009) | `department` |
| `department.config.update` | [L106029](../extracted/neo-agent.fmt.js#L106029) | `config`, `department`, `model`, `updates` |
| `okr.store.get` | [L106190](../extracted/neo-agent.fmt.js#L106190) |  |
| `okr.store.update` | [L106197](../extracted/neo-agent.fmt.js#L106197) | `departmentId`, `scope`, `store` |
| `objective.create` | [L106227](../extracted/neo-agent.fmt.js#L106227) | `objective` |
| `objective.update` | [L106247](../extracted/neo-agent.fmt.js#L106247) | `objective`, `objectiveId` |
| `objective.delete` | [L106274](../extracted/neo-agent.fmt.js#L106274) | `objectiveId` |
| `objective.state.patch` | [L106294](../extracted/neo-agent.fmt.js#L106294) | `objectiveId`, `patch` |
| `key_result.create` | [L106321](../extracted/neo-agent.fmt.js#L106321) | `keyResult` |
| `key_result.update` | [L106341](../extracted/neo-agent.fmt.js#L106341) | `keyResult`, `keyResultId` |
| `key_result.delete` | [L106368](../extracted/neo-agent.fmt.js#L106368) | `keyResultId` |
| `key_result.state.patch` | [L106388](../extracted/neo-agent.fmt.js#L106388) | `keyResultId`, `patch` |
| `okr_task.list` | [L106416](../extracted/neo-agent.fmt.js#L106416) | `department` |
| `okr_task.upsert` | [L106419](../extracted/neo-agent.fmt.js#L106419) | `department`, `task` |
| `okr_task.check_in` | [L106422](../extracted/neo-agent.fmt.js#L106422) | `checkIn`, `department`, `taskId` |
| `dashboard.config.get` | [L106425](../extracted/neo-agent.fmt.js#L106425) |  |
| `dashboard.config.update` | [L106430](../extracted/neo-agent.fmt.js#L106430) | `enabled`, `focus`, `frequency` |
| `dashboard.refresh.run` | [L106456](../extracted/neo-agent.fmt.js#L106456) |  |
| `media.characterAsset.register` | [L106465](../extracted/neo-agent.fmt.js#L106465) | `assetUri`, `description`, `imagePath`, `imageUrl`, `name` |
| `skill.list` | [L108980](../extracted/neo-agent.fmt.js#L108980) | `department` |
| `skill.create` | [L109005](../extracted/neo-agent.fmt.js#L109005) | `category`, `content`, `department`, `description`, `files`, `name`, `symbolName`, `tagline` |
| `skill.delete` | [L109051](../extracted/neo-agent.fmt.js#L109051) | `department`, `skill` |
| `skill.file.write` | [L109070](../extracted/neo-agent.fmt.js#L109070) | `content`, `department`, `path`, `skill` |
| `skill.file.delete` | [L109093](../extracted/neo-agent.fmt.js#L109093) | `department`, `path`, `skill` |
| `memory.list` | [L109456](../extracted/neo-agent.fmt.js#L109456) | `department` |
| `userProfile.get` | [L103614](../extracted/neo-agent.fmt.js#L103614) |  |
| `userProfile.update` | [L103617](../extracted/neo-agent.fmt.js#L103617) | `content`, `expectedVersion` |
| `userProfile.discover` | [L103635](../extracted/neo-agent.fmt.js#L103635) | `includeBrowserHistory`, `previewOnly`, `requestId` |
| `userProfile.discovery.cancel` | [L103690](../extracted/neo-agent.fmt.js#L103690) | `requestId` |
| `chat.send` | [L106920](../extracted/neo-agent.fmt.js#L106920) | `attachments`, `department`, `requestId`, `sessionId`, `text` |
| `chat.rerun` | [L107128](../extracted/neo-agent.fmt.js#L107128) | `attachments`, `department`, `requestId`, `sessionId`, `targetChatId`, `targetHistoryId`, `targetRequestId`, `text` |
| `chat.abort` | [L107196](../extracted/neo-agent.fmt.js#L107196) | `chatId`, `clearPending`, `department`, `requestId`, `sessionId` |
| `chat.queue.resume` | [L107216](../extracted/neo-agent.fmt.js#L107216) | `department`, `sessionId` |
| `chat.queue.retry` | [L107231](../extracted/neo-agent.fmt.js#L107231) | `department`, `sessionId` |
| `chat.queue.steer` | [L107248](../extracted/neo-agent.fmt.js#L107248) | `department`, `requestId`, `sessionId` |
| `chat.queue.cancel` | [L107278](../extracted/neo-agent.fmt.js#L107278) | `department`, `requestId`, `sessionId` |
| `chat.queue.clear` | [L107303](../extracted/neo-agent.fmt.js#L107303) | `department`, `sessionId` |
| `chat.history` | [L107429](../extracted/neo-agent.fmt.js#L107429) | `after`, `around`, `before`, `department`, `forceHydrate`, `limit`, `sessionId` |
| `chat.search` | [L107475](../extracted/neo-agent.fmt.js#L107475) | `department`, `limit`, `query`, `sessionId` |
| `transcript.explain` | [L107532](../extracted/neo-agent.fmt.js#L107532) | `department`, `sessionId` |
| `chat.bootstrap` | [L107318](../extracted/neo-agent.fmt.js#L107318) | `department`, `endpoint`, `forceHydrate`, `limit`, `prewarm`, `returnCurrentSnapshotOnHydrationTimeout`, `sessionId` |
| `chat.live_state` | [L107561](../extracted/neo-agent.fmt.js#L107561) | `department`, `sessionId` |
| `chat.reply_mode.get` | [L107581](../extracted/neo-agent.fmt.js#L107581) |  |
| `chat.reply_mode.set` | [L107590](../extracted/neo-agent.fmt.js#L107590) | `replyMode` |
| `chat.endpoint.ack` | [L107609](../extracted/neo-agent.fmt.js#L107609) | `department`, `endpoint`, `endpointId`, `seq` |
| `chat.endpoints` | [L107600](../extracted/neo-agent.fmt.js#L107600) | `department` |
| `wechat.status` | [L106503](../extracted/neo-agent.fmt.js#L106503) |  |
| `wechat.configure` | [L106507](../extracted/neo-agent.fmt.js#L106507) |  |
| `wechat.connect` | [L106513](../extracted/neo-agent.fmt.js#L106513) |  |
| `wechat.stop` | [L106519](../extracted/neo-agent.fmt.js#L106519) |  |
| `wechat.sign_out` | [L106523](../extracted/neo-agent.fmt.js#L106523) |  |
| `telegram.status` | [L106527](../extracted/neo-agent.fmt.js#L106527) |  |
| `telegram.configure` | [L106531](../extracted/neo-agent.fmt.js#L106531) |  |
| `telegram.connect` | [L106535](../extracted/neo-agent.fmt.js#L106535) |  |
| `telegram.stop` | [L106539](../extracted/neo-agent.fmt.js#L106539) |  |
| `telegram.sign_out` | [L106543](../extracted/neo-agent.fmt.js#L106543) |  |
| `session.create` | [L106559](../extracted/neo-agent.fmt.js#L106559) | `canonical`, `department`, `endpoint`, `sessionId` |
| `session.list` | [L106547](../extracted/neo-agent.fmt.js#L106547) | `department` |
| `session.attach` | [L106602](../extracted/neo-agent.fmt.js#L106602) | `endpoint`, `sessionId` |
| `session.detach` | [L106639](../extracted/neo-agent.fmt.js#L106639) | `sessionId` |
| `session.close` | [L106677](../extracted/neo-agent.fmt.js#L106677) | `sessionId` |
| `session.send` | [L106690](../extracted/neo-agent.fmt.js#L106690) | `attachments`, `requestId`, `sessionId`, `text` |
| `session.interrupt` | [L106771](../extracted/neo-agent.fmt.js#L106771) | `clearPending`, `sessionId` |
| `session.history` | [L106784](../extracted/neo-agent.fmt.js#L106784) | `before`, `limit`, `sessionId` |
| `session.live` | [L106794](../extracted/neo-agent.fmt.js#L106794) | `sessionId` |
| `session.models.list` | [L106807](../extracted/neo-agent.fmt.js#L106807) | `refresh`, `sessionId` |
| `session.set_model` | [L106819](../extracted/neo-agent.fmt.js#L106819) | `expectedRevision`, `model`, `provider`, `reasoningEffort`, `serviceTier`, `sessionId` |
| `session.refresh` | [L106879](../extracted/neo-agent.fmt.js#L106879) | `sessionId` |
| `session.context` | [L106903](../extracted/neo-agent.fmt.js#L106903) | `sessionId` |
| `session.cache_stats` | [L106912](../extracted/neo-agent.fmt.js#L106912) | `sessionId` |
| `session.toggle_plan_mode` | [L106893](../extracted/neo-agent.fmt.js#L106893) | `enabled`, `sessionId` |
| `task.list` | [L107631](../extracted/neo-agent.fmt.js#L107631) | `department` |
| `task.stop` | [L107702](../extracted/neo-agent.fmt.js#L107702) | `department`, `sessionId`, `taskId` |
| `task.interrupt` | [L107832](../extracted/neo-agent.fmt.js#L107832) | `department`, `sessionId` |
| `task.steer` | [L107858](../extracted/neo-agent.fmt.js#L107858) | `department`, `sessionId`, `taskId`, `text` |
| `task.messages` | [L108284](../extracted/neo-agent.fmt.js#L108284) | `department`, `taskId` |
| `task.detail` | [L108316](../extracted/neo-agent.fmt.js#L108316) | `department`, `includeTranscript`, `taskId` |
| `task.permission.respond` | [L108259](../extracted/neo-agent.fmt.js#L108259) | `decision`, `reason`, `taskId`, `toolUseId`, `updatedInput` |
| `pool.metrics` | [L108357](../extracted/neo-agent.fmt.js#L108357) | `department` |
| `runtime.stream.list` | [L108395](../extracted/neo-agent.fmt.js#L108395) |  |
| `runtime.stream.events` | [L108399](../extracted/neo-agent.fmt.js#L108399) | `afterSeq`, `limit`, `streamId`, `tail` |
| `config.providers.list` | [L108408](../extracted/neo-agent.fmt.js#L108408) |  |
| `config.providers.get` | [L108421](../extracted/neo-agent.fmt.js#L108421) |  |
| `config.providers.set` | [L108429](../extracted/neo-agent.fmt.js#L108429) |  |
| `config.providers.openrouter.models.search` | [L108443](../extracted/neo-agent.fmt.js#L108443) | `apiKey`, `baseUrl`, `limit`, `query` |
| `config.providers.delete` | [L108457](../extracted/neo-agent.fmt.js#L108457) |  |
| `config.providers.set_active` | [L108466](../extracted/neo-agent.fmt.js#L108466) |  |
| `config.providers.oauth.start` | [L108482](../extracted/neo-agent.fmt.js#L108482) |  |
| `config.providers.oauth.complete` | [L108495](../extracted/neo-agent.fmt.js#L108495) |  |
| `config.providers.oauth.sign_out` | [L108540](../extracted/neo-agent.fmt.js#L108540) |  |
| `config.test_connection` | [L108564](../extracted/neo-agent.fmt.js#L108564) | `credential`, `provider` |
| `codex.service.status` | [L108586](../extracted/neo-agent.fmt.js#L108586) |  |
| `codex.service.login.start` | [L108593](../extracted/neo-agent.fmt.js#L108593) |  |
| `codex.service.login.cancel` | [L108603](../extracted/neo-agent.fmt.js#L108603) |  |
| `codex.service.connect` | [L108614](../extracted/neo-agent.fmt.js#L108614) | `activateDefault` |
| `codex.service.import_user_default` | [L108648](../extracted/neo-agent.fmt.js#L108648) | `activateDefault` |
| `codex.service.disconnect` | [L108672](../extracted/neo-agent.fmt.js#L108672) |  |
| `codex.service.sign_out` | [L108702](../extracted/neo-agent.fmt.js#L108702) |  |
| `runtime.capabilities` | [L105612](../extracted/neo-agent.fmt.js#L105612) |  |
| `runtime.integrations.refresh` | [L105615](../extracted/neo-agent.fmt.js#L105615) |  |
| `runtime.list` | [L108726](../extracted/neo-agent.fmt.js#L108726) |  |
| `runtime.worker_models.list` | [L108731](../extracted/neo-agent.fmt.js#L108731) | `sessionId` |
| `runtime.install` | [L108746](../extracted/neo-agent.fmt.js#L108746) | `kind` |
| `runtime.cancel_install` | [L108755](../extracted/neo-agent.fmt.js#L108755) | `kind` |
| `runtime.uninstall` | [L108764](../extracted/neo-agent.fmt.js#L108764) | `kind` |
| `runtime.set_billing` | [L108773](../extracted/neo-agent.fmt.js#L108773) | `billing`, `kind` |
| `runtime.set_model` | [L108784](../extracted/neo-agent.fmt.js#L108784) | `kind`, `modelId`, `provider` |
| `billing.activity` | [L108797](../extracted/neo-agent.fmt.js#L108797) | `limit`, `since`, `workspace` |
| `runtime.sign_in` | [L108809](../extracted/neo-agent.fmt.js#L108809) | `kind` |
| `runtime.sign_out` | [L108826](../extracted/neo-agent.fmt.js#L108826) | `kind` |
| `runtime.import_user_default_auth` | [L108837](../extracted/neo-agent.fmt.js#L108837) | `kind` |
| `runtime.sign_in.provide_code` | [L108852](../extracted/neo-agent.fmt.js#L108852) | `code`, `kind` |
| `runtime.sign_in.cancel` | [L108867](../extracted/neo-agent.fmt.js#L108867) | `kind` |
| `config.models.list` | [L108875](../extracted/neo-agent.fmt.js#L108875) | `refresh` |
| `config.models.set_enabled` | [L108886](../extracted/neo-agent.fmt.js#L108886) | `enabled`, `expectedRevision`, `modelId`, `provider` |
| `config.models.set_default` | [L108927](../extracted/neo-agent.fmt.js#L108927) | `expectedRevision`, `modelId`, `provider`, `updateExisting` |
| `cron.list` | [L109113](../extracted/neo-agent.fmt.js#L109113) | `department` |
| `cron.create` | [L109122](../extracted/neo-agent.fmt.js#L109122) | `activeHours`, `department`, `enabled`, `keyResultId`, `prompt`, `purpose`, `recurring`, `schedule`, `sourceRefs`, `taskId` |
| `cron.update` | [L109194](../extracted/neo-agent.fmt.js#L109194) | `activeHours`, `department`, `enabled`, `id`, `keyResultId`, `prompt`, `purpose`, `recurring`, `schedule`, `sourceRefs`, `taskId` |
| `cron.delete` | [L109285](../extracted/neo-agent.fmt.js#L109285) | `department`, `id` |
| `cron.history` | [L109308](../extracted/neo-agent.fmt.js#L109308) | `department`, `id`, `limit` |
| `cron.trigger` | [L109324](../extracted/neo-agent.fmt.js#L109324) | `department`, `force`, `id`, `prompt` |
| `hooks.list` | [L109388](../extracted/neo-agent.fmt.js#L109388) | `department` |
| `hooks.update` | [L109403](../extracted/neo-agent.fmt.js#L109403) | `department`, `hooks` |
| `hook.work.list` | [L109416](../extracted/neo-agent.fmt.js#L109416) | `activeOnly`, `department`, `limit` |
| `wake.history` | [L109340](../extracted/neo-agent.fmt.js#L109340) | `limit` |
| `nudge.decisions.list` | [L109347](../extracted/neo-agent.fmt.js#L109347) | `department`, `limit` |
| `focus.broadcast` | [L109368](../extracted/neo-agent.fmt.js#L109368) | `focusedDepartmentId` |
| `activity.broadcast` | [L109380](../extracted/neo-agent.fmt.js#L109380) | `lastActivityMs` |
| `workspace.fs.read` | [L104940](../extracted/neo-agent.fmt.js#L104940) | `_localActor`, `maxBytes`, `path`, `source` |
| `workspace.fs.preview` | [L104989](../extracted/neo-agent.fmt.js#L104989) | `path` |
| `workspace.fs.readBinary` | [L104961](../extracted/neo-agent.fmt.js#L104961) | `maxBytes`, `path` |
| `workspace.fs.write` | [L105009](../extracted/neo-agent.fmt.js#L105009) | `_localActor`, `content`, `create`, `expectedModifiedAt`, `path`, `source` |
| `workspace.fs.move` | [L105060](../extracted/neo-agent.fmt.js#L105060) | `_localActor`, `destinationPath`, `source`, `sourcePath` |
| `workspace.fs.copy` | [L105110](../extracted/neo-agent.fmt.js#L105110) | `_localActor`, `destinationPath`, `source`, `sourcePath` |
| `workspace.fs.batch` | [L105162](../extracted/neo-agent.fmt.js#L105162) | `_localActor`, `operations`, `source` |
| `workspace.fs.tag.add` | [L104905](../extracted/neo-agent.fmt.js#L104905) |  |
| `workspace.fs.tag.remove` | [L104906](../extracted/neo-agent.fmt.js#L104906) | `_localActor`, `operationID`, `path`, `source`, `tag` |
| `workspace.fs.trash.prepare` | [L105214](../extracted/neo-agent.fmt.js#L105214) | `_localActor`, `path`, `source` |
| `workspace.fs.trash.commit` | [L105234](../extracted/neo-agent.fmt.js#L105234) | `operationID`, `path` |
| `workspace.fs.trash.abort` | [L105276](../extracted/neo-agent.fmt.js#L105276) | `operationID`, `path`, `reason` |
| `workspace.fs.upload.begin` | [L105293](../extracted/neo-agent.fmt.js#L105293) | `_localActor`, `overwrite`, `path`, `size`, `source` |
| `workspace.fs.upload.chunk` | [L105351](../extracted/neo-agent.fmt.js#L105351) | `contentBase64`, `offset`, `uploadId` |
| `workspace.fs.upload.commit` | [L105380](../extracted/neo-agent.fmt.js#L105380) | `uploadId` |
| `workspace.fs.upload.abort` | [L105432](../extracted/neo-agent.fmt.js#L105432) | `uploadId` |
| `workspace.fs.importDirectory.begin` | [L105441](../extracted/neo-agent.fmt.js#L105441) | `_localActor`, `path`, `source` |
| `workspace.fs.importDirectory.chunk` | [L105517](../extracted/neo-agent.fmt.js#L105517) | `contentBase64`, `fileIndex`, `importId`, `offset` |
| `workspace.fs.importDirectory.commit` | [L105550](../extracted/neo-agent.fmt.js#L105550) | `importId` |
| `workspace.fs.importDirectory.abort` | [L105603](../extracted/neo-agent.fmt.js#L105603) | `importId` |
| `terminal.run` | [L105621](../extracted/neo-agent.fmt.js#L105621) | `command`, `cwd`, `department`, `timeoutMs` |
| `terminal.session.create` | [L105660](../extracted/neo-agent.fmt.js#L105660) | `args`, `cols`, `command`, `cwd`, `department`, `rows`, `title` |
| `terminal.session.list` | [L105698](../extracted/neo-agent.fmt.js#L105698) | `department` |
| `terminal.session.attach` | [L105706](../extracted/neo-agent.fmt.js#L105706) | `sessionId`, `sinceSeq` |
| `terminal.session.input` | [L105726](../extracted/neo-agent.fmt.js#L105726) | `dataBase64`, `sessionId` |
| `terminal.session.resize` | [L105740](../extracted/neo-agent.fmt.js#L105740) | `cols`, `rows`, `sessionId` |
| `terminal.session.close` | [L105761](../extracted/neo-agent.fmt.js#L105761) | `sessionId`, `signal` |
| `trace.list` | [L109528](../extracted/neo-agent.fmt.js#L109528) | `department`, `limit` |
| `maintenance.config.get` | [L109539](../extracted/neo-agent.fmt.js#L109539) |  |
| `maintenance.config.update` | [L109544](../extracted/neo-agent.fmt.js#L109544) | `crystallize` |
| `maintenance.trigger` | [L109574](../extracted/neo-agent.fmt.js#L109574) | `action`, `department`, `departmentId` |
| `ping` | [L109603](../extracted/neo-agent.fmt.js#L109603) |  |
| `sync.status` | [L109605](../extracted/neo-agent.fmt.js#L109605) |  |
| `bench.mail.inject` | [L106132](../extracted/neo-agent.fmt.js#L106132) | `benchVMs`, `body`, `department`, `from`, `subject` |
| `bench.nudge.tick` | [L106153](../extracted/neo-agent.fmt.js#L106153) | `department`, `kind` |
| `bench.cron.trigger` | [L106173](../extracted/neo-agent.fmt.js#L106173) | `department`, `id` |
| `sync.push` | [L109623](../extracted/neo-agent.fmt.js#L109623) |  |
| `sync.pull` | [L109674](../extracted/neo-agent.fmt.js#L109674) |  |
| `sync.apply` | [L109733](../extracted/neo-agent.fmt.js#L109733) |  |
| `sync.conflicts` | [L109789](../extracted/neo-agent.fmt.js#L109789) |  |
| `sync.conflict.resolve` | [L109826](../extracted/neo-agent.fmt.js#L109826) | `opId`, `resolution` |
| `workspace.fs.collaboration.recent` | [L104474](../extracted/neo-agent.fmt.js#L104474) | `departmentID`, `limit`, `projection` |
| `workspace.fs.collaboration.delta` | [L104496](../extracted/neo-agent.fmt.js#L104496) | `paths`, `projection` |
| `workspace.fs.collaboration.rebuild` | [L104526](../extracted/neo-agent.fmt.js#L104526) |  |

## Declared Events

| Event | Declaration |
|---|---|
| `chat.message` | [L30271](../extracted/neo-agent.fmt.js#L30271) |
| `chat.delta` | [L30272](../extracted/neo-agent.fmt.js#L30272) |
| `chat.delta.done` | [L30273](../extracted/neo-agent.fmt.js#L30273) |
| `user.input.delivery` | [L30274](../extracted/neo-agent.fmt.js#L30274) |
| `department.status` | [L30275](../extracted/neo-agent.fmt.js#L30275) |
| `department.catalog.changed` | [L30276](../extracted/neo-agent.fmt.js#L30276) |
| `okr.task.changed` | [L30277](../extracted/neo-agent.fmt.js#L30277) |
| `workspace.fs.changed` | [L30278](../extracted/neo-agent.fmt.js#L30278) |
| `workspace.fs.indexing.progress` | [L30279](../extracted/neo-agent.fmt.js#L30279) |
| `task.update` | [L30280](../extracted/neo-agent.fmt.js#L30280) |
| `tool.start` | [L30281](../extracted/neo-agent.fmt.js#L30281) |
| `tool.update` | [L30282](../extracted/neo-agent.fmt.js#L30282) |
| `tool.end` | [L30283](../extracted/neo-agent.fmt.js#L30283) |
| `task.delta` | [L30284](../extracted/neo-agent.fmt.js#L30284) |
| `task.delta.done` | [L30285](../extracted/neo-agent.fmt.js#L30285) |
| `task.tool.start` | [L30286](../extracted/neo-agent.fmt.js#L30286) |
| `task.tool.update` | [L30287](../extracted/neo-agent.fmt.js#L30287) |
| `task.tool.end` | [L30288](../extracted/neo-agent.fmt.js#L30288) |
| `tool.input.delta` | [L30289](../extracted/neo-agent.fmt.js#L30289) |
| `thinking.delta` | [L30290](../extracted/neo-agent.fmt.js#L30290) |
| `trace.append` | [L30291](../extracted/neo-agent.fmt.js#L30291) |
| `runtime.raw.event` | [L30292](../extracted/neo-agent.fmt.js#L30292) |
| `task.permission.request` | [L30293](../extracted/neo-agent.fmt.js#L30293) |
| `cron.job.changed` | [L30294](../extracted/neo-agent.fmt.js#L30294) |
| `cron.run.status` | [L30295](../extracted/neo-agent.fmt.js#L30295) |
| `chat.aborted` | [L30296](../extracted/neo-agent.fmt.js#L30296) |
| `task.created` | [L30297](../extracted/neo-agent.fmt.js#L30297) |
| `task.updated` | [L30298](../extracted/neo-agent.fmt.js#L30298) |
| `hook.work.changed` | [L30299](../extracted/neo-agent.fmt.js#L30299) |
| `runtime.state_changed` | [L30300](../extracted/neo-agent.fmt.js#L30300) |
| `runtime.progress` | [L30301](../extracted/neo-agent.fmt.js#L30301) |
| `runtime.subscription_prompt` | [L30302](../extracted/neo-agent.fmt.js#L30302) |
| `wechat.status_changed` | [L30303](../extracted/neo-agent.fmt.js#L30303) |
| `telegram.status_changed` | [L30304](../extracted/neo-agent.fmt.js#L30304) |
| `bench.mail.inject` | [L30305](../extracted/neo-agent.fmt.js#L30305) |
| `bench.nudge.tick` | [L30306](../extracted/neo-agent.fmt.js#L30306) |
| `bench.cron.trigger` | [L30307](../extracted/neo-agent.fmt.js#L30307) |
| `terminal.session.output` | [L30308](../extracted/neo-agent.fmt.js#L30308) |
| `terminal.session.status` | [L30309](../extracted/neo-agent.fmt.js#L30309) |
| `userProfile.discovery.progress` | [L30310](../extracted/neo-agent.fmt.js#L30310) |
| `userProfile.discovery.result` | [L30311](../extracted/neo-agent.fmt.js#L30311) |
