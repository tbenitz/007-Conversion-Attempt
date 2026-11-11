## v0.8 — 2026-11-11: multi-map exploration and first-person weapons

The user-download `GoldenEye_World_Explorer_v08_COMPLETE.zip` contains a **single standalone HTML** with these assets embedded:

- [x] 23 selectable background geometry maps (Facility prefers the textured, patched GLB; the other maps are partial vertex-colour geometry)
- [x] 42 selectable original character **geometry** models
- [x] 62 selectable XBLA gun/item geometry models, including 20 recognizable firearm models
- [x] First-person default, with selected original 3D weapon geometry in view and rotation sliders per gun
- [x] Third-person character preview, camera mouse controls, sprint and cosmetic gun recoil/flash
- [x] Free movement by default to prevent the previously reported staircase deadlock
- [x] File-integrity and JavaScript syntax checks
- [ ] Chrome graphical playtest: blocked by browser testing sandbox; user verification needed
- [ ] Correct all remaining 3D model placement and weapon axis transforms
- [ ] Convert all corresponding textures and UV/material assignments for non-Facility maps, character bodies and guns
- [ ] Original game character skeletons, walk/run animations, doors, props and true collision
- [ ] Repair Aztec and other nonconvertible resource files
- [ ] User feature approval (do not mark as approved until user confirms)

The build intentionally embeds user-provided copyrighted source-derived assets **only in the private downloadable artifact**, not in GitHub. The hosted GitHub source remains an experimental GLB-import viewer; it does not include these assets. The downloadable HTML does *not* require separate GLB uploads to run, but it needs a connection to load the Three.js CDN modules.

### Resource counts

Original 23 exported level meshes plus 42 successful character mesh conversions and 62 successful gun/item mesh conversions. Six character/gun items failed and are recorded in the downloadable `conversion_report.json`.

**Known limitations:** Most models are partial geometry, not complete textured levels or rigged animated game characters. A chosen weapon uses its real converted mesh, but pose/orientation may require the angle sliders; a cosmetic click/recoil is not a combat simulation. Wall collision is deliberately disabled for traversal until the staircase bug and source geometry can be properly fixed. Aztec remains unavailable.

## v0.7 — 2026-11-11: stair rollback + bulk content conversion

**Playable game:** `goldeneye_facility_explorer_v07_free_stairs.html` (user download) uses the original v0.1 principle: move horizontally without requiring a collision-mesh hit. The later collision algorithm repeatedly trapped the player against stairs. This build therefore **disables source wall collision by default** rather than claiming to have a completed character controller.

- [x] Free horizontal movement by default, including through incomplete imported mesh collisions
- [x] Best-effort ground/stair-following with forward higher-tread probe
- [x] Experimental solid collision toggle (C), OFF by default
- [x] PageUp / PageDown manual altitude correction at geometry gaps
- [ ] Verified correct automatic staircase traversal on Chromebook (user approval required)
- [ ] Fully reconstructed wall collision and authentic navigable stair surface

**Bulk conversion completed from user-supplied XBLA retail package:**

| Item | Result |
|---|---:|
| Remastered source asset bundles examined | 499 |
| Successfully decoded bundles | 489 |
| PNG texture images decoded | 3,039 |
| Remastered map backgrounds with partial GLB geometry | 23 of 24 |
| Unresolved source bundles | 10 |

The 10 exceptions are documented in `conversion_report.json` inside the downloadable user-owned asset pack. Aztec is among them. Individual texture records in successfully decoded bundles had no reported decode failures.

**User deliverables:** `GoldenEye_XBLA_ALL_Converted_Assets.zip`, plus smaller `GoldenEye_XBLA_Levels_Assets.zip`, `GoldenEye_XBLA_Characters_Weapons_Assets.zip` and `GoldenEye_XBLA_Props_Assets.zip`. The bundles contain numbered source PNGs, source CAFF resource files, an inventory and 23 partially decoded geometry GLBs.

**What these packages are NOT:** complete fully textured playable stages, original skeletal animations, accurate map collision, placed interactive doors, or a random map generator. The GLBs are partial vertex-colored meshes with separate numbered texture images. Mapping source image indexes and UVs for *all* draw batches remains further work.

**How to repeat:** `python tools/bulk_extract_and_decode.py user-provided.live output_dir` after installing the NumPy/Pillow dependencies. The source package has to be supplied locally by its owner.

**Public repository policy:** Script and viewer code are committed here; copyrighted extracted models, textures and derived game builds are not committed to this public repo.

