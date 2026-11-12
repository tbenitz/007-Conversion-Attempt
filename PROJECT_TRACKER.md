# GoldenEye XBLA — Master Development Tracker

Updated 2026-11-11, v1.9. Goal: polished playable exploration with complete assets, movement, audio, map building and optional missions.

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
| GE-116 | Restore source-material associations on all converted level draw batches | BROKEN — materials rendered black in user testing: 22 newly textured maps + existing Facility | [ ] |
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
| GE-128 | Generate continuous exterior ring with rolling terrain outside source map footprints | BROKEN in v1.8 — Archives exterior ground used a painting; v1.9 curated source ground pending playtest | [ ] |
| GE-129 | Generate textured connecting paths using source game textures | IMPLEMENTED — VERIFY: placement is procedural, not authentic | [ ] |
| GE-130 | Convert recognizable game-source crates, barrels, barricades, vehicles and trees | IN PROGRESS — original props exist but vehicle surfaces white in v1.8; v1.9 batch materials pending playtest | [ ] |
| GE-131 | Place original prop meshes near player and in outdoor surroundings | IN PROGRESS — props placed but several white / incorrect material assignments in v1.8 | [ ] |
| GE-132 | Automatically switch biome style for each selectable map | IMPLEMENTED — VERIFY: heuristic snow/forest/urban/rock/industrial categories | [ ] |
| GE-133 | Toggle map texture repair, outdoor generation and prop population separately | IMPLEMENTED — VERIFY | [ ] |
| GE-134 | Guarantee collision-safe seamless navigation across every outdoor/indoor transition | IN PROGRESS — geometry collision and outdoor/indoor traversal still fail player reports; v2.0 trial source-ray controller not yet verified | [ ] |
| GE-135 | Restore all original map texture UV bindings without reprojecting | IN PROGRESS — CAFF vertex format decoding required | [ ] |
| GE-136 | Validate map visuals and prop scale/placement interactively on Chromebook | NEEDS USER TEST — browser local file blocked in test environment | [ ] |

**Accuracy and source policy:** v1.4 programmatically creates **new terrain/road/path geometry**, as explicitly requested, but it uses recovered game textures only. Plants, vehicles and environmental objects are **converted game-source meshes**, not substituted cone-tree or placeholder models. Terrain shape, prop placement, biome choices and roads are generated rather than actual GoldenEye level-authored layouts. Some object textures are planar-projected because authentic source UV decoding is unfinished. Exteriors are a reconstructed annex, not the original outdoor level. No feature approvals have been checked.

## L — v1.5 visible texture recovery and complete asset coverage audit

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-137 | Audit all 23 embedded level GLBs and source image references | IMPLEMENTED — VERIFY: 23/23 GLBs parsed; 518836 triangles | [ ] |
| GE-138 | Exclude pure white/black decals and masks from fallback environment textures | IMPLEMENTED — VERIFY: 4–6 per-map original-source textures | [ ] |
| GE-139 | Apply per-face planar UV fallback to invalid converted map texture charts | BROKEN — v1.5/v1.6 black maps: live renderer, Chromebook test pending | [ ] |
| GE-140 | Retain valid Facility UVs and preserve glass/transparent materials | IMPLEMENTED — VERIFY: conditional repair | [ ] |
| GE-141 | Reduce overexposed lighting washing out source materials | IMPLEMENTED — VERIFY | [ ] |
| GE-142 | Clean up temporary material buffers when switching levels | IMPLEMENTED — VERIFY | [ ] |
| GE-143 | Verify source atlas and material appearances visually on ChromeOS for each level | NEEDS USER TEST — headless test blocked | [ ] |
| GE-144 | Reconstruct exact source UVs, full original geometry and missing Aztec | IN PROGRESS / BLOCKED — source decoder research | [ ] |

All 23 available converted GLB files can be reopened and have source texture images, and all are present in the standalone build. This **does not mean every map is historically complete or that all UVs are accurate**. New default reprojection uses only recovered game images. 3D browser testing is blocked; no visual user approval is recorded. Aztec remains missing and several maps have very incomplete geometry.

