"""Extract GoldenEye XBLA CAFF bundles from a user-provided LIVE package/ZIP.
Usage: python tools/extract_xbla.py game.zip local-assets
No game data is included.
"""
import argparse, math, zipfile, shutil, tempfile
from pathlib import Path

TARGETS = [
    "files/new/background/facility/default.bin",
    "files/new/char/boris/default.bin",
    "files/new/char/oddjob/default.bin",
    "files/new/char/trevelyan/default.bin",
]

def blockoffset(n):
    return 0xc000 + (n + n // 170 + n // 28900) * 4096

def read_block(f, n):
    f.seek(blockoffset(n))
    return f.read(4096)

def catalog(f):
    entries = []
    for block in range(57):
        data = read_block(f, block)
        for j in range(64):
            e = data[j * 64:(j + 1) * 64]
            name = e[:40].split(b"\0")[0].decode("utf8", "replace")
            if not name:
                continue
            entries.append(dict(id=block * 64 + j, name=name,
                start=int.from_bytes(e[47:50], "little"),
                size=int.from_bytes(e[52:56], "big"),
                parent=int.from_bytes(e[50:52], "big"),
                contiguous=bool(e[40] & 64)))
    by_id = {x["id"]: x for x in entries}
    for e in entries:
        names = [e["name"]]
        parent, seen = e["parent"], set()
        while parent in by_id and parent not in seen:
            seen.add(parent)
            item = by_id[parent]
            names.insert(0, item["name"])
            parent = item["parent"]
        e["path"] = "/".join(names)
    return {x["path"]: x for x in entries}

def extract(package, output):
    package, output = Path(package), Path(output)
    if zipfile.is_zipfile(package):
        with zipfile.ZipFile(package) as z:
            entries = sorted((x for x in z.namelist()
                if not x.endswith("/") and z.getinfo(x).file_size > 10000000),
                key=lambda x:z.getinfo(x).file_size, reverse=True)
            if not entries:
                raise ValueError("ZIP contains no large STFS package")
            with tempfile.TemporaryDirectory() as temp:
                target = Path(temp) / "package.live"
                with z.open(entries[0]) as source, target.open("wb") as out:
                    shutil.copyfileobj(source, out)
                return extract(target, output)
    with package.open("rb") as f:
        index = catalog(f)
        for name in TARGETS:
            item = index.get(name)
            if item is None or not item["contiguous"]:
                raise ValueError("Missing or fragmented STFS entry: " + name)
            # Validate CAFF rather than assuming the raw STFS start is correct.
            shifts = [k for k in range(-6,9) if item["start"]+k >= 0
                      and read_block(f, item["start"]+k)[:4] == b"CAFF"]
            if len(shifts) != 1:
                raise ValueError("Cannot uniquely find CAFF: %s %s" % (name, shifts))
            target = output / name
            target.parent.mkdir(parents=True, exist_ok=True)
            remaining = item["size"]
            with target.open("wb") as out:
                for i in range(math.ceil(remaining / 4096)):
                    chunk = read_block(f, item["start"]+shifts[0]+i)[:remaining]
                    out.write(chunk)
                    remaining -= len(chunk)
            print(name, target.stat().st_size, "shift", shifts[0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("package")
    parser.add_argument("output", nargs="?", default="local-assets")
    a = parser.parse_args()
    extract(a.package, a.output)
