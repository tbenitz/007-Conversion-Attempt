# 2026-11-12 — Public viewer: 10× generated outdoors + real glTF rig audit (work in progress)

> **Latest source-authentic research release (2026-11-12): v4.7.** The user-owned private ZIP `GoldenEye_World_Explorer_v47_NATIVE_AI_OBJECTIVES_SOURCE_AUDIT.zip` contains the playable-browser prototype, original embedded assets, decoded collision/setup/AI records, decoders, and the complete per-stage objective/map audit. Its static checks pass but the full original campaign is **not yet playable**: only the six original Train brake-controller targets have a connected runtime model, and native exits/global AI/most objective interactions remain incomplete. No original-game asset payload is published in this repository. See [v4.7 research audit](research/V47_NATIVE_MISSION_AND_MAP_AUDIT.md) and [master tracker](PROJECT_TRACKER.md). All new gameplay acceptance remains unchecked until user testing.\n\n
**Scope:** The repository contains the older public `index.html` viewer, not the private v2.8 asset-embedded build described below. This update edits the committed public viewer only. It does not alter the unavailable private v2.8 ZIP, and does not claim any newly recovered Xbox animation bytes.

- `src/outdoor.js` adds four **generated/reconstructed** outdoor outpost compounds, tree models and cover. A deterministic seed requests **540 combined tree/cover placements** (10× the previously documented 54 source-prop placements) and returns the actual placed totals on screen; generated compound walls are additional geometry. Instanced meshes keep tree draw calls low. Ground, boundary walls and approximate horizontal obstacle collision are included. These are not extracted original GoldenEye objects. Per-object collision and ground integration still need in-browser playtesting.
- `index.html` loads the exterior at start and displays counts. It imports authored glTF animation clips **only when provided in the locally uploaded GLB**, clones actual skinned meshes with Three.js SkeletonUtils and selects recognized idle/walk/run tracks by names. J/H/K can preview authored firing/hit/death tracks if present. Naming conventions are guesses, and the old fallback articulated animation remains procedural. The broken `a.body.position` access in the fallback gait is fixed.
- `tools/audit_rigs_and_animations.py` (standard-library only) inventories glTF nodes, child/parent links, joint indices, inverse bind matrix accessor metadata, skin roots, animation target channels and sampler metadata. It **does not** decode source CAFF animations; use it on user-converted local GLB files to collect evidence before mapping native skeleton and animation bank formats.
- **Outstanding:** native CAFF/XEX authored animation parsing; confirmed bone hierarchy/coordinate frames; animation-to-character/source ID mapping; retargeting if exported GLBs are unskinned; reliable local Chromebook WebGL QA; test of generated obstacle placement and collision. No user approval is implied.

Example: `python tools/audit_rigs_and_animations.py boris_textured.glb --out rig_report.json`

---

# v2.8 — Original Xbox skeleton metadata research and outdoor room compounds

**Original source findings, not invented clip data:** Direct analysis of the user's original GoldenEye XBLA STFS package found 42 original and 42 remastered `char/*_hits/default.rbh` resources. Their CAFF payloads include actual `SKEL_*` bone/skinning names (`SKEL_RT_HIP`, `SKEL_RT_KNEE`, `SKEL_RT_ANKLE`, `SKEL_NECK`, wrists, etc.) and `|POSITION|BASE|...` skinning chains. The per-character audit lists **765 joint/skinning label entries in original and 1,060 in remastered** files, with original byte offsets and SHA-256. Label counts are not unique bones, and several files expose no names. **No original pose frames or authentic clips have been decoded yet.**

The original animation catalog documents walk `0x28`, run `0x29`, jogging `0x2A`, fire while walking `0x30`, hit shoulder `0x0E`, hit arm `0x10`, hit leg `0x14`, death forward `0x1A`, backward fall `0x1C`. Source: https://goldeneyedepot.com/anims . The user-download contains a 62-ID reference manifest; it is a research mapping, not raw animation bytes. Current guard logic records desired source clip IDs for walk/fire/hit/death but **does not play original clips**. The legacy procedural fallback is still clearly separate. Genuine XBLA animation bank or source XEX2 tables are not yet unpacked.

