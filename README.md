# World Explorer v1.9 — Source-textured world shell, curved character faces and roaming Snowguards

**Downloadable single HTML + ZIP:** The user-owned offline-style release `GoldenEye_World_Explorer_v19_SINGLE_GAME.zip` is delivered through this conversation. It embeds game-derived content from the user's copy; Three.js still loads via CDN. Copyright-derived game meshes and images are *not* committed here.

### v1.9 response to player screenshots

- **No backward square heads:** Replaced the portrait billboard on reconstructed character heads with a curved spherical face surface, facing the player's forward movement direction. The true original rig/head UVs are still not restored.
- **Not white vehicles:** The original converted BMW and truck meshes remain; wheel/tire, silver side/body, glass, grille and green truck panel surfaces now select distinct **real GoldenEye game images**, with temporary projected UVs where original UVs are missing. 17 recovered prop model types are placed in the environment.
- **No paintings for ground:** Inspected level texture sheets and curated ground/wall/path/roof material image selections for every one of the 23 map options. Archives ground now uses the source stone floor texture, not its paintings/portraits. 92 decoded game images are embedded in the curated environment set.
- **Larger connected world:** Keeps each actual converted level as the central geometry, adds a continuous *visible and walkable* ground mesh under it (including conversion holes), rolling outskirts and textured paths. Indoor stages get an outer building shell and converted original game-door meshes at generated accessible entrances plus some interior demonstration doors. Terrain and new wall geometry are generated; material images are original.
- **Roaming guards:** Three procedural Snowguard NPCs appear around the map spawn. They patrol, detect/chase the player, fire at intervals, take weapon/Slappers/mine damage, fall down and respawn. Toggle them off in the menu. They use recovered Snowguard face/uniform images but reconstructed animated bodies and newly coded AI, not original GoldenEye enemy animations or game logic.

### Quality gates and limitations

All 23 map choices, 42 character selections and 64 selectable weapons/items are retained. Source imagery and proxy geometry *do not guarantee original asset fidelity*. Accurate head/prop UV maps, original collision/navigation, authored door placements, original skeletal animations and Aztec conversion remain unresolved. Browser visual testing on ChromeOS is still required: Chromium in the test container blocks both local-file and localhost URLs. Static Node JS syntax, 92+40 embedded source-image decode checks, converted prop GLB openings, and ZIP integrity have passed. All user acceptance checkboxes stay unchecked.

[Master progress tracker (GE-001 through GE-191)](PROJECT_TRACKER.md)

---

# GoldenEye XBLA World Explorer v1.8 — Source-textured characters, Slappers and mines

**Latest user's screenshot:** Facility/Bunker map textures show again, but props render solid black, Suit Bond and many other characters lack proper body textures, and Snowguard looks unnaturally short. v1.8 targets those regressions using original game source face/clothing/prop/gun texture atlases.

**New in private downloadable game:** 41 proportional reconstructed character previews using recovered source face and clothing textures (plus previous Boris asset), procedural walk/run limb articulation, 17 source-prop diffuse texture replacements displayed with unlit materials, source texture previews for all 62 original gun/item models, Slappers melee mode, and Remote/Timed/Proximity mine selection with throws, detonations, ammo counters and newly synthesized sounds.

**Mine asset provenance:** Remote Mine (80 converted original faces) and Timed Mine (96 faces) use the recovered original chassis and red/blue original texture atlases. Proximity Mine uses the genuine green source atlas *on the converted Remote chassis* because the separate proximity mesh decoder remains broken. All three can be placed; Remote detonates with G, Timed triggers after roughly 5.5s, and Proximity triggers near the player for standalone testing. Explosions and sounds are procedural, **not extracted from the game**.

**Visual limitations:** The original character rig and UV charts are still unavailable. The character bodies in v1.8 are rebuilt previews, not restorations of the game's original bodies; source atlas mapping is approximate. This is not a finished game. The original Boris model is left unchanged. The archived source assets are not in this public repository.

**Verification:** New JavaScript passes Node's module syntax check; converted mine GLBs reopen; original texture sheets decode. The local Chromium environment returned `ERR_BLOCKED_BY_ADMINISTRATOR` when attempting to open the HTML, so graphics and interaction require user testing. All feature approval checkboxes in [PROJECT_TRACKER.md](PROJECT_TRACKER.md) remain unchecked.

---

# v1.7 — Black material regression rollback and visible Snowguard head

After user testing reported that **even previously working Facility textures became black**, the new downloadable game does not modify Facility's source GLB material instances/UVs at all. For the other 22 available maps, material repair now rebuilds invalid material batches using recovered source map images and **MeshBasicMaterial** so inverted normals and absent indoor lighting cannot produce a black shader result. UVs are reprojected as a temporary visualization method; authentic source UVs remain incomplete.

