# Original XBLA executable, STAN and AI-list decoding — November 12, 2026

This research supersedes the earlier claim that the original XEX was corrupted at block 8. **The STFS extractor had an extra hash-table block at its first 170-block boundary**. The corrected extraction has XEX SHA-256 `00b9197180cb044142dd78f2591ff721b1884f1b87aca5b566a325770054b8fa`, and **123/123** AES-decrypted compressed XEX blocks authenticate with the original SHA-1 chain.

All **542** LZX frames decompress to a valid **17,760,256-byte** PowerPC Xbox PE image (SHA-256 `048c9a725e0163de3f1631651f7e250baaa01747d76c3e32cd62501cafefacd9`).

Using documented original XBLA setup/stage offsets and reading the decrypted PE, **28/28 original STAN clipping/room-geometry slot sizes validate** against their allocations. The scanner also finds **641 candidate original AI-list pointer/ID records across 20 setup regions**. Train does not satisfy the current tail-table heuristic and remains under investigation. These are validated structural candidates, *not* decoded AI command grammar, genuine mission trigger execution or verified original object/door/guard coordinates. The complete retail package has 3,627 filesystem entries, including 1,803 files; setup resources are not individually named in the catalog.

**Progress accounting:** Native XEX extraction and decompression: fully verified for the known original executable. STAN slot metadata: 28/28 validated. Candidate AI-list reference discovery: 641 records. **Functional original objective triggers: 0% verified. Original door/prop/guard placements integrated: 0% verified.** Overall percentage cannot be calculated until original record totals and game behavior are verified.

The noncopyright code-only decoder/research archive is saved to the user's ChatGPT Library as `GoldenEye_XBLA_ORIGINAL_SETUP_DECODE_PROGRESS.zip`. Scripts: `recover_verified_xbla.py`, `decode_xbla_executable.py`, `scan_xbla_setup_ai.py` with JSON reports. Original game bytes are intentionally excluded from public GitHub.

## Further work
- Decode original AI opcodes, lengths, branching and objective/failure conditions from the now readable script pointers.
- Parse the full original setup/pad/prop/guard/door placement records; align original stage coordinate frames and integrate only proven transforms.
- Decode original Dam STAN and collision geometry for real walkable floor triangles; avoid fabricated collision platforms.
- Implement and playtest authentic scripts, AI, mission triggers and audio cue links in the source-only explorer.
- Preserve all original tracker items and user-approval states; the current HTML v3.4 is unchanged in this decoding-only pass.

References: [XBLA Setup Editor](https://github.com/murkantor/XBLA-Setup-Editor), [Xenia XEX implementation](https://github.com/xenia-project/xenia/blob/master/src/xenia/cpu/xex_module.cc).