**More substantial exteriors:** Up to nine existing original-prop cover yards are now surrounded by **new game-textured multiroom enclosures**, with up to 72 wall segments, 18 partly roofed rear rooms, and nine terrain-following open walkways. Each open front entry and inner room passage is 3.7 scene units wide. Walls are included in source-textured generated collision and use distance prechecks to avoid expensive offscreen rays. The props remain game-derived crate/ammunition/barricade meshes; wall arrangement and wall geometry are generated, **not restored original GoldenEye buildings**.

**Private deliverables:** `GoldenEye_World_Explorer_v28_OUTPOSTS_AND_RIG_RESEARCH.zip` (playable asset-embedded HTML, 42/42 rig report and code) and `GoldenEye_v28_ANIMATION_RESEARCH_SOURCE_ONLY.zip` (full code, rig audit and reference catalogs without embedded game media). No copyrighted assets added to this public repository.

**QA:** Node `--check` and independent TypeScript AST parser pass, rig audit checks and generated wall-gap/collision-broadphase assertions pass, archives pass CRC. Chromium refused local HTML with `ERR_BLOCKED_BY_ADMINISTRATOR`; no visual test or user approval. Existing stairs, source collision, original skeletal skinning, original motion clips and head UVs remain open.

---
# GoldenEye World Explorer v2.7 — Physical ramps, solid retaining walls, source-prop outdoor cover

**User report:** v2.6 ramps were visually present but not traversable; raised-room retaining walls were pass-through; some ramps did not meet their source-game door, and the outdoor level had unguarded boundaries. The recovered military truck looked wooden from incorrect source texture assignments. Original walk/run/hit/death animations remain outstanding.

## Changes delivered in the private downloadable game

- **Physical entrance ramps:** The browser controller now supports ramp-height interpolation tied to the **same visible game-textured ramp strip**. The ramp starts 1.2 units inside a validated source-wall position, touches the recovered game door, and extends to sampled outdoor terrain; length scales with elevation drop to keep slopes manageable. Each new ramp requires a successfully loaded original source-door mesh. For original solid wall polygons that have not been cut, press E at the source door to cross, rather than walking through the wall.
- **Solid supports and world edges:** The actual source-textured retaining-wall mesh is raycast during player collision, no longer just decorative. A visible source-textured perimeter wall follows the terrain around the full outside area, and player/vehicle movement is checked against its matching playable bounds. Interior raised-room ledges can still produce falls.
- **Outdoor cover using original models only:** Nine generated sheltered cover yards use **54 source-model placements** from converted original GoldenEye barricades, ammunition crates, steel crates and wooden crates; approximate collision is active. Yard arrangements are reconstructed, not authored GoldenEye layout. No invented building assets, trees or fabricated box models.
- **Truck original materials:** Identified original military truck draw batches 013–014 as wheels and bind them to its recovered 009 wheel atlas. Cab, steel body, canvas and glass groups now use separate source texture images including newly embedded 003, 005, 006, 008 sheets. Authentic per-vertex UVs remain incomplete.
- **Crash prevention:** Fixed an existing out-of-scope variable `sz.z` in outdoor prop creation that could interrupt asset population when a vehicle model was spawned.

## Source animation and collision audit

The user's original retail STFS listing contains **23 remastered and 23 original level collision/hit resources** and **42 remastered and 42 original character hit resources**. Remastered Facility `default.mb.hit.bin` is a CAFF data payload identifying itself as `hits` version `04.05.05.0032`, with one ~1.39MB data resource. These resources have **not** been reverse engineered into native browser collision meshes. No standalone decoded skeletal walk, run, hit or death animation clips were found in the exported file listing. Those original motions remain blocked pending format decoding; the existing provisional browser movement is NOT original GoldenEye animation.

## QA and approval

