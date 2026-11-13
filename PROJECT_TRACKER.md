## 2026-11-12 — v4.9 source-native AI VM and mission dependency decoding (IMPLEMENTED FOR STATIC TEST, NOT USER-APPROVED)

**Score 22/100 engineering milestones, unchanged from v4.8. Fully verified original campaign missions: 0/21.** There are **7 permanent new child requirements** under the existing 34 fixed milestones, with no deletion or change to previously recorded approvals. Full versioned private ZIP keeps original embedded game assets and all previous decoding notes.

- [ ] **AI-05.1:** Fixed real script-interpreter bug: after original `jump_to_ai_list`, subsequent commands execute the destination AI list, not the previous list with a reset PC. Native VM test verifies objective flag source.
- [ ] **AI-05.2:** Fixed native conditional-label halt propagation. When source goto label is unresolved, no later objective flag write is run.
- [ ] **AI-05.3:** Original initial guard AI program is selected only when unique and fully terminated. Original records show 637 guard placements; 308 references resolve to unique terminated source lists, 329 do not.
- [ ] **AI-05.4 (BLOCKED):** Of 480 original AI list transitions, 234 resolve to a unique terminated stage-local source list, 246 are still missing/ambiguous/truncated (some may refer to system/shared scripts). Recover full original binary/native shared lists rather than invent behavior.
- [ ] **AI-06.1 (BLOCKED):** Previous fake hearing/partial LOS/witnessed-shot branches now stop as unsupported native event logic. Genuine source sensory events not yet reconstructed.
- [ ] **OBJ-02.1 (BLOCKED):** Original raw 17,760,256-byte Xbox PE absent from supplied v4.8 archive. New strict parser preserves known original record offsets; N64 `0x20` enter-room length is a documented *candidate*, not used to skip unknown native Xbox bytes.
- [ ] **OBJ-03.1 (DECODED AUDIT, GAMEPLAY OPEN):** Source dependency graph covers 21 setup stages, 55 objective groups / 136 conditions; 72 destroy requirements, 12 linked tags and six physically connected renderable Train targets. Candidate bitfield setters are source references only, not verified executable game events.
- [ ] **Browser acceptance still required:** No source-correct all-map mission/AI playthrough completed. Static tests: Node syntax, VM list-jump/conditional-halt, source property mock structural fixture, original 20 embedded source payloads byte-identical from v4.8, 34 original IDs preserved, full ZIP integrity.
- [ ] **Cannot mark whole campaign playable:** Native extraction, original asset draw batches, objective interactions, shared AI lists and numerous map/STAN registration issues remain.

Details: [v4.9 source evidence](research/V49_SOURCE_OBJECT_AI_DEPENDENCY_AND_RUNTIME.md), [immutable progress scoreboard](CONVERSION_PROGRESS.md). Private downloadable archive: `GoldenEye_World_Explorer_v49_NATIVE_AI_VM_AND_OBJECT_DEPENDENCY_DECODING.zip`. **Preserve every earlier tracker item below.**

---

## 2026-11-12 — v4.8 permanent 100-point conversion ledger and source global AI control-flow audit (NOT USER APPROVED)

**Engineering milestone estimate: 22/100 points; v4.7 scored 20/100 under the same rubric (+2). Fully verified original campaign missions: 0/21.** The engineering score is not the percent of missions playable.

**Permanent rule:** never delete a feature/issue from this tracker, whether complete or blocked; retain stable IDs, append new discoveries, add dated evidence, and keep completed requirements visible. Only the user's explicit approval can mark an acceptance checkbox. A regression stays recorded and can remove earned engineering credit until repaired. See [root permanent roadmap](CONVERSION_PROGRESS.md) (34 stable milestones / 12 scored workstreams).

- [ ] **AI-03 source decoder implemented / awaiting user acceptance:** Audited 184 source global AI lists / 5,887 instructions, including 118 lists with duplicated original labels, 24 truncated/nonterminated lists, and 189 original room-test branches of which 81 have unresolved or ambiguous jump targets.
- [ ] **AI-04 control-flow safety implemented / awaiting user acceptance:** Removed invented `goto_next` wrap to first source label; ambiguous duplicate or truncated `jump_to_ai_list` target is blocked instead of arbitrarily selected. Node VM branch tests and JavaScript syntax pass.
- [ ] **Progress dashboard implemented / awaiting user acceptance:** Single-file game now shows the fixed 22% engineering estimate, +2 points this release, all 12 workstreams and the separate 0/21 actually verified mission statistic.
- [ ] **Preserved source-data audit / awaiting acceptance:** All 20 embedded v4.7 source-asset datasets are byte-identical in v4.8. Private ZIP includes 91 retained/new files, the full original embedded assets, decoder scripts, control-flow JSON, release manifest and older decoding notes; ZIP CRC passed.
- [ ] **Critical incomplete campaign:** Original global AI and native mission completion remain unported; 55 original objective groups exist but only six source Train brake controller objective models are physically connected. Unknown setup property types cannot be fully recovered without original executable bytes, which are absent as raw binaries in the supplied v4.7 ZIP. Source map geometry gaps and collision registration remain.
- [ ] **Visual and runtime QA:** No certified ChromeOS browser / WebGL playtest; no fully playable source mission; do not mark the above accepted until user testing.

Research: [v4.8 original AI audit](research/V48_NATIVE_GLOBAL_AI_CONTROL_FLOW_SUMMARY.md). User-held archive: `GoldenEye_World_Explorer_v48_NATIVE_GLOBAL_AI_AND_PERMANENT_PROGRESS.zip`. Historical tracking below remains unmodified.

---

## 2026-11-12 — v4.7 original-source objective runtime and playability coverage (IMPLEMENTED FOR TEST / NOT USER APPROVED)

**Do not classify the full campaign as playable.** Original source decoding is incomplete and authenticated objectives beyond the six Train brake units are unimplemented. The supplied private v4.7 ZIP retains the full HTML, source assets, original decoder JSON and previous research. This public repository tracks progress and research without redistributing game asset payloads.

- [ ] **Original difficulty-scoped objective HUD:** Source objective groups filtered for Agent / Secret Agent / 00 Agent. Missing conditions stay unresolved; there is no fabricated mission victory. Browser verification pending.
- [ ] **Native AI branch repairs:** Original character-ID check for actor dying/dead, actual guard hit-count condition, Bond death condition, and fail-closed unresolved label jumps. Browser AI verification pending.
- [ ] **Original collision-backed movement:** Source guard steps ray-test against recovered rendered walls; source room conditions require authored STAN and matching converted floor. Verify patrol routes and wall collision in all maps on Chromebook.
- [ ] **Consistent mission reset on death:** Reloads entire authored stage state (guards, objects, objective flags) rather than healing only the player. Browser verification pending.
- [ ] **Source payload preservation / static checks:** All 20 original embedded raw data blocks unchanged from v4.6; `node --check` passes and archive CRC passes. Automated static checks do not count as user approval.
- [ ] **Critical mission blockers:** 21 original setup stages, 55 objective condition groups, 72 destroy-object criteria, just 12 linked original tags, and only six physically recoverable in-game source target models (Train model 120). Cannot call remaining mission objectives operational.
- [ ] **Critical map blockers:** 28 original STAN blocks and 36,699 authentic tiles decoded; Dam, Facility, Streets, Statue, Runway have nontrivial disagreement with rendered geometry; do not fabricate missing floors or guessed universal coordinate transforms.
- [ ] **Playability blocker:** Full original global AI, NPC/object and door interaction, source-model lookup, exfil/victory and missing render batches still unported. Real WebGL/ChromeOS acceptance required; testing environment blocked Chromium navigation.

Details: [v4.7 original mission and layout audit](research/V47_NATIVE_MISSION_AND_MAP_AUDIT.md). Private user-held archive: `GoldenEye_World_Explorer_v47_NATIVE_AI_OBJECTIVES_SOURCE_AUDIT.zip`. Preserve all historical checklist items and prior explicit user approvals below.

---

## 2026-11-12 — v4.4 original mission insertion and Train object-trigger gameplay (IMPLEMENTED FOR TEST; USER APPROVAL PENDING)

**This is a partial native mission implementation, not a complete restored campaign. All new acceptance boxes remain unchecked; do not change any existing acceptance state.**

- [ ] **Train source mission insertion:** Load the original normal mission start pad 186, native coordinates (117,45,-9), source-to-GLB and original STAN floor checked. Verify in running Chromebook game that it is the correct START rather than the end/exfil position.
- [ ] **Other maps source insertion:** Audit 18 original stage entry pads, enable source entry only when the original floor and existing recovered rendered mesh support the position. Dam's actual source pad 33 lies outside the currently rendered graphics, so the game explicitly uses an **EXPLORER START** rather than a made-up authentic entry.
- [ ] **First actual gameplay objective, Train A:** Decode original type 0x16 tag links 8–13 to six *source model ID 120* original Train brake-controller instances. Recover the real 62-triangle brakeunit CAFF source model and six original bound pad positions (10000, 10052, 10055, 10075, 10103, 10119); place on verified Train source STAN. Shooting them updates native destroyed-object tags; objective A completes only after all six source tags are destroyed. One-hit target damage is simplified; original UV/scale exactness pending.
- [ ] **Original Train background event subset:** The original 0x1009 background list checks the source room of pad 98 then sets original objective bitmask 0x00100000. Browser stage trigger performs a source-STAN room comparison and sets only that exact original bit. Full AI interpreter unavailable.
- [ ] **Real Restart Mission action:** Re-load actual stage, original spawn where supported, six Train objects, guards and objective state; verify in browser.
- [ ] **Critical remaining original campaign:** Natalya rescue and all other Train objectives, exact native exfil/victory, doors and prop interactions, full source AI global script semantics, and every other level's original gameplay.
- [ ] **Visual and controller QA:** Test six source brake meshes visible, hits do not penetrate carriage walls, mission status is correct and no unexpected 3D offset; verify insertion on each eligible map, collision, guard respawns and restart.
- [ ] **Static tests completed but not user-approved:** Source model, six tag/model/pad associations, six STAN floor matches, JavaScript syntax, JSON scripts and ZIP CRC. **No Chromebook WebGL runtime test claimed.**

Research: `research/V44_SOURCE_MISSION_START_AND_TRAIN_BRAKEUNIT.md`. Private source-derived asset package: `GoldenEye_World_Explorer_v44_ORIGINAL_MISSION_START_AND_TRAIN_TARGETS.zip`, saved to ChatGPT Library. Preserve all historical checklist items below.

## 2026-11-12 — v4.3 AI movement efficiency and original command-name decoding (NOT USER APPROVED)

- [ ] **Implemented; needs Chromebook acceptance:** Correct double-stepping NPC movement, index source Train STAN floor collision, share original guard atlas/mesh resources, stagger sight queries and guard AI ticks, and render-cull distant guard models. Measured AI CPU status is visible while source guards are running.
- [ ] **Implemented; needs behavioral acceptance:** Reconcile native original 253 opcode names and label 2,914 previously unidentified instructions in 662 authentic stage lists without altering their bytecode or silently simulating unsupported instructions.
- [ ] **Implemented; needs acceptance:** Add conservative source AI state register/guard flags/pad preset commands and Train-only source distance condition checks. Original global AI lists and command effects still incomplete.
- [ ] **Perf test needed on Chromebook:** Validate FPS, guard model textures, walking/pursuit smoothness, source-position accuracy, floor transitions and whether AI CPU readout decreases during Train gameplay. No live WebGL QA was possible in restricted test browser.
- [ ] **Full campaign still open:** Decode complete native global AI, patrol path command behavior, mission triggers, bone weights, and all-map original coordinate transforms. Do not claim full original AI from mere opcode-name recovery.

See `research/V43_AI_CPU_AND_NATIVE_COMMAND_PROGRESS.md` for documented static checks. All prior requirements and approvals below are retained without modification.

## 2026-11-12 — Private v4.2: source-textured guard models, test patrol motion, native objective HUD, restored settings, top-left minimap (NOT USER APPROVED)

- [x] **Code patched / browser visual QA pending:** Original source-guard loader no longer directly displays white/untextured or malformed skinned CAFF character GLBs. It now builds the project's source texture atlas-based articulated guard avatar using original uniform/face texture assets and reconstructed geometry/head binding (the full original skinned body model UV/bind-pose remains unsolved). No plain-white GLB fallback.
- [x] **Code patched / actual movement QA pending:** Source guard AI list movement retains original recovered stage patrol pad order wherever available. Guards blocked by unsupported GLOBAL native AI-list handoffs/opcodes, or motionless native loops, can now circulate on a *clearly reconstructed* local route assembled from **actual original nearby source pad coordinates** with strict source floor support, instead of freezing or generating random XYZ waypoints. Train has no decoded patrol-path table: its nearest-pad circulation is **NOT recovered original authored patrol AI**. Short-range sight/pursuit/fire are partial approximations.
- [x] **Code patched:** Original objective condition HUD shows decoded stage objective condition groups and original named objective descriptions. Supported source AI objective-bitfield set/clear opcodes can update native objective state; display does not mark unknown native object-tag/destroy or unsupported triggers as complete. Fail condition checks no longer incorrectly block success unless the fail bit was actually asserted.
- [x] **Code patched:** Replaced simplified menu vs hidden legacy settings with Play / All Settings tabs; all legacy controls preserved, including original character/head preview options. Source diagnostics still accessible separately.
- [x] **Code patched:** Moved live existing HUD minimap to **upper-left**, objective HUD below it; responsive layout offsets main menu so they do not overlap at typical desktop widths.
- [x] **Static QA passed:** Node JS check, complete 43-entry ZIP CRC, source module bytes embedded in updated HTML, old 41 research/assets files retained, no altered original embedded assets. Private file `GoldenEye_World_Explorer_v42_TEXTURED_GUARDS_PATROL_OBJECTIVES_UI.zip` uploaded to user's Library.
- [ ] **Critical user signoff needed:** Actual textured body/head appearance, source model memory footprint for 35 Train guards, patrol-motion path selection / obstacles and LOS, original Train carriage transitions, objective HUD behavior on real Chromebook.
- [ ] **NOT COMPLETE:** Original sourced skin weights, correct guard model/body ID and head ID matching, real native global AI lists, authentic Train patrol sequences, authoritative native objective event triggers and complete campaign behavior. Reconstructed source-pad circulation should not be misrepresented as fully authentic.
- [ ] No prior user approval toggled. Retain historical master checklist and all open map/audio issues below.