## v0.6 — November 11, 2026: user-reported leg and stair fixes + traversal interactions

This release responds to the supplied screenshot showing Boris's lower legs/boots missing and the character blocked on stairs.

- [x] **Local standalone playable HTML** rebuilt with Boris's original head and facial textures, connected reconstructed trousers, articulated knees, boots, jacket and arms.
- [x] Walk and sprint drive explicit hip, knee, shoulder and elbow movement. Original skeletal animation/rig is still **not recovered**.
- [x] Improved stair stepping using forward ground probes, vertical riser bypass only when a higher valid tread is found, and fall/landing physics.
- [x] Local interactive **demonstration** door that opens with E or automatically as the character sprints toward it; N places a demonstration door on the floor ahead (up to 12).
- [x] Space mantle for detected low obstacles with landing checks; this is experimental, not yet an original game's authored window system.
- [x] Player HP with fall damage (greater than 3 scene units) and respawn.
- [x] Updated public-source viewer; it asks the player to supply local GLBs.
- [ ] Verify step traversability on every Facility staircase from actual Chromebook playtesting.
- [ ] Proper character skeleton, skinning and original walk/run clips.
- [ ] Original level doors with exact asset locations, opening/closing sound and physics.
- [ ] Find and reconstruct the authentic windows and mantle collision profiles.
- [ ] Verify damage balance and address missing original geometry.
- [ ] User acceptance testing; current functionality is **not approved** by the user.

### v0.6 controls

WASD walk, Shift sprint, mouse look, E interact with a nearby door, N place a demonstrator door, Space mantle a ledge/window (Space ascends in free-flight), F toggle free flight, V switch first/third person, R respawn/reset, Esc unlock mouse.

**Accuracy note:** The original Boris asset conversion still contains broken rigid vertex layouts. Reconstructed legs and clothing are not the source game's original character rig. Doors are placed interactively/demonstration props, not recovered Facility placements. Missing geometry cannot be assumed complete; movement and collision remain experimental. The local build is self-contained except for Three.js CDN. A scripted Chromium playtest was attempted but the browser environment blocked local URLs, so no graphical-playtest success is claimed.

# 007 Conversion Attempt

A playable GoldenEye 007 XBLA Facility geometry-and-texture conversion experiment built from **user-supplied** XBLA game files.

## v0.5 — November 11, 2026: screenshot-reported Boris and stair fixes

- [x] Diagnose exploded/disconnected Boris: converted arm/torso mesh batches 000–005, 010–012 are effectively planar in source GLB, not simply texture rotations.
- [x] Hide those malformed batches in both the local embedded build and the hosted source viewer.
- [x] Rebuild provisional articulated torso/arms using a crop of Boris's genuine jacket atlas, retaining original character head, face, lower-body and shoe geometry.
- [x] Animate reconstructed shoulder/elbow joints and procedurally deform the retained leg geometry in the local build.
- [x] Raise walkable stair step-up threshold to 0.9 scene units and change collision tests to let low stair risers pass while continuing to block higher walls.
- [x] Provide self-contained local v0.5 HTML and a ZIP with embedded user-derived assets and source.
- [ ] Restore character skeleton / actual XBLA animation clips; current gait is procedural.
- [ ] Complete detailed geometry conversion and proper character-controller collision, including steps, doors and slopes.
- [ ] Independently validate gameplay with actual browser playtest and user approval.

**Important:** The converted static Boris model has severe vertex-layout/skeleton issues. This interim fix does not constitute proper reconstruction of his source rig. The public GitHub viewer still requires users to import their locally converted GLBs, because copyrighted game models and textures are not pushed to GitHub.

## v0.4 — November 11, 2026: walkability, Boris gait and gap repair

The downloadable standalone local HTML version `goldeneye_facility_boris_walkable_v04.html` includes assets from the user-provided XBLA package and starts directly as Boris. The **hosted GitHub viewer** runs the updated controls but still asks you to import the two locally converted GLB files; game artwork is not committed.