Snowguard's real head batches still exist, but their shape/UV data made the head effectively invisible in the v1.6 preview. The new build retains those source batches and provides a **provisional hood/head volume** textured with the original Snowguard face atlas. It is not an original rig or animated original head model.

**Verification:** Node syntax checked, original image sets readable for all 23 available maps, single ZIP CRC checked. **ChromeOS GPU visual playtesting remains unverified.** Aztec remains unsupported. Read [PROJECT_TRACKER.md](PROJECT_TRACKER.md) for user-reported regressions and GE-155–159. Never mark feature user-approved without explicit user confirmation. No user-owned copyright-derived assets have been committed to the public repository.

---

# v1.6 — Black-scene visibility and Snowguard character rebuild

**Playable user-owned download:** `GoldenEye_World_Explorer_v16_ONE_ZIP.zip` containing a single HTML game with embedded 23 maps, 42 character meshes, 62 gun/item meshes and the original game texture imagery (no copyrighted files checked into this repository).

## Fixed or changed in code (awaiting Chromebook playtest)

- **Black / silhouette maps:** Bunker, Bunker2, Statue Park, Dam and Cavern now use map-specific oversized-face cleanup to remove likely conversion artifacts. Bunker had 3,388 removed; Bunker2 3,401; Statue Park 17,255; Dam 34; Cavern 8. This cleanup is experimental, may discard legitimate giant source polygons, and does not restore missing game geometry.
- **Unlit interiors:** stronger hemisphere lighting, a camera-proximate fill light, and source-texture emissive fill keep converted rooms and underground areas from relying solely on sunlight.
- **Source texture selection:** avoids discarding valid snow, shadow and concrete images just because they contain white/dark pixels. Original texture index mappings are retained where available; UV projection remains provisional.
- **Snowguard:** source body GLB batches 000–009 are effectively flat, disconnected geometry. The viewer keeps the original head and its eye-mask atlas and rebuilds a provisional articulated winter uniform/boots from Snowguard's actual recovered texture sheets. This is **not** its original geometry rig or animation.
- **Character ground alignment:** all characters now position their lowest geometry at the floor. The locomotion loop no longer overwrites the vertical rest offset each frame.

**Validation:** Main JS passed Node syntax checks, five filtered GLBs reopen and all their recovered texture images can be loaded, and the single ZIP passes archive CRC. The available Chromium sandbox has failed WebGL/EGL initialization, so no graphical success is claimed. All feature approvals remain unchecked.

[Master issue tracker, GE-001 through GE-154](PROJECT_TRACKER.md) · [Oversized-face conversion audit tool](tools/clean_oversized_meshes.py)

**Open priorities:** original map UV chart recovery, real collision and map spawns, authentic character geometry and skeletal animations, Aztec decoding, actual game doors and placements.

---

# World Explorer v1.5 — white-wall material repair and 23-map audit

**This release targets the reported failure:** 23 of the selectable XBLA background meshes existed but still displayed many mostly-white surfaces. Their source material indices were available; their converted UV charts were incomplete and the previous fallback sometimes chose game decals/masks instead of usable environment textures.

### Changes in the single-file private download

- Rebuilt *per-map* texture fallbacks from the user's original recovered GoldenEye source sheets. Excluded mostly-white, mostly-black, low-variation and mask-like images; every map has 4–6 alternative game-source images.
- Render mode **Restore visibility with original game-source wall/floor textures** is enabled by default. It keeps an existing usable original source texture when possible and replaces bad source images with game-owned material fallbacks.
- Triangle-local UV projection on converted meshes with missing/incorrect UV data, rather than stretching an atlas or sampling one point repeatedly. Existing well-textured Facility UVs are retained wherever usable.
- Preserved transparent game materials (glass/decals), reduced overbright exposure, and disposed of temporary projected geometry/materials when changing levels.
- All 23 packaged map GLBs verified readable programmatically (**518,836 triangles total**), with source image references. **Aztec remains missing** due to original CAFF parser failure.
- Recompressed opaque source textures inside GLBs to high-quality JPEG; preserved textures with alpha as PNG. One archive is approximately **28.5 MB**.
- `MAP_TEXTURE_QA.json` within the download lists material/image counts, original atlas sources, and expected fallback count for all 23 maps.

