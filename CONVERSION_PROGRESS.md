# GoldenEye 007 — Permanent conversion progress

**v4.8 (November 12, 2026): 22/100 engineering milestone points (22%), up from 20/100 on the retrospective v4.7 baseline.**

**Fully verified playable original missions: 0 of 21.** The engineering percentage is **NOT** the proportion of missions playable, and a static implementation does not imply user approval.

## Permanent tracking rules

1. Never delete an existing requirement, even when implemented. Retain its stable ID and completion evidence.
2. Append newly discovered requirements beneath an existing workstream / parent ID. Do not silently move goalposts or change the fixed 100-point rubric.
3. Distinguish source decoded, code implemented, gameplay tested, and **user accepted**. Every new acceptance checkbox remains unchecked until the user expressly approves it.
4. When a feature regresses, preserve its history, flag it as regressed, and remove milestone credit until corrected; never conceal it.
5. Every later “keep decoding” pass appends a dated progress step, updates this scoreboard and the master tracker, and supplies a separate user-owned ZIP with the executable HTML, assets, decoding data, tests, and historical notes.

## Scored workstreams

| Workstream | Earned | Possible |
|---|---:|---:|
| Source provenance | 3 | 5 |
| Original map geometry | 3 | 15 |
| Original textures | 2 | 7 |
| STAN collision | 5 | 12 |
| Map registration | 1 | 10 |
| Original object setup | 2 | 12 |
| Characters and animation | 1 | 8 |
| Original AI | 4 | 10 |
| Mission objectives | 1 | 10 |
| Native interactions | 0 | 4 |
| Mission completion | 0 | 4 |
| Runtime QA | 0 | 3 |

## Permanent milestone checklist (34 stable IDs; 100 points)

All acceptance boxes are unchecked. “Implemented” means code/source evidence exists; it does not certify ChromeOS game behavior.

- [ ] **SRC-01 · 3 pts · IMPLEMENTED, awaiting user acceptance** — Verified source executable identity and extracted-record SHA
- [ ] **SRC-02 · 2 pts · OPEN** — Archive original raw executable and native graphics containers
- [ ] **GEO-01 · 3 pts · IMPLEMENTED, awaiting user acceptance** — Extract initial original geometry for 23 browser map assets
- [ ] **GEO-02 · 6 pts · OPEN** — Recover missing original draw batches on every stage
- [ ] **GEO-03 · 6 pts · OPEN** — Validate full authored floors, walls and rooms on every stage
- [ ] **TEX-01 · 2 pts · IMPLEMENTED, awaiting user acceptance** — Decode source textures and attach to recovered material batches
- [ ] **TEX-02 · 5 pts · OPEN** — Verify source UV, transparency and materials across every source mesh
- [ ] **COL-01 · 5 pts · IMPLEMENTED, awaiting user acceptance** — Decode all 28 original collision blocks and 36,699 native tiles
- [ ] **COL-02 · 4 pts · OPEN** — Use native collision authoritatively on all playable stages
- [ ] **COL-03 · 3 pts · OPEN** — Verify original stairs, ramps, gravity, ledges and multi-floor transitions
- [ ] **REG-01 · 1 pt · IMPLEMENTED, awaiting user acceptance** — Calibrate original Train STAN to converted graphics
- [ ] **REG-02 · 6 pts · OPEN** — Validate source transforms independently across every other stage
- [ ] **REG-03 · 3 pts · OPEN** — Explain and recover missing original visual geometry without invented floors
- [ ] **OBJ-01 · 2 pts · IMPLEMENTED, awaiting user acceptance** — Recover strict partial original object/guard/tag inventory
- [ ] **OBJ-02 · 6 pts · OPEN** — Decode all original setup property types and record lengths
- [ ] **OBJ-03 · 4 pts · OPEN** — Connect mission objects to source model, tag, pad and interactive states
- [ ] **RIG-01 · 1 pt · IMPLEMENTED, awaiting user acceptance** — Recover first original source-textured character and guard renderers
- [ ] **RIG-02 · 4 pts · OPEN** — Restore original skeleton, skin weights and authored character bindings
- [ ] **RIG-03 · 3 pts · OPEN** — Run native walk, shoot, hit, death and movement keyframes
- [ ] **AI-01 · 1 pt · IMPLEMENTED, awaiting user acceptance** — Identify original native AI opcode names
- [ ] **AI-02 · 1 pt · IMPLEMENTED, awaiting user acceptance** — Implement partial original-pad guards and source command interpreter
- [ ] **AI-03 · 1 pt · IMPLEMENTED, awaiting user acceptance** — Audit original global-script branch targets, repeated labels and termination
- [ ] **AI-04 · 1 pt · IMPLEMENTED, awaiting user acceptance** — Stop native goto_next and list transitions when the source target is ambiguous
- [ ] **AI-05 · 2 pts · OPEN** — Execute complete native background/global AI scripts
- [ ] **AI-06 · 4 pts · OPEN** — Restore full original guard pathing, pursuit, visibility, combat and reactions
- [ ] **MIS-01 · 1 pt · IMPLEMENTED, awaiting user acceptance** — Decode source objective groups and difficulty conditions
- [ ] **MIS-02 · 6 pts · OPEN** — Connect all original objective conditions to source objects and authentic events
- [ ] **MIS-03 · 3 pts · OPEN** — Verify all objective conditions at all three mission difficulties
- [ ] **INT-01 · 2 pts · OPEN** — Restore native doors, alarms, access controls and props
- [ ] **INT-02 · 2 pts · OPEN** — Restore source vehicle, inventory, pickups and scripted actor interactions
- [ ] **END-01 · 2 pts · OPEN** — Recover and implement native exfil, win/fail and transitions
- [ ] **END-02 · 2 pts · OPEN** — Finish entire original campaign as linked playable source missions
- [ ] **QA-01 · 2 pts · OPEN** — Test and approve every original stage in real ChromeOS/WebGL
- [ ] **QA-02 · 1 pt · OPEN** — Validate Chromebook memory/AI/performance and restarts under load

## Progress history

- **v4.7 baseline: 20/100.** Retrospectively scored with this fixed rubric; no claim of earlier user approval.
- **v4.8 step 1: 21/100.** AI-03 — Audited 184 native global AI scripts / 5,887 instructions; flagged duplicate labels and unsupported lists from the original source records.
- **v4.8 step 2: 22/100.** AI-04 — Fixed original AI label/list target handling to block invented wraparounds, truncated program jumps and duplicate script IDs. Static Node tests pass.

## Outstanding blockers

Missing raw original binary prevents further unknown-property-byte decoding from already-extracted records alone. Several maps still have missing source draw groups, collision ↔ render gaps, incomplete native object/gameplay bindings, and no recovered original mission extraction/victory transitions. Source objective groups: 55. Connected source-native shootable objective targets: 6 (Train brake controllers). Fully gameplay-verified original missions: 0.

See [v4.8 native global AI research](research/V48_NATIVE_GLOBAL_AI_CONTROL_FLOW_SUMMARY.md), [master history](PROJECT_TRACKER.md), and the private v4.8 archive supplied in ChatGPT for the complete source files and tools.