## 2026-11-12 — v4.1 ORIGINAL Train STAN floor and source guard/AI playtest (NOT USER APPROVED)

**User scope was strictly two things: source map floor/layout recovery and original enemy spawns/behavior. No changes to mission objective UI, audio, or unrelated menus.**

- [x] **Native Xbox source format decoded:** Parsed original source **STAN clipping polygons for all 28/28 game blocks** from the user's authenticated 17,760,256-byte Xbox PE: **36,699 authored source polygons**. Per-block pointer lists and variable vertex counts parsed end-to-end, with all original block termination offsets matched. This is real source collision layout; only Train has been verified against browser render coordinates and activated.
- [x] **Train floor integration:** 694 authentic original STAN tiles; source-to-Train GLB scale=0.0512 and translation from original CAFF graph centre validated by matching authored train X bounds within ~0.04 scene units. Of the source-authored clipping tile centres, 636 coincide with recovered visible render triangles, while **58 have no rendered floor at the same Y**. The browser now renders those 58 missing areas using authentic native STAN polygons with clearly UNTEXTURED neutral metal appearance, not fabricated geometry or invented UVs. Invisible original STAN tile mesh is Train collision authority, preventing missing render batches and overhead roof polygons from determining player/guard floor.
- [x] **Original player Train entry:** Uses the original Train intro spawn pad and native STAN-supported floor rather than the old guessed explorer spawn. Requires browser check.
- [x] **Train guards:** All **35 native source spawn-pad records** were independently tested against authentic Train STAN geometry and all **35/35** intersected source walkable tiles. Browser guard placement for Train uses the calibrated original coordinate transform rather than the old player-centred 0.01 projection; attempts to spawn all 35 subject to original character GLB availability/Chromebook memory. Shooting, hit/death and reconstructed animations remain.
- [x] **Native original patrol path tables:** Decoded **86 original path records** across 21 stage setup regions (e.g., Dam 8 paths / 108 pad visits, Facility 7 paths, Surface 1 16 paths). Each retains native pad order, loop flag and offset. Source AI `guard_start_patrol` now follows its original path IDs through original pad positions; unsupported tile or coordinate alignment stops the movement. **Train itself has no authored patrol paths** in its source table; Train guard scripts react through vision/combat instructions instead.
- [x] **Expanded partial AI command interpreter:** Source-directed conditional branches, timers, random seed, original walk/run/sprint-to-pad, patrol path visits, guard sight checks, original fire/aim attempt commands, label jump, some same-stage AI list jumps, and hit/death animation reactions implemented for browser. Combat damage, sight/room logic, global AI list behavior and original keyframe clips still approximate/incomplete. Native Xbox engine is NOT running in HTML.
- [x] **Static validation:** 28/28 STAN end boundaries, Train 694 exact tiles, all 35 native guard pads supported, 86 paths, JSON parse, Node JS syntax, ZIP CRC, byte-for-byte preservation of 35 earlier auxiliary files and all original embedded game asset payloads. **No real ChromeOS WebGL playtest**; user approval strictly pending.
- [ ] **Critical:** Train still missing 11 original graphical draw batches and some source UV/material assignments; STAN-only visible floor tiles are original clipping geometry, NOT exact original render floor textures.
- [ ] **Critical:** Individually verify original STAN-to-GLB transforms on each of the other 22 browser maps before enabling their original clipping meshes or claiming source-perfect guard positions. Partial data for all 28 blocks included in v4.1 research ZIP.
- [ ] **Critical:** Implement full original global AI lists, native guard path scheduler, hearing, accurate combat, original animation timeline and enemy movement all maps; test browser performance for 35 Train models and guard corridor LoS.
- [ ] Test and fix native Train carriage transitions, 58 floor patch visibility, original player starting room, enemy spawn count, AI combat and non-Train patrol paths in actual ChromeOS browser. Leave all unapproved until explicit user verification. All previous tracker items preserved below.

## 2026-11-12 — v4.0 Dam layered-floor fix and authentic source geometry recovery (NOT user approved)

- [x] **Code patched:** Dam/regional player movement no longer samples source walkable floors 1.10+ units ABOVE feet or probes and instantaneously snaps to an elevated catwalk 1.27 scene units ahead. Replaced with near-layer raycast limits (+0.34/-0.55) and continuous sample-by-sample grounded step validation. Original-only step-rise helper no longer changes player height before destination validation. Some legitimate tall stair treads may now be blocked; original STAN stair collision required for full fix.
- [x] **Code patched:** Restored **232 missing original Statue Park GLB mesh batches** from the already decoded original source asset archive, preserving existing **82 source-textured batches** unchanged. Total restored source **314 / 518 known draw calls represented**, not 518/518. Supplemental batches retain ORIGINAL source vertex colors and names; texture indices/UVs for these restored batches are still unknown, no random textures assigned. Duplicate batches filtered.
- [x] **Audit completed:** Compared the 23 existing embedded maps to the 23 early original source maps in the archive. Other early source conversions mostly have the same missing geometry as the game; a replacement cannot fill the missing Dam 162/391 draw calls, Surface 128/215, Library 52/66, Complex 29/43, etc. The per-map metadata is saved in `V40_ORIGINAL_MAP_MESH_TEXTURE_AUDIT.json`; draw count is not a completeness proof.
- [x] **Preservation checks:** All 33 auxiliary older files byte-identical; embedded original `EMBED` asset payload byte-identical; Statue Park supplemental raw original geometry separately embedded. JS syntax (Node), ZIP CRC, source/HTML integration checked. No fabricated platforms, props, mission boxes, AI or fake textures added.
- [ ] **User-reported Dam elevated walkway teleport still requires Chromebook visual playtest:** Verify walk on lower ground does not warp to upper mesh; recover authentic STAN collision and navigable stairs/ramps. Do not mark user-approved until explicitly reported working.
- [ ] Recover missing original world meshes and exact original texture/UV assignments for every incomplete level, particularly Dam, Surface, Library, Complex, Statue Park, and fix remaining original floor gaps.
- [ ] Run GPU browser QA on all 23 maps, verify full mesh batches, floor traversal, texture transparencies and performance. All previous approved/unapproved requirements below unchanged.

## 2026-11-12 — Private v3.9 Jungle original-terrain and bounded native AI/audio corrections (NOT USER APPROVED)

- [x] **Original Jungle texture decoding repaired:** The embedded source Jungle GLB had 1 malformed leaf image, descriptor #37. Replaced that image with the same original game archive texture #037 converted to a valid PNG; preserved the other 54 existing images and original geometry/UV data. Set alpha MASK on six original foliage materials, so previously opaque leaf cards no longer obscure source terrain.
- [x] **Original Jungle floor collision adjusted:** Identified original source terrain meshes `batch_008`/`batch_009`; former fixed Jungle spawn intersected leaf-card polygons near foot Y=-9.895, with genuine terrain beneath near Y=-11.457. Explicitly reject original leaf render cards as player/guard walkable geometry and ground spawn using the terrain triangles. No invented terrain/platform mesh. **Requires real browser QA for fully traversable Jungle.**
- [x] **Original AI instruction subset implemented in JavaScript (NOT native Xbox engine):** Bounded per-guard interpreter for authentic source bytecode instructions label, sleep, end, source goto labels, original attributes and original *walk/run/sprint to pad* targets. Existing native guard records/pad indexes used, original floor supports checked for motion. Unimplemented AI, including patrol path scheduler, combat, mission event scheduler and unsupported global lists, halts rather than inventing routes, weapon fire or mission success.
- [x] Added guarded original objective-condition progress readout from stage native condition records. Unsupported native objective events remain unresolved and **cannot be falsely completed**. Does not constitute authentic mission trigger execution.
- [x] Original XSB/XWB SFX 209 cue-to-wave associations retained. Original per-level soundtrack cue names displayed with **unresolved music cue→wavebank identifiers**; no invented soundtrack, exact native AI→sound ID alignment STILL INCOMPLETE.
- [x] Packaged in `GoldenEye_World_Explorer_v39_JUNGLE_SOURCE_AI_AUDIO.zip`; original 31 auxiliary files unchanged, all game meshes except original Jungle texture/material alpha unchanged, browser source/HTML JS synchronized. JavaScript syntax, ZIP CRC, original repaired PNG and original GLB passed static tests.
- [ ] **Critical remaining:** Native full campaign objective interpreter, original door/prop setup meshes, guard patrol path tables and global AI command engine, source-aligned combat events, native soundtrack XSB→XWB mapping, and corresponding level audio playback.
- [ ] Validate correct Jungle terrain rendering/collision under ChromeOS WebGL, guard spawn and script-pads, source UI objectives, actual sound against game reference. Preserve all earlier user issues/approvals below without changing any prior checkbox.
- [ ] The original Xbox 360 PowerPC executable engine **cannot be executed inside a standalone Chromebook HTML file**. Only a ported subset of its original data and logic is presently implemented; do not call it the original native game engine.

## 2026-11-12 — v3.8 Source-guard autoload + simplified menu + audio-command audit (NOT user approved)

- [x] **Code integrated / browser QA pending:** Actual v3.7 asset-embedded playable HTML now attempts pad-linked original guard model placement **automatically on every map load**. Original floor raycasts reject unsupported placements, the source-XYZ-to-converted-map transform is still provisional (0.01x anchored). Stage guard attempts/counted results shown; unknown stages legitimately get zero, no random replacements.
- [x] **Code integrated / browser QA pending:** Simplified the regular menu to map/weapon/play/audio/respawn/guard retry. Original character and head swapping were leftover research/sandbox functionality, not canonical GoldenEye mission mechanics. These controls now live behind **Show research / diagnostics** instead of the main menu.
- [x] **Code integrated / browser QA pending:** Changed original-only mode sound playback from always muted to selected ORIGINAL XSB→XWB verified embedded sound examples on named gameplay actions. Cue-to-wave identities verified; trigger associations are **inferred from source cue names**, NOT yet native script-to-cue alignment. No synthesized audio for original-only mode. Source male guard hit + body fall cues used for source guard hit/fall examples.
- [x] Audited **147 stage AI sound/music commands** with original script offsets and unmodified operands: **63 sfx_play, 30 sfx_emit_from_object, 30 sfx_emit_from_pad, 19 music_xtrack_play, 5 music_xtrack_stop**. Original XEX script arguments-to-XACT cue index mapping still unverified; stored as `V38_NATIVE_AI_AUDIO_COMMAND_AUDIT.json`.
- [x] New private `GoldenEye_World_Explorer_v38_SIMPLIFIED_SOURCE_GUARDS_AUDIO.zip` contains updated single playable HTML, matching source module, v3.8 audio audit/progress report and ALL prior auxiliary research artifacts. JavaScript syntax and ZIP CRC passed, original model/audio embeds preserved.
- [ ] **Critical: Actual original AI patrol/combat/mission script runtime NOT implemented.** Source-script guard loops and native branch/event effects must be recovered and executed; source-record models are currently stationary except shot/hit reactions.
- [ ] **Critical: Source guard-to-GLB coordinate transform unverified.** Some maps may display no guards; do not fabricate floor supports or characters to fill gaps.
- [ ] Fix original guard model/face fidelity, missing original floor triangles, Dam walkway, natural original animations and all map geometry/texture issues.
- [ ] Align native XEX music/SFX AI-command parameters to XSB/XWB cue IDs, original event timing and original soundtrack. Validate original audio by source events rather than names only.
- [ ] Playtest initial autoload, guard shooting/hits, sound, reloading, menu and map switches on ChromeOS; leave unchecked until explicit user approval. Historical checklist continues unchanged below.

## 2026-11-12 — Playable PRIVATE v3.7 original guard records + source-only playtest (NOT user approved)

- [x] Extended original XEX guard-record scanner to find 578 additional high-confidence **contiguous native 0x09 guard-record candidates** from 21 stage setups, in addition to 59 previously strictly parsed guards; **637 total**, with original offsets, IDs, native spawn pads and facing coordinates preserved. Candidate status intentionally explicit pending full setup grammar.
- [x] Decoded 32 original native intro spawn-pad records and grouped known source objective conditions by source objective index.
- [x] Expanded original opcode names for 662 existing AI scripts with documented GoldenEye AI command definitions; labels are forensic descriptions, NOT proof of runtime execution.
- [x] Added opt-in source-guard playtest to real source-only asset-embedded HTML (v3.7) using **original character GLBs**, native guard pad records, and strict support from decoded map triangles. No random patrol targets, fake objective markers, or enemy respawns. Model shots/hits are testable.
- [x] Preserved original binary assets and prior auxiliary research files, Node JS syntax and ZIP CRC passed. The 79–82 MB source asset-embedded HTML is contained in `GoldenEye_World_Explorer_v37_ORIGINAL_GUARD_PLAYTEST.zip` in ChatGPT Library; public demo index not substituted.
- [ ] **CRITICAL: Original source-to-browser map conversion unverified.** v3.7 source guard playtest uses an **experimental 0.01x offset from source intro pad to current explorer spawn**. Guards with unsupported floors are excluded. Placement is *NOT authenticated* to converted 3D geometry, even if their native pad IDs are authentic.
- [ ] **CRITICAL: Native AI patrol, combat, and mission objective execution NOT implemented.** Native original bytecode remains research/inspection-only; source GLB guard avatars are static until verified game AI and motion keyframes are restored.
- [ ] Recover accurate pad XYZ-to-GLB transform; finish original prop/door full grammar, AI opcodes, path patrol arrays, event trigger/audio links, original objective conditions.
- [ ] Fix missing Dam walkway and 23-stage geometry/UV meshes and collision; visually playtest on Chromebook, establish performance and source guard model fidelity.
- [ ] All previous checklist entries and explicit approvals below remain unchanged. These new code items are NOT user-approved or declared fully tested.

