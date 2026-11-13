# v5.0 — Native AI return-list decoding and cross-character target safeguards

**2026-11-12 · engineering score 22/100 (unchanged) · 0/21 original campaign missions browser-verified.** The private user-owned v5.0 ZIP retains the original embedded assets and all previous decoding notes. No game-derived binaries are committed to the public repo.

## Source-backed original opcode census

Original Xbox stage setup SHA256 recorded by extracted records: `048c9a725e0163de3f1631651f7e250baaa01747d76c3e32cd62501cafefacd9`. Raw 17,760,256-byte Xbox PE itself **not included** in archived release; counts below re-audit its earlier recovered instruction streams, not newly recovered executable bytes.

| Opcode/control flow | Source occurrences |
|---|---:|
| `jump_to_ai_list` | 480 |
| Actor operand `0xFD` (source convention for self target) | 428 |
| Other actor selectors (including `0xF8`, explicit character IDs) | 52 |
| `set_return_ai_list` | 87 |
| Return-list setter pointing to unique terminated stage-local list | 38 |
| `jump_to_return_ai_list` | 37 |
| Direct self-target handoffs with unique terminated stage-local list | 186 |

**Previously incorrect runtime behavior:** v4.9 ignored the first operand of `jump_to_ai_list`; therefore any of the 52 non-self-selector instructions could redirect the *current* guard's AI rather than its intended actor. v5.0 retains actor selector byte and target list ID in the AI instance, and does **not** execute non-self handoffs pending recovery of the original source character registry.

**Implemented for static test:** `set_return_ai_list` records the original two-byte list ID in the actor's return register; `jump_to_return_ai_list` reads that saved ID and switches to the unique fully decoded, terminated program if stage-local lookup can prove it. No fabricated/default return list, no fallback to an arbitrary duplicate or truncated list. A missing stage-local list does not prove the source target never existed: original shared/global AI lists may be elsewhere.

## Per-stage original source command counts

| Stage | Self list handoffs | Other actor handoffs | Return setters | Return jumps |
|---|---:|---:|---:|---:|
| Archives | 22 | 2 | 8 | 4 |
| Control | 20 | 1 | 0 | 0 |
| Facility | 36 | 3 | 17 | 5 |
| Aztec | 12 | 0 | 0 | 0 |
| Caverns | 19 | 2 | 7 | 4 |
| Cradle | 32 | 6 | 0 | 1 |
| Egyptian | 8 | 1 | 2 | 4 |
| Dam | 16 | 2 | 3 | 1 |
| Depot | 8 | 4 | 1 | 0 |
| Frigate | 8 | 1 | 3 | 0 |
| Jungle | 39 | 3 | 13 | 6 |
| Cuba | 3 | 2 | 0 | 0 |
| Streets | 8 | 7 | 0 | 0 |
| Runway | 7 | 1 | 0 | 0 |
| Bunker 1 | 17 | 1 | 5 | 0 |
| Bunker 2 | 18 | 2 | 7 | 4 |
| Surface 1 | 34 | 2 | 1 | 2 |
| Surface 2 | 40 | 2 | 14 | 0 |
| Silo | 29 | 2 | 5 | 4 |
| Statue | 22 | 5 | 0 | 0 |
| Train | 30 | 3 | 1 | 2 |

## Validation

- PASS: Node syntax + VM tests for original return-list register/handoff chain, wrong-actor selector, explicit actor ID, missing/unresolved return, truncated/duplicate program.
- PASS: all 21 original JSON source/asset records and earlier decoded stage data sections byte-identical to v4.9; v5.0 adds one new independent audit JSON and updates only progress.
- PASS: 34/34 original stable milestones and 7/7 prior subrequirements preserved; new children AI-05.5 through AI-05.8 appended, no user approvals marked.
- PASS: ZIP integrity, 119 archived files; 103 prior records preserved verbatim.
- NOT TESTED: actual Chromebook WebGL gameplay; authentic full native AI; cross-character script execution; original mission extraction or victory.

**Engineering percentage stays 22/100.** Full original Xbox native AI remains incomplete, and no original source mission is certified playable. Detailed per-program original offsets, operand hex and source stage IDs are in the **private** ZIP's `V50_NATIVE_AI_RETURN_AND_ACTOR_SCOPE_AUDIT.json`.

[Permanent conversion checklist](../CONVERSION_PROGRESS.md) · [historical tracker](../PROJECT_TRACKER.md).