**Important limitation:** This repairs *visible game-owned texturing* through projection. It is **not yet a complete, visually verified reconstruction of the game's original per-triangle UV charts, all geometry, authentic object positions, or Aztec**. The 23 map models remain partial source geometry, and map appearance still needs a real Chromebook playtest. The browser test environment blocks local-file navigation; static JS syntax, map GLB readability/image validation, and ZIP CRC passed. User-approval checkboxes remain unchecked.

[Master requirements tracker](PROJECT_TRACKER.md)

**One-file policy:** copyrighted source-model data stays in the user's private downloadable HTML/ZIP, not committed to the public repository. This repository only hosts source converters, renderer helper code, reports and the tracker.

---

# GoldenEye World Explorer v1.4 — Game-asset-only generated environments

**Downloadable standalone build:** `GoldenEye_World_Explorer_v14_ONE_ZIP.zip` is delivered in the ChatGPT conversation. It contains one self-contained HTML with converted map/prop meshes and game-derived textures embedded (external Three.js module CDN still required).

### Changed after v1.3 reports of white walls, missing ground and empty maps

- On 23 converted maps, reprojection of source textures onto incomplete/blank map materials using local geometry normals and position instead of the inaccurate fixed-point UV scaling. This is an **approximation**: original material UV chart coordinates are not faithfully recovered.
- 92 **actual GoldenEye Xbox texture images** selected from corresponding map CAFF atlases. No external stock imagery or invented diffuse textures.
- Procedural exterior terrain **geometry** around all 23 converted map bounding boxes, with rolling hills and 3 textured approach paths; all rendered texture images sourced from original game assets. The new topography, path layout and alignment to the map **are generated**, not authentic original GoldenEye stage layout.
- 17 converted source prop model types (including actual game-source trees, trucks, barrels, crates, barricades) placed in user-test arrangements around the map and near spawn. They are not fake cone trees or generic proxy crates. Texture UVs for some props are provisional.
- Menu toggles to compare map texture repair, generated exteriors and game props independently, all on by default.
- Reuses original map geometry and per-map spawn candidate while leaving authentic collision/navmesh, terrain transitions and original map-object positions as open requirements.

### Validation

`node --check` passed and the single ZIP CRC test passed. Full in-browser interactive rendering could not be tested because local-file access was blocked in the Chromium test environment. **No user approval is inferred.**

[Full tracker — GE-001 through GE-136](PROJECT_TRACKER.md)

**Game-derived meshes and textures are intentionally not checked into this public repository.** The user-supplied retail archive remains local to the user; the downloadable HTML contains their converted files.

---

# World Explorer v1.3 — source-map textures, spawn safety, distinct footsteps

User-download artifact: `GoldenEye_World_Explorer_v13_ONE_ZIP.zip` (one ZIP with the standalone asset-embedded HTML, reports, and README).

**Source-level material conversion:** Original Xbox CAFF opcode 0x2d records identify the texture bound to each original draw batch. The local pipeline uses preserved `batch_NNN` GLB names to associate textures with 22 converted map GLBs and retains the previously textured Facility. 23 total playable selectable maps are embedded. Aztec remains unsupported. Recovered source UVs are signed 16-bit values with **provisional** scale/offset choices; not every texture placement has been verified. Invalid or unresolved batches remain vertex-colored.

**Spawn/floor fixes:** Map-specific starting points are drawn from original horizontal polygons rather than a ray cast down from each map's roof. Stair stepping is limited to a nearby support elevation rather than jumping onto overhead surfaces. The relocated Surface outdoor overlay is **OFF by default**, so it cannot unintentionally present a barren exterior on load. Missing genuine collision surfaces and map geometry remain unfinished.

**Audio:** The walk/run triggers now call a quiet filtered shoe-contact synthesizer rather than the WAV samples that resembled gunshots. Shot audio is only called by the weapon-fire action.

**Verification:** Node JavaScript syntax and single ZIP CRC tested. Interactive visual playback has not been validated. All feature checklist approvals remain unchecked.

[Master tracker: 125 stable requirements](PROJECT_TRACKER.md)

---

# v1.2 — Ground fall-through safety + character texture atlas audit

**User test build:** One downloadable HTML/ZIP made from the user's supplied source game files. Ground-fall protection is now **enabled by default**, holding the last known supported floor height if the imported level is missing a polygon underneath the player or has an incorrect lower surface. This does not invent visible geometry or replace the source map: **visual holes remain**.

**Character materials:** The source assets carry separate face and clothing texture atlases. The new preview uses a different recovered sheet for each region for 41 character options, plus skips flattening artifacts in the source mesh preview. Boris remains exempt from automatic remapping to preserve previous manual work. All these bindings use approximate projected UVs — **they do not yet faithfully reproduce every original game character**. The original per-vertex UVs, proper mesh weights, authentic rigging and animations still require a source decoder.