Node JavaScript syntax and independent TypeScript AST parse pass; all eight embedded asset JSON sections parse; source-derived truck materials and GLB batch IDs verified; deterministic ramp/width/endpoint/boundary fixture passed; downloadable single HTML embedded source matches code-only source; ZIP CRC passes. **No live ChromeOS WebGL playtest**, and no user approval checkboxes were marked.

The private game delivery is `GoldenEye_World_Explorer_v27_ONE_GAME.zip` with one standalone HTML plus QA, animation/hit inventory and source. `GoldenEye_v27_CODE_ONLY.zip` is 54 KB with the game source and tests, no game media. Copyright-derived models, images and sound are excluded from this public repository.

[Master tracker through GE-325](PROJECT_TRACKER.md)

---

# GoldenEye World Explorer v2.6 — falling, raised-room supports, flush doors, drive direction and windshield POV

## User-reported problems
v2.5 screenshot shows a raised Facility room with no geometry below it; player cannot naturally fall off an edge to lower terrain. Source doors protrude from wall surfaces, and converted source cars drive facing the opposite direction to their camera/heading. First-person car view can be obstructed by nontransparent source windshield models.

## v2.6 playable code changes (UNVERIFIED VISUALLY)
- The previously enabled invisible last-known-floor safety is now OFF by default. Normal gravity applies when original mesh floor drops away. A downward ray checks both original polygons and generated game-textured ground/entrance ramps; a swept falling path catches landings when falling fast. Fall damage remains.
- Exterior terrain is about 4.2 game units below indoor starting-floor elevation instead of exactly aligned to it. Under some exposed original elevated room edges the viewer generates retaining-wall skirts down to the terrain using **recovered original GoldenEye wall textures**. The supports are NOT original level geometry; they are reconstructed and incomplete.
- The rendered original-source door model is compressed to a thin leaf plane (max ~0.085 scene-unit depth and width capped ~1.65) and positioned ~0.014 scene units outside the detected original wall plane, to avoid jutting slab artifacts. This does NOT remove the original wall polygons, create an actual authored doorway, or confirm historical door placement.
- For original source BMW/truck/APC geometries, the visual model is rotated 180 degrees around Y to align the visible car front with newly coded W-forward motion. First-person driver camera moves forward from the middle of the car to just outside the windshield, offset toward the driver's side and looking in the direction of travel. Third-person view follows the same forward direction.
- All original embedded meshes, audio and textures are otherwise retained from v2.5.

### Known issues and QA
Actual original level placement data, collision/navigation and staircase volumes are NOT recovered. Source maps have incomplete floor/wall geometry. Generated retaining walls are a prototype and may not cover every detached platform. Car orientation, first-person camera and wall-mounted door position require real ChromeOS testing. No new features are user approved.

`node --check` and independent TypeScript JS AST parsing pass; all eight embedded JSON data sections parse; standalone browser JS exactly matches the HTML module; ZIP integrity check passes. No graphical WebGL test performed.

**User delivery:** Private `GoldenEye_World_Explorer_v26_ONE_GAME.zip` and separate `GoldenEye_World_Explorer_v26_CODE_ONLY.zip`. Game-derived data is in the private playable HTML, not added to the public repository.

[Master development tracker](PROJECT_TRACKER.md)

---
# v2.5 — Verified Xbox sound cue bindings and corrected source-head fragments

**User-reported regressions:** v2.4 painted the same original portrait repeatedly on badly displaced source head draw groups, producing body-shaped heads and faces on clothing. The sound audition incorrectly assumed a cue's list index equaled its WAV's index; the user heard a gun sound labeled as a door. Both were real implementation errors.

## Confirmed XACT sound fix

The original Xbox `sfx.xsb` is big-endian `SDBK` with 209 simple cues. Each 5-byte simple-cue entry contains a sound-record offset. Each 19-byte sound record contains a **distinct 16-bit wavebank index** (all 209 verified). For example:
- `195_DOOR_SHUTTER_CLOSE_SFX`: **cue position 87** → **original WAV 155**, NOT WAV 87.
- `46_GUN_SILPPK_A_SFX`: **cue position 169** → **original WAV 37**, NOT WAV 169.
- `196_DOOR_METAL_OPEN_SFX`: **cue position 88** → **original WAV 156**.

