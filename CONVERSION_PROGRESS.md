# Permanent game-conversion progress ledger

**Estimated engineering conversion progress: 25 / 100 points (25%) · v5.1: 23 / 100 · +2 evidence-backed partial points this pass.**

**Fully verified playable original missions: 0 / 21 (0%).** The engineering score includes 22 points from completed milestones plus one partial point each within AI-06, AI-05 and MIS-02. These parent milestones remain open, and no user acceptance is assumed.

The master progress items below **never disappear**. Implemented items remain visible and are NOT user-approved merely because code or static tests pass. New discoveries get a new child item beneath a milestone rather than silently changing the fixed 100-point denominator. If an existing feature regresses, retain the item, mark it regressed and reduce its earned points until corrected.

| Workstream | Earned / possible | Progress |
|---|---:|---:|
| Source provenance | 3 / 5 | 60.0% |
| Original map geometry | 3 / 15 | 20.0% |
| Original textures | 2 / 7 | 28.6% |
| STAN collision | 5 / 12 | 41.7% |
| Map registration | 1 / 10 | 10.0% |
| Original object setup | 2 / 12 | 16.7% |
| Characters and animation | 1 / 8 | 12.5% |
| Original AI | 6 / 10 (4 complete + 2 partial) | 60.0% |
| Mission objectives | 2 / 10 (1 complete + 1 partial) | 20.0% |
| Native interactions | 0 / 4 | 0.0% |
| Mission completion | 0 / 4 | 0.0% |
| Runtime QA | 0 / 3 | 0.0% |

## v5.2 — Train source runtime and bytecode framing

- [ ] **AI-05.10** — Corrected null-terminated debug instruction framing across 122 affected lists. The decoder recovered 833 net instruction records and invalidated 11 false terminators.
- [ ] **AI-05.11** — Runs the original Train room and exit-approach scripts through supported commands. +1 partial AI-05 point.
- [ ] **MIS-02.2** — Reaching Train's original escape room completes its source condition. Six brake events now also drive the original guard pursuit handoff. +1 partial MIS-02 point.
- [ ] **END-01.1** — Original pad 203, timer and death branch execute, but hostage, cutscene and victory remain open. No mission-completion credit awarded.

Evidence: `V52_TRAIN_RUNTIME_NOTES.md`, `V52_AI_FRAMING_AUDIT.json` and `test_v52_source_runtime.cjs`. Browser/Chromebook verification pending.

---

## v5.1 — original explicit-character AI dispatch · +1 verified partial point

**23/100 engineering conversion points**, up from 22. This **does not** close AI-06 or certify any completed mission. This fixes the previous zero-progress accounting by allowing evidence-backed partial points **within existing weights**, while preserving all requirements, the fixed total of 100, and every prior user-acceptance state.

- [ ] **AI-05.9 · IMPLEMENTED AND STATIC-TESTED:** Source `jump_to_ai_list` carries an original actor selector. A valid explicit character ID dispatches to that actor's **own** source AI runtime, preserving the caller's current instructions; if the original guard is absent/duplicate/dead or destination list missing/ambiguous/truncated, the transfer is blocked. Actual Chromebook gameplay still needs verification.
- [ ] **AI-06.2 · PARTIAL AI-06 CREDIT 1/4:** Source graph contains **20** explicit character-ID handoffs; **14** have one original guard record and one unique terminated original destination script. Those 14 are eligible for execution **when the named original guard is actually spawned**. There are 32 reserved 0xF8 selectors, still unimplemented rather than guessed.
- [ ] **AI-05.8 remains OPEN:** Full original actor registry, uninstantiated guards, pseudo-characters, original global AI and native hearing/combat/exit not restored.
- [ ] **No browser gameplay approval:** 0/21 fully verified original missions. Original embedded assets/records remain byte-identical to v5.0. Source and VM tests pass.

**Evidence:** `V51_NATIVE_ACTOR_AI_DISPATCH_SOURCE_AUDIT.json`, `test_v51_native_ai.cjs`, full private v5.1 archive and the immutable historical master tracker.

---

## Permanent milestones (stable IDs)

