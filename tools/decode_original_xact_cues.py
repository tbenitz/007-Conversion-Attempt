#!/usr/bin/env python3
"""Decode original Xbox 360 XACT SDBK simple-cue to XWB wave references.

Usage: python tools/decode_original_xact_cues.py sfx.xsb original_cues.csv
Requires source sound bank supplied by game owner. No source audio included.
Fails closed on unsupported complex cue formats. Python standard library.
"""
import sys, struct, csv
from pathlib import Path

def parse(path):
    b=Path(path).read_bytes()
    if b[:4]!=b'KBDS':
        raise ValueError("Expected Xbox 360 big-endian SDBK bank")
    count=struct.unpack_from('>H',b,0x13)[0]
    complex_count=struct.unpack_from('>H',b,0x15)[0]
    if complex_count:
        raise ValueError("Complex XACT cue format not yet supported")
    cuebase=struct.unpack_from('>I',b,0x22)[0]
    names_at=struct.unpack_from('>I',b,0x2a)[0]
    names_size=struct.unpack_from('>I',b,0x1e)[0]
    soundbase=struct.unpack_from('>I',b,0x46)[0]
    names=b[names_at:names_at+names_size].decode('ascii','replace').split('\0')[:count]
    if len(names)!=count:raise ValueError("Cue name table truncated")
    rows=[]
    for i in range(count):
        p=cuebase+i*5;flag=b[p];soundpos=struct.unpack_from('>I',b,p+1)[0]
        if flag!=4 or not soundbase<=soundpos<cuebase:
            raise ValueError("Unsupported cue at index "+str(i))
        if b[soundpos]!=2 or b[soundpos+8]!=19:
            raise ValueError("Unsupported sound type at index "+str(i))
        wave=struct.unpack_from('>H',b,soundpos+9)[0]
        rows.append(dict(cue_index=i,cue_name=names[i],
                         source_sound_offset=soundpos,
                         wavebank_index=b[soundpos+11],wave_index=wave))
    return rows

if __name__=='__main__':
    if len(sys.argv)!=3:sys.exit(__doc__)
    rows=parse(sys.argv[1]);dest=Path(sys.argv[2])
    dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)
    print('Decoded',len(rows),'source cue-to-wave mappings')