## 2026-11-12 — v3.6 authentic original prop + AI opcode stream decoding (NOT user approved)

- [x] Extended original XEX stage property parser with **strict type 0x03 standard object (0x80 bytes)** and **type 0x08 original weapon/item record (0x8C bytes)**, validated against original binary record boundaries; unknown records stop decoding rather than corrupting later offsets.
- [x] Extracted **444 original prop/item records (390 standard props + 54 weapon/item)** and exact source model IDs, scale words, pad indices, original XYZ/face when linked. **384 have valid source pad associations.** These are not yet verified world placements.
- [x] Extracted **662 referenced original AI script records** from stage tables. Decoded instruction framing for **15,913 bytecode instructions** using documented GoldenEye AI command-length constants. **521/662** script streams reach the original END opcode; remaining 141 stop safely at boundary or unsupported frame (not arbitrarily parsed).
- [x] Expanded real asset-embedded explorer's **Original setup data** panel to inspect source model IDs/positions and original stage AI opcode/name previews. No random mission cubes, fake guards, invented trigger completions or unverified physical placements introduced.
- [x] Preserved all previous v2.8-v3.5 auxiliary tracking files and existing embedded GLB assets. Added `V36_AUTHENTIC_ORIGINAL_STAGE_RECORDS.json`, `decode_original_ai_lists_v36.py`, `decode_authentic_stage_records_v36.py`, `V36_PROGRESS_AND_OPEN_ISSUES.md`.
- [x] JavaScript syntax, source extraction and ZIP CRC checked. No browser/WebGL runtime claim.
- [ ] **0% authenticated objective trigger execution implemented:** AI frame decoding does not establish opcode runtime effects/event feeds/branch label state, guards' AI state machines or the native objective flag scheduler. Need explicit implementation and tests against source game.
- [ ] **0% verified original physical object placement implemented in browser:** Source pad records are recovered, but source-to-current-GLB coordinate transform, source model ID->GLB binding and source map floor/collision completeness remain unverified.
- [ ] Decode all unsupported native prop record types, especially doors and cameras; validate remaining scripts and stage triggers.
- [ ] Repair missing original Dam walkway surfaces from STAN source data and calibrate map transforms with source landmarks, then spawn original guards/props/doors (NOT synthesized proxy assets).
- [ ] Validate full mission behavior, difficulty, success/failure events and audio alignment in ChromeOS; explicit user testing/approval required. Historical full master tracker below remains unchanged.

## 2026-11-12 — v3.5 original stage setup records (source-authenticated, NOT user approved)

- [x] Decoded **5,200 normal source pad records** across original XBLA stage setup arrays, including native XYZ, up/look orientation, pad-to-room pointers and record offsets; Cuba needs a separate pointer-layout pass. These coordinates are ORIGINAL game units, not calibrated to converted browser map geometry.
- [x] Decoded **235 supported original objective record entries** (watch labels, objective starts/ends, destroy-objects, complete/fail condition flags). These are real native metadata, **not executable objective triggers**.
- [x] Strictly decoded **37 guard records**, including **36 Dam guards**, with native body ID, AI-list ID and pad-linked source positions/facing. Found 564 additional *candidate* guard records in contiguous native type-9 clusters, but these require full prop-type grammar proof before being considered complete.
- [x] Added `Original setup data` panel to the actual asset-embedded source-only v3.5 private explorer. Shows real stage pad/guard/objective records without inventing physical objects or marking objectives done.
- [x] Included decoder, original stage JSON and `V35_DECODER_PROGRESS_AND_OPEN_ISSUES.md` in new private ZIP. JS syntax and ZIP CRC verified; original embedded game assets retained.
- [ ] **Original objective execution: 0% verified.** Need actual AI opcode/branch/flag semantics and source-event bindings, not only objective condition descriptors.
- [ ] **Original prop/door/guard physical placement: 0% verified in explorer.** Native pad-linked guard records found, but original-to-GLB coordinate conversion must be calibrated and verified before spawning.
- [ ] Decode all source prop record sizes, including door/standard/surveillance camera, to traverse every stage object list safely.
- [ ] Calibrate source-to-converted-map coordinate units and axes with real source landmarks or shared geometry; do not invent transforms.
- [ ] Reconstruct complete original per-stage mission triggers, guards, doors, props, audio bindings, paths; correct missing Dam floor geometry and other maps.
- [ ] Real Chromebook visual/gameplay QA and explicit user approval. All earlier tracker items remain intact below.

## 2026-11-12 — Full authentic XBLA executable decompression and stage pointer discovery (NOT USER APPROVED)

- [x] Fixed STFS first hash-table boundary in native XEX extraction; original full retail game is intact. Correct extracted XEX SHA-256 `00b9197180cb044142dd78f2591ff721b1884f1b87aca5b566a325770054b8fa`.
- [x] Authenticated **123/123** original XEX compressed-block SHA-1 hashes. Old block-8 failure was an extractor bug and is resolved.
- [x] Decompressed **542/542** LZX frames to a valid 17,760,256-byte Xbox PowerPC PE image. Original PE SHA-256 `048c9a725e0163de3f1631651f7e250baaa01747d76c3e32cd62501cafefacd9`.
- [x] Matched **28/28 original STAN clipping block headers** and lengths to named stage allocation slots; this is structural decoding, not functional collision restoration.
- [x] Inventoried **641 structurally valid candidate original AI-list address/ID references** across 20 stage setup regions. Train requires a different parsing pass. Original opcode semantics not decoded.
- [ ] **Native objective command execution: 0% verified.** Decode exact script opcode lengths, branches, objective triggers and mission failure conditions; restore only verifiable original gameplay.
- [ ] **Original door/prop/guard positions integrated: 0% verified.** Parse stage pad/preset and setup object records and verify stage coordinate transforms.
- [ ] Convert STAN/hits data into actual source walkable triangles and repair Dam's missing walkway surface, rather than inventing a bridge.
- [ ] Match original scripted events to soundtrack and XACT cue identifiers, test and validate visually on Chromebook.
- [ ] Explicit user verification/approval and preserve every prior open issue below.

See `research/XBLA_VERIFIED_EXECUTABLE_AND_STAGE_TABLES.md` for exact source evidence. Code-only decoder ZIP has been saved privately to ChatGPT Library; no original copyrighted game binary is committed.

## 2026-11-12 — Original XBLA mission/placement decoding evidence (NOT user-approved)

- [x] Inspected original user-supplied `original_default.xex`, not a simulated mission catalogue. XEX2 header parsed; AES encryption type 1, Normal LZX compression type 2, 32 KiB window.
- [x] Recovered the working XEX devkit-key decryption path and authenticated the first **seven consecutive XEX compressed blocks** against the on-disk SHA-1 linked-block chain.
- [ ] The eighth block, index 7 at decrypted offset `0x63000`, fails the SHA-1 chain. Cannot claim full XEX payload extraction or original mission records. Investigate source integrity and block format before using any unauthenticated payload.
- [x] Audited the 4,565-entry decoded asset archive; no separately named original source setup/pad/AI script files recovered. The already-completed model conversion is not equivalent to mission-setup decoding.
- [ ] **Original objective scripts/triggers: 0% VERIFIED** (zero native mission records extracted, linked and tested).
- [ ] **Original door/prop/guard placements: 0% VERIFIED** (zero source-authenticated setup-to-pad transforms linked and tested).
- [ ] Decode complete XEX PE and/or original game stage setup resources; map source record types, original pads/presets/door transforms, guard spawns and AI lists to actual source geometry.
- [ ] Implement native objective triggers, difficulty conditions, failure states and audio alignment ONLY when source evidence exists.
- [ ] Full Chromebook gameplay validation and explicit user acceptance. Retain v3.4 source-only behavior; do not re-enable fabricated missions or objects.
- [x] Added documentation at `research/XBLA_XEX_ORIGINAL_SETUP_PROGRESS.md` and an evidence-only XEX audit script/report deliverable. Historical tracker below retained unmodified.

## 2026-11-12 — v3.4 SOURCE-ONLY Dam collision regression & original mission audit (not user approved)

**User-reported regressions:** Falling through Dam walkway, random floating colored mission cubes, non-authentic pseudo-mission objectives, incomplete map meshes/textures, and invented object placement/audio alignments. All are kept as outstanding until tested and explicitly accepted.

- [x] **Code change / QA pending:** Source-only collision guards stop a grounded walking step if no original decoded floor triangle supports the destination. Axis-slide fallback and restoring the last verified source-supported position replace plunging into a conversion hole. No invisible floor or fabricated map mesh was added. Actual Dam crossing remains unverified.
- [x] **Code change / QA pending:** Removed v3.3 fabricated mission objective target meshes, instant completion markers, and unverified progress state. The original mission names remain reference-only, not gameplay completion.
- [x] **Code change / QA pending:** Disabled by default all procedurally generated exteriors, fake outpost structures, random prop/NPC/car/door spawns, waypoint targets, stored unverified placements on map load, and synthetic soundtrack/footsteps. No invented in-game world content in source-only mode.
- [x] **Code change / QA pending:** Source GLB textures, materials and UVs are preserved; alternate bright material mode OFF by default. Missing authored texture/UV mappings are still unfixed.
- [x] Inspected the user's `original_default.xex` XEX2 executable (7,266,304 bytes), and 4,565-entry decoded asset ZIP. Found no separately decoded original stage setup/pad tables in available archive. **Does not claim XEX itself lacks embedded mission setup data.** No authentic stage/mission/guard scripting decoded in this pass.
- [x] Existing verified original XSB name → XWB wave map (209/209) preserved; gameplay model/event-to-cue mappings are still provisional and automatic event playback is disabled in source-only mode. Manual original cue audition remains.
- [x] Wrote `V34_ORIGINAL_SOURCE_AND_DAM_AUDIT.json` and `V34_PROGRESS_AND_OPEN_ISSUES.md` into new private v3.4 Library ZIP. All old auxiliary files and embedded game assets unchanged; Node syntax and ZIP CRC verified.
- [ ] **Critical:** Extract/reverse-engineer original XBLA stage setup/pad tables, object transforms and mission AI/script triggers from authenticated original game binary resources and place source objects correctly.
- [ ] **Critical:** Recover all missing Dam bridge/walkway triangles and authored collision surfaces. v3.4 stops fall-through by blocking invalid steps; this may block progress at map gaps and is not geometry restoration.
- [ ] Decode per-stage original sound cues / alignment and soundtrack assignment; test each associated event against game behavior.
- [ ] Correct actual original batch material index / UV mapping, broken mesh geometry and source proper environment textures; audit all maps.
- [ ] Run real Chromebook WebGL tests for Dam walkway, collision, textures, and interactions. Preserve all user-unapproved defects and existing master checklist items below.

## 2026-11-12 — Private playable v3.3 mission SIMULATION (code implemented; NOT user-approved)

- [x] Added initial Dam campaign selection instead of Facility and 20 original N64 **00 Agent** briefing/objective catalogues (80 objective entries); source citation included in private documentation. 18 campaign stages plus Aztec and Egyptian; Aztec remains unplayable due missing converted map.
- [x] Added mission selector, loaded stage transition, per-stage progress reset/save, and objective HUD within the actual embedded-asset world explorer (not the obsolete public demo).
- [x] Added reconstructed gameplay objective markers anchored when possible to raycast floor triangles from source converted maps: E interact/collect/reach/extract, firearm shoot for red destroy markers, extract gated by other objectives; persistent completion.
- [x] Surface 1 / Surface 2 reference missions select the same available Surface asset, not fabricated second source map.
- [x] Moved old game files forward intact to `GoldenEye_World_Explorer_v33_MISSIONS_AND_OBJECTIVES.zip` and added `V33_MISSION_REFERENCE.json`, `V33_PROGRESS_AND_OPEN_ISSUES.md`. All previous auxiliary research/tracking files retained byte-for-byte; Node JavaScript syntax, ZIP CRC, and source/HTML sync tested.
- [ ] **Critical:** This is explicitly a mission training SIMULATION, not original complete single-player campaign. Original pad/setup coordinates, object identity placement, AI scripts, hostage/survival logic, cutscenes, original mission triggers, timing, fail conditions and difficulty-specific rules are still not decoded.
- [ ] Decode source stage setup and all mission/guard/AI logic, then populate original object/pad transforms. Replace stand-ins only when evidence supports authenticity.
- [ ] Validate mission markers are accessible and all objective flows work on each map using Chromebook WebGL playtesting. Some maps have incomplete floors or missing geometry.
- [ ] Restore Aztec source map, multiple original objective-object instances, civilians/scientists, rescue escorts, real explosives and scripted enemies.
- [ ] Explicit user approval required; previous unresolved requirements and user approvals below unchanged.

## 2026-11-12 — v3.2 private playable map object-placement research (NOT user-approved)

- [x] Inspected the current v3.1 private playable ZIP and 4,565-file decoded asset archive; no decoded original stage setup/pad object tables were present. Game-derived model identity **does not** prove authored placement.
- [x] Added source-floor-raycast object-placement panel to the actual 79 MB asset-embedded world explorer. Users can choose any recovered `ENV.propModels` model and place it on an original decoded walkable floor under the crosshair.
- [x] Per-map manual placements persist locally; portable JSON export/import with coordinate-system and provenance labels, validation, per-map undo and clear. Imported placements are explicitly **unverified**, not presented as original level setup locations.
- [x] Added `V32_PLACEMENT_SOURCE_AUDIT.json` and `V32_PROGRESS_AND_OPEN_ISSUES.md` inside the private ZIP. All 12 original non-game auxiliary files were verified byte-for-byte unchanged; game HTML and source module kept synchronized; Node JS syntax and ZIP integrity passed.
- [ ] Decode original stage setup files and pad/preset positions from user-owned source data for every map, including doors, object IDs, flags, guards, path networks and scene coordinate transforms.
- [ ] Validate original authored object transform mapping against each CAFF level with a scene overlay. Only then replace biome-based / randomly reconstructed scatter with authenticated instances.
- [ ] Continue missing original geometry draw recovery and source UV/shader repair for heavily incomplete maps; Aztec still unresolved.
- [ ] Add collision validation, performance measurements, on-device screenshot QA and user-approved test results before marking features accepted.
- [ ] The historical master checklist below and all previous unresolved bugs remain applicable and untouched.

