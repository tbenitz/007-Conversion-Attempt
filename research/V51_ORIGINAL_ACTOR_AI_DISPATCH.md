# v5.1 — Source-authentic cross-character AI script dispatch

**2026-11-12 · 23/100 engineering points (22 previously complete + 1 AI-06 partial) · AI-06 remains open · 0/21 source missions fully browser-verified.**

This is gameplay-engine work rather than just counting existing source records. The actual runnable single-file HTML in the private ZIP now transfers original decoded script execution to other named original guards when the source can uniquely identify both the intended character and the destination AI program. It does **not** emulate Xbox executable code or declare the full native AI system finished.

## Evidence from extracted original Xbox stage data

| Original source record | Count |
|---|---:|
| All decoded `jump_to_ai_list` commands | 480 |
| Selector `0xFD` (self) | 428 |
| Selector `0xF8` (reserved pseudo-character, still unresolved) | 32 |
| Explicit actor-character ID selectors | 20 |
| Explicit actor handoffs with exactly one source guard + one terminated matching stage-local script | **14** |
| Explicit actor handoffs that cannot be uniquely resolved from extracted stage data | 6 |

The 14 resolved source **relationships** are recorded with original byte offsets, original program ID, guard ID, destination program ID, and counts of matching source records in the private ZIP's `V51_NATIVE_ACTOR_AI_DISPATCH_SOURCE_AUDIT.json`. The source relation is not a claim that the corresponding guard can spawn successfully on every incomplete converted map.

## Runtime changes

- Original `jump_to_ai_list` validates both the native actor selector and 16-bit program ID.
- `0xFD` continues as self-program handoff.
- An explicit character ID matches **exactly one** instantiated native guard with that original ID; a transfer is allowed only if that actor is alive, has an AI instance and the destination program has a **unique, terminated** original decoded definition.
- On valid cross-character handoff, the target guard's own instruction program, counter and movement/patrol state change, while **the caller's program counter continues**. This prevents the previously blocked author-script effects and also prevents redirecting the wrong character.
- Missing, duplicate, dead or uninstantiated target guards remain unsupported; no guessed actor substitution.
- Special selector `0xF8` has not been verified as an ordinary guard ID, so it remains blocked.
- Source Data pane reports per-stage original explicit actor links and how many are source-resolvable; objective HUD reports actual in-session source actor transfers.

## Static tests

**PASS**: `node --check`, `test_v51_native_ai.cjs` with correct caller and recipient paths, missing actor, duplicate actor, dead actor and reserved `0xF8` tests; v5.1 archive CRC and original embedded source payload byte preservation. All 34 scored milestones and 11 previous child tasks remain, with 2 new child IDs (AI-05.9 and AI-06.2).

**NOT TESTED**: ChromeOS 8 GB GPU runtime, whether the intended original target guard is spawned for a given cross-character event, native global/background AI execution, original sound/vision event semantics, full mission completion, and exfil victory.

## 23% accounting without hiding incomplete work

The original fixed rubric has AI-06 worth 4 points. Previously the score only advanced when an entire parent was complete, so v4.9 and v5.0 source-correct patches scored zero. From v5.1, **1/4 of AI-06** is an explicitly identified partial credit for working source-actor dispatcher and guards, verified with Node VM. **AI-06 remains OPEN**. No prior completed milestones are changed; source milestones fully completed still sum to 22, documented partial credit 1, fixed denominator 100. User acceptance remains unchecked.

## Remains necessary

Recover missing native character registry (including `0xF8`), all shared AI lists, native global/background programs, source-accurate hearing and collision/perception, mission object/door triggers, missing render geometry, and mission-level exfil and transitions.

Archive: `GoldenEye_World_Explorer_v51_NATIVE_CHARACTER_AI_HANDOFFS_PROGRESS.zip` (private; game-derived asset bytes not added to this public repository).

[Permanent score and checklist](../CONVERSION_PROGRESS.md) · [historical tracker](../PROJECT_TRACKER.md).
