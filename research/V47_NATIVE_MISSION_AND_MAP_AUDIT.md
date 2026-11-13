# v4.7 — Authored mission logic, patrol wall checks, map-source playability audit

**2026-11-12 · Partial implementation / static validation only · USER ACCEPTANCE PENDING**

The private v4.7 distribution is a user-owned single-file HTML game plus original source assets, collision records, original setup/AI/object records, and versioned decoder research in `GoldenEye_World_Explorer_v47_NATIVE_AI_OBJECTIVES_SOURCE_AUDIT.zip`. **Game-derived asset bytes are not committed to this public repository.** This is NOT a fully playable original GoldenEye campaign.

## Implemented in v4.7 game runtime
- Original objective groups are filtered by Agent / Secret Agent / 00 Agent mask before displaying or calculating completion. An unknown/unported source event is never treated as success. Even all decoded conditions passing cannot declare mission victory without recovered native exit logic.
- Native `if_chr_dying_or_dead` checks a matched original character/guard ID, not the querying guard. Uninstantiated characters do not cause an invented true result. `if_guard_hits_greater_than` checks actual guard hit counts; `if_bond_is_dead` sees real player health.
- Decoded source room checks require original STAN floor and converted graphics support; native guard patrol steps test collision against recovered rendered walls and stop when blocked instead of walking through.
- Player death/reaching a map's void triggers complete map reload including native objective flags and original guard/object states; no silent player-only health respawn.
- Unresolved native AI label jumps do not silently resume through incorrect instructions.
- All **20 embedded original/decoded source payload sections** are unchanged compared with v4.6. JavaScript syntax passed `node --check`; ZIP integrity test passed. Chromium/WebGL browser gameplay test was blocked by the testing environment (ERR_BLOCKED_BY_ADMINISTRATOR); no completed visual gameplay test is claimed.

## Authenticated decoding inventory (not the same as implementation)
- 28 native STAN collision-stage blocks / 36,699 authentic collision polygons.
- 21 native setup stages / 55 original objective condition groups; 72 `objective_destroy_object` criteria.
- Only 12/72 destroy criteria have a recovered linked tag; only **6 Train tag/model/pad associations (model 120 brake units)** are available as actual shootable original-source objective models.
- 637 guard-placement records (including separately identified candidate clusters); 444 strictly parsed normal object records; 33 tagged-object links. Object-property stream decoding stops at unknown types rather than jumping guessed lengths.
- Train graphics/STAN registration is close; Depot is reasonably close. Dam, Facility, Streets, Statue, Runway and other stages have severe room/collision/render mismatch. Median nearest STAN-to-graphics vertex gaps are exploratory diagnostics and do not by themselves prove a conversion offset bug. No invented geometry or universal guessed transform was introduced.

## Source-specific blockers
- Unknown property record types block complete original stage object/model/door catalog, model ID-to-CAFF mapping and interactions.
- Source AI runtime supports only selected opcodes; global AI/NPC scripts, door state, escort/sabotage objectives and all native mission extraction/level-exit logic are not fully recovered.
- Recovered render batches and native collision do not align on many maps; those maps are not declared correct or playable.
- Original Train model 120 brake-controller objective can be physically tested; other objectives are not marked gameplay-verified.
- No user signoff or acceptance tests have been performed. Preserve existing accepted/unchecked statuses in PROJECT_TRACKER.md.

## Private ZIP included research and independent checks
`V46_NATIVE_OBJECT_SPAWN_LOCATIONS_AND_OBJECTIVES.json`, `V46_ORIGINAL_STAN_ROOM_TILES.json`, `V46_MAP_SOURCE_REGISTRATION_AUDIT.json`, `V47_MISSION_PLAYABILITY_EVIDENCE.json`, `V47_MISSION_PROGRESS_AND_BLOCKERS.md`, `V47_RELEASE_MANIFEST.json`, `test_v47_release.py`, `patch_v47.py`, earlier source decoders and notes, and user-owned embedded game asset payloads.

## Decoder tasks still open (all unapproved)
- [ ] Parse native setup properties without unknown byte strides and link every objective's original model ID, tag and pad.
- [ ] Recover per-stage CAFF room/object transforms and verify actual floor/wall alignment against native STAN.
- [ ] Recover native global AI execution, character state, door/vehicle interaction semantics and fail conditions.
- [ ] Implement exact source-level end/exfil/victory transitions rather than invented win trigger.
- [ ] Test complete level traversal, enemy patrols, objective objects, three difficulty modes, fail/restart and extraction on real Chromebook/WebGL.

The private ZIP contains the runnable HTML and assets; repository progress notes do **not** imply that its public GitHub Pages build has the new runtime or bundled copyrighted source assets.