- [x] Replaced fail-closed floor ray with nearest walkable ground sampling; a missing source-floor polygon no longer completely freezes horizontal movement
- [x] Added horizontal wall collision against the rendered source Facility mesh with sliding along surfaces
- [x] Added third-person camera occlusion ray so it comes closer when near walls
- [x] Added a **procedural** Boris leg/arm gait that activates during movement (shader-driven deformation of original model, not original skeletal animation clips)
- [x] Compared the supplied remastered Facility geometry to its **original-generation** background; recovered 165 unmatched source triangles as a separate repair mesh (total 13,919 triangles in the local patched asset)
- [x] Added `tools/patch_missing_facility.py` for repeating the original-geometry gap repair with user-provided locally extracted files
- [ ] Decode original Boris skeleton and authentic walk/run animation clips
- [ ] Place all doors, props and interactive objects using original stage setup data
- [ ] Reconstruct full original collision/nav areas (the `background_hits` data is projectile impact data, not a drop-in character navigation map)
- [ ] Verify every patch face and source UV/material, including in browser on Chromebook
- [ ] Full Facility gameplay and user playtest

**Important limitation:** this is a materially improved **explorer**, not a completely reconstructed game level. The missing 165 source polygons are colored because their original-generation material atlas is not yet merged into the remastered atlas. Doors and props may still be absent. Geometry-based wall collision cannot block an opening where the source conversion has no wall polygon.

Controls: WASD walking, Shift running, mouse look, V first/third person, F free-flight, Q/E altitude in flight, R reset, Esc unlock pointer.

To patch the locally converted Facility GLB:

```bash
python -m pip install numpy scipy trimesh
python tools/patch_missing_facility.py converted/facility_textured.glb local-assets/files/original/background/facility/default.bin converted/facility_textured_repaired.glb
```

When running the hosted viewer, import `facility_textured_repaired.glb` and `boris_textured.glb`. The standalone HTML already embeds both.

## Earlier v0.3 — Textured Facility + playable Boris

**Implemented in source:**
- [x] Corrected user-supplied XBLA/STFS extraction to CAFF asset bundles
- [x] CAFF resource-table parser
- [x] Decode all 69 source Facility images (tiled Xbox GPU images / DXT)
- [x] Decode all four Boris source images
- [x] Read shader/material image slots from CAFF draw commands
- [x] Export textured Facility GLB (120 meshes; 118 linked with source textures)
- [x] Export textured Boris GLB (16 meshes; all linked with source textures)
- [x] HTML viewer imports the textured GLBs and defaults to Boris in third person
- [x] Ground-height following, WASD, mouse look, Shift sprint, V camera, F free-flight
- [ ] Verified geometry/collision of every original Facility surface
- [ ] Decode all remaining unusual UV layouts and material variants
- [ ] Character skeleton and walk animation
- [ ] Solid wall/door collision and traversal
- [ ] Mission AI, doors, authentic spawn points and objectives
- [ ] User playtest and approval

**Known limitations:** The 13,754-triangle Facility export is an experimental partial decode, not guaranteed to include every original surface. The textured Boris is a static unrigged source model that can be moved as the player, **not an animated walking character**. The floor-following algorithm is an approximation, not authentic physics. The original source textures are recovered but some UV transforms/special materials may be incorrect; don't consider them validated until playtested.

## Downloadable single-file prototype

The ChatGPT-provided `goldeneye_facility_boris_textured.html` bundles the two user's converted GLBs inside the HTML, loads Three.js over CDN, and starts as Boris. This artifact is **not committed to the public repository** because it contains derived copyrighted GoldenEye artwork and models.

## To prepare the same files locally

Install Python 3 with `numpy pillow trimesh`, then use the user's own ZIP:

```bash
python -m pip install numpy pillow trimesh
python tools/extract_xbla.py GoldenEye_007_XBLA_Retail.zip local-assets
python tools/decode_textures.py local-assets/files/new/background/facility/default.bin textures/facility
python tools/decode_textures.py local-assets/files/new/char/boris/default.bin textures/boris
python tools/export_textured_glbs.py local-assets textures converted
```

Then open `index.html` in Chrome and select `converted/facility_textured.glb` and `converted/boris_textured.glb`. The GitHub-hosted viewer requires those two local files to be supplied by the user; it does not host the game's artwork.

### Controls

WASD move • mouse look (click Explore) • Shift sprint • V toggle third person • F toggle free-flight • Q/E descend/ascend during flight • Esc release mouse • Reset button.

### Original game materials

The texture format is Xbox 360 Xenos tiled GPU surfaces; the numbered images are linked using material op `0x2d` image indices in each draw command. A small number of unusual meshes remain untextured while their vertex/UV layout is being researched.

Conversion code was informed by [Sightline's published format research](https://github.com/mscrnt/Sightline). Source asset bytes and user-provided game files are deliberately excluded from this public repository.