## 2026-11-12 — Private v3.1 map geometry / texture audit (implementation; not user-approved)

- [x] Audited all 23 map GLBs actually embedded in the v3.0 playable HTML, compared against recovered original CAFF draw records and texture descriptors. Report stored as `V31_MAP_COVERAGE_AUDIT.json` in new private ZIP.
- [x] Found serious missing geometry draw records, especially Statue Park (82/518 represented), Library (14/66), Complex (14/43), Surface (87/215), and Dam (229/391). These are coverage proxies; **none are certified complete**.
- [x] Removed hash-based random assignment of a level's textures and forced planar UV override in the existing bright-material function. Now preserves the specific originally embedded GLB texture and UV mapping for each decoded mesh, with optional faithful unlit display.
- [x] Added per-level on-screen source geometry/texture diagnostic and separate documentation. Existing v3.0 binary-embedded game and historical tracking files are preserved; no geometry is fabricated as original.
- [x] JavaScript syntax check and ZIP integrity check passed, and all original auxiliary archive files were byte-for-byte preserved.
- [ ] Recover missing draw batches for heavily incomplete maps from original game CAFF geometry and texture mapping tables.
- [ ] Confirm every original shader/image binding and UV geometry by evidence and visual Chromebook QA. Authored source textures are not proven correct just because a GLB contains them.
- [ ] Rebuild Aztec map (not decoded/available in the 23-map list), and examine missing Frigate skydome source.
- [ ] Test every map for entrances, collision, holes, ramps, spawns and missing rooms; preserve earlier open defects and all prior user approval states.

## 2026-11-12 — Private playable v3.0 rig movement and clip-import work (NOT user-approved)

- [x] Implemented source-label-based reconstructed character pivot hierarchy: BASE → BACK → NECK/SHOULDER → ELBOW → WRIST and BASE → HIP → KNEE → ANKLE, grounded in 217 CAFF skin-chain strings from 42 original-character metadata reports.
- [x] Reworked playable reconstructed character and NPC guards' fallback walk/run, firing, hit and staged falling animation states. These are reconstructed motions, **not actual original source keyframe clips**.
- [x] Added optional local animated glTF/GLB clip import and quaternion-channel mapping to matching source-labeled pivots with AnimationMixer. Imported clips are preview only and may need retarget calibration.
- [x] Created `V30_SOURCE_RIG_RELATIONSHIPS.json` source audit and `V30_PROGRESS_AND_OPEN_ISSUES.md` inside v3.0 private package; preserved previous v2.8/v2.9 research and tracking.
- [x] Verified 218 decoded GLB models in the Library asset archive contain zero `skins` and zero `animations`. Thus no native GoldenEye motion was actually decoded from these files; DO NOT mark original animation restoration complete.
- [x] Static tests and JavaScript syntax passed; no full WebGL/Chromebook gameplay test was performed.
- [ ] Locate original animation bank bytes from user-owned N64/XBLA source; decode authentic keyframes, timebase, bone matrices and skin weights.
- [ ] Verify original animation identities/relationships, bone axis conventions, per-character retargeting and browser playback across all movement states.
- [ ] Test game and optional GLB import on Chromebook; resolve head-parenting, reaction, foot sliding and other bugs reported.
- [ ] Explicit user approval for any item after practical testing. No prior master checklist approvals changed.

## 2026-11-12 — Private playable v2.9 Library ZIP (additive; NOT user-approved)

- [x] Created `GoldenEye_World_Explorer_v29_DENSE_EXTERIORS_AND_RIG_RESEARCH.zip` from the actual asset-embedded v2.8 private archive in ChatGPT Library. This is implementation, not acceptance.
- [x] Added `populateDenseSourceExterior` to target 486 additional existing-source tree and cover prop placements outside nine preserved outpost sites, on top of the original ~54 source cover props. Count varies with map/assets; reports actual numbers.
- [x] Left original embedded game-derived assets, existing rig audit, original animation ID catalog, reverse-engineering notes, release notes and tests unchanged.
- [x] Added `V29_PROGRESS_AND_OPEN_ISSUES.md` inside private ZIP for additional implementation and open issues.
- [ ] User-confirmed Chromebook in-game test: source trees, terrain placement, performance, outpost doors and movement collision.
- [ ] Native Xbox/XBLA original keyframe/skeleton decoder (CAFF/XEX) with validated bones, animations and source model relationships.
- [ ] User approval of any v2.9 features.
- [ ] Additional full master tracker items still apply unchanged below.

## 2026-11-12 — Public viewer animation / exterior work

- [x] Code added: deterministic generated exterior with four outposts and ~10× (540 target) scattered tree/cover instances. **Not user-approved or playtested.**
- [x] Code added: show real placement counts, boundary walls and simple obstacle collisions; real movement QA pending.
- [x] Code added: glTF skin/animation relationship inspection CLI.
- [x] Code added: authored glTF clip playback when present with name-based idle/walk/run/fire/hit/death selection; no proof that local exports include original clips.
- [x] Code fix: remove invalid `a.body` access in procedural walking.
- [ ] Decode proprietary Xbox/XBLA CAFF animation banks, times, transforms and original source skeleton relationships.
- [ ] Identify validated source character-to-skeleton and animation ID mappings.
- [ ] Test generated scenery, character animation and collision on Chromebook WebGL.
- [ ] Port these changes into the separately distributed v2.8 private asset-embedded viewer when that actual source is available.
- [ ] Obtain user's explicit acceptance/approval of new features.

# GoldenEye XBLA — Master Development Tracker

Updated 2026-11-11, v1.9. Goal: polished playable exploration with complete assets, movement, audio, map building and optional missions.

**Progress semantics:** `IMPLEMENTED — VERIFY` means coded but **not approved**. All approval checkboxes remain `[ ]` until the user explicitly approves the corresponding ID. When a feature regresses, set its status to BROKEN and uncheck its approval. Keep IDs stable; new features get new IDs. Syntax tests are not gameplay tests.

**User priority:** No multipart archives. One compressed ZIP with one ready-to-play HTML and bundled models. Preserve free traversal while stair/solid-wall collision is being rebuilt.

## A — Movement & core gameplay

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-001 | One ZIP containing one asset-embedded HTML | IMPLEMENTED — VERIFY | [ ] |
| GE-002 | Chromebook local-file execution with Three.js CDN | IMPLEMENTED — VERIFY | [ ] |
| GE-003 | Map selection (23 map meshes) | IMPLEMENTED — VERIFY | [ ] |
| GE-004 | Character selection (42 partial models) | IN PROGRESS | [ ] |
| GE-005 | Original gun/item model selection and viewmodel (62) | IMPLEMENTED — VERIFY | [ ] |
| GE-006 | Adjust individual weapon rotation and orientation | IMPLEMENTED — VERIFY | [ ] |
| GE-007 | Smooth movement acceleration and stopping | IMPLEMENTED — VERIFY | [ ] |
| GE-008 | Sprinting plus stamina drain/recovery | IMPLEMENTED — VERIFY | [ ] |
| GE-009 | Crouch and camera height | IMPLEMENTED — VERIFY | [ ] |
| GE-010 | Jump and gravity | IMPLEMENTED — VERIFY | [ ] |
| GE-011 | Accurate fall damage | IN PROGRESS | [ ] |
| GE-012 | Climb every Facility staircase without getting stuck | BROKEN / IN PROGRESS — some stairs still blocked; v2.6 fall controller does not recover missing original stairs | [ ] |
| GE-013 | Solid wall collision | BROKEN — disabled by default | [ ] |
| GE-014 | Accurate floor, slope and platform handling | IN PROGRESS — v1.2 last-known-safe-floor fallback | [ ] |
| GE-015 | Third-person camera occlusion handling | IMPLEMENTED — VERIFY | [ ] |
| GE-016 | First-person bob/lean/sprint FOV | IMPLEMENTED — VERIFY | [ ] |
| GE-017 | Safe spawn point for every map | IN PROGRESS | [ ] |
| GE-018 | Respawn and recovery | IMPLEMENTED — VERIFY | [ ] |
| GE-019 | Mouse sensitivity, FOV, keybind settings | PLANNED | [ ] |
| GE-020 | Gamepad/controller support | PLANNED | [ ] |
| GE-021 | Touch/mobile controls | PLANNED | [ ] |
| GE-022 | Save input and UI settings | IN PROGRESS | [ ] |

## B — Characters and animation

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-023 | Repair Boris original character mesh/vertex layout | IN PROGRESS | [ ] |
| GE-024 | Boris pants/leg/shoe textures | IN PROGRESS | [ ] |
| GE-025 | Decode character skeleton and skinning weights | PLANNED | [ ] |
| GE-026 | Decode original walk/run/idle/crouch animations | BLOCKED — source decoder needed | [ ] |
| GE-027 | Retarget locomotion to all character assets | PLANNED | [ ] |
| GE-028 | Fix 42 character orientations/scales | IN PROGRESS | [ ] |
| GE-029 | Complete face/clothing materials | IN PROGRESS — source face/clothing atlas preview, UVs unrecovered — planar texture preview for 4 characters; original UVs missing | [ ] |
| GE-030 | Hands grip weapon and original reload animations | PLANNED | [ ] |
| GE-031 | Correct third-person stride/turning | IN PROGRESS — procedural leg deformation, not game rig | [ ] |
| GE-032 | Character preview and 360-degree inspect | PLANNED | [ ] |

## C — Maps, texture and asset completeness

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-033 | Decode all XBLA CAFF source bundles (489/499 passed) | IN PROGRESS | [ ] |
| GE-034 | Finish Aztec background extraction | BLOCKED | [ ] |
| GE-035 | All 24 level geometry exports complete | IN PROGRESS — 23 partial maps | [ ] |
| GE-036 | UV/material references restored on every map | IN PROGRESS — original UVs incomplete; PPK rainbow from lookup image 003 corrected to source diffuse 005 in v2.4 (unverified visually) | [ ] |
| GE-037 | Apply all 3039 source-decoded textures | IN PROGRESS | [ ] |
| GE-038 | Glass/transparency/decals/emissive materials | PLANNED | [ ] |
| GE-039 | Original props and placement transforms | PLANNED | [ ] |
| GE-040 | All original Facility/stage doors and animations | IN PROGRESS — v2.4 source-wall exit scan plus game-textured ramps; original authored door coordinates and doorway cutouts missing | [ ] |
| GE-041 | Mantling through real window openings | IN PROGRESS | [ ] |
| GE-042 | Separate real level collision and navigation mesh | PLANNED | [ ] |
| GE-043 | Reconstructed proper stair/ramps colliders | BROKEN — some original stair volumes remain unwalkable; original collision mesh not recovered | [ ] |
| GE-044 | Elevators/ladders/moving platforms | PLANNED | [ ] |
| GE-045 | Gun/prop textures and UV maps | IN PROGRESS — provisional projected gun images | [ ] |
| GE-046 | Fix rotated and disconnected weapon meshes | IN PROGRESS — wristwatch source geometry/face material improved; original wristwatch UVs unverified | [ ] |
| GE-047 | Original level fixture lights | PLANNED | [ ] |
| GE-048 | Level streaming/LOD/Chromebook optimization | PLANNED | [ ] |

## D — Sounds, lighting, polish

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-049 | Generated footsteps for walking/sprinting | IMPLEMENTED — VERIFY | [ ] |
| GE-050 | Weapon sound/flash/cosmetic recoil | IMPLEMENTED — VERIFY | [ ] |
| GE-051 | Jump, fall and landing sounds | IMPLEMENTED — VERIFY | [ ] |
| GE-052 | Ambient environmental synthesized sound | IMPLEMENTED — VERIFY | [ ] |
| GE-053 | Audio toggle and volume | IMPLEMENTED — VERIFY | [ ] |
| GE-054 | Decode original game audio | PLANNED | [ ] |
| GE-055 | Spatial reverb and sound occlusion | PLANNED | [ ] |
| GE-056 | Day/night lighting presets and fog | IMPLEMENTED — VERIFY | [ ] |
| GE-057 | Map-specific lighting/material polish | IN PROGRESS | [ ] |
| GE-058 | Polished menus/loading/error state | IN PROGRESS | [ ] |
| GE-059 | Compass, HP, stamina and exploration HUD | IMPLEMENTED — VERIFY — added ammo and armor HUD | [ ] |
| GE-060 | Graphics quality presets and FPS counter | PLANNED | [ ] |
| GE-061 | Accessibility/reduced motion/contrast/subtitles | PLANNED | [ ] |

## E — Open world, AI, missions

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-062 | Choose and explore any converted map | IMPLEMENTED — VERIFY | [ ] |
| GE-063 | Next World button/world navigation | IMPLEMENTED — VERIFY | [ ] |
| GE-064 | Procedural discovery landmarks | IMPLEMENTED — VERIFY | [ ] |
| GE-065 | Persist discoveries and visited maps | IMPLEMENTED — VERIFY | [ ] |
| GE-066 | Actual in-world connected map portals | PLANNED | [ ] |
| GE-067 | Large outdoor connected explorable world | PLANNED | [ ] |
| GE-068 | Generate random maps from modular rooms | PLANNED | [ ] |
| GE-069 | Procedural terrain/buildings/objectives | PLANNED | [ ] |
| GE-070 | Animated NPC guards and patrols | PLANNED | [ ] |
| GE-071 | Real weapon hits, damage and ammo | PLANNED | [ ] |
| GE-072 | Mission objectives and saves | PLANNED | [ ] |
| GE-073 | Original doors/windows interactive gameplay | PLANNED | [ ] |
| GE-074 | Free exploration vs missions modes | PLANNED | [ ] |

