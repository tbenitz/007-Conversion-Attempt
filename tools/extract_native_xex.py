"""Extract compiled Xbox default.xex from user's own GoldenEye XBLA STFS package.
This does NOT decompile or recover the original source code.

Usage: python tools/extract_native_xex.py GoldenEye_007_XBLA_Retail.zip default.xex
"""
import hashlib,sys,zipfile,tempfile,shutil,math
from pathlib import Path
from extract_xbla import catalog,read_block

def read_xex_block(f,n):
    """Retail LIVE forensic fix: extra table block at the first 170-block boundary.

    Verified for this GoldenEye retail XEX with 123 SHA-1 linked blocks. Do not
    assume it is a universal STFS allocation mapping for other files/packages.
    """
    f.seek(0xc000+(n+n//170+n//28900+(1 if n>=170 else 0))*4096)
    return f.read(4096)

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
        if not entry or not entry['contiguous'] or read_xex_block(f,entry['start'])[:4]!=b'XEX2':
            raise ValueError('Valid contiguous XEX2 executable not found')
        remaining=entry['size'];dest.parent.mkdir(parents=True,exist_ok=True)
        with dest.open('wb') as out:
            for i in range(math.ceil(remaining/4096)):
                chunk=read_xex_block(f,entry['start']+i)[:remaining]
                out.write(chunk);remaining-=len(chunk)
    digest=hashlib.sha256(dest.read_bytes()).hexdigest()
    print('XEX2 compiled executable',dest,digest)
    print('For GoldenEye retail package, verified good original XEX SHA-256: 00b9197180cb044142dd78f2591ff721b1884f1b87aca5b566a325770054b8fa')

if __name__=='__main__':
    if len(sys.argv)!=3:sys.exit(__doc__)
    extract(sys.argv[1],sys.argv[2])
