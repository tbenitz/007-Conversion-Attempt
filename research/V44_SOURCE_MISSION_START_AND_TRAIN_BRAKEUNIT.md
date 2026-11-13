# GoldenEye v4.4 — original source mission insertion and Train brake-unit objective

User's request: "continue decoding, am i spawning at the exfil point? i want to be abe to do the missions".

## Found and authenticated

Previous v4.3 used arbitrary explorer starts on most maps, not the native stage mission insertion or exit. The actual original Train insertion is original pad 186 at native XYZ (117,45,-9), with matching original Train STAN floor. The full 18-stage insertion audit is bundled as `V44_MISSION_INSERTION_AUDIT.json`. Nine original insertion points have preliminary source-floor and rendered-map support; runtime validation is required. Dam source insertion pad 33 falls outside the currently recovered visible map, so a fallback explorer start must be shown honestly until actual Dam graphics are recovered.

Original Train 0x16 tag records 8–13 each reference the following original type 0x03 standard prop with native model ID 120. The GoldenEye source model enum names model 120 `PROP_BRAKEUNIT`. Six source bound-pad records 10000, 10052, 10055, 10075, 10103, 10119 provide exact source position/facing. They all validate against original Train STAN collision. The corresponding source model file `files/new/prop/brakeunit/default.bin` was independently extracted from the user-owned 372 MB Xbox retail package; its 62 original triangles and vertex colors were exported to a 2.8KB GLB (exact original material UVs and scale are not fully reconstructed).

Browser v4.4 spawns precisely those six original source models on Train and uses raycast hit events to mark original destroyed-object tags 8–13. The original objective evaluator completes objective A only when all six are destroyed. The event is actual hit testing with source model geometry, although original damage/health is approximated as one-hit and original XEX engine code is not running.

Original Train background list id 0x1009 includes an authored “Bond in pad-98 room” test followed by objective flag 0x00100000. Implemented as source STAN room comparison and native flag event, not as generated area markers. Other original events still require command decoding.

## Status and limits

This version **does not yet make the complete campaign playable**. Remaining Train objectives (including Natalya rescue and complete exfil), additional original map entry visualization, all non-Train object interactions, mission victory conditions and native global AI remain incomplete. Sprite/mesh/cue adjustments are not part of this stage.

Static JavaScript syntax and ZIP integrity passed, original embedded asset payload preserved. Browser playtest on Chromebook not yet performed. All user-approval requirements remain unchecked.

Do not commit original proprietary executable, extracted CAFF, GLB or original stage data to this public repository; user-owned assets are delivered only inside the private ChatGPT artifact ZIP.

Original source references: [n64decomp GoldenEye project](https://github.com/n64decomp/007) for model enum and stage macro semantics. Original data: user's own retail Xbox archive.
