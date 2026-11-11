# GoldenEye XBLA — Master Development Tracker

Updated 2026-11-11, v1.4. Goal: polished playable exploration with complete assets, movement, audio, map building and optional missions.

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
| GE-012 | Climb every Facility staircase without getting stuck | BROKEN — free-walk workaround | [ ] |
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
| GE-036 | UV/material references restored on every map | IN PROGRESS | [ ] |
| GE-037 | Apply all 3039 source-decoded textures | IN PROGRESS | [ ] |
| GE-038 | Glass/transparency/decals/emissive materials | PLANNED | [ ] |
| GE-039 | Original props and placement transforms | PLANNED | [ ] |
| GE-040 | All original Facility/stage doors and animations | IN PROGRESS — source-door showcase, locations unverified | [ ] |
| GE-041 | Mantling through real window openings | IN PROGRESS | [ ] |
| GE-042 | Separate real level collision and navigation mesh | PLANNED | [ ] |
| GE-043 | Reconstructed proper stair/ramps colliders | PLANNED | [ ] |
| GE-044 | Elevators/ladders/moving platforms | PLANNED | [ ] |
| GE-045 | Gun/prop textures and UV maps | IN PROGRESS — provisional projected gun images | [ ] |
| GE-046 | Fix rotated and disconnected weapon meshes | IN PROGRESS | [ ] |
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
| GE-087 | Full level map projected from converted geometry | IMPLEMENTED — VERIFY | [ ] |
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
| GE-116 | Restore source-material associations on all converted level draw batches | IMPLEMENTED — VERIFY: 22 newly textured maps + existing Facility | [ ] |
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
| GE-128 | Generate continuous exterior ring with rolling terrain outside source map footprints | IMPLEMENTED — VERIFY: newly generated geometry with source texture images | [ ] |
| GE-129 | Generate textured connecting paths using source game textures | IMPLEMENTED — VERIFY: placement is procedural, not authentic | [ ] |
| GE-130 | Convert recognizable game-source crates, barrels, barricades, vehicles and trees | IMPLEMENTED — VERIFY: 17 unique source prop model types | [ ] |
| GE-131 | Place original prop meshes near player and in outdoor surroundings | IMPLEMENTED — VERIFY: generated arrangements, not authored placements | [ ] |
| GE-132 | Automatically switch biome style for each selectable map | IMPLEMENTED — VERIFY: heuristic snow/forest/urban/rock/industrial categories | [ ] |
| GE-133 | Toggle map texture repair, outdoor generation and prop population separately | IMPLEMENTED — VERIFY | [ ] |
| GE-134 | Guarantee collision-safe seamless navigation across every outdoor/indoor transition | IN PROGRESS — incomplete source navigation, last-floor safety workaround | [ ] |
| GE-135 | Restore all original map texture UV bindings without reprojecting | IN PROGRESS — CAFF vertex format decoding required | [ ] |
| GE-136 | Validate map visuals and prop scale/placement interactively on Chromebook | NEEDS USER TEST — browser local file blocked in test environment | [ ] |

**Accuracy and source policy:** v1.4 programmatically creates **new terrain/road/path geometry**, as explicitly requested, but it uses recovered game textures only. Plants, vehicles and environmental objects are **converted game-source meshes**, not substituted cone-tree or placeholder models. Terrain shape, prop placement, biome choices and roads are generated rather than actual GoldenEye level-authored layouts. Some object textures are planar-projected because authentic source UV decoding is unfinished. Exteriors are a reconstructed annex, not the original outdoor level. No feature approvals have been checked.