The single-file v2.5 game audition panel now uses these correct WAVs for 62 embedded source clips, and verified source event names for door, punching, mine attaching, explosion, empty-trigger and applicable weapon firing. The original game's firearm-to-event logic has not been recovered, so cross-weapon **category assignments** remain provisional; cue-to-wave links themselves are verified. No original footsteps were identified.

## Source-character geometry correction

v2.4 attached all of each head's source draw groups, including polygons in the wrong original local coordinate frames. Those fragments resembled bodies or long columns. v2.5 keeps one coherent **original source geometry** group for each of 35 heads, trims displaced outlier faces, and normalizes to a realistic head-sized display. It crops the center of each real source head atlas rather than painting the full side/front atlas repeatedly on disconnected sections. No invented 3D head geometry was added. Original UVs, bone transforms, animation and unverified head-to-character pairings remain unresolved; **visual playtesting is still essential**.

The original body/face atlas audit also found and corrected four reversed atlas assignments: moonguard, moonfemale, commguard and rusguard.

**QA:** 35 cleaned original head GLBs reopen with source-derived faces, all 209 original wave references are valid and distinct, all eight embedded data blocks parse, Node JS syntax + TypeScript parser have zero errors, ZIP archive integrity verified. Full ChromeOS graphical playtest is not claimed. No user approval boxes checked.

The actual game-derived head and sound bytes are distributed only in the user-owned private downloadable build, not this public GitHub repo.

[Master progress tracker through GE-300](PROJECT_TRACKER.md) | [Original XACT cue decoder](tools/decode_original_xact_cues.py) | [Head mesh cleanup utility](tools/clean_head_glb.py)

---

# GoldenEye v2.4 — original sound-bank relationships, correct pistol diffuse and grounded exterior entries

**Private user download:** `GoldenEye_World_Explorer_v24_ONE_GAME.zip` containing one 73 MB standalone asset-embedded HTML with a 42-clip original-bank sound preview interface, cue tables, and audio/asset QA. Separate `GoldenEye_World_Explorer_v24_SOURCE_ONLY.zip` is the 136 KB full browser-game script + HTML source shell, original-cue catalog and corrective code without game assets. Proprietary game-derived media are never committed here.

## Source asset audit findings

- The source `music.xsb` includes **56 named stage/music cues** including Facility, Dam, Bunker 1/2, Archives, Train, Jungle, Control, Caverns and alternate music variants. The numeric link between those source cues and the **61 decoded music wave tracks remains unverified**. The viewer shows candidate stage music names but does not automatically assign arbitrary music files.
- The SFX bank has **209 original PCM WAV entries** and **209 candidate XSB cue strings**. Candidate cue categories include specific silenced PPK, rifles, metal/wood doors, explosions, punches, mines and train/alarms. The cue-to-wave numeric mapping is still **unverified**, so users can audition 42 embedded files and manually assign sounds per event; assignments are stored locally and explicitly labelled provisional. No original source-named footstep recording was verified.
- The original PPK diffuse atlas is `textures/gun/ppk/005.webp` (dark gun and grip). The old build incorrectly used image `003`, a rainbow/palette lookup. This release selects the true game-owned 005 images for PPK/PPK Silenced/Gold PPK/Ruger where present; exact UVs are still unfinished.
- The 35 recovered source-head GLBs have unusual geometry depths (many roughly 0.08 scene units and `headjoe` around 1.37). The viewer now conservatively normalizes the original mesh proportions instead of inventing a generic head; original face UVs, skeleton and character associations are still unresolved.

## Exterior entries and elevated maps

