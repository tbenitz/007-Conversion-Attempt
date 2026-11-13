# v4.3 — Authentic AI opcode labeling and CPU optimization (November 12, 2026)

The user requested continued original-source enemy decoding and resolution of guard movement lag. This version preserves source-only maps, audio, objectives, HUD/minimap, settings and all previously converted game assets; no new objective or audio subsystem changes.

## Implemented in private playable ZIP (not user-approved)

1. Train original 694 STAN polygons are indexed using a 3.2-unit X/Z hash of 689 nondegenerate horizontal source triangles; no scene floor proxy is introduced. The source-coordinate floor query agrees with a full brute-force triangle scan on **10,000/10,000** deterministic sample points. Standalone source-index lookup completed 10,000 queries in approximately 6 ms on the tool machine, **not** a Chromebook FPS measurement.
2. Source guards no longer run duplicate movement steps within the same frame. AI decisions are scheduled at 40 ms near the player and 100 ms when farther than 28 world units, and native source-floor movement is applied once per scheduled step.
3. Original uniform + original head texture template is built once per source guard skin. Individual rig joints still move independently, while texture and mesh resources are shared across guard instances.
4. Guard sight raycasts now run only for sight-relevant opcodes; sight results cached for approximately 175–241 ms per guard. Original global AI lists and source combat accuracy remain unimplemented.
5. Guards more than 86 units from the player are hidden for render performance but retain state. Source AI fallback-route search attempts are throttled. Non-Train maps use original mesh AABB candidate filtering prior to full source triangle intersection.
6. Added measured guard **CPU loop ms/frame** and query counts to the existing NPC status display; this is not GPU time or FPS and must not be represented as such.
7. Completed ID/name reconciliation for **253 known original AI bytecode opcodes** using the [n64decomp/007 bondaicommands.h](https://github.com/n64decomp/007/blob/master/src/bondaicommands.h) source reference. Updated labels for **2,914** undernamed commands within **15,913** source instructions across **662** staged AI lists. Opcodes, offsets, operands and original script lengths were preserved exactly. **Command naming is not equivalent to implementing commands.**
8. Extended native interpreter subset with local byte registers and branches, guard flags, guard bitfield operations and pad preset movement. The pad-distance conditional is enabled only on Train, whose original source-to-GLB coordinate transform was previously verified.

## Tests and remaining work

- Node syntax check passed.
- Deterministic 10,000-source-floor-query comparison passed with 0 mismatches.
- ZIP CRC and original embedded game assets validated unchanged; all 41 older auxiliary files preserved.
- Browser runtime smoke test blocked by administrator policy for both file:// and localhost HTTP in the test environment; no Chromebook WebGL FPS claim.
- Original Xbox global guard AI, full native patrol schedules, mission objective event handling, guard skin weights/keyframes, non-Train coordinate calibration and exact audio command effects remain incomplete.
- Preserve all user acceptance checklist items; the changes above are NOT user-approved.

Private output: `GoldenEye_World_Explorer_v43_OPTIMIZED_SOURCE_GUARDS_AI.zip`, saved to ChatGPT Library.