## M — v1.6 reported black maps and Snowguard body regression

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-145 | Dam converted scene too dark / source-mesh occluders | BROKEN — user reports maps still black (lighting and 34 huge-face removals) | [ ] |
| GE-146 | Bunker and Bunker 2 mostly black views | BROKEN — user reports black in v1.6 (lighting and oversized-face filtering) | [ ] |
| GE-147 | Cavern black / unlit underground surfaces | BROKEN — user reports black in v1.6 (near-camera fill and emissive map) | [ ] |
| GE-148 | Statue Park malformed giant triangles | IMPLEMENTED — VERIFY (experimental face filtering) | [ ] |
| GE-149 | Preserve genuine snow/concrete/shadow texture images instead of blanket rejecting white and dark images | IMPLEMENTED — VERIFY (conservative source image checks) | [ ] |
| GE-150 | Snowguard source head and original face map retained | BROKEN — head still invisible in v1.6 user playtest (projected UV preview) | [ ] |
| GE-151 | Replace Snowguard's disconnected flat body with coherent original-atlas uniform and articulated limbs | BROKEN — user reports Snowguard undersized in v1.7; v1.8 normalized proportions pending test (provisional reconstruction only) | [ ] |
| GE-152 | Ground third-person characters correctly and preserve animation vertical offset | IN PROGRESS — v1.7 Snowguard was too short; new proportion correction awaits test | [ ] |
| GE-153 | Restore authentic Snowguard body mesh and original skeletal animation | NOT DONE — original decoder needed | [ ] |
| GE-154 | Graphical Chromebook test of Dam, Bunker, Cavern and Snowguard | NEEDS USER REVIEW — browser GPU unavailable here | [ ] |

The new v1.6 single-file explorer includes camera fill lighting and emissive texture illumination, conservative original map-image filtering, and per-map huge triangle removal: Bunker 3,388, Bunker 2 3,401, Statue Park 17,255, Dam 34, Cavern 8. These are experimentally classified triangles and may include legitimate source faces; original assets remain unchanged in the user's master archive. Snowguard retains the real source head and texture atlases but the body geometry is reconstructed, not recovered. Existing character vertical placement is repaired. These are unverified JS/static checks; browser WebGL test blocked. No user approval is recorded.

## N — v1.7 rollback for black maps and missing Snowguard head

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-155 | Never overwrite Facility’s known-working original GLB materials/UVs | IMPLEMENTED — VERIFY in v1.7; no visual playtest | [ ] |
| GE-156 | Source-textured unlit fallback on non-Facility maps to avoid black shader output | IMPLEMENTED — VERIFY in v1.7; visual verification needed | [ ] |
| GE-157 | Per-batch image readability test, with original-game fallback textures only | IMPLEMENTED — VERIFY; all 23 map image sets decode | [ ] |
| GE-158 | Explicit visible Snowguard head volume and original face atlas | IMPLEMENTED — VERIFY; provisional rig and face placement | [ ] |
| GE-159 | Confirm Facility, Bunker, Cavern and Snowguard visually on Chromebook | NEEDS USER TEST; previous v1.6 failed | [ ] |

**Regression rule:** The user reported black textures, including Facility, and Snowguard's missing head in v1.6. Previously marked code-ready items GE-116, GE-139 and GE-145–147 and GE-150 are now marked BROKEN pending new verification. v1.7 bypasses global material overrides on Facility and switches the other maps to source-textured MeshBasicMaterial with recomputed UVs. A clearly visible hood/head is provisionally constructed using Snowguard's own original face pixels. This is not genuine original skeletal animation or complete accurate UV mapping. All user approvals remain unchecked. Node syntax test, source-image audit and ZIP CRC passed; WebGL visual testing unavailable.

