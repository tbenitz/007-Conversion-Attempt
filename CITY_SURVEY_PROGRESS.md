# GoldenEye City · Field Survey v0.1.0

This is a separate local exploration build from the campaign conversion. No source-derived game assets are published here.

- Registered 24 original base GLBs, 5 GLB-local Streets extras, 24 collision files, and 25 setup variants. Surface 1 and 2 share a source GLB but have independent district instances and setups. Train retains scene-space STAN.
- Added a walking route from Foundry Row around a native Streets wall, across a native STAN loop and back to City Hall, then on to Union Transit. Closed City Hall doors block movement, the Records key comes from Reception, and both stair flights and designated loot containers have stable IDs.
- Added service routes from Union Transit, Pier 4, Airport Approach, and Works Corridor. Travel is a paired transfer, not a seamless geographic link. Every linked district has a surveyed arrival and a return interaction.
- Automated movement and logic tests cover the city route, doors, stairs, loot, crouch clearance, save data, two Archives round trips, and all service endpoints at walk and sprint speeds. The harness uses actual kit assets and runtime collision, with rendering and browser storage adapters stubbed.
- Pending: visual playtest, physical Chromebook performance and browser storage verification, full imported interiors, native door art and lock behavior, and incomplete doorway/landing checks. This does not certify mission objectives or campaign completion.

The private handoff contains the offline HTML, editable multi-file project, coordinate probes, asset provenance, route graphs, and test traces.