## F — Testing and delivery

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-075 | Syntax check every game release | IMPLEMENTED — VERIFY | [ ] |
| GE-076 | Verify single-ZIP integrity | IMPLEMENTED — VERIFY | [ ] |
| GE-077 | Graphical Chromium/Chrome playtest | BLOCKED — local URL refused | [ ] |
| GE-078 | User-approved working stairs | BROKEN — unapproved | [ ] |
| GE-079 | 8GB Chromebook performance stress test | PLANNED | [ ] |
| GE-080 | All-maps regression smoke tests | PLANNED | [ ] |
| GE-081 | Asset provenance and conversion quality metadata | IN PROGRESS | [ ] |
| GE-082 | Repo versioning and downloadable source history | IN PROGRESS | [ ] |

## v0.9 implementation notes
- Momentum walking, sprint/stamina, crouch, jumping and camera effects.
- Web Audio synthesized footsteps, gunshots, jumps, landings, ambiance, discoveries; sound toggle/volume. These are **not** decoded GoldenEye audio recordings.
- Day/night lighting and fog, discovery waypoint markers, compass distance, progression stored locally where permitted.
- Preserved v0.8 embedded 23 maps / 42 characters / 62 item models, first-person gun selection and camera.
- The user-download package contains the full HTML source and conversion report. Original game models and texture data are **not** included in this public GitHub repo.

## QA and next implementation order
1. Fix GE-012/013/042/043: robust stairs and separate collision. Do not revert to a character-sticking collision system.
2. Fix GE-023–029: recover actual original character mesh and skeletal animations.
3. Finish GE-035–040/045: missing geometry, authentic textures, doors and props.
4. Add GE-060/079 performance settings and Chromebook GPU tests.
5. Expand GE-066–074 linked worlds, random maps, combat, NPCs and missions.

**Test evidence:** v0.9 Node JavaScript syntax passed. ZIP integrity passed. Chromium smoke testing was attempted but the local HTTP URL was blocked by an administrator policy; graphical functionality remains unverified. User approval is pending for every item.

## G — v1.0 HUD, tactical map, materials and interactive door showcase

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-083 | Ammo and reserve UI | IMPLEMENTED — VERIFY | [ ] |
| GE-084 | Per-weapon magazine reload empty trigger | IMPLEMENTED — VERIFY | [ ] |
| GE-085 | Armor absorption and meter | IMPLEMENTED — VERIFY | [ ] |
| GE-086 | Health and armor pickups | IMPLEMENTED — VERIFY | [ ] |
| GE-087 | Full level map projected from converted geometry | IMPLEMENTED — VERIFY: original M-key full map still in v2.2; v2.3 adds always-visible minimap | [ ] |
| GE-088 | Map player heading door and waypoint markers | IMPLEMENTED — VERIFY | [ ] |
| GE-089 | Three recovered door meshes shown in Facility | IMPLEMENTED — VERIFY — test placements | [ ] |
| GE-090 | Decode original accurate Facility door coordinates | BLOCKED — stage setup parser needed | [ ] |
| GE-091 | Door interactions and relocating via game controls | IMPLEMENTED — VERIFY | [ ] |
| GE-092 | Authentic char and gun UV texture restoration | IN PROGRESS — projected texture preview only | [ ] |
| GE-093 | Original character skeletal animations | BLOCKED — rig parser needed | [ ] |
| GE-094 | Ten original-created synthesized WAV effects | IMPLEMENTED — VERIFY | [ ] |
| GE-095 | Original game audio decoding | PLANNED | [ ] |
| GE-096 | Interactive browser playtest of complete v1.0 | BLOCKED — browser launch timed out | [ ] |

All new checkboxes remain unchecked pending direct user approval. Three Facility doors use converted original geometry at grounded **test positions**, not authentic authored door coordinates. Source UVs are unavailable for most models, so provisional planar projection is opt-in. WAV effects are newly synthesized, not original game audio. JavaScript syntax and ZIP CRC verified; graphical Chromium test timed out.

## H — v1.1 authentic-source doors and surrounding world

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-097 | Remove previously fabricated door panels, surrounds and orange dots | IMPLEMENTED — VERIFY | [ ] |
| GE-098 | Use original XBLA prop geometry for visible door leaves | IMPLEMENTED — VERIFY | [ ] |
| GE-099 | Bind original door texture images using source UVs | IN PROGRESS — currently projected UVs only | [ ] |
| GE-100 | Recover authentic Facility door locations/rotations | BLOCKED — stage placement parser needed | [ ] |
| GE-101 | Enable adjustable source-door showcase positions | IMPLEMENTED — VERIFY — not game placement | [ ] |
| GE-102 | Convert original Surface outdoor terrain triangles | IMPLEMENTED — VERIFY — 3878 source faces | [ ] |
| GE-103 | Show repositioned original Surface ground outside Facility | IMPLEMENTED — VERIFY — original adjacency not known | [ ] |
| GE-104 | No fabricated hills/trees/terrain meshes for exterior | IMPLEMENTED — VERIFY | [ ] |
| GE-105 | Authentic Facility external boundaries and stage transitions | PLANNED | [ ] |
| GE-106 | Chrome graphical test of exterior and door visuals | IN PROGRESS — user verification needed | [ ] |

**Source accuracy:** Converted game door meshes now replace generated flat panels, proxy frames and glowing orbs. Textures come from recovered source prop sheets, but UV mapping is provisional. Exact Facility door transforms have **not** been recovered. Exterior is 3,878 original faces from the *Surface* map translated vertically (+62 scene units) and clipped away from the Facility area: **no artificial polygons, trees or hills**. This is not the original geographical adjacency of the two maps. Feature approvals remain unchecked. JS syntax and ZIP integrity checks passed; graphical playtesting still pending.

## I — v1.2 falling-through-ground recovery and character texture audit

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-107 | Keep player above last confirmed ground height when imported floor has a hole | IMPLEMENTED — VERIFY (safety toggle ON by default) | [ ] |
| GE-108 | Prevent lower, misplaced mesh from pulling grounded player through a floor | IMPLEMENTED — VERIFY (threshold-based) | [ ] |
| GE-109 | Add user toggle to disable safety for testing real drops | IMPLEMENTED — VERIFY | [ ] |
| GE-110 | Reconstruct all actual missing visible ground polygons using original asset sources | IN PROGRESS — not solved; safety is invisible | [ ] |
| GE-111 | Catalog recovered face/clothing images for every available character | IMPLEMENTED — VERIFY (41 auto pairs; Boris manual) | [ ] |
| GE-112 | Preview face atlas separately from clothing atlas on each character | IMPLEMENTED — VERIFY (approximate projection, not original UVs) | [ ] |
| GE-113 | Suppress flattened incorrectly converted character mesh ribbons in atlas preview | IMPLEMENTED — VERIFY; conservative bounds checks | [ ] |
| GE-114 | Recover exact source vertex texture coordinates and skeletal rig for all characters | BLOCKED — CAFF mesh format decoding unfinished | [ ] |
| GE-115 | Verify textured character previews on ChromeOS visually | NEEDS USER TEST — no browser runtime validation | [ ] |

### Limitations of v1.2

The ground-safety layer prevents unsupported falls by **retaining confirmed height**; it does not paint a fake floor and will not repair visible source map gaps. It deliberately changes fall behavior where geometry is incomplete. Source texture pairing uses original recovered images, but UV positions are projected and do not reproduce the game atlas binding, so characters are **not yet visually accurate recreations**. Boris's previous custom work is exempt from automatic remapping. No entry above is user-approved until the user tests and confirms it.

## J — v1.3 Source map textures, floor tracking and footstep audio

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-116 | Restore source-material associations on all converted level draw batches | BROKEN — materials rendered black in user testing: 22 newly textured maps + existing Facility | [ ] |
| GE-117 | Decode exact original vertex UV layout/scale on every level | IN PROGRESS — signed-16 UV extraction, several scales unverified | [ ] |
| GE-118 | Retain unconvertible/invalid source draw batches as vertex-color geometry | IMPLEMENTED — VERIFY | [ ] |
| GE-119 | Choose spawns from walkable original geometry rather than top-down roof hits | IMPLEMENTED — VERIFY: offline per-map candidate positions | [ ] |
| GE-120 | Stop roof-snapping from high step-up tolerance | IMPLEMENTED — VERIFY: cap near 0.68 scene units | [ ] |
| GE-121 | Disable relocated Surface ground on initial load | IMPLEMENTED — VERIFY | [ ] |
| GE-122 | Keep footstep audio distinct from gunfire samples | IMPLEMENTED — VERIFY: quiet lowpass footstep synthesis | [ ] |
| GE-123 | Check each source-textured level visually for correct UVs and sky/floor materials | NEEDS USER TEST | [ ] |
| GE-124 | Verify all level spawns are inside intended traversable areas | NEEDS USER TEST | [ ] |
| GE-125 | Restore Aztec background to complete 24-map library | BLOCKED — CAFF parser exception | [ ] |

**v1.3 source integrity:** Source texture indices are read from original 0x2d material-slot records and mapped to preserved `batch_NNN` draw labels. Source texture pixels are from the user's asset archive. UV coordinate offset/scale remains partly heuristic and needs validation; these are not guaranteed complete authentic textured maps. The new v1.3 standalone HTML is bundled in one ZIP; extracted copyrighted game assets are not published on GitHub. Ground candidate spawns are computed from original floor triangle centroids rather than a ray from the top of the level, but require playtesting. All approval boxes remain empty.

## K — v1.4 recovered-texture environment generation

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-126 | Repair white/blank converted map surfaces from source textures | IMPLEMENTED — VERIFY: planar fallback, not exact original UVs | [ ] |
| GE-127 | Select only original map-owned Xbox textures for procedurally assembled environments | IMPLEMENTED — VERIFY: 92 game-derived texture images across 23 maps | [ ] |
| GE-128 | Generate continuous exterior ring with rolling terrain outside source map footprints | BROKEN in v1.8 — Archives exterior ground used a painting; v1.9 curated source ground pending playtest | [ ] |
| GE-129 | Generate textured connecting paths using source game textures | IMPLEMENTED — VERIFY: placement is procedural, not authentic | [ ] |
| GE-130 | Convert recognizable game-source crates, barrels, barricades, vehicles and trees | IN PROGRESS — original props exist but vehicle surfaces white in v1.8; v1.9 batch materials pending playtest | [ ] |
| GE-131 | Place original prop meshes near player and in outdoor surroundings | IN PROGRESS — props placed but several white / incorrect material assignments in v1.8 | [ ] |
| GE-132 | Automatically switch biome style for each selectable map | IMPLEMENTED — VERIFY: heuristic snow/forest/urban/rock/industrial categories | [ ] |
| GE-133 | Toggle map texture repair, outdoor generation and prop population separately | IMPLEMENTED — VERIFY | [ ] |
| GE-134 | Guarantee collision-safe seamless navigation across every outdoor/indoor transition | IN PROGRESS — v2.6 physical fall-through and real terrain fallback, user test pending | [ ] |
| GE-135 | Restore all original map texture UV bindings without reprojecting | IN PROGRESS — CAFF vertex format decoding required | [ ] |
| GE-136 | Validate map visuals and prop scale/placement interactively on Chromebook | NEEDS USER TEST — browser local file blocked in test environment | [ ] |

**Accuracy and source policy:** v1.4 programmatically creates **new terrain/road/path geometry**, as explicitly requested, but it uses recovered game textures only. Plants, vehicles and environmental objects are **converted game-source meshes**, not substituted cone-tree or placeholder models. Terrain shape, prop placement, biome choices and roads are generated rather than actual GoldenEye level-authored layouts. Some object textures are planar-projected because authentic source UV decoding is unfinished. Exteriors are a reconstructed annex, not the original outdoor level. No feature approvals have been checked.

## L — v1.5 visible texture recovery and complete asset coverage audit

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-137 | Audit all 23 embedded level GLBs and source image references | IMPLEMENTED — VERIFY: 23/23 GLBs parsed; 518836 triangles | [ ] |
| GE-138 | Exclude pure white/black decals and masks from fallback environment textures | IMPLEMENTED — VERIFY: 4–6 per-map original-source textures | [ ] |
| GE-139 | Apply per-face planar UV fallback to invalid converted map texture charts | BROKEN — v1.5/v1.6 black maps: live renderer, Chromebook test pending | [ ] |
| GE-140 | Retain valid Facility UVs and preserve glass/transparent materials | IMPLEMENTED — VERIFY: conditional repair | [ ] |
| GE-141 | Reduce overexposed lighting washing out source materials | IMPLEMENTED — VERIFY | [ ] |
| GE-142 | Clean up temporary material buffers when switching levels | IMPLEMENTED — VERIFY | [ ] |
| GE-143 | Verify source atlas and material appearances visually on ChromeOS for each level | NEEDS USER TEST — headless test blocked | [ ] |
| GE-144 | Reconstruct exact source UVs, full original geometry and missing Aztec | IN PROGRESS / BLOCKED — source decoder research | [ ] |

All 23 available converted GLB files can be reopened and have source texture images, and all are present in the standalone build. This **does not mean every map is historically complete or that all UVs are accurate**. New default reprojection uses only recovered game images. 3D browser testing is blocked; no visual user approval is recorded. Aztec remains missing and several maps have very incomplete geometry.