Indoor game stages get a **new scan for likely outside-facing source wall polygons**: visible vertical wall, original source floor on near side, no comparable source floor immediately outside, and no second blocking wall within a short distance. Up to five original converted GoldenEye door meshes can be placed flush to these verified candidates. Generated ramps use decoded original ground/path texture images and extend from supported threshold elevations to generated outdoor terrain. Generated game-textured foundation supports appear below some exposed elevated floor edges. The ramp surfaces are included in floor raycasting for walking. The authored entrance/door coordinates and physical opening-cutouts remain unavailable, so these are *reconstructed test links*, not restored original level design.

## QA and known limits

`node --check`, TypeScript JavaScript AST parsing, all eight JSON sections, and one-game ZIP/source ZIP CRC checks passed. No runtime/WebGL test on Chromebook is claimed. Some geometry, movement, texture UVs, audio event mappings and original character animations remain incomplete, and all checklist user-approval boxes remain unchecked.

[Tracker through GE-288](PROJECT_TRACKER.md)

---

# Recovery pass: Aztec geometry/textures + original music bank (Nov 11, 2026)

**New downloadable private artifact:** `GoldenEye_NEWLY_DECODED_AZTEC_MUSIC_ASSETS.zip` (78.7 MB). It is a **delta** to the previously supplied asset archive, not the full collection and not a completed original-game conversion.

### Confirmed advances
- Recovered Aztec CAFF layout with a +4096-byte resource-section shift. The original 57 texture images decode successfully. The recovered command stream yields 77 readable draw batches and 26,942 original geometry triangles; GLBs include vertex-colored geometry and a source-material textured **preview** with experimental UV scaling. The CAFF stream appears to have a missing 4096-byte tail, so all original geometry may NOT be present.
- Recovered 7 more original texture images: Head Neil (4), Uzi magazine (1), and Frigate skydome (2). Their meshes remain incomplete.
- Found a previously unprocessed `music.xwb` bank in the user's original retail STFS package. It contains 61 wave entries: 60 XMA entries and one WMA entry. All have best-effort Opus exports, but **every track generated decoder warnings** and the WMA track produced severe warnings. Neither fidelity nor named cue-to-wave associations have been verified. Existing `sfx.xwb` decoder generated 209 original PCM WAV entries previously; they are not re-shipped in this delta.
- 3,037 previously verified archived texture sheets plus 64 newly recovered images = 3,101 available source texture images across the two asset deliveries. **This is not proof every original game texture has been decoded.**

### Still unconverted
Six CAFF sources remain unsupported: `prop/consolesevGEa`, `prop/hatchdoor`, `prop/hind`, `prop/jungle5tree`, `prop/oildrum2`, and `prop/sat1reflect`. There are 37 original head model bundles but only 35 converted 3D head GLBs; character rigs and authored animation clips are not decoded. Original UV charts, exact stage setup/doors/props placement and missing map triangles remain unfinished. The game executable is compiled native code, not recovered source code.

### Verification
All 57 Aztec and 7 other newly decoded PNGs pass image verification, both Aztec GLBs reopen with 26,942 faces each, and all 61 converted audio outputs have non-zero ffprobe durations. The 144-entry ZIP passes CRC and includes SHA-256 manifests and exact per-asset failure statuses. No in-browser visual/aural playtest is claimed, and no features are marked user-approved.

**Distribution:** Game media stays in the private user download only, not this public GitHub repository.

---
# v2.3 — Full game browser source separated from all currently decoded assets

**Requested delivery:** Two separate archives from ChatGPT's current v2.3 turn:

1. `GoldenEye_BROWSER_GAME_SOURCE_CODE_ONLY.zip` — 74 KB source code with the full `src/game.mjs` browser gameplay implementation (125,218 bytes, 1,764 lines), HTML source shell (17,451 bytes), CSS (6,355 bytes), STFS/CAFF extraction tools, and `build_single_file.py`. No embedded model, sound, or image bytes.
2. `GoldenEye_DECODED_ASSETS_COMPACT_ONE_ZIP.zip` — 176 MB decoded-source asset package with 3,037 previously converted WebP texture sheets, every binary asset referenced by the v2.3 game (converted map/character/head/prop/weapon GLBs and extra original texture images), 209 extracted original Xbox sound bank entries, original firebomb artwork, checksums, and six structured JSON data sections required to rebuild the HTML. Also contains **the original compiled XEX2 executable** (`original-native-executable/default.xex`, 7,266,304 bytes).

