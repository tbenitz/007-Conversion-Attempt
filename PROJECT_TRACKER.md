# GoldenEye XBLA — Master Development Tracker

Updated 2026-11-11, v0.9. Goal: polished playable exploration with complete assets, movement, audio, map building and optional missions.

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
| GE-014 | Accurate floor, slope and platform handling | IN PROGRESS | [ ] |
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
| GE-029 | Complete face/clothing materials | IN PROGRESS | [ ] |
| GE-030 | Hands grip weapon and original reload animations | PLANNED | [ ] |
| GE-031 | Correct third-person stride/turning | IN PROGRESS | [ ] |
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
| GE-040 | All original Facility/stage doors and animations | PLANNED | [ ] |
| GE-041 | Mantling through real window openings | IN PROGRESS | [ ] |
| GE-042 | Separate real level collision and navigation mesh | PLANNED | [ ] |
| GE-043 | Reconstructed proper stair/ramps colliders | PLANNED | [ ] |
| GE-044 | Elevators/ladders/moving platforms | PLANNED | [ ] |
| GE-045 | Gun/prop textures and UV maps | IN PROGRESS | [ ] |
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
| GE-059 | Compass, HP, stamina and exploration HUD | IMPLEMENTED — VERIFY | [ ] |
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