- [ ] **SRC-01 · 3 pts · IMPLEMENTED (user review pending)** — Verified source executable identity and source record SHA. *Evidence / blocker:* V36/V41 source extraction and V48 AI input hash
- [ ] **SRC-02 · 2 pts · OPEN** — Archive original raw executable and native graphics containers with provenance. *Evidence / blocker:* Original raw binary absent from the existing user-held ZIP
- [ ] **GEO-01 · 3 pts · IMPLEMENTED (user review pending)** — Extract initial original geometry for the 23 browser map assets. *Evidence / blocker:* V40 mesh-batch audit
- [ ] **GEO-02 · 6 pts · OPEN** — Recover all missing source draw batches on every stage. *Evidence / blocker:* Dam, Statue, Surface and others incomplete
- [ ] **GEO-03 · 6 pts · OPEN** — Validate faithful complete original floor, walls and room assembly on every map. *Evidence / blocker:* No complete 23-map traversal
- [ ] **TEX-01 · 2 pts · IMPLEMENTED (user review pending)** — Decode source textures and attach to recovered material batches. *Evidence / blocker:* Source texture and GLB converter audits
- [ ] **TEX-02 · 5 pts · OPEN** — Verify original UV, textures, transparency and materials on every mesh. *Evidence / blocker:* UV/atlas assignment not fully decoded
- [ ] **COL-01 · 5 pts · IMPLEMENTED (user review pending)** — Decode 28/28 source STAN collision blocks and all 36,699 tiles. *Evidence / blocker:* V41 collision audit and v47 static test
- [ ] **COL-02 · 4 pts · OPEN** — Use source collision authoritatively on every playable stage. *Evidence / blocker:* Only Train source floor verified for runtime placement
- [ ] **COL-03 · 3 pts · OPEN** — Verify source stairs, edges, ramps, gravity and multi-floor transitions. *Evidence / blocker:* Dam elevations and missing map floors
- [ ] **REG-01 · 1 pts · IMPLEMENTED (user review pending)** — Calibrate source collision to Train converted graphics. *Evidence / blocker:* V41 source Train transform
- [ ] **REG-02 · 6 pts · OPEN** — Validate source transforms independently for all other stages. *Evidence / blocker:* V46 registration audit finds severe gaps
- [ ] **REG-03 · 3 pts · OPEN** — Explain/fix missing source visual geometry without synthetic workarounds. *Evidence / blocker:* Missing original draw groups in several stages
- [ ] **OBJ-01 · 2 pts · IMPLEMENTED (user review pending)** — Recover strict partial object/guard/tag placement inventory. *Evidence / blocker:* V46 audited partial object records
- [ ] **OBJ-02 · 6 pts · OPEN** — Decode every original setup property record type and length. *Evidence / blocker:* Original parser stops at unsupported property types
- [ ] **OBJ-03 · 4 pts · OPEN** — Bind every mission object to source model, tag, pad and usable state. *Evidence / blocker:* Only six Train shootable model instances linked
- [ ] **RIG-01 · 1 pts · IMPLEMENTED (user review pending)** — Recover first source textured character/guard renderers. *Evidence / blocker:* V42 source body/atlas prototype
- [ ] **RIG-02 · 4 pts · OPEN** — Restore exact original skeleton hierarchy, skin weights and model bindings. *Evidence / blocker:* Exact authored skin weights still unknown
- [ ] **RIG-03 · 3 pts · OPEN** — Run original walk, shoot, hit, death and movement keyframes. *Evidence / blocker:* Reconstructed animation remains
- [ ] **AI-01 · 1 pts · IMPLEMENTED (user review pending)** — Identify native opcode names across decoded instruction records. *Evidence / blocker:* V43 native opcode dictionary
- [ ] **AI-02 · 1 pts · IMPLEMENTED (user review pending)** — Implement limited guards under original pads and subset AI commands. *Evidence / blocker:* V47 partial instruction interpreter
- [ ] **AI-03 · 1 pts · IMPLEMENTED (user review pending)** — Audit original global-script control flow, room branch targets and repeated labels. *Evidence / blocker:* V48 global AI audit: 184 lists
- [ ] **AI-04 · 1 pts · IMPLEMENTED (user review pending)** — Fail closed on unresolved goto_next instead of inventing wrap target. *Evidence / blocker:* V48 nativeAIJump patch + Node branch tests
- [ ] **AI-05 · 2 pts · OPEN (1/2 partial)** — Execute complete original native background/global AI scripts. *Evidence / blocker:* Global scripts and NPC actions not implemented end-to-end
- [ ] **AI-06 · 4 pts · OPEN (1/4 partial earned; 3/4 pending)** — Restore original enemy AI pathing, pursuit, visibility, combat and reaction across all maps. *Evidence / blocker:* Only partial original interpreter exists
- [ ] **MIS-01 · 1 pts · IMPLEMENTED (user review pending)** — Decode original objective groups and difficulty conditions. *Evidence / blocker:* V47 55 source objective groups
- [ ] **MIS-02 · 6 pts · OPEN (1/6 partial)** — Connect all original mission conditions to source objects and authentic world actions. *Evidence / blocker:* Only six Train brake targets have physical source models
- [ ] **MIS-03 · 3 pts · OPEN** — Verify all objective conditions at Agent, Secret Agent and 00 Agent. *Evidence / blocker:* No campaign mission fully verified
- [ ] **INT-01 · 2 pts · OPEN** — Restore original doors, alarms, locked access, triggers and prop handling. *Evidence / blocker:* Stateful native interactions incomplete
- [ ] **INT-02 · 2 pts · OPEN** — Restore original vehicle, inventory, pickups, scripted actor interactions. *Evidence / blocker:* Source AI and object handlers incomplete
- [ ] **END-01 · 2 pts · OPEN** — Decode and implement native exfil and success/failure mission transitions. *Evidence / blocker:* Train exit approach and timer run. Hostage, finale and mission result are unported
- [ ] **END-02 · 2 pts · OPEN** — Finish entire original campaign as playable linked missions. *Evidence / blocker:* 0 source-authentic missions fully playable
- [ ] **QA-01 · 2 pts · OPEN** — Test and approve every stage in browser/Chromebook. *Evidence / blocker:* No complete source-authentic stage acceptance
- [ ] **QA-02 · 1 pts · OPEN** — Validate Chromebook performance/AI, memory and restarts under load. *Evidence / blocker:* Requires actual Chromebook/WebGL performance QA