A third optional `GoldenEye_World_Explorer_v23_HUD_STAIRS_PLAYABLE.zip` contains the rebuilt one-file playable HTML and QA notes. Its embedded game data and game JavaScript were byte/JSON verified to match the source+asset rebuild. All ZIP files passed CRC and the source passed Node syntax and TypeScript AST checks.

**Truthful source-status distinction:** The *original game native engine logic and authored C/C++ source have NOT been recovered*. `default.xex` is compiled Xbox machine code, not a native source listing. The complete `game.mjs` is OUR browser-game logic, not decompiled GoldenEye source. The 3,037 WebP atlases are compressed derivatives of earlier decoded PNG source images; pixel-lossless original PNGs and all raw CAFF assets remain in the user's original supplied/previous extraction archives.

**Map and movement:** The original fullscreen tactical map was still available under M, and health/armor HUD remained present in v2.2. In v2.3 an always-visible clickable HUD minimap was added. To address the still-BROKEN stairs, a stair-tread probe checks for supported real map polygons ahead up to 1.08 scene units, with a second support sample to avoid using a stray sliver. This is an unverified *attempt*, not a repaired original navmesh. True stair/wall navigation remains the highest priority.

All master tracker user-approval boxes remain unchecked. No graphics/browser success is claimed; static syntax, AST, JSON identity and archive CRC were checked.

[Tracker with 257 stable requirements](PROJECT_TRACKER.md)

---

# GoldenEye World Explorer v2.2 — Original 3D heads and map-aligned door repair

**Player-reported regressions:** The v2.1 screenshot showed a solid black rectangle as a door, arbitrary door positions at the generated level boundary, and different characters rendered with nearly identical fabricated heads. The original sprint meter ran out too quickly. These were genuine issues; prior approval was not inferred.

### Original character heads instead of generic fake face spheres

The compact original XBLA asset archive includes **37 separate `files/new/head/*/default.bin` 3D head model bundles**. The source parser converts **35** to genuine, distinctive GLBs; `headbike` and `headneil` are still unsupported. In v2.2, reconstructed character bodies use these original head meshes and their authentic source face image sheets, not the common spherical head or square face billboard. Face textures are projected on the frontal triangles of the source head, not painted on the back of the skull. Global head UV bounds prevent repeated copies of a portrait on individual submeshes.

The source record describing **which original head belongs to which character body is still missing**. Initial associations are previews; a new *Original 3D head model* dropdown lets players select any recovered head and save their preferred character-specific association. A *Flip head forward axis* option handles remaining ambiguous mesh axes. These are original source geometry and images, but **not a fully restored original head assembly or skeletal animation system**.

### Doors on actual wall faces, no black rectangles

The `doormf`, `doorpanel`, `doorstarec2` and `doorroller1` original game meshes use inspected real Xbox source metal textures. A few old source atlas choices were nearly-black masks; these are replaced by readable metal source sheets, using lighting-independent materials. v2.2 disables the synthetic world-boundary portal shell and the floating test-door placements.

At runtime, original map geometry is raycast to find nearby vertical wall surfaces with **walkable floor support on both sides**. A source door is placed flush against that wall; if none can be verified, no imaginary door is placed. The independent Facility source-mesh audit located **four** plausible wall+floor candidate positions. Pressing E at a mounted door transfers the character **only 1.75 meters to the other side of that very wall**, conditional on real floor support. The old distant exterior teleports are removed. **Open wall cutouts and accurate original stage door coordinates are not decoded yet**—an original wall may remain visible behind a door leaf.

### Sprint

