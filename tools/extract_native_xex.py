"""Extract compiled Xbox default.xex from user's own GoldenEye XBLA STFS package.
This does NOT decompile or recover the original source code.

Usage: python tools/extract_native_xex.py GoldenEye_007_XBLA_Retail.zip default.xex
"""
import hashlib,sys,zipfile,tempfile,shutil,math
from pathlib import Path
from extract_xbla import catalog,read_block

def extract(package,dest):
    package=Path(package);dest=Path(dest)
    if zipfile.is_zipfile(package):
        with zipfile.ZipFile(package) as z,tempfile.TemporaryDirectory() as d:
            f=max((x for x in z.infolist() if not x.is_dir()),key=lambda x:x.file_size)
            temp=Path(d)/'retail.live'
            with z.open(f) as src,temp.open('wb') as target:shutil.copyfileobj(src,target)
            return extract(temp,dest)
    with package.open('rb') as f:
        entry=catalog(f).get('default.xex')
        if not entry or not entry['contiguous'] or read_block(f,entry['start'])[:4]!=b'XEX2':
            raise ValueError('Valid contiguous XEX2 executable not found')
        remaining=entry['size'];dest.parent.mkdir(parents=True,exist_ok=True)
        with dest.open('wb') as out:
            for i in range(math.ceil(remaining/4096)):
                chunk=read_block(f,entry['start']+i)[:remaining]
                out.write(chunk);remaining-=len(chunk)
    print('XEX2 compiled executable',dest,hashlib.sha256(dest.read_bytes()).hexdigest())

if __name__=='__main__':
    if len(sys.argv)!=3:sys.exit(__doc__)
    extract(sys.argv[1],sys.argv[2])
