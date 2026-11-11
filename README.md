# 007 Conversion Attempt

A browser-based **GoldenEye 007 XBLA Facility exploration prototype** and experimental converter for user-supplied game assets.

## Status — 2026-11-11

- [x] Identified STFS package structure in the supplied Xbox 360 LIVE package.
- [x] Corrected the extraction offset (CAFF headers must occur at byte 0 in an extracted model file; the earlier extraction began two blocks too early).
- [x] Parsed CAFF resource tables for Facility, Boris, Oddjob and Trevelyan.
- [x] Converted real indexed triangle geometry to GLB.
- [x] Built a downloadable single-file HTML preview containing converted models.
- [x] Prototype keyboard movement, mouse look, character switching, stationary/patrolling NPC placeholders and free-flight.
- [ ] Fully decoded original textures, materials and UVs.
- [ ] Character animations and original skeletons.
- [ ] Complete conversion validation for every vertex layout and level surface.
- [ ] Accurate geometry-based collision, spawn positions and navigation.
- [ ] Full level gameplay and AI.

**Current conversion counts (first pass, not exhaustive fidelity):**

| Asset | Triangle faces |
|---|---:|
| Facility | 13,754 |
| Boris | 3,536 |
| Oddjob | 6,474 |
| Trevelyan | 3,316 |

The prototype loads actual geometry but **is not yet the complete original Facility map**, and the source textures, rigging and original character animations are not reconstructed.

## Using the playable build

Download `goldeneye_xbla_facility_real_assets.html` from the ChatGPT deliverable and open in Chrome. It embeds the user-provided converted assets and needs an Internet connection for Three.js modules.

Controls: WASD movement, mouse look (click Explore), Shift sprint, Q/E vertical movement, 1/2/3 character switching, V third person, Esc mouse release.

## Repository model

This public repository tracks **source code and workflows**, not redistributed copyrighted GoldenEye/XBLA assets. Keep `*.live`, `*.xex`, extracted `default.bin`, converted `*.glb`, and asset-bearing standalone builds locally or in a private untracked folder. The supplied game package is user-provided and not uploaded here.

The converter source (including CAFF parsing and geometry export) is provided in the download bundle from this ChatGPT session. Upstream format research was informed by [Sightline](https://github.com/mscrnt/Sightline), especially `tools/worldasset/xblaworld.py` and `tools/texpack/caff.py`.

## Next engineering step

Finish texture decoding and vertex-layout coverage, verify orientation and spawn coordinates against the original game, and implement collision from the original level collision meshes. Do not label these complete without validation.
