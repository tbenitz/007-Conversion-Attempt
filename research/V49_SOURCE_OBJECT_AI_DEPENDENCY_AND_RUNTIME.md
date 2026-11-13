# v4.9 — Original-source object/mission dependency graph and AI VM correctness

**2026-11-12 · ENGINEERING PROGRESS 22/100 (unchanged) · USER ACCEPTANCE PENDING · 0/21 full original missions verified.**

This is a real partial source conversion, not a restored campaign. The **user-owned private v4.9 ZIP** retains the standalone HTML and all original embedded game assets, prior decoders, previous audits, and newly generated source dependency records. No copyrighted game-asset payload is published in this public repository.

## Fixed in the runnable v4.9 HTML

1. **Native list transition bug**: `runNativeGuardAI` previously captured the instruction array outside the execution loop, then replaced `ai.program` and reset `ai.pc` on `jump_to_ai_list`. Subsequent instructions incorrectly came from the *old* list. The interpreter now reloads the active original program's instructions before every command. A Node VM regression tests source-program A handing off to B, ensuring B's original flag instruction executes and A's unrelated flag does not.
2. **Native conditional halt bug**: an unresolved source-label jump previously marked the AI state as blocked but continued execution during that tick. The interpreter now stops immediately; a regression confirms no subsequent `objective_bitfield_set_on` can run.
3. **Ambiguous initial guard AI lists**: program selection requires exactly one matching original list with `status=terminated`; duplicate, missing, or truncated lists are not arbitrarily selected.
4. **Unsupported source event logic**: native hearing, partial LOS, observed gunfire/death and missed-shot predicates no longer silently assume visibility or false. Unported conditions halt as unsupported; this is **not** an implementation of authentic hearing.
5. The existing in-game **Source Data** panel displays per-stage source objective-condition, tag/model linkage and script-handoff counts. Every executed decoded AI instruction tracks its original byte offset.

## Evidence-backed decoding counts (private derived source data)

| Metric | Verified extracted data |
|---|---:|
| Original setup stages | 21 |
| Original objective groups | 55 |
| Total decoded objective conditions | 136 |
| Object destruction conditions | 72 |
| Source-authenticated destroy-tag links | 12 |
| Destroy conditions with connected renderable original objective model | 6 (Train brakeunit) |
| Original guard placement records in extracted dataset | 637 |
| Guard initial AI references resolving to unique, terminated extracted source list | 308 |
| Missing/duplicate/truncated initial guard-list references | 329 |
| Original source AI-list handoffs | 480 |
| Handoffs to uniquely identified terminated *stage-local* source list | 234 |
| Handoffs still unresolved at stage-local scope | 246 |

**Important:** Some of the 246 unmatched handoffs may refer to original shared system AI programs not present in the extracted stage setup. They are not proof of original-game bugs. The graph keeps original PE offsets, tag/model/pad bindings, floor evidence, and candidate flag-writing opcodes; a writer appearing in an original AI list **does not** certify it can execute in the browser.

## Strict original-property decoder progress

`decode_v49_propdefs_strict.py`, shipped inside the private ZIP, validates the supplied original Xbox PE identity (17,760,256-byte original; SHA256 `048c9a725e0163de3f1631651f7e250baaa01747d76c3e32cd62501cafefacd9`). Only previously source-verified byte lengths are read. Public N64 objective record references, including type `0x20` (enter room), are noted as **cross-platform candidate definitions**, not silently treated as confirmed Xbox record widths. Parser stops and retains the original unknown offset. The raw original PE is absent from the current v4.8 ZIP, so later property bytes **were not decoded in this pass**.

## Test evidence and limits

- PASS: `node --check` for v4.9 module; source VM tests for list transitions, failed conditional jumps, no unknown AI execution, unique initial script selection.
- PASS: strict object decoder structural test (explicit synthetic fixture, not game data).
- PASS: all **20 original embedded source/asset data blocks** unchanged from v4.8, all embedded JSON parse, all 34 milestone IDs retained, previous scoreboard 22/100 retained.
- PASS: versioned ZIP CRC, 106 entries, including 88 unchanged retained v4.8 files and original v4.8 roadmap snapshots.
- **NOT** tested: ChromeOS WebGL, level traversal, native full objective completion, accurate AI hearing, original extraction / mission win. **No real original campaign mission is certified fully playable.**

## Permanent checklist children — never remove

- [ ] **AI-05.1** — Native AI target-list instruction-array correctness: code implemented, static tested, needs user browser acceptance.
- [ ] **AI-05.2** — Native conditional unresolved jump must halt before effects: code implemented, static tested, browser acceptance pending.
- [ ] **AI-05.3** — Initial guard source AI list uniqueness/termination: code implemented, static tested, browser acceptance pending.
- [ ] **AI-05.4** — Recover shared original AI programs and resolve missing list handoffs: blocked by unavailable original raw bytes.
- [ ] **AI-06.1** — Authentic hearing / partial LOS / witnessed-shot event semantics: still NOT implemented; guessing removed.
- [ ] **OBJ-02.1** — Recover and verify missing native property grammar including original 0x20 room objectives: blocked by missing original bytes.
- [ ] **OBJ-03.1** — Source objective/tag/model/pad/AI-writer dependency graph: decoded audit complete; actual gameplay binding incomplete.

**Progress score policy:** A completed substep inside an unfinished parent doesn't grant the parent’s full point allocation. Therefore **v4.8 22% → v4.9 22%**. No requirements or approvals removed or auto-marked complete. Details also in [permanent roadmap](../CONVERSION_PROGRESS.md) and [historical tracker](../PROJECT_TRACKER.md).

**Private ZIP:** `GoldenEye_World_Explorer_v49_NATIVE_AI_VM_AND_OBJECT_DEPENDENCY_DECODING.zip`; source assets and original binaries are not shipped publicly.
