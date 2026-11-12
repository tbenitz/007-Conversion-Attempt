"""Extract PCM WAVs from an Xbox 360 XACT wave bank supplied by its owner.

Usage: python tools/extract_xact_pcm.py sfx.xwb sfx.xsb output_dir
This script ships no game audio. XSB cue-name positions are only CANDIDATE
wave labels; the event-to-wave mapping still requires an XACT cue parser.
Python standard library only.
"""
from pathlib import Path
import struct, wave, re, json, sys

def export(xwb, xsb, output):
    b=Path(xwb).read_bytes()
    names=Path(xsb).read_bytes()
    if b[:4]!=b'DNBW' or names[:4]!=b'KBDS':
        raise ValueError('Expected original Xbox big-endian WBND/SDBK headers')
    entry_offset,entry_size=struct.unpack_from('>II',b,0x14)
    wave_offset,_=struct.unpack_from('>II',b,0x2c)
    n=struct.unpack_from('>I',b,0x38)[0]
    if n<1 or n>4000 or n*24!=entry_size:
        raise ValueError('Unsupported XACT entry table layout')
    suggestions=[x.decode() for x in re.findall(rb'([0-9]+_[A-Z0-9_]{2,})\x00',names)]
    out=Path(output);out.mkdir(parents=True,exist_ok=True)
    report=[]
    for i in range(n):
        _,fmt,off,length,_,_=struct.unpack_from('>6I',b,entry_offset+i*24)
        codec=fmt&3; channels=(fmt>>2)&7
        rate=(fmt>>5)&0x3ffff
        block_align=(fmt>>23)&0xff
        bits=8+8*((fmt>>31)&1)
        if codec!=0 or channels not in (1,2) or bits!=16 or block_align!=2*channels:
            report.append({'index':i,'status':'unsupported','format':hex(fmt)})
            continue
        start=wave_offset+off
        if start+length>len(b):
            report.append({'index':i,'status':'out-of-bounds'})
            continue
        raw=bytearray(b[start:start+length])
        for k in range(0,len(raw)-1,2):
            raw[k],raw[k+1]=raw[k+1],raw[k]
        file=out/('wave_%03d.wav'%i)
        with wave.open(str(file),'wb') as f:
            f.setnchannels(channels)
            f.setsampwidth(2)
            f.setframerate(rate)
            f.writeframes(raw)
        report.append({'index':i,'wav':file.name,
          'seconds':round(len(raw)/(rate*block_align),3),
          'candidate_cue':suggestions[i] if i<len(suggestions) else None,
          'status':'decoded'})
    (out/'WAVE_BANK_REPORT.json').write_text(json.dumps({
        'note':'Cue labels are tentative. Original XSB event-to-wave bindings not verified.',
        'entries':report},indent=2))
    print('Decoded',sum(r['status']=='decoded' for r in report),'of',n,'PCM waves')

if __name__=='__main__':
    if len(sys.argv)!=4:
        sys.exit('Usage: python tools/extract_xact_pcm.py sfx.xwb sfx.xsb output_dir')
    export(*sys.argv[1:])
