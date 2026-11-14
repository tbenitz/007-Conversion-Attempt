# GoldenEye Frontier

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