Unlimited sprint is on by default, but can be disabled in the menu. In stamina mode, sprint drain is **4.8 per second versus the previous 24**, so stamina lasts five times as long, with 30/s recovery instead of 15/s.

### Verification and limitations

The standalone HTML and its JavaScript module pass Node syntax and TypeScript AST parsing. All embedded JSON sections decode; 35 recovered head GLBs reopen; the single ZIP passes a complete CRC integrity check. A direct independent geometry test found four usable Facility door candidates. Head render orientation, door visuals, transitions, and sprint still require actual ChromeOS gameplay validation; the container Chromium smoke test failed at EGL/ANGLE graphics initialization. No code is marked user-approved by assistant action.

The game file contains derived copyrighted assets from the user's game copy, so they are provided only in the private download and **not committed to this public repo**.

[Track GE-001–GE-245](PROJECT_TRACKER.md) · [Head asset decoder](tools/export_original_heads.py)

---

# GoldenEye World Explorer v2.1 — Source layout audit, original wristwatch and vehicle driving

**User download:** GoldenEye_World_Explorer_v21_ONE_ZIP.zip. Contains one asset-embedded HTML, SOURCE_LAYOUT_AUDIT.json, source code and README.

## Confirmed source discovery
Audited all 24 original Xbox CAFF background model bundles. 23 parse successfully; Aztec remains unsupported. Their rendergraph streams contain original draw commands, material image-slot records and texture descriptors. The audit reports original draws versus recovered model batches. For example, Facility is 120/120, Dam 230/391, and Library 14/66. Source UV declarations and the original game placement/setup coordinates for doors, vehicles and props remain incomplete or unavailable as separately extracted files.

The original Xbox source folder named 'gun' contains VHS videotapes, data tapes, watches, keys, gadgets and firearms: it is a held-object asset category, not a firearm list. The v2.1 UI separates combat weapons and mines from inspectable mission items and gadgets. A tape no longer has ammunition or a fire action.

## New v2.1 game features (awaiting user test)
- Watch communicator uses actual 3D source casing/strap/dial geometry (2,431 source triangles). The recovered watch image is projected onto dial mesh groups rather than onto the whole watch body; casing retains vertex colors. Watchlaser combines original laser attachment with the watch body. Original watch UV semantics remain unresolved.
- Source BMW, military truck and APC models can be entered/exited using E, driven with WASD, accelerated using Shift, braked with Space, and viewed in first- or third-person using V. Press J to place a source BMW near the player. Car physics are newly coded, not original GoldenEye driving mechanics.
- Three generated building-shell door openings (front/left/right) with original converted door mesh assets and game-textured approach ramps. The entry and interior portal locations are reconstructed, not authentic stage placement data.
- The in-game map selector shows per-map original draw counts, recovered draw counts and texture descriptors.

## Known limitations and QA
True authored level layouts, original per-vertex UVs, fully reconstructed map geometry, original driving physics, animations and collision/navmesh remain unfinished. Gameplay is not claimed to be an authentic remaster. No user approval checkboxes have been marked. Source assets are in the private download only, not this public repo. Node JS syntax, TypeScript AST, embedded source refs and ZIP CRC passed; interactive Chromebook WebGL testing is pending.

[Master requirement tracker](PROJECT_TRACKER.md)

---
# GoldenEye World Explorer v2.0.1 — Critical JavaScript parsing hotfix

User's ChromeOS console reported `Uncaught SyntaxError: Unexpected token '}'` on line 1069 of the v2.0 standalone HTML. Root cause: `updateMines()` prematurely closed its source-mine loop, moving the timed/proximity checks outside their intended scope and leaving an extra brace.

The **v2.0.1** user download corrects the mine-update braces without changing original game assets or other gameplay systems. All four embedded JSON sections parse; Node syntax checking passes; a separate TypeScript JavaScript AST check reports zero errors and confirms that timed/proximity mine handling and blast animation stay inside `updateMines`. ZIP CRC and exact HTML checksum also passed. This is **not** a graphical playtest or confirmation that all earlier collision/material bugs are resolved.