## O — v1.8 game-prop materials, all-character previews, Slappers and mines

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-160 | Correct black world-object textures using their original prop texture sheets | IMPLEMENTED — VERIFY: 17 source prop texture choices, unlit materials | [ ] |
| GE-161 | Select original recovered source texture images for every weapon/item | IMPLEMENTED — VERIFY: 63 weapon/item images, provisional projected UVs | [ ] |
| GE-162 | Rebuild coherent connected third-person bodies for characters with failed mesh conversion | IN PROGRESS — v1.8 source head textures were square/back-facing; v1.9 curved-face repair pending playtest | [ ] |
| GE-163 | Show each character's real source face and clothing atlas rather than a generic face | IN PROGRESS — wrapped source portraits on curved heads in v1.9; original UVs still incomplete | [ ] |
| GE-164 | Preserve existing Boris character model during generalized preview changes | IMPLEMENTED — VERIFY | [ ] |
| GE-165 | Restore standard adult height across character previews; Oddjob shorter, Jaws taller | IMPLEMENTED — VERIFY: ~1.78m adults, 1.52m Oddjob, 2.02m Jaws | [ ] |
| GE-166 | Walk/sprint with articulated shoulders, elbows, hips and knees | BROKEN / UNAPPROVED — v1.9 procedural animation rejected by user; original source clips unavailable | [ ] |
| GE-167 | Add Slappers as a selectable first-person unarmed melee weapon | IN PROGRESS — Slappers input/hit logic works in code; authentic original model/animation unavailable | [ ] |
| GE-168 | Animate alternating left/right melee swing, impact checks and sound | BROKEN / UNAPPROVED — synthetic swing/audio rejected; v2.0 hides fabricated motion, original PCM cue candidate now available | [ ] |
| GE-169 | Restore original Remote Mine source mesh/texture and in-game placing | IMPLEMENTED — VERIFY: 80 source triangles | [ ] |
| GE-170 | Restore original Timed Mine source mesh/texture and 5.5-second detonation | IMPLEMENTED — VERIFY: 96 source triangles | [ ] |
| GE-171 | Proximity Mine green original texture and trigger radius | IN PROGRESS — source mine textures improved; Proximity chassis not converted | [ ] |
| GE-172 | Remote trigger key, mine counters, throwing arc and explosion visuals | BROKEN / UNAPPROVED — prior mines passed through walls; v2.0 swept collision attempt pending user test | [ ] |
| GE-173 | Original GoldenEye mine/slappers sound recordings and motion clips | NOT DONE — only newly synthesized effect clips | [ ] |
| GE-174 | Full ChromeOS visual interaction regression test of props, character scaling, melee and mines | NEEDS USER TEST — local test browser denied file access | [ ] |

**Accuracy:** 41 non-Boris characters have a reconstructed, articulated body using original source face/clothing sheets, not restored original skinning or game-authentic face UV layouts. Boris's previous source geometry is left alone. The original Proximity Mine texture exists, but its standalone geometry still fails decoding; the source Remote Mine chassis is a temporary visual substitute. Slappers hands, all gait motion, effects and sound clips are procedural recreations. World objects now use their own original game-source texture imagery, but UV projection remains approximate. Prior Snowguard height regression was not approved. The v1.8 local asset archive passed JavaScript syntax and embedded mesh/image checks; graphical Chromium access remained blocked. All user approvals remain unchecked.

