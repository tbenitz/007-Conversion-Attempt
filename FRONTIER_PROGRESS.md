# GoldenEye Frontier

## v0.5.0 — Motor Pool

- Densified developed neighborhoods with roofed Surface cabins, shared footpaths and separately operable instanced doors. In the default South Lane sector, the count rose from 34 to 331 buildings, from 40 to 140 Jungle trees and from 62 to 260 understory props. Woodland, mission entries and the protected starter paths retain more space.
- Spawned original crates and player-drivable parked cars and trucks. The yellow taxi reuses an original hatchback mesh. Sandbox vehicle mechanics include steering, reverse, braking, collision and safe dismount. No AI traffic.
- Added first-person PP7 and KF7 Soviet sandbox loadouts with unlimited ammo and destructible crates. The models are recovered original geometry. The campaign and its shooting rules were not changed.
- The packaged runtime passed driving and braking for all three vehicle classes, the Motor Pool atlas route, both compact door orientations and crate unload/reload. Hardware performance remains unmeasured. The local package includes the standalone HTML, editable source, provenance and route logs. No game assets were added to this tracker.

## v0.4.0 — Connected Grounds

- Reproduced the Birch Court missing-floor bug against v0.3.0. Removed the oversized Streets cutout from the outdoor grid and kept native Streets behind its existing marked entrance. The walk-in Runway now has continuous, source-textured apron backfill around its native strip.
- Added Grove Lane, Fern Court, a greenway loop, 12 roofed Surface buildings and new back lots in eligible procedural neighborhoods. Reused original Jungle tree and undergrowth models without blocking the public walks.
- Streamed ground follows exact sector boundaries and keeps the four-sector detail cap. A distant terrain-only mesh avoids looking out into a sky gap.
- The packed offline build passed 32 crossing traces at walk and sprint speeds, the new Grove/Fern loop and door regression, and earlier map transfers. Not all original districts have physical seams. No hardware frame-rate claims or full manual playthrough are recorded.
- The local release includes the playable single HTML, editable project, source provenance and route-test logs. The public tracker does not host game assets.

## v0.3.0 — Neighborhoods

- Removed the façade-only building modules shown in the v0.2.0 user playtest. Reused roofed Surface and Depot geometry plus original vegetation, vehicles, fences, furniture, doors and street materials.
- Added Birch Court and Mill Lane as two connected cul-de-sacs with working through-houses, a pedestrian green, and South Lane. Added a guided walk to the Station Quarter loading hall. Road widths and lot placement are distinct from the 250 m streaming grid.
- Reused the original door and floorboard assets for a new rear opening in the copied cabin. Original source missions are unchanged. The assembled scene received an independent offline render review using its actual meshes and textures.
- Tests cover both through routes, closed-door blocking, source-floor traversal, sampled procedural rotations and seeds, and older map seams. Chromebook WebGL performance and a complete playtest of the mission interiors remain unverified.

## v0.2.0 — Initial procedural build

Separate exploration build. City Survey and campaign builds are unchanged. Source-derived game assets are not published to the tracker.

- Generated world art uses clipped GoldenEye Streets, Depot, Surface and Runway meshes and original recovered prop GLBs. No invented building shells. The 4.5 km × 4.5 km starter footprint uses streaming 250 m sectors, with seed-based generation beyond the core.
- All 24 source maps and 25 setup instances are linked. Runway has a physical, bidirectional road-to-STAN seam. Both Surface/Bunker variants have aligned upper/lower entry points and two-way transfers. Streets and the remaining unsupported geographic seams use marked transfers.
- Automated runtime checks cover Streets travel and original collision, all map landings, streaming beyond the starter region, the recovered wooden cabin door, and return/route HUD behavior. Rendering, end-to-end native interiors, local Chrome storage and physical Chromebook performance remain unverified.
- The local handoff includes the self-contained HTML, editable source, asset provenance and route test records.
