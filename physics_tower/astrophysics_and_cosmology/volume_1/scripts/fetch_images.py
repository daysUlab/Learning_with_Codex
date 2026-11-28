"""公開画像を公式配布元から取得する。出典・ライセンスは external_images.json。"""
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "external"
OUT.mkdir(parents=True, exist_ok=True)
MAX_BYTES = 20 * 1024 * 1024

def jpeg_ok(data):
    return 1000 < len(data) <= MAX_BYTES and data.startswith(b"\xff\xd8") and data.endswith(b"\xff\xd9")

for asset in json.loads((ROOT / "external_images.json").read_text(encoding="utf-8"))["assets"]:
    dest = OUT / asset["file"]
    if dest.exists() and jpeg_ok(dest.read_bytes()):
        print(f"cached: {dest.name}")
        continue
    req = Request(asset["url"], headers={"User-Agent": "Learning-with-Codex textbook image retrieval"})
    with urlopen(req, timeout=60) as response:
        data = response.read(MAX_BYTES + 1)
    if not jpeg_ok(data):
        raise ValueError(f"公式JPEGの取得に失敗: {asset['url']}")
    tmp = dest.with_suffix(".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, dest)
    print(f"downloaded: {dest.name}")
