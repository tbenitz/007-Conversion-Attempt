# Authenticated XBLA XEX setup audit — 2026-11-12

**Important: not an original stage setup decoder yet.**

The user's Library `original_default.xex` (7,266,304 bytes, SHA-256 `7c1a5e22679bfb770004603c038c6c679383e364961a85f67464b12b79f412b9`) has a well-formed XEX2 header:
- Header data offset: `0x3000`; image bytes: 17,760,256 (declared)
- File-format header: `0x1c00`; encryption type **1** (AES); compression type **2** (normal LZX), LZX window 32 KiB
- Using the XEX2 devkit session-key path, **seven successive linked compressed blocks pass their stored SHA-1 digest**, authenticating the decryption key and those sections.
- The **eighth block** (`index=7`, decrypted payload offset `0x63000`, declared length `0xE800`) **fails the SHA-1 chain**. The tool stops: this may indicate modified/corrupted image data or an unsupported layout; do not silently continue to claim mission decoding.
- No verified full decompressed PE image or authenticated setup/pad stage records obtained.
- The user's 4,565-entry converted asset archive has no standalone source setup/pad/AI script files under recognized names. GLB models and textures do not constitute original authored object placement or trigger tables.

## Demonstrated completion percentages

- **Original objective trigger scripts/mission execution: 0% verified** (0 confirmed original stage scripts or trigger records integrated).
- **Original door/prop/guard placement: 0% verified** (0 confirmed original setup-to-pad placements integrated).
- This metric is *verified functional restoration*, not an estimate of time spent or unknown format bytes decoded. The actual record totals are not established; do not present made-up denominators.
- XEX container metadata parsing and seven block SHA-1 validations are research progress but **not** progress percentage towards native mission script extraction.

## Remaining required work
1. Resolve block-chain integrity after block 7; obtain a matching intact user-owned development image or matching unpacked original PE image. Full game package also may contain separate required raw level resources that are not in the derived asset archive.
2. Inspect decompressed PE sections, level setup pointer tables and resource references, and validate stage setup/pad/preset/AI/object records against known reverse-engineered structures.
3. Link original pad transforms to source geometry, identify original door/guard/prop object IDs, restore difficulty-specific triggers and failure states; cross-check against original game behavior.
4. Playtest every stage and mission on the target Chromebook; do not mark original mission implementation done without it.

`tools/audit_xbla_missions.py` is a non-destructive, reproducible XEX integrity and candidate setup-file auditor. It exports only JSON metadata, not copyrighted game binary content.

Sources used for independent format verification:
- https://reverseengineering.wiki/index.php/Format:XEX2_(Xbox_360_executable)
- https://github.com/murkantor/XBLA-Setup-Editor
- https://github.com/n64decomp/007

Preserve all earlier master tracker items and all user approval states. The v3.4 game ZIP is **not modified** in this audit, because no source-authenticated mission logic/placements were recovered to integrate.
