# GoldenEye v5.3 — Mission Files

## Try the build

Extract the ZIP and open **GoldenEye_v53_GAME_TRANSITION.html** in Chrome. Choose a file, select a mission, choose difficulty and read the briefing. Choose **Start mission**, then **Deploy** when the map is ready. **Esc** or the top-right button opens the Q Watch. It pauses the scene, shows objectives and loadout status, and lets you resume or abort. The old explorer, free flight and advanced controls are still in **Explorer / all settings**.

This recreates the original single-player menu sequence, not the exact N64 or XBLA menu artwork. Save slots remember the last selection. They do not claim unlocks or mission clears. Exact briefing text, complete loadouts, cutscenes and multiplayer are not restored. Original visual assets are preserved. Three.js and the GLB loader are bundled in this HTML. The game no longer needs a CDN to start.

## Dam and original floor data

The previous shared 0.0512 transform did not fit Dam. Matching retained original STAN coordinates against the shipped GLB found scale **0.01** and translation **[0.0354, −7.4819, 0.0170]**. **2,115 of 2,197** unique collision vertices are within 0.18 scene units of a rendered vertex. The median residual is under 0.01 scene units. Dam now uses its original insertion pad **33** and **2,755 original STAN tiles** for floor support, ground checks, guard grounding and falling. **73** conservative source-floor fragments are rendered with a neutral material where none of five interior samples matched a nearby original visible floor. These do not restore original texture coordinates or wall geometry. Train retains its original registered collision.

The registration audit tracks all **23 packaged map assets**. No other tentative fit was enabled. The package is still missing **622 original render batches** across the map set, including 162 on Dam, 204 on Statue and 128 on Surface. Full-map fidelity, all floor transitions and ChromeOS play-throughs remain open.

## Guard movement

The v5.2 interpreter still executed supported native movement and pursuit commands. Its fallback was an empty function. The new fallback runs only when an original guard program is blocked or missing, chooses nearby **original stage pads**, checks floor continuity and walls, and never writes mission flags. Working native scripts and intentional waits retain priority. This is a **reconstructed route**, not an original patrol assignment. The Q Watch options can turn it off. A stage without registered guard positions will not acquire fabricated guards.

## Tests

Automated runtime and DOM tests cover Dam registration, source floor elevation and guard positioning, fallback selection/strict mode, mission file selection, difficulty-specific objectives, deploy, pause/resume clock and abort. v5.2 Train mission checks also run against the new module. No full rendered route or Chromebook performance certification is implied.

The mission flow follows the [GoldenEye instruction booklet](https://www.world-of-nintendo.com/manuals/nintendo_64/goldeneye_007.shtml). The implementation and visual styling are new browser code.
