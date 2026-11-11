# 007 Conversion Attempt

A playable GoldenEye 007 XBLA Facility geometry-and-texture conversion experiment built from **user-supplied** XBLA game files.

## November 11, 2026 — Textured Facility + playable Boris

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