## v5.0 — source-native return-list commands and actor-target resolution

**Engineering completion: 22/100 = 22%, no full milestone added. Native original campaign missions browser-verified playable: 0/21.** Previous 34 scored milestones, 7 v4.9 child requirements, and all earlier progress updates remain in place.

- [ ] **AI-05.5 · IMPLEMENTED FOR TEST:** Native original `set_return_ai_list` reads its 2-byte script ID into each guard's own return-list register. `jump_to_return_ai_list` resolves the stored native ID uniquely and switches the executing AI program. Absent or duplicate target: halt, never guess. Node VM test passes.
- [ ] **AI-05.6 · IMPLEMENTED FOR TEST:** `jump_to_ai_list` must check its first actor-selector byte. Recovered original command records contain 428 `0xFD` target selectors and 52 others; only self-target handoffs can be faithfully executed by the current per-guard interpreter. Preserving and blocking other actor selectors prevents corrupting the wrong guard's script. Node VM tests pass.
- [ ] **AI-05.7 · SOURCE DATA DECODED / GAMEPLAY OPEN:** Complete 21-stage audit of 480 handoffs, 87 return-list setters (38 refer to a uniquely resolved terminated stage-local list) and 37 return jumps, each retaining its original source byte offset and instruction parameters.
- [ ] **AI-05.8 · NOT IMPLEMENTED:** Full source character registry, native return state initialized outside the current interpreter, and shared AI list lookup. Stage-local absence is not evidence that an original target is invalid.

No original-game world geometry, mission objects, or other decoded binary payload was changed. This pass is **not** a claim of a complete AI engine or a playable original mission. Full private v5.0 ZIP retains prior asset/code/research snapshots and adds `V50_NATIVE_AI_RETURN_AND_ACTOR_SCOPE_AUDIT.json` and tests.

## v4.9 — source-native interpreter and object dependency advancement (all acceptance pending)

**Score remains 22/100.** The completed sub-steps below are inside unfinished parent AI-05, AI-06, OBJ-02 and OBJ-03. Awarding full parent credit now would falsely claim complete global AI or full objective model binding.

