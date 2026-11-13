# v4.8 — Binary-extracted original global AI control-flow audit (2026-11-12)

This audit is built from original Xbox-stage script records already embedded in the private v4.7 source HTML. It does **not** simulate original AI state or establish that any source campaign mission is playable.

## Verified from original extraction

| Source finding | Count |
|---|---:|
| Native setup stages | 21 |
| Native global AI lists (`id >= 0x1000`) | 184 |
| Source-decoded instructions in those lists | 5,887 |
| Lists with repeated label IDs | 118 |
| Lists not fully terminated (truncated / unsupported) | 24 |
| Source `if_bond_in_room_with_pad` branches | 189 |
| Room branches without exactly one matching label target | 81 |
| Source-level room → objective-bitfield-set candidate links | 6 |

**Original source executable SHA256:** `048c9a725e0163de3f1631651f7e250baaa01747d76c3e32cd62501cafefacd9`.

A candidate link means an original conditional appears to target a label whose branch includes an `objective_bitfield_set_on` instruction; it does **not** establish that the script is reachable, its actor exists or the browser can execute all prerequisites.

## Exact confirmed Train example

Original Train global list **0x1009** has original `if_bond_in_room_with_pad` operand `006201`: pad 98, branch label 1. Following that label, the original script executes `switch_fog_instantly` then `objective_bitfield_set_on 00100000` and later a list transition. This source relation was revalidated from the original decoded instruction stream, not invented from the objective text. The full list's transitions and visual effects are not all ported.

Source candidate examples outside Train include Egyptian and Surface 1, but both have broader script branching and/or source actor/difficulty dependencies, so they are **NOT** promoted to completed gameplay objectives.

## v4.8 runtime safety fix

The old interpreter selected the *first* matching label if `goto_next` had no subsequent matching label. This could produce a made-up flow of execution. v4.8 preserves the unresolved state instead. A script transition with a duplicate original list ID or truncated program now blocks rather than running a guessed first match.

Tests cover `goto_first`, a subsequent `goto_next`, missing-following-label behavior, ambiguous duplicate list IDs and incomplete target-list rejection. These are **static / Node VM tests**, not real ChromeOS WebGL mission tests.

## Still required

- Recover raw source executable bytes for unknown object-property sizes, missing opcode semantics and exact list-transition behavior.
- Complete the native global AI interpreter, with source-authenticated pad coordinates, state/room references and stage events.
- Reconcile graphics with native STAN collision on non-Train maps without fabricated floors or guessed universal transforms.
- Reconstruct native object IDs, models and interactions for every original mission condition, then implement native exfil and success/fail transitions.
- Verify actual gameplay on Chromebook. No campaign mission is user-approved as fully playable.

**Private archive:** `GoldenEye_World_Explorer_v48_NATIVE_GLOBAL_AI_AND_PERMANENT_PROGRESS.zip` (91 files; complete user-owned source/asset snapshots, progress ledger, Python audit scripts and Node checks). Full per-program offset-level JSON audit: `V48_NATIVE_GLOBAL_AI_CONTROL_FLOW_AUDIT.json`, in private ZIP.

Tracked under AI-03/AI-04 with stable progress IDs: [permanent roadmap](../CONVERSION_PROGRESS.md). All previous master tracker records remain intact.