The browser's `file://` unique-origin warning is a separate Chrome security warning, not the JavaScript parser error. The app has no self-referencing iframe and does not attempt to fetch its own HTML file.

No user-approval boxes have been checked. See [PROJECT_TRACKER.md](PROJECT_TRACKER.md), GE-213–215.

---

# v2.0 source-asset interaction release — November 11, 2026

**Player feedback prompting this release:** v1.9 shows incomplete wall texture charts, floating/oversized vehicles in Facility, missing exterior access, walk-through walls/stairs, mines passing through walls or missing textures, and game-inaccurate fabricated Slappers/explosion effects. These remain **unapproved regressions**, not previously solved features.

**User-download artifact:** `GoldenEye_World_Explorer_v20_SOURCE_ASSET_TEST.zip`, one ZIP containing a playable asset-embedded HTML file, conversion/QA notes, and 11 extracted original XBLA PCM WAV samples.

### Implemented code, awaiting actual ChromeOS playtest

- Wall-hit raycasts against converted source level geometry with horizontal sliding, plus limited floor-step lookahead to climb low stair risers. **Neither a real GoldenEye collision mesh nor authored stair navigation has been recovered.** If a wall polygon is missing, raycast collision cannot block it.
- Mines now use swept ballistic raycasts against converted original map and door faces, and stick to the impact point and surface normal. Original Remote/Timed mine source meshes and game-owned red/blue/green texture imagery remain. Proximity still uses the decoded Remote chassis because the Proximity mesh decoder remains unresolved.
- **Original firebomb FX frames:** 24 recovered 256×256 Xbox CAFF textures (`files/new/texture/sfx/firebomb0` to `firebomb23`) decoded from Xbox tiled ARGB surfaces into an animated sheet, replacing the fabricated glowing sphere.
- **Original Xbox audio extraction breakthrough:** The original retail STFS package includes `sfx.xwb` and `sfx.xsb`; all **209 wave-bank entries decode as 44.1kHz mono signed 16-bit big-endian PCM**. 11 WAVs are in the user package and selected WAVs embedded in the game. **Caveat:** Matching names from XSB string-table order to corresponding XWB wave entries remains a provisional cue mapping, NOT an independently parsed/verified cue event binding.
- Slappers' fabricated animated hand spheres are hidden. Hit logic and candidate original decoded punch audio are available, but the **actual original Slappers fist animation has not been decoded** and must not be claimed restored. The original fist CAFF mesh presently yields no geometry because its pool layout is unsupported.
- Added generated test entrances to/from the procedurally placed exterior using actual converted source door meshes; original geographic connections remain unknown.
- Added source-model crates and recovered armor/ammo prop models at generated floor-and-wall-aligned positions; crates contain **newly designed gameplay** credits, armor plates, health, and ammunition. Recovered ammo crate meshes function as buy stations. Buy station menus and credits are **not original GoldenEye game mechanics**.
- Limited vehicles around map spawn/inside rooms and capped oversized prop bounding-box scales. Original vehicle UVs are still provisional; verified real colors/appearance require user testing.
- The packaged HTML still contains 23 converted map choices, 42 selectable character previews, 64 gun/item selections, and 24 original converted prop types. It is NOT a complete conversion of all authored maps.

**Verification:** Node `--check` passed; 24 firebomb source images were decoded; all 209 Xbox soundbank entries were extracted to WAV without unsupported formats; 7 newly converted prop models reopen; the compressed ZIP passed CRC. Chromium explicitly returned `ERR_BLOCKED_BY_ADMINISTRATOR` for the local HTML, so runtime gameplay and graphics are **not confirmed**. No approval checkboxes changed.

The public GitHub repo contains **source-only** converter/tracking tools. The user's original copyright-derived asset bytes remain exclusively in their private downloadable build.

[Development tracker](PROJECT_TRACKER.md) · [Original-asset extraction tools](tools)

---

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