- [ ] **AI-05.1 · IMPLEMENTED_STATIC_TEST_PASS_USER_REVIEW_PENDING** — Original AI list changes must fetch new instruction array. Evidence: v49 test source original program A to B demonstrates target flag selection.
- [ ] **AI-05.2 · IMPLEMENTED_STATIC_TEST_PASS_USER_REVIEW_PENDING** — Stop native AI immediately after failed conditional label jump. Evidence: v49 VM test proves no post-failure objective flag write.
- [ ] **AI-05.3 · IMPLEMENTED_STATIC_TEST_PASS_USER_REVIEW_PENDING** — Require unique fully decoded original guard initial AI list. Evidence: 308 of 637 source guard records resolve to unique terminated original list; 329 not yet resolved.
- [ ] **AI-05.4 · BLOCKED_UNRECOVERED_RAW_EXE** — Recover original shared/global AI programs beyond stage setup streams. Evidence: 246 of 480 native list handoffs lack unique terminated stage-local destination; some may refer to shared lists.
- [ ] **AI-06.1 · IN_PROGRESS_BLOCKED_NATIVE_EVENT_SYSTEM** — Replace guessed hearing/partial LOS/witnessed-shot source condition outcomes with original event logic. Evidence: v49 now fails closed at these unknown conditions; original event model remains unimplemented.
- [ ] **OBJ-02.1 · BLOCKED_UNRECOVERED_RAW_EXE** — Recover XBLA property 0x20 objective_enter_room record length and associated fields from raw original bytes. Evidence: v49 strict parser retains original offset and N64 documentation as unverified candidate; no guessed strides.
- [ ] **OBJ-03.1 · SOURCE_AUDIT_COMPLETE_IMPLEMENTATION_NOT_DONE** — Trace objective-to-native-tag-to-prop-model-to-floor-to-AI-writer dependencies on all setup stages. Evidence: v49 source graph 55 groups/136 criteria, 72 destroy checks/12 linked/6 with runtime model.

Original objective records: **55 groups / 136 conditions** (72 object-destruction, 34 completion-flag, 30 failure-flag). **12/72** destroy criteria have a decoded source tag link, only **6/72** have a connected renderable source objective model. Original source guard records: **637**, with **308** unique and terminated initial AI-list references, **329** unresolved/ambiguous/truncated. Native program handoffs: **480**, of which **234** target a uniquely resolved terminated stage-local program. These are static source evidence counts and do not imply gameplay verification.

## Step-by-step progress log

- **v4.7 — 20/100**: Retrospectively scored pre-v48 verified extraction and partial game milestones under the new fixed scoring rubric.
- **v4.8-step-1 — 21/100**: Decoded and audited native global AI structure/room branch topology across 21 setup stages.
- **v4.8-step-2 — 22/100**: Guard nativeAIJump no longer guesses initial label when goto_next has no matching successor; fail-closed until exact semantics verified.

- **v4.9-step-1 — 22/100**: Source VM executes the *new* original AI list following a native list handoff, not stale source commands.
- **v4.9-step-2 — 22/100**: Failed source conditional jumps stop before any later flag/object event. Regression tested.
- **v4.9-step-3 — 22/100**: Initial source guard AI list must resolve uniquely and be complete; unverified hearing/partial LOS/witnessed-shot predicates no longer fabricate events.
- **v4.9-step-4 — 22/100**: Produced 21-stage, per-objective source dependency graph with authentic original offsets, tagged objects, scene transform/stage support, native AI-flag writers, and missing dependencies.
- **v4.9-step-5 — 22/100**: Added strict original-property byte parser. First new candidate type (0x20, objective enter room) remains marked as *unverified for XBLA* until the raw PE is supplied; no speculative byte skipping.

## Confirmed unconverted parts / no fake fixes

- 184 original global AI lists recovered from source records; 118 contain repeated labels and 24 are truncated/nonterminated, so global script runtime is NOT complete.
- Only six Train original brake units are verified as connected source objective shootable objects; other objective actions remain unimplemented.
- Original render/STAN alignment is not resolved for most maps. Never replace original layout with invented supports or derived fake victory triggers.
- No real-world ChromeOS/WebGL acceptance test has certified any original campaign mission.

## Scoring changes policy

Keep milestone IDs and original historical tracker intact. Append new discoveries under their parent as `ID.subnumber`, never remove or silently tick an acceptance box. Recompute weights only if the user explicitly authorizes a new scoring rubric, and always keep prior release snapshots for comparison.