## M — v1.6 reported black maps and Snowguard body regression

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-145 | Dam converted scene too dark / source-mesh occluders | BROKEN — user reports maps still black (lighting and 34 huge-face removals) | [ ] |
| GE-146 | Bunker and Bunker 2 mostly black views | BROKEN — user reports black in v1.6 (lighting and oversized-face filtering) | [ ] |
| GE-147 | Cavern black / unlit underground surfaces | BROKEN — user reports black in v1.6 (near-camera fill and emissive map) | [ ] |
| GE-148 | Statue Park malformed giant triangles | IMPLEMENTED — VERIFY (experimental face filtering) | [ ] |
| GE-149 | Preserve genuine snow/concrete/shadow texture images instead of blanket rejecting white and dark images | IMPLEMENTED — VERIFY (conservative source image checks) | [ ] |
| GE-150 | Snowguard source head and original face map retained | BROKEN — head still invisible in v1.6 user playtest (projected UV preview) | [ ] |
| GE-151 | Replace Snowguard's disconnected flat body with coherent original-atlas uniform and articulated limbs | BROKEN — user reports Snowguard undersized in v1.7; v1.8 normalized proportions pending test (provisional reconstruction only) | [ ] |
| GE-152 | Ground third-person characters correctly and preserve animation vertical offset | IN PROGRESS — v1.7 Snowguard was too short; new proportion correction awaits test | [ ] |
| GE-153 | Restore authentic Snowguard body mesh and original skeletal animation | NOT DONE — original decoder needed | [ ] |
| GE-154 | Graphical Chromebook test of Dam, Bunker, Cavern and Snowguard | NEEDS USER REVIEW — browser GPU unavailable here | [ ] |

The new v1.6 single-file explorer includes camera fill lighting and emissive texture illumination, conservative original map-image filtering, and per-map huge triangle removal: Bunker 3,388, Bunker 2 3,401, Statue Park 17,255, Dam 34, Cavern 8. These are experimentally classified triangles and may include legitimate source faces; original assets remain unchanged in the user's master archive. Snowguard retains the real source head and texture atlases but the body geometry is reconstructed, not recovered. Existing character vertical placement is repaired. These are unverified JS/static checks; browser WebGL test blocked. No user approval is recorded.

## N — v1.7 rollback for black maps and missing Snowguard head

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-155 | Never overwrite Facility’s known-working original GLB materials/UVs | IMPLEMENTED — VERIFY in v1.7; no visual playtest | [ ] |
| GE-156 | Source-textured unlit fallback on non-Facility maps to avoid black shader output | IMPLEMENTED — VERIFY in v1.7; visual verification needed | [ ] |
| GE-157 | Per-batch image readability test, with original-game fallback textures only | IMPLEMENTED — VERIFY; all 23 map image sets decode | [ ] |
| GE-158 | Explicit visible Snowguard head volume and original face atlas | IMPLEMENTED — VERIFY; provisional rig and face placement | [ ] |
| GE-159 | Confirm Facility, Bunker, Cavern and Snowguard visually on Chromebook | NEEDS USER TEST; previous v1.6 failed | [ ] |

**Regression rule:** The user reported black textures, including Facility, and Snowguard's missing head in v1.6. Previously marked code-ready items GE-116, GE-139 and GE-145–147 and GE-150 are now marked BROKEN pending new verification. v1.7 bypasses global material overrides on Facility and switches the other maps to source-textured MeshBasicMaterial with recomputed UVs. A clearly visible hood/head is provisionally constructed using Snowguard's own original face pixels. This is not genuine original skeletal animation or complete accurate UV mapping. All user approvals remain unchecked. Node syntax test, source-image audit and ZIP CRC passed; WebGL visual testing unavailable.

## O — v1.8 game-prop materials, all-character previews, Slappers and mines

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-160 | Correct black world-object textures using their original prop texture sheets | IMPLEMENTED — VERIFY: 17 source prop texture choices, unlit materials | [ ] |
| GE-161 | Select original recovered source texture images for every weapon/item | IMPLEMENTED — VERIFY: 63 weapon/item images, provisional projected UVs | [ ] |
| GE-162 | Rebuild coherent connected third-person bodies for characters with failed mesh conversion | BROKEN / UNDER REVIEW — user reports generic heads; v2.2 loads real source head meshes, not verified in Chrome | [ ] |
| GE-163 | Show each character's real source face and clothing atlas rather than a generic face | BROKEN IN v2.4 — face/body texture selection reversed for some characters; v2.5 audited 4 swapped pairs, source head UVs still open | [ ] |
| GE-164 | Preserve existing Boris character model during generalized preview changes | IMPLEMENTED — VERIFY | [ ] |
| GE-165 | Restore standard adult height across character previews; Oddjob shorter, Jaws taller | IMPLEMENTED — VERIFY: ~1.78m adults, 1.52m Oddjob, 2.02m Jaws | [ ] |
| GE-166 | Walk/sprint with articulated shoulders, elbows, hips and knees | BROKEN / UNAPPROVED — v1.9 procedural animation rejected by user; original source clips unavailable | [ ] |
| GE-167 | Add Slappers as a selectable first-person unarmed melee weapon | IN PROGRESS — Slappers input/hit logic works in code; authentic original model/animation unavailable | [ ] |
| GE-168 | Animate alternating left/right melee swing, impact checks and sound | BROKEN / UNAPPROVED — synthetic swing/audio rejected; v2.0 hides fabricated motion, original PCM cue candidate now available | [ ] |
| GE-169 | Restore original Remote Mine source mesh/texture and in-game placing | IMPLEMENTED — VERIFY: 80 source triangles | [ ] |
| GE-170 | Restore original Timed Mine source mesh/texture and 5.5-second detonation | IMPLEMENTED — VERIFY: 96 source triangles | [ ] |
| GE-171 | Proximity Mine green original texture and trigger radius | IN PROGRESS — source mine textures improved; Proximity chassis not converted | [ ] |
| GE-172 | Remote trigger key, mine counters, throwing arc and explosion visuals | IN PROGRESS — source mine attachment/collision pending user playtest | [ ] |
| GE-173 | Original GoldenEye mine/slappers sound recordings and motion clips | NOT DONE — only newly synthesized effect clips | [ ] |
| GE-174 | Full ChromeOS visual interaction regression test of props, character scaling, melee and mines | NEEDS USER TEST — local test browser denied file access | [ ] |

**Accuracy:** 41 non-Boris characters have a reconstructed, articulated body using original source face/clothing sheets, not restored original skinning or game-authentic face UV layouts. Boris's previous source geometry is left alone. The original Proximity Mine texture exists, but its standalone geometry still fails decoding; the source Remote Mine chassis is a temporary visual substitute. Slappers hands, all gait motion, effects and sound clips are procedural recreations. World objects now use their own original game-source texture imagery, but UV projection remains approximate. Prior Snowguard height regression was not approved. The v1.8 local asset archive passed JavaScript syntax and embedded mesh/image checks; graphical Chromium access remained blocked. All user approvals remain unchecked.

## P — v1.9 curved faces, source materials, continuous world and roaming guards

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-175 | Replace square portrait plane with a curved forward-facing source-textured head surface | BROKEN — user reports same-looking faces and portrait projection on v2.1; replaced with source head mesh in v2.2 | [ ] |
| GE-176 | Correct face orientation while running forward; keep avatar local +Z as forward | BROKEN — user reported faces looking backward; v2.2 detects native head frontal direction | [ ] |
| GE-177 | Use different recovered game-source texture sheets for car wheel, body paint, glass and grille | BROKEN / UNAPPROVED — user screenshot still shows vehicles white/bad materials | [ ] |
| GE-178 | Differentiate military truck and APC body, wheel, panel material groups | IMPLEMENTED — VERIFY (per-batch source sheets) | [ ] |
| GE-179 | Stop using posters and paintings as generated ground textures | IMPLEMENTED — VERIFY (23 curated source-image palettes) | [ ] |
| GE-180 | Use 23 explicit game-owned ground/wall/path/roof material sets | IMPLEMENTED — VERIFY (92 recovered images) | [ ] |
| GE-181 | Create continuous walkable terrain below/around original level geometry | IN PROGRESS — v2.5 elevated rooms floated; v2.6 ground lowered and generated retaining walls (unverified) | [ ] |
| GE-182 | Make interior building shells around complete source maps without covering authored interiors | IMPLEMENTED — VERIFY (source wall/roof textures, generated geometry) | [ ] |
| GE-183 | Install authentic converted door models at exterior entrance and interior test locations | IN PROGRESS — generated paired source-door exterior access added, locations remain unverified | [ ] |
| GE-184 | Place source GoldenEye crates, barrels, foliage and vehicles in world surroundings | IMPLEMENTED — VERIFY (17 converted model types) | [ ] |
| GE-185 | Spawn 3 roaming Snowguard enemies with source face/uniform images | IMPLEMENTED — VERIFY (provisional articulated avatars) | [ ] |
| GE-186 | Enemy patrol, vision checks, pursuit and movement | IMPLEMENTED — VERIFY (new AI state machine, not original) | [ ] |
| GE-187 | Enemy firing, damage, death, respawn and player armor interaction | IMPLEMENTED — VERIFY (prototype combat) | [ ] |
| GE-188 | Player weapons, Slappers and mine explosions affect nearby guards | IN PROGRESS — damage logic present, weapon and mine hit interactions not yet user verified | [ ] |
| GE-189 | Remove generated exterior, doors and NPCs on map switching | IMPLEMENTED — VERIFY (stale-load guards, no live playtest) | [ ] |
| GE-190 | Restore authentic original character faces, original stage door positions, UVs and navigation | IN PROGRESS / BLOCKED — source converters still incomplete | [ ] |
| GE-191 | Check v1.9 character faces, vehicle materials, ground surfaces and NPCs in ChromeOS | NEEDS USER TEST — headless WebGL blocked in environment | [ ] |

**Scope:** Original game maps stay the level centerpiece. The outer walls, terrain shape, paths and object placements are reconstructed code-generated geometry and layout, but use only genuine decoded XBLA texture images and converted original prop models. Character heads are curved rather than square pictures and face local +Z (the walking direction). The source-derived silver BMW, military truck and other props now have separate source-texture assignments for wheels/body/windows; UV mapping remains provisional. Three new Snowguard agents patrol, chase, can attack/take damage/respawn; AI is not the original game code. **No user approval recorded.** JS syntax, source-image decoding (92 environmental + 40 prop sheets), and one-ZIP CRC verified. Chromium local/localhost navigation returned ERR_BLOCKED_BY_ADMINISTRATOR, so graphical playtest remains pending.

## Q — v2.0 source effects, collision, loot and exploratory map access

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-192 | Decode original 30-frame Xbox firebomb CAFF image sequence | IMPLEMENTED — VERIFY: 24 coherent source frames used | [ ] |
| GE-193 | Extract original sfx.xwb/sfx.xsb PCM data without generated replacement recordings | IMPLEMENTED — VERIFY: 209 source 44.1kHz mono PCM WAV entries | [ ] |
| GE-194 | Resolve correct XSB event-to-XWB entry bindings | IN PROGRESS — cue-name string table order tentatively matched; not verified | [ ] |
| GE-195 | Replace fabricated glowing mine explosion with original firebomb sprite sequence | IMPLEMENTED — VERIFY; graphical test pending | [ ] |
| GE-196 | Original Slappers hand/fist animation/mesh | BLOCKED — source fist CAFF pool/animation decoder not ready; synthetic swing disabled | [ ] |
| GE-197 | Play provisional original-bank punch/explosion/mine/door WAV samples | IMPLEMENTED — VERIFY audio decoding, cue assignments not confirmed | [ ] |
| GE-198 | Mines use swept collision against floor, walls and doors rather than passing through | IMPLEMENTED — VERIFY (source polygons only), user test pending | [ ] |
| GE-199 | Orient stuck mines along source surface normal and display game-owned atlas | IMPLEMENTED — VERIFY | [ ] |
| GE-200 | Wall collision from actual converted source mesh with horizontal slide | IMPLEMENTED — VERIFY (not fully reconstructed collision/nav data) | [ ] |
| GE-201 | Stair lookahead for low risers with no roof teleportation | IMPLEMENTED — VERIFY, user test pending | [ ] |
| GE-202 | Recover true game collision maps and stair volumes for all original levels | BLOCKED / NOT DONE | [ ] |
| GE-203 | Source door-mesh paired portals between generated indoor shell and exterior | IMPLEMENTED — VERIFY (not original placement) | [ ] |
| GE-204 | Room-aware test crate placement near authored walls on source floor polygons | IMPLEMENTED — VERIFY (generated placement logic) | [ ] |
| GE-205 | Source box/cartridge/armor meshes exported and included | IMPLEMENTED — VERIFY, 7 newly extracted models | [ ] |
| GE-206 | Credits, plate, health, ammo loot in interactable crates | IMPLEMENTED — VERIFY (new gameplay economy) | [ ] |
| GE-207 | Buy stations using recovered source ammo crates for ammo/plates/health/weapons | IMPLEMENTED — VERIFY (reconstructed economy and UI) | [ ] |
| GE-208 | Reduce oversized vehicles and avoid spawning them immediately inside authored rooms | IMPLEMENTED — VERIFY (appearance requires test) | [ ] |
| GE-209 | Original vehicle material UV mapping / placement and correct scale across all maps | IN PROGRESS — source military truck looked wooden; remapped original batch 013/014 to tire image 009 in v2.7, pending visual test | [ ] |
| GE-210 | Restore full authored exteriors, cave/bunker entrances and object placements | IN PROGRESS — synthetic stage linkage is a test, not authentic source reconstruction | [ ] |
| GE-211 | Full acceptance test of v2.0 with stairs, collisions, mines, shops, audio on Chromebook | BROKEN in v2.0 — a syntax error prevented any gameplay from starting | [ ] |
| GE-212 | Optimize wall-ray performance and test on 8GB Chromebook | PLANNED — may be expensive on high-triangle maps | [ ] |

