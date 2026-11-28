"""生成HTMLの全ページを3画面幅で診断する。実機Safari・目視とは別。"""
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
config=(root/"_quarto.yml").read_text()
paths=re.findall(r"^\s*- ((?:chapters|supplements)/\S+\.qmd)\s*$",config,re.M)
pages=["index.html",*[str(Path(x).with_suffix(".html")) for x in paths],"glossary.html","references.html"]
sample={"index.html",paths[0].replace(".qmd",".html"),paths[4].replace(".qmd",".html"),paths[8].replace(".qmd",".html"),paths[13].replace(".qmd",".html"),paths[17].replace(".qmd",".html"),paths[18].replace(".qmd",".html"),"glossary.html"}
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
server=ThreadingHTTPServer(("127.0.0.1",0),partial(QuietHandler,directory=str(root/"_book")))
Thread(target=server.serve_forever,daemon=True).start()
results=[]
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(channel="chrome",headless=True,args=["--no-sandbox"])
        for width,height in [(390,844),(820,1180),(1280,900)]:
            context=browser.new_context(viewport={"width":width,"height":height},device_scale_factor=1)
            for path in pages:
                page=context.new_page()
                errors=[]
                page.on("pageerror",lambda exc: errors.append(str(exc)))
                row={"path":path,"width":width}
                try:
                    response=page.goto(f"http://127.0.0.1:{server.server_port}/{path}",wait_until="domcontentloaded",timeout=30000)
                    row["http"]=response.status if response else None
                    try:
                        page.wait_for_function("!document.querySelector('.math') || !!document.querySelector('mjx-container')",timeout=5000)
                    except Exception:
                        errors.append("MathJax rendering not confirmed within 5s")
                    # 遅延読み込み画像はビューポート外でもロードを要求する。
                    page.evaluate("() => document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')")
                    try:
                        page.wait_for_function("Array.from(document.images).every(i=>i.complete)",timeout=5000)
                    except Exception:
                        errors.append("Some image loads not confirmed within 5s")
                    row["metrics"]=page.evaluate("""() => {
                        const main=document.querySelector('#quarto-document-content');
                        const math=[...document.querySelectorAll('mjx-container[display=true]')];
                        return {
                            viewport:window.innerWidth,
                            pageWidth:document.documentElement.scrollWidth,
                            mainWidth:main?.clientWidth,
                            mainScrollWidth:main?.scrollWidth,
                            equations:document.querySelectorAll('mjx-container').length,
                            brokenImages:[...document.images].filter(i=>i.complete&&!i.naturalWidth).map(i=>i.getAttribute('src')),
                            pendingImages:[...document.images].filter(i=>!i.complete).length,
                            scrollableMath:math.filter(e=>e.scrollWidth>e.clientWidth+2).length,
                            unscrollableMath:math.filter(e=>e.scrollWidth>e.clientWidth+2&&!['auto','scroll'].includes(getComputedStyle(e).overflowX)).length,
                            overflowElements:[...document.querySelectorAll('#quarto-document-content *')].filter(e=>{
                                const r=e.getBoundingClientRect();
                                if(r.width===0 || (r.right<=window.innerWidth+2 && r.left>=-2)) return false;
                                for(let p=e.parentElement;p&&p!==main;p=p.parentElement){
                                    if(['auto','scroll','hidden','clip'].includes(getComputedStyle(p).overflowX))return false;
                                }
                                return true;
                            }).slice(0,15).map(e=>({tag:e.tagName,text:e.textContent.slice(0,100),right:Math.round(e.getBoundingClientRect().right)})),
                            bridgeCallouts:[...document.querySelectorAll('.callout-title-container')].filter(e=>e.textContent.includes('高校数学からの橋渡し')).length
                        };
                    }""")
                    if path in sample or row['metrics']['pageWidth']>width+2:
                        page.screenshot(path=str(out/f"html-{width}-{Path(path).stem}.png"),full_page=False,timeout=15000)
                except Exception as exc:
                    errors.append(str(exc))
                finally:
                    row["diagnostics"]=errors
                    results.append(row)
                    page.close()
            context.close()
        browser.close()
finally:
    server.shutdown()
    (out/"browser-report.json").write_text(json.dumps(results,ensure_ascii=False,indent=2))
    wide=[r for r in results if r.get("metrics",{}).get("pageWidth",0)>r["width"]+2]
    failures=[r for r in results if r.get("http")!=200 or r.get("diagnostics") or r.get("metrics",{}).get("brokenImages") or r.get("metrics",{}).get("unscrollableMath")]
    print(f"HTML visits={len(results)}/{len(pages)*3}, page overflow={len(wide)}, diagnostic candidates={len(failures)}")
    for r in wide+failures:
        print(json.dumps(r,ensure_ascii=False))