**Verification:** JavaScript syntax and ZIP integrity tested. No interactive ChromeOS browser playtest yet. The complete feature tracker now has 115 stable requirements, and all user-approval boxes remain unchecked until the user verifies the features.

[Master tracker](PROJECT_TRACKER.md)

---

# v1.1 — GoldenEye source doors and outdoor Surface terrain

The private downloadable game **GoldenEye_World_Explorer_v11_ONE_ZIP.zip** contains one playable HTML file with the existing 23 maps, 42 partial characters and 62 gun/item meshes.

**Response to user screenshots:** Removed the synthetic doorframe, solid placeholder door panel and orange glowing sphere. The Facility demo doors now use converted original XBLA prop geometry and source door texture sheets. UV texture projection remains provisional; door positions are test placements, not recovered original Facility coordinates.

**Exterior:** Retains **3,878 original source triangles** from the XBLA Surface map after removing triangles overlapping Facility's footprint, with a vertical world offset. No generated terrain polygons, invented trees or fabricated hills. The actual physical connection between Surface and Facility is not claimed: it is a relocated original-game-ground demonstration. Toggle it using **Show original Surface outdoor ground** in the game menu.

**Remains open:** actual stage prop transform decoding, correct game material UVs, Facility exit-door alignment, uninterrupted walkable exterior, authentic stage transition, stair/wall collision and animated character skeletons.

Source-only conversion scripts can be run locally against files extracted from the user's legally supplied game copy. **Copyrighted meshes, source textures, and derived private builds are not committed to the public GitHub repo.**

[Track all 106 requirements](PROJECT_TRACKER.md). No user-approval checkboxes have been checked by the assistant.

---

# World Explorer v1.0 — HUD, animations, doors and tactical map

**New private single-ZIP build (downloaded from this conversation):** 23 maps, 42 character meshes, 62 gun/item meshes. Adds a first-person ammo/reload HUD, armor and health, collectible test pickups, M fullscreen tactical map drawn from converted mesh triangles, original-derived door meshes with E interaction and user-position controls, procedural movement deformation, and 10 original-created synthetic WAV effects.

**Source accuracy:** Authentic **door locations are not recovered**. The default Facility map places three door meshes at grounded showcase positions near player spawn; the user can move/place them to test. Weapon/character texture images are read from original assets but their UV positions remain unconverted, so the new optional preview uses automatically projected UV coordinates rather than authentic UVs. No original character skeletal animation or game sound pack has been decoded.

**Verification:** JS syntax and ZIP integrity were tested. A headless browser test timed out and the player has not approved this version. Free world traversal remains default because the correct wall/stair collision is still unresolved.

[Full 96-ID master tracker](PROJECT_TRACKER.md) | [Original conversion tools](tools)

**Controls:** WASD movement; Shift sprint; Space jump; V first/third person; R reload; M full map; E operate nearest test door; P place test door; K toggle sound; F free flight. Menu: door asset type / relocate / reset, original vertex colors versus projected texture preview.

**Do not mark any checklist approval boxes until the user validates the feature.**

---

# GoldenEye XBLA World Explorer — v0.9

**Current build:** 23 partial maps, 42 converted character meshes, 62 gun/item meshes. A single downloadable HTML contains the user-supplied-derived assets (not published in this public repository).

### Project status and feature tracking

**[Open the 82-item master feature tracker](PROJECT_TRACKER.md)** — development status and user-approval checkboxes kept separate. Features are **never** approved based solely on code changes or tests.

### New in v0.9

- Smooth walking acceleration, sprinting with stamina, crouch and jump with gravity
- First-person head bob, camera tilt, sprint FOV, third-person obstruction checks
- Generated Web Audio footsteps, gunfire effects, jumping/landing, wind ambience; audio volume and toggle
- Day/night lighting, adjustable fog and brighter weapon lighting
- Compass, exploration markers and discovered-location progress saved locally where allowed
- One-click Next World, preserved map/character/weapon selection

**Not yet complete:** original Boris/other character rigs and animations, authentic weapon sounds, many gun/character textures, Aztec, true solid-world collision, walkable steps with walls enabled, original level doors and prop placements. The current build intentionally preserves freely passing through incomplete walls to avoid the user-reported staircase deadlock.

**Testing:** source JavaScript syntax and ZIP integrity verified; interactive Chromium testing was blocked by local URL policy. All user-approval boxes remain unchecked.

**Delivery:** The proprietary model/textures from the supplied XBLA package are provided in a private downloadable **one-ZIP** build. This public repo contains extraction/conversion/viewer code and tracking, not the proprietary assets.

---

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