**User approvals:** All GE-192..GE-212 items are unchecked; no code or static test constitutes user approval. v1.9 complaints about floaty/white vehicles, wall/stair pass-through, fake Slappers and mine explosions are recorded as open regressions. The new soundbank source is actual original signed PCM and the firebomb artwork is sourced from the retail copy, but XACT cue binding needs independent parsing and the original character animations remain blocked. Generated crates, credits, gear station menus and exterior portal locations are explicitly not original GoldenEye-authored map elements.

## R — v2.0.1 mine-update parsing hotfix

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-213 | Repair v2.0 JavaScript parse crash at updateMines (Unexpected token at line 1069) | IMPLEMENTED — VERIFY in v2.0.1; user runtime test pending | [ ] |
| GE-214 | Add independent strict JavaScript AST parsing as QA gate beyond Node --check | IMPLEMENTED — VERIFY locally; zero parser diagnostics and checked mine-loop nesting | [ ] |
| GE-215 | Confirm local ChromeOS loading and gameplay after parse hotfix | NEEDS USER TEST; file:// warning may be independent | [ ] |

The user reported a startup-blocking syntax error in v2.0. The generator closed its `for (const m of gameMines)` loop before timed/proximity mine checks, leaving one extra closing brace. v2.0.1 fixes the nesting without altering source assets. All embedded JSON data parsed, the extracted module passed Node plus TypeScript AST parsing, and the new ZIP CRC matches. The separate file:// security warning is not claimed fixed. Previous regression approvals remain unchecked.


## S — v2.1 Source decode and drivable vehicle milestone

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-216 | Audit 24 original source background CAFF rendergraphs and texture descriptors | IMPLEMENTED — VERIFIED DATA (23 parse, Aztec exception) | [ ] |
| GE-217 | Report source draw counts vs extracted geometry including Library/Dam missing batches | IMPLEMENTED — VERIFIED DATA | [ ] |
| GE-218 | Recover authentic authored doors, room/setup coordinates and full vertex UV descriptors | IN PROGRESS — data not independently recovered | [ ] |
| GE-219 | Separate firearms/mines from VHS tapes, wristwatches and mission gadgets | IMPLEMENTED — VERIFY | [ ] |
| GE-220 | 3D inspect nonweapon source models without ammo or firing | IMPLEMENTED — VERIFY | [ ] |
| GE-221 | Use original watch geometry and apply source watch image to the dial rather than the entire model | IN PROGRESS — watch original UV maps still unverified | [ ] |
| GE-222 | Combine original watch body and laser source attachment for watchlaser | IMPLEMENTED — VERIFY | [ ] |
| GE-223 | Enter/exit converted original BMW, military truck and APC meshes | IN PROGRESS — reverse-facing source car issue reported by user; 180-degree visual rotation in v2.6 pending test | [ ] |
| GE-224 | WASD driving/reverse/steering, Space braking and Shift acceleration | IMPLEMENTED — VERIFY | [ ] |
| GE-225 | First-person and third-person driving camera modes using V | IN PROGRESS — first-person driver view obstructed by glass; v2.6 camera moved outside windshield (unverified) | [ ] |
| GE-226 | Accessible source BMW near generated shell entrance and J spawn action | IMPLEMENTED — VERIFY | [ ] |
| GE-227 | Three original-source door meshes at front, left and right generated shell entrances | BROKEN — user reported freestanding/random black doors; retired boundary gates in v2.2 | [ ] |
| GE-228 | Game-textured access ramp geometry through entrance wall gaps | IN PROGRESS — old boundary walkway gate placements retired; original entry geometry still missing | [ ] |
| GE-229 | Inside source-door pairs linking exterior via test interaction | BROKEN — arbitrary linked exterior portals rejected; replaced with short opposite-side wall transitions pending user test | [ ] |
| GE-230 | Accurate original car collision, suspension and vehicle steering behavior | IN PROGRESS — simple source mesh ground/wall collision only | [ ] |
| GE-231 | Validate metadata, HTML references, content count, parser and ZIP checksums | IMPLEMENTED — VERIFIED STATIC | [ ] |
| GE-232 | ChromeOS visual gameplay test of driving, watch, item classification and all three entrances | NEEDS USER TEST; no successful WebGL test | [ ] |

Source file audit confirms CAFF material commands and texture descriptors, not original stage object placement. The gameplay entrance coordinates, paths and car physics are newly coded and require user review. Tape/watch/gadget resources are classified separately from firearms. No approval checkbox is checked.

## T — v2.2 source-head conversion, wall-aligned metal doors and sprint

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-233 | Convert original XBLA head bundles into distinct source geometry | IMPLEMENTED — STATIC VERIFIED: 35 of 37 head bundles | [ ] |
| GE-234 | Replace single generic portrait sphere with original source head triangles | BROKEN IN v2.4 — multiple original head draw groups attached in wrong locations; v2.5 selects one coherent source mesh, visual test pending | [ ] |
| GE-235 | Preserve each original source portrait across one global head UV frame, not repeated per submesh | BROKEN IN v2.4 — full head atlas projected repeatedly onto disconnected fragments; v2.5 crops one front-face region, authentic UVs missing | [ ] |
| GE-236 | Detect per-source head forward face direction so faces are not painted on backs | IMPLEMENTED — VERIFY; user visual test needed | [ ] |
| GE-237 | Allow manual original head selection and flip/persistence per character | IMPLEMENTED — VERIFY; head-body pairings unverified | [ ] |
| GE-238 | Recover actual original game head-to-character attachment and authentic UV layout | IN PROGRESS / BLOCKED — stage attachment data not recovered | [ ] |
| GE-239 | Use original GoldenEye metal-door textures instead of nearly-black masks | IN PROGRESS — original source-door mesh flattened and aligned against found walls in v2.6, original cutouts absent | [ ] |
| GE-240 | Remove random freestanding/boundary gates and find nearby actual map wall faces | IMPLEMENTED — VERIFY; source-wall raycast selection | [ ] |
| GE-241 | Require walkable floor on both sides before placing a wall-mounted door | IMPLEMENTED — VERIFY; 4 candidates confirmed from Facility source geometry | [ ] |
| GE-242 | Keep E-triggered door transitions within 1.75 meters across the selected wall | IMPLEMENTED — VERIFY; no distant arbitrary teleport | [ ] |
| GE-243 | Cut genuine door openings into source wall triangles and verify original authored door coordinates | NOT DONE — door source mapping/openings undecoded | [ ] |
| GE-244 | Increase sprint duration by at least five times and offer unlimited toggle | IMPLEMENTED — VERIFY: drain 24/s → 4.8/s; unlimited default | [ ] |
| GE-245 | Runtime WebGL QA of head faces, wall doors and sprint on user's Chromebook | NEEDS USER TEST — Chromium graphics initialization failed | [ ] |

**Regression handling:** The user reported black rectangular doors, arbitrary boundary teleports, and identical fabricated character faces in v2.1. GE-175/176 and GE-227/229 remain marked BROKEN, not approved, until a real playtest. v2.2 replaces generic sphere heads with 35 genuine 3D head asset bundles; original head-to-body assignments are explicitly provisional and editable. The default exterior-boundary shell gates are disabled, source-wall door positions are derived from vertical original map polygons and two supported floor samples. E crosses just 1.75m through a mounted door; original wall polygons are not cut into doorway openings. All user acceptance checkboxes remain unchecked. The standalone JS, independent AST parser, asset JSON and ZIP CRC pass; GUI WebGL smoke test fails in container's EGL initialization, so these are unverified visually.


## U — v2.3 reproducible assets/code separation, original XEX and map/stair audit

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-246 | Deliver complete browser game source as separate asset-free JS/HTML/CSS package | IMPLEMENTED — VERIFIED STATIC: source-only ZIP 74KB | [ ] |
| GE-247 | Deliver all currently decoded model, image and original-bank WAV assets in one archive | IMPLEMENTED — VERIFIED STATIC: asset ZIP 176MB, 4562 entries | [ ] |
| GE-248 | Generate manifest of every binary asset and its source/checksum | IMPLEMENTED — VERIFIED STATIC: ASSET_MANIFEST.json | [ ] |
| GE-249 | Rebuild the standalone game from source-only ZIP plus decoded-assets ZIP | IMPLEMENTED — VERIFIED STATIC: all six embedded data objects match | [ ] |
| GE-250 | Reinstate a clearly visible HUD minimap with click-to-open full map | IMPLEMENTED — VERIFY in v2.3; game graphical test pending | [ ] |
| GE-251 | Preserve full M-key tactical map overlay and drawing | IMPLEMENTED — VERIFIED CODE: full map remains in v2.2 and v2.3 | [ ] |
| GE-252 | Improve source-only stair tread stepping to supported risers up to 1.08 units | IN PROGRESS — v2.3 code change; user reported blocked stairs; not verified | [ ] |
| GE-253 | Decode original Xbox native executable into original C/C++ game logic | NOT DONE — compiled default.xex extracted, native source not decompiled | [ ] |
| GE-254 | Extract and verify original default.xex native Xbox executable | IMPLEMENTED — VERIFIED DATA: 7,266,304 byte XEX2 binary | [ ] |
| GE-255 | Resolve original level floor, staircase and collision/navigation data | BROKEN / IN PROGRESS — current raycast proxy insufficient | [ ] |
| GE-256 | Restore authentic original game animation/event scripts | BLOCKED / NOT DONE — source animation and native executable logic undecoded | [ ] |
| GE-257 | Run full WebGL game and staircase playtest on Chromebook | NEEDS USER TEST — cannot validate in container | [ ] |

**Important:** The user asked for all actual decoded assets, original game logic and source in separate packages. This release ships 3037 compressed source texture atlases, 23 early GLB backgrounds, 195 embedded GLB resources, 209 original decoded wave-bank WAV entries, 30 source effect frames, and additional embedded source textures/samples, with a complete manifest. The resource list is complete for the CURRENTLY ASSEMBLED decoded build, but the original game's assets are **not 100% decoded**. Original Xbox compiled default.xex is provided separately inside the asset archive, as compiled machine code, NOT game source. The browser game engine/source is assistant-developed. Code-only v2.3 game source is 125218 bytes JS plus 17,451 byte HTML source shell and 6,355 byte CSS. No user approvals are claimed. The new floor stepping probe is experimental; old stair regression remains open.

## V — Original-source recovery: Aztec, failed CAFF images and new music bank

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-258 | Find and correct Aztec CAFF section alignment to parse material descriptors and original draw streams | IMPLEMENTED — VERIFIED DATA: +4096 byte section offset | [ ] |
| GE-259 | Recover Aztec original source PNG texture images | IMPLEMENTED — VERIFIED DATA: 57/57 images | [ ] |
| GE-260 | Export source-derived Aztec GLB geometry | IMPLEMENTED — VERIFIED DATA: 77 parsed draws / 26942 triangles | [ ] |
| GE-261 | Export Aztec source material textured preview with exact UVs | IN PROGRESS — material IDs original, UV normalization experimental | [ ] |
| GE-262 | Verify Aztec map contains every authored geometry batch | NOT DONE — resource stream appears truncated by 4096 bytes | [ ] |
| GE-263 | Recover Head Neil source texture images | IMPLEMENTED — VERIFIED DATA: 4 images, geometry still unsupported | [ ] |
| GE-264 | Recover Uzi magazine source texture image | IMPLEMENTED — VERIFIED DATA: 1 image, geometry still unsupported | [ ] |
| GE-265 | Recover Frigate skydome source texture images | IMPLEMENTED — VERIFIED DATA: 2 images, geometry still unsupported | [ ] |
| GE-266 | Extract original Xbox music.xwb and parse its 61 entries | IMPLEMENTED — VERIFIED DATA: 60 XMA and 1 WMA | [ ] |
| GE-267 | Provide all 61 music bank entries as playable Opus test exports | IMPLEMENTED — STATIC VERIFIED; decoder warnings on every track | [ ] |
| GE-268 | Verify original music decode fidelity and cue mappings | IN PROGRESS — music XSB stage cue NAMES present, decoded XWB wave-index links/fidelity remain unresolved | [ ] |
| GE-269 | Decode all remaining CAFF model bundles | NOT DONE — six unresolved source bundles and unsupported vertex formats | [ ] |
| GE-270 | Decode all original character animations and attach original heads/rigs | NOT DONE — animation data/source rig parser missing | [ ] |
| GE-271 | Ensure all original 3D level meshes and exact shader UV maps are recovered | NOT DONE — missing batches remain in many maps | [ ] |
| GE-272 | Deliver one audited incremental recovery archive | IMPLEMENTED — ZIP CRC, GLB reopen, PNG verification, audio probes, checksum manifest | [ ] |

**Source count audit:** Earlier archive has 3037 texture sheets. The new verified delta has 64 original images, so current collection contains 3101 texture images, with 24 source background bundles at least partially parsed. Music has 61 best-effort converted Opus exports but every one has FFmpeg warnings and cue associations remain unverified. The six failed resource bundles, original skeleton animations and complete map geometry remain open. No user acceptance boxes are checked.

