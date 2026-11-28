"""Chromiumの画面幅を変えた表示の診断。Safari実機確認とは別。"""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
import json
import re
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
out=root/"_quality"
out.mkdir(exist_ok=True)
paths=re.findall(r"^\s*- (chapters/[^\s]+\.qmd)\s*$",(root/"_quarto.yml").read_text(),re.M)
pages=["index.html",*[str(Path(p).with_suffix(".html")) for p in paths],"glossary.html","references.html"]
server=ThreadingHTTPServer(("127.0.0.1",0),partial(SimpleHTTPRequestHandler,directory=str(root/"_book")))
Thread(target=server.serve_forever,daemon=True).start()
results=[]
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(channel="chrome",headless=True,args=["--no-sandbox"])
        for width,height in [(390,844),(820,1180),(1280,900)]:
            context=browser.new_context(viewport={"width":width,"height":height})
            page=context.new_page()
            for path in pages:
                errors=[]
                def on_error(exc):
                    errors.append(str(exc))
                page.on("pageerror",on_error)
                response=page.goto(f"http://127.0.0.1:{server.server_port}/{path}",wait_until="domcontentloaded",timeout=30000)
                try:
                    page.wait_for_function("!document.querySelector('.math') || !!document.querySelector('mjx-container')",timeout=5000)
                except Exception:
                    errors.append("MathJax rendering not confirmed within 5s")
                metrics=page.evaluate("""() => ({
                    pageWidth:document.documentElement.scrollWidth,
                    viewport:window.innerWidth,
                    equations:document.querySelectorAll('mjx-container').length,
                    brokenImages:[...document.images].filter(i=>i.complete&&!i.naturalWidth).map(i=>i.getAttribute('src')),
                    clippedMath:[...document.querySelectorAll('mjx-container[display=true]')].filter(e=>e.scrollWidth>e.clientWidth+2).length
                })""")
                results.append({"path":path,"width":width,"http":response.status if response else None,"metrics":metrics,"diagnostics":errors})
                if path in ["index.html","chapters/00_physical_discoveries.html","chapters/03_quantum_mechanics.html","chapters/12_scalar_quantization.html","chapters/17_electrodynamics.html","glossary.html"]:
                    page.screenshot(path=str(out/f"html-{width}-{Path(path).stem}.png"),full_page=False)
                page.remove_listener("pageerror",on_error)
            context.close()
        browser.close()
finally:
    server.shutdown()
    (out/"browser-report.json").write_text(json.dumps(results,ensure_ascii=False,indent=2))
    print(json.dumps(results,ensure_ascii=False,indent=2))
