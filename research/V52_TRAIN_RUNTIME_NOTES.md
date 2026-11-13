# GoldenEye World Explorer v5.2 — Train source runtime

## What changed in play

1. **Escape to safety.** Train's original background list `0x1009` at `0xdc1a28` now executes its original sleep, forward label branch, loop and objective flag write. Pad `0x0062` (98) is 27 native units above its underlying STAN floor. The floor under that pad is tile 67 in room 53. Resolving the floor before comparing rooms removes the former fixed-height guess. Standing on original room 53's floor can set `0x00100000` and complete the Escape to safety objective. Free-flight mode does not trigger it. The original visual fog command is recorded but original fog parameters have not been applied.
2. **Brake-linked guards.** Original Train actors 66 and 68 share list `0x0411`. That list now reads the real destruction state for tags 8–13. All six are required. It then transfers to reframed pursuit list `0x0409`. Train's `0x0407` guards can also resolve the `0x2328` pad-preset selector from their own original setup record (e.g. actor 18 → pad 159). Distance operands use their documented ×10 scale and three axes. Pursuit uses source STAN and the existing browser wall collision. This is not a recovered full patrol graph.
3. **Exit approach.** The original `0x1006` list at `0xdc1840` checks distance to pad 203 and runs its 180-tick delay and death branch. When it reaches the unsupported damage/control/hostage/finale sequence, the HUD reports the exit approach and the player retains control. It does not set Natalya's rescue flag, fake a win, or grant a campaign clear.

## Recovered bytecode framing

The older decoder advanced 50 bytes for every `0xAD` (debug print). The reference interpreter scans the string to its terminating zero byte. Applying that framing to retained, contiguous XBLA bytes across the 21 extracted stage setups reframed **122 affected lists**, exposing a net **833 more instruction records**. Seven previously incomplete lists reach a provable end inside their retained bytes. Eleven old END claims were invalidated and those lists are now blocked instead of run. For example, Train `0x0409` grows from 70 to 91 instructions, including the command at `0xdc0ec9`. Train `0x1002` contains later character-spawn instructions but no provable END in its retained bytes.

The original source JSON, converted geometry, STAN tiles, models, textures and audio stay byte-identical. The corrected instruction overlay retains original offsets and operands and is applied to matching original program IDs and start offsets. It contains no guessed bytes beyond the original extraction. Opcode behavior was cross-checked with the [GoldenEye 007 decompilation interpreter](https://github.com/n64decomp/007/blob/master/src/game/chrai.c) and [character/pad helpers](https://github.com/n64decomp/007/blob/master/src/game/chraction.c). The scripts, pads and collision used in the build are from the retained XBLA data, not a replacement N64 level.

## How to try it

Open `GoldenEye_World_Explorer_v52_TRAIN_SOURCE_RUNTIME.html` in Chrome, choose Train in the mission selector and load the mission. It starts at original insertion pad 186. Destroy the six brake units and check Objective A. On the final car, observe the two guards linked to the brake check. Reaching the source exterior room on foot should show Objective E as completed. The separate exit approach, farther out, only produces a status line after the source delay. Use **Restart mission** to clear the objectives and timers. The game assets are embedded in the HTML. It still loads Three.js from the same CDN as v5.1, so an internet connection is needed unless those modules are already cached.

## Verification and remaining scope

The release includes automated tests using the shipped Train bytecode and all 694 original Train STAN tiles. They cover original room/floor matching, reset, blocked bad branches, exit delay and death abort, the six-tag guard handoff, a real STAN-grounded movement step, and debug framing. They do not replace a walk-through in ChromeOS. Chromium could not start in the execution environment, so the complete rendered route and browser performance are unverified. Hostage actors, their dialogue and actions, the original exit cutscene, the complete patrol graph, and overall mission victory remain open. **0/21 original missions are fully verified.**

The permanent engineering ledger now records **25/100** (22 complete milestone points and 3 partial points). The two new points are within AI-05 and MIS-02. All existing milestone weights and user-acceptance entries are preserved.