## W — v2.4 source audio mapping and exterior/foundation/material corrections

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-273 | Extract and categorize all 209 original Xbox sfx XSB candidate names against PCM WAV files | IMPLEMENTED — VERIFIED DATA: source candidate catalog, cue-to-wave numeric binding not parsed | [ ] |
| GE-274 | Extract stage-named original music cues for each map, including alternate X tracks | IMPLEMENTED — VERIFIED DATA: 56 original XSB named cues; XWB wave link unresolved | [ ] |
| GE-275 | Audit proper original gunshots, metallic doors, mine SFX, melee and watch candidate cues | IN PROGRESS — v2.5 VERIFIED actual XACT cue-to-WAV numeric mapping; original model-to-event gameplay choice still partly provisional | [ ] |
| GE-276 | Find original source footstep WAV recordings and per-material footsteps | NOT DONE — no FOOT/STEP candidate cue names in 209 current sfx entries | [ ] |
| GE-277 | Provide in-browser sound-cue audition for 42 original PCM files with local event overrides | IN PROGRESS — v2.5 62 original bank clips, real cue-to-WAV mapping replaces false list-order labels, user audition pending | [ ] |
| GE-278 | Fix PPK rainbow lookup texture 003 used instead of real diffuse slide/grip sheet 005 | IMPLEMENTED — VERIFIED IMAGE SOURCE, visual runtime test pending | [ ] |
| GE-279 | Apply source image 005 to PPK, PPK Silenced, Gold PPK and Ruger where available | IMPLEMENTED — VERIFY; exact source UV maps remain open | [ ] |
| GE-280 | Normalize 35 original source head model proportions when Z is flattened or extreme | IMPLEMENTED — VERIFY; original source geometry adjusted, not original rig | [ ] |
| GE-281 | Correct source headjoe extreme depth 1.372 vs most other head depths near 0.08–0.13 | IMPLEMENTED — STATIC VERIFIED bounds; graphical test pending | [ ] |
| GE-282 | Scan for exterior-facing walls using original geometry rather than source-wall boundary coordinates | IMPLEMENTED — VERIFY: floor on inside / apparent gap outside, no authored entrance data | [ ] |
| GE-283 | Add additional game-mesh doors mounted flush with validated exit walls | IMPLEMENTED — VERIFY: up to five candidate source-wall entries, may find fewer | [ ] |
| GE-284 | Connect elevated exit thresholds down to terrain via original game-textured walkable ramps | BROKEN in v2.6 user test — ramps do not always meet doors/ground; v2.7 rebuilt, pending user test | [ ] |
| GE-285 | Generate original-game-textured foundation supports under some exposed elevated floor edges | BROKEN in v2.6 user test — supports were visual only and floating; v2.7 geometry raycast, pending user test | [ ] |
| GE-286 | Add generated ramp meshes to ground-following collision instead of leaving them visual only | BROKEN in v2.6 user test — ramps passed through by player; v2.7 analytic ramp support, pending user test | [ ] |
| GE-287 | Parse XACT cue-to-wave indices and verify original music and every sound effect event | IN PROGRESS — original 209 sfx cue-to-wave references VERIFIED; original music cue-to-track binding not yet parsed | [ ] |
| GE-288 | Check exterior entrances, ramps, head shapes, source pistol diffuse and sound in Chromebook | NEEDS USER TEST; available container lacks working graphical WebGL | [ ] |

**User-owned asset evidence:** music.xsb contains 56 named stage cues; original sound bank reports 209 PCM entries and 209 candidate XSB name strings. The relationship of XACT events to wavebank numeric indices is not parsed, so the cue audition is deliberately candidate-level. Original footstep cues not found by name. The source PPK 003 image is an unsuitable rainbow palette lookup; PPK 005 shows the real dark gun/grip diffuse texture. Original head source files are abnormally thin on the Z axis, with headjoe a large outlier. New exterior exits are detected using real original wall polygons, near-side source floors, and a lack of authoring-floor support immediately outside, with generated ramps/foundations using only recovered game textures. The shell and new geometry are reconstructed; original doors and collision data are not decoded. All user-approval boxes remain unchecked. JS + AST + embedded JSON and ZIP CRC checks passed; no visual/runtime game test.


## X — v2.5 verified Xbox XACT cue mapping and cleaned original source heads

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-289 | Confirm original Xbox XSB simple-cue offsets and decode actual cue→sound→wave links | IMPLEMENTED — VERIFIED DATA: 209/209 cue bindings; one wavebank; 209 distinct indices | [ ] |
| GE-290 | Fix mislabeled original sound: door shutter close cue 195 is wave 155, not wave 87 | IMPLEMENTED — VERIFIED DATA | [ ] |
| GE-291 | Map source original silenced PPK gun cue index 169 to PCM wave 37 | IMPLEMENTED — VERIFIED DATA | [ ] |
| GE-292 | Show original correct XACT sound cue and verified WAV index in the audio audition UI | IMPLEMENTED — STATIC VERIFIED; runtime audition pending | [ ] |
| GE-293 | Use verified named source sound effects for pistol, door, punch, mine attach, explosions and empty gun trigger | IMPLEMENTED — VERIFY; gun-class to cue relationships may still be approximate | [ ] |
| GE-294 | Preserve 209 original sound names and correct wave index in downloadable CSV/JSON | IMPLEMENTED — VERIFIED DATA | [ ] |
| GE-295 | Remove badly displaced original head model draw batches that resemble body-shaped towers | IMPLEMENTED — VERIFIED GEOMETRY: 35 source head GLBs cleaned, no fabricated polygons | [ ] |
| GE-296 | Normalize cleaned original head mesh dimensions without adding substitute head triangles | IMPLEMENTED — VERIFIED SOURCE GEOMETRY; appearance still requires user approval | [ ] |
| GE-297 | Use a single centered original source face crop on the head, not the entire repeated texture atlas | IMPLEMENTED — VERIFY; original UV mapping not recovered | [ ] |
| GE-298 | Correct reversed original character face/clothing atlas choices | IMPLEMENTED — VERIFIED IMAGE: moonguard, moonfemale, commguard, rusguard | [ ] |
| GE-299 | Preserve original actor head-to-body pairings, bone placement and face UV charts | NOT DONE — converter still lacks original rig/attachment/UV data | [ ] |
| GE-300 | Verify repaired heads and correct source audio on user's ChromeOS | NEEDS USER TEST; no successful WebGL playtest | [ ] |

The user provided screenshots of head textures stretched into body-like structures and reported that a door-labeled audio clip was actually a gun sound. v2.5 corrects the XSB sound-to-wave mapping at the binary structural level (209 verified source references) and selects one coherent original mesh for each of the 35 cleaned heads, rejecting disconnected/flattened draw fragments. No invented head triangles or generated source WAVs. Weapon class→named cue assignment, authentic vertex UV mapping and skeletal animations still require original game logic decoding. All user approvals remain unchecked.


## Y — v2.6 ground physics, raised-room support, source-door depth and car alignment

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-301 | Allow actual falling off original map edges rather than freezing on last-known support | IMPLEMENTED — VERIFY: safe ledge assist OFF by default; user test needed | [ ] |
| GE-302 | Find lower physical surfaces using down ray against original level, generated ground and ramps | IMPLEMENTED — VERIFY: original/source materials unchanged | [ ] |
| GE-303 | Swept vertical fall-to-ground collision to prevent tunneling through a thin floor at high speed | IMPLEMENTED — VERIFY: static checks only | [ ] |
| GE-304 | Retain fall damage on real landing after dropping from an elevated platform | IMPLEMENTED — VERIFY | [ ] |
| GE-305 | Lower generated source-textured exterior terrain below indoor starting floor for visible height separation | IMPLEMENTED — VERIFY: 4.2 scene units lower | [ ] |
| GE-306 | Construct game-textured retaining-wall supports beneath sampled exposed raised room floors | BROKEN in v2.6 user test — pass-through retaining walls; v2.7 collision added, unapproved | [ ] |
| GE-307 | Correct source door local depth/origin against existing vertical wall face | IMPLEMENTED — VERIFY: <=0.085 source-derived door display depth | [ ] |
| GE-308 | Cut genuine doorway openings into original wall polygons and reconstruct authored door positions | NOT DONE — model/stage setup decoder incomplete | [ ] |
| GE-309 | Align converted BMW/truck/APC visual forwards with W-forward movement | IMPLEMENTED — VERIFY: Y-axis model rotation, visual playtest pending | [ ] |
| GE-310 | Position first-person driving view in front of the original windshield obstruction | IMPLEMENTED — VERIFY: windshield-just-outside offset, visual test pending | [ ] |
| GE-311 | Full ChromeOS graphical test: fall edge, raised room, door flushness, car heading and windshield POV | NEEDS USER TEST | [ ] |
| GE-312 | Restore original per-stage supported outside terrain/ground and collision instead of reconstructed supports | NOT DONE — original stage setup/collision decoding incomplete | [ ] |

v2.6 changes are independently written prototype logic. No original game stage setup/collision or car camera code is recovered. Visual assets and textures remain the original recovered Xbox media. Full GUI gameplay testing unavailable; all approval boxes unchecked.


## Z — v2.7 walkable ramps, solid outside boundaries, authentic-source prop cover and original hit format audit

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-313 | Pair each generated outside door with a continuous visibly source-textured ramp footprint | IMPLEMENTED — VERIFY; wall cutout not yet decoded | [ ] |
| GE-314 | Use ramp-centerline mathematical height support for player climbing/descending | IMPLEMENTED — STATIC TEST PASS; ChromeOS playtest pending | [ ] |
| GE-315 | Adapt approach ramp length to entrance elevation and meet actual terrain height at endpoint | IMPLEMENTED — STATIC TEST PASS | [ ] |
| GE-316 | Make visually generated retaining/support walls physical colliders | IMPLEMENTED — VERIFY; raycast generated wall triangles | [ ] |
| GE-317 | Create source-textured world perimeter barrier that follows outside terrain | IMPLEMENTED — VERIFY | [ ] |
| GE-318 | Stop both player and driveable vehicles at the actual generated world limits | IMPLEMENTED — STATIC TEST PASS | [ ] |
| GE-319 | Place original barricade/wood/steel/ammo crate meshes in logical outdoor cover yards | IMPLEMENTED — VERIFY: 9 groups, 54 source-model placements | [ ] |
| GE-320 | Add approximate collision volumes to outdoor source-prop cover | IMPLEMENTED — VERIFY | [ ] |
| GE-321 | Repair original truck materials for wheels/canvas/body/glass using original source atlases | IMPLEMENTED — VERIFIED MODEL BATCH DATA; visual test pending | [ ] |
| GE-322 | Fix undefined `sz.z` outdoor vehicle-population code regression | IMPLEMENTED — STATIC VERIFIED | [ ] |
| GE-323 | Inventory original stage and character hit/collision source resources | IMPLEMENTED — VERIFIED DATA: 23 level hits + 42 character hits per version | [ ] |
| GE-324 | Inspect original Facility `hits` binary format before authentic collision decoding | IMPLEMENTED — VERIFIED HEADER; format decoding unfinished | [ ] |
| GE-325 | Decode original authored walk/run/get-shot/fall animations and use original source rig | NOT DONE — standalone clips not found; requires animation format/executable research | [ ] |
| GE-326 | Verify v2.7 ramp, terrain support, perimeter, truck and cover gameplay on Chromebook | NEEDS USER TEST — no graphical WebGL playtest | [ ] |
| GE-327 | Decode original collision/hit CAFF resource into stair, wall and door physics volumes | IN PROGRESS / BLOCKED — actual hit resource found, internal structure not decoded | [ ] |

**Regression discipline:** Previously delivered ramps and supports were reported visually present but non-collidable, so the old GE-284–286 and GE-306 entries remain broken until user re-approval. The v2.7 changes are new unverified implementation attempts. The source-only audit finds real Xbox collision/hit data, but no decoded original character animation clips. No source-model approval or graphical runtime success is asserted.

## AA — v2.8 source skeleton research and dense outdoor compounds

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-328 | Audit all original GoldenEye Xbox character hit CAFF resources for real skeletal/skin metadata | IMPLEMENTED — VERIFIED DATA: 42 original and 42 remastered resources | [ ] |
| GE-329 | Export original SKEL_* joint references, skin-chains and byte offsets | IMPLEMENTED — VERIFIED DATA: 765 original / 1060 remastered label entries | [ ] |
| GE-330 | Find and verify original walking/jogging/running animation source IDs | RESEARCH MAPPED — historical 0x28,0x29,0x2A IDs; XBLA frame offsets not extracted | [ ] |
| GE-331 | Identify original fire-while-walking/hit/death/fall animation IDs | RESEARCH MAPPED — historical IDs from GoldenEye animation reference catalog | [ ] |
| GE-332 | Decode real XBLA original keyframes and clip headers from native executable/animation data | BLOCKED / NOT DONE — zero original clip frames recovered | [ ] |
| GE-333 | Decode actual skin weights, bind transforms and attach source animation tracks to recovered character models | NOT DONE — only named joint and skinning-chain labels recovered | [ ] |
| GE-334 | Record real original animation ID targets during AI patrol, hit, fire and death states | IMPLEMENTED — VERIFIED CODE; NO source clip playback | [ ] |
| GE-335 | Preserve original/user-supplied asset provenance without fabricating animation clips | IMPLEMENTED — VERIFIED: no motion data labeled original | [ ] |
| GE-336 | Build actual multiroom outdoor walled compounds instead of open prop-only fields | IMPLEMENTED — VERIFY: up to 9 compounds based on original-prop yards | [ ] |
| GE-337 | Add walkable front and internal openings into generated outdoor rooms | IMPLEMENTED — STATIC VERIFIED: 3.7-unit open spans | [ ] |
| GE-338 | Add original-source-textured roof shelter and terrain-following access paths to outposts | IMPLEMENTED — VERIFY: 18 roofs and 9 paths maximum | [ ] |
| GE-339 | Collide against generated compound wall faces and skip distant wall raycasts | IMPLEMENTED — STATIC VERIFIED: generated walls shared with collision list, radius precheck | [ ] |
| GE-340 | Verify all exterior outposts, doorways, motion debug references and performance on Chromebook | NEEDS USER TEST — graphical Chromium blocked | [ ] |
| GE-341 | Locate decrypted original remaster XEX animation table/segment and recover exact binary keyframe stream | NOT DONE — compiled source XEX remains packed and animation mapping unresolved | [ ] |

**Evidence:** Original XBLA CAFF `hits` resources expose joint and skinning-chain metadata for 42 original plus 42 remastered character variants. This is not the original animation track data; `clip_frames_decoded=0`. A reference list of 62 historical N64 animation IDs is included but not claimed as decoded original Xbox bytes. Exterior compounds use newly generated walls/roofs/path GEOMETRY with original XBLA diffuse textures and original-source movable props, and feature genuinely open door widths without arbitrary teleports. No user approval boxes checked; visual gameplay remains untested.
