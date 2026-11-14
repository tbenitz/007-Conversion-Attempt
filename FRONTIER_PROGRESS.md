# GoldenEye Frontier v0.2.0

Separate exploration build. City Survey and campaign builds are unchanged. Source-derived game assets are not published to the tracker.

- Generated world art uses clipped GoldenEye Streets, Depot, Surface and Runway meshes and original recovered prop GLBs. No invented building shells. The 4.5 km × 4.5 km starter footprint uses streaming 250 m sectors, with seed-based generation beyond the core.
- All 24 source maps and 25 setup instances are linked. Runway has a physical, bidirectional road-to-STAN seam. Both Surface/Bunker variants have aligned upper/lower entry points and two-way transfers. Streets and the remaining unsupported geographic seams use marked transfers.
- Automated runtime checks cover Streets travel and original collision, all map landings, streaming beyond the starter region, the recovered wooden cabin door, and return/route HUD behavior. Rendering, end-to-end native interiors, local Chrome storage and physical Chromebook performance remain unverified.
- The local handoff includes the self-contained HTML, editable source, asset provenance and route test records.