## P — v1.9 curved faces, source materials, continuous world and roaming guards

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-175 | Replace square portrait plane with a curved forward-facing source-textured head surface | IMPLEMENTED — VERIFY (generated spherical face patch, user visual test needed) | [ ] |
| GE-176 | Correct face orientation while running forward; keep avatar local +Z as forward | IMPLEMENTED — VERIFY (third-person yaw consistent with movement) | [ ] |
| GE-177 | Use different recovered game-source texture sheets for car wheel, body paint, glass and grille | BROKEN / UNAPPROVED — user screenshot still shows vehicles white/bad materials | [ ] |
| GE-178 | Differentiate military truck and APC body, wheel, panel material groups | IMPLEMENTED — VERIFY (per-batch source sheets) | [ ] |
| GE-179 | Stop using posters and paintings as generated ground textures | IMPLEMENTED — VERIFY (23 curated source-image palettes) | [ ] |
| GE-180 | Use 23 explicit game-owned ground/wall/path/roof material sets | IMPLEMENTED — VERIFY (92 recovered images) | [ ] |
| GE-181 | Create continuous walkable terrain below/around original level geometry | IN PROGRESS — user still encountered source geometry holes/exterior placement issues | [ ] |
| GE-182 | Make interior building shells around complete source maps without covering authored interiors | IMPLEMENTED — VERIFY (source wall/roof textures, generated geometry) | [ ] |
| GE-183 | Install authentic converted door models at exterior entrance and interior test locations | IN PROGRESS — generated paired source-door exterior access added, locations remain unverified | [ ] |
| GE-184 | Place source GoldenEye crates, barrels, foliage and vehicles in world surroundings | IMPLEMENTED — VERIFY (17 converted model types) | [ ] |
| GE-185 | Spawn 3 roaming Snowguard enemies with source face/uniform images | IMPLEMENTED — VERIFY (provisional articulated avatars) | [ ] |
| GE-186 | Enemy patrol, vision checks, pursuit and movement | IMPLEMENTED — VERIFY (new AI state machine, not original) | [ ] |
| GE-187 | Enemy firing, damage, death, respawn and player armor interaction | IMPLEMENTED — VERIFY (prototype combat) | [ ] |
| GE-188 | Player weapons, Slappers and mine explosions affect nearby guards | IN PROGRESS — damage logic present, weapon and mine hit interactions not yet user verified | [ ] |
| GE-189 | Remove generated exterior, doors and NPCs on map switching | IMPLEMENTED — VERIFY (stale-load guards, no live playtest) | [ ] |
| GE-190 | Restore authentic original character faces, original stage door positions, UVs and navigation | IN PROGRESS / BLOCKED — source converters still incomplete | [ ] |
| GE-191 | Check v1.9 character faces, vehicle materials, ground surfaces and NPCs in ChromeOS | NEEDS USER TEST — headless WebGL blocked in environment | [ ] |

**Scope:** Original game maps stay the level centerpiece. The outer walls, terrain shape, paths and object placements are reconstructed code-generated geometry and layout, but use only genuine decoded XBLA texture images and converted original prop models. Character heads are curved rather than square pictures and face local +Z (the walking direction). The source-derived silver BMW, military truck and other props now have separate source-texture assignments for wheels/body/windows; UV mapping remains provisional. Three new Snowguard agents patrol, chase, can attack/take damage/respawn; AI is not the original game code. **No user approval recorded.** JS syntax, source-image decoding (92 environmental + 40 prop sheets), and one-ZIP CRC verified. Chromium local/localhost navigation returned ERR_BLOCKED_BY_ADMINISTRATOR, so graphical playtest remains pending.

