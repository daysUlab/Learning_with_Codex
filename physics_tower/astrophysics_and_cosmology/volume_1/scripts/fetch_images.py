"""Download official images; for NASA SVS only, disclose unavailable images in the render."""
import base64
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "external"
OUT.mkdir(parents=True, exist_ok=True)
MAX_BYTES = 20 * 1024 * 1024

def jpeg_ok(data):
    return 1000 < len(data) <= MAX_BYTES and data.startswith(b"\xff\xd8") and data.endswith(b"\xff\xd9")

def atomic_write(dest, data):
    tmp = dest.with_suffix(dest.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, dest)

def download(asset):
    dest = OUT / asset["file"]
    if dest.exists():
        data = dest.read_bytes()
        if jpeg_ok(data):
            print(f"cached: {dest.name}")
            return data
    errors = []
    for url in [asset["url"], *asset.get("alternate_urls", [])]:
        try:
            req = Request(url, headers={"User-Agent": "Learning-with-Codex textbook image retrieval", "Accept": "image/jpeg,image/*"})
            with urlopen(req, timeout=60) as response:
                data = response.read(MAX_BYTES + 1)
            if not jpeg_ok(data):
                raise ValueError("invalid JPEG")
            atomic_write(dest, data)
            print(f"downloaded: {dest.name} from {url}")
            return data
        except (URLError, OSError, ValueError) as exc:
            errors.append(f"{url}: {exc}")
    if not asset.get("allow_unavailable_notice", False):
        raise RuntimeError("Official image retrieval failed: " + "; ".join(errors))
    print("::warning title=NASA image unavailable::" + "; ".join(errors))
    return None

def render_nasa(asset, data):
    # An SVG envelope makes the real JPEG available to HTML and PDF alike.
    # It is never a fake JPEG or an unlabelled substitute. The caption links
    # the official page regardless of the fetch outcome.
    w, h = asset["render_size"]
    if data is not None:
        content = f'<image width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet" xlink:href="data:image/jpeg;base64,{base64.b64encode(data).decode("ascii")}"/>'
    else:
        w, h = 1000, 220
        content = (
            '<rect width="1000" height="220" rx="10" fill="#eef2f6" stroke="#9aaabb"/>'
            '<g font-family="sans-serif" text-anchor="middle" fill="#25364a">'
            '<text x="500" y="85" font-size="32">Official NASA image unavailable in this build</text>'
            '<text x="500" y="135" font-size="22">See the official source link in the caption.</text>'
            f'<text x="500" y="178" font-size="18">{escape(asset["file"])}</text></g>'
        )
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{content}</svg>'
    atomic_write(OUT / asset["render_file"], svg.encode("utf-8"))

if __name__ == "__main__":
    for asset in json.loads((ROOT / "external_images.json").read_text(encoding="utf-8"))["assets"]:
        data = download(asset)
        if "render_file" in asset:
            render_nasa(asset, data)
