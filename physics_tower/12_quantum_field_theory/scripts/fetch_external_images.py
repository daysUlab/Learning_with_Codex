"""出典とライセンスが確認済みの画像をローカルへ取得する。失敗時はビルドを停止。"""
import hashlib
import json
import os
import struct
import time
from pathlib import Path
from urllib.request import Request, urlopen

root = Path(__file__).resolve().parents[1]
out = root / "figures" / "external"
out.mkdir(parents=True, exist_ok=True)
limit = 10 * 1024 * 1024

def valid(data, a):
    if not 1000 < len(data) <= limit:
        return False
    if a.get("bytes") and len(data) != a["bytes"]:
        return False
    if a.get("sha1") and hashlib.sha1(data).hexdigest() != a["sha1"]:
        return False
    if a["file"].endswith(".jpg"):
        return data.startswith(b"\xff\xd8") and data.endswith(b"\xff\xd9")
    if not data.startswith(b"\x89PNG\r\n\x1a\n") or data[12:16] != b"IHDR":
        return False
    if "width" in a:
        width, height = struct.unpack(">II", data[16:24])
        # 配布元の整数ピクセル丸めの差を最大1pxだけ許容する。
        return width == a["width"] and abs(height - a["height"]) <= 1
    return True

for a in json.loads((root/"external_images.json").read_text())["assets"]:
    dest = out/a["file"]
    if dest.is_file() and valid(dest.read_bytes(), a):
        print("cached:", dest.name)
        continue
    for attempt in range(3):
        try:
            req = Request(a["url"], headers={"User-Agent": "Learning-with-Codex/1.0 educational textbook (https://github.com/daysUlab/Learning_with_Codex)"})
            with urlopen(req, timeout=60) as response:
                data = response.read(limit+1)
            if not valid(data, a):
                raise ValueError("image signature, length, or checksum mismatch: "+a["file"])
            tmp = dest.with_suffix(".tmp")
            tmp.write_bytes(data)
            os.replace(tmp, dest)
            print("downloaded:", dest.name, hashlib.sha256(data).hexdigest())
            break
        except Exception:
            if attempt == 2:
                raise
            time.sleep(3*(attempt+1))