## Q — v2.0 source effects, collision, loot and exploratory map access

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-192 | Decode original 30-frame Xbox firebomb CAFF image sequence | IMPLEMENTED — VERIFY: 24 coherent source frames used | [ ] |
| GE-193 | Extract original sfx.xwb/sfx.xsb PCM data without generated replacement recordings | IMPLEMENTED — VERIFY: 209 source 44.1kHz mono PCM WAV entries | [ ] |
| GE-194 | Resolve correct XSB event-to-XWB entry bindings | IN PROGRESS — cue-name string table order tentatively matched; not verified | [ ] |
| GE-195 | Replace fabricated glowing mine explosion with original firebomb sprite sequence | IMPLEMENTED — VERIFY; graphical test pending | [ ] |
| GE-196 | Original Slappers hand/fist animation/mesh | BLOCKED — source fist CAFF pool/animation decoder not ready; synthetic swing disabled | [ ] |
| GE-197 | Play provisional original-bank punch/explosion/mine/door WAV samples | IMPLEMENTED — VERIFY audio decoding, cue assignments not confirmed | [ ] |
| GE-198 | Mines use swept collision against floor, walls and doors rather than passing through | IMPLEMENTED — VERIFY (source polygons only), user test pending | [ ] |
| GE-199 | Orient stuck mines along source surface normal and display game-owned atlas | IMPLEMENTED — VERIFY | [ ] |
| GE-200 | Wall collision from actual converted source mesh with horizontal slide | IMPLEMENTED — VERIFY (not fully reconstructed collision/nav data) | [ ] |
| GE-201 | Stair lookahead for low risers with no roof teleportation | IMPLEMENTED — VERIFY, user test pending | [ ] |
| GE-202 | Recover true game collision maps and stair volumes for all original levels | BLOCKED / NOT DONE | [ ] |
| GE-203 | Source door-mesh paired portals between generated indoor shell and exterior | IMPLEMENTED — VERIFY (not original placement) | [ ] |
| GE-204 | Room-aware test crate placement near authored walls on source floor polygons | IMPLEMENTED — VERIFY (generated placement logic) | [ ] |
| GE-205 | Source box/cartridge/armor meshes exported and included | IMPLEMENTED — VERIFY, 7 newly extracted models | [ ] |
| GE-206 | Credits, plate, health, ammo loot in interactable crates | IMPLEMENTED — VERIFY (new gameplay economy) | [ ] |
| GE-207 | Buy stations using recovered source ammo crates for ammo/plates/health/weapons | IMPLEMENTED — VERIFY (reconstructed economy and UI) | [ ] |
| GE-208 | Reduce oversized vehicles and avoid spawning them immediately inside authored rooms | IMPLEMENTED — VERIFY (appearance requires test) | [ ] |
| GE-209 | Original vehicle material UV mapping / placement and correct scale across all maps | IN PROGRESS — previous screenshots show failures | [ ] |
| GE-210 | Restore full authored exteriors, cave/bunker entrances and object placements | IN PROGRESS — synthetic stage linkage is a test, not authentic source reconstruction | [ ] |
| GE-211 | Full acceptance test of v2.0 with stairs, collisions, mines, shops, audio on Chromebook | BROKEN in v2.0 — a syntax error prevented any gameplay from starting | [ ] |
| GE-212 | Optimize wall-ray performance and test on 8GB Chromebook | PLANNED — may be expensive on high-triangle maps | [ ] |

**User approvals:** All GE-192..GE-212 items are unchecked; no code or static test constitutes user approval. v1.9 complaints about floaty/white vehicles, wall/stair pass-through, fake Slappers and mine explosions are recorded as open regressions. The new soundbank source is actual original signed PCM and the firebomb artwork is sourced from the retail copy, but XACT cue binding needs independent parsing and the original character animations remain blocked. Generated crates, credits, gear station menus and exterior portal locations are explicitly not original GoldenEye-authored map elements.

## R — v2.0.1 mine-update parsing hotfix

| ID | Requirement | Development status | User approved |
|---|---|---|---|
| GE-213 | Repair v2.0 JavaScript parse crash at updateMines (Unexpected token at line 1069) | IMPLEMENTED — VERIFY in v2.0.1; user runtime test pending | [ ] |
| GE-214 | Add independent strict JavaScript AST parsing as QA gate beyond Node --check | IMPLEMENTED — VERIFY locally; zero parser diagnostics and checked mine-loop nesting | [ ] |
| GE-215 | Confirm local ChromeOS loading and gameplay after parse hotfix | NEEDS USER TEST; file:// warning may be independent | [ ] |

The user reported a startup-blocking syntax error in v2.0. The generator closed its `for (const m of gameMines)` loop before timed/proximity mine checks, leaving one extra closing brace. v2.0.1 fixes the nesting without altering source assets. All embedded JSON data parsed, the extracted module passed Node plus TypeScript AST parsing, and the new ZIP CRC matches. The separate file:// security warning is not claimed fixed. Previous regression approvals remain unchecked.
