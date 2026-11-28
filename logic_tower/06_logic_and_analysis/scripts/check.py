"""原稿構造と第1章の代表的な意味論の検算（形式証明の機械検証ではない）。"""
from pathlib import Path
from itertools import product
import re
root=Path(__file__).resolve().parents[1]
paths=re.findall(r"^\s*- (chapters/\S+\.qmd)\s*$",(root/"_quarto.yml").read_text(),re.M)
assert paths
for i,p in enumerate(paths,1):
    assert Path(p).name.startswith(f"{i:02d}_")
    s=(root/p).read_text()
    assert "未執筆スケルトン" not in s
    for title in ["この章で学ぶ理由","## 初読の到達目標","## 演習","## 解答"]:
        assert title in s,(p,title)
    assert len(re.findall(r"^\$\$\s*$",s,re.M))%2==0
    for name in re.findall(r"\]\(\.\./figures/([^)]*)\)",s):
        assert name in (root/"scripts/figures.py").read_text(),name
imp=lambda p,q:max(1-p,q)
rows=list(product([0,1],repeat=2))
assert [imp(p,q) for p,q in rows]==[1,1,0,1]
assert [imp(p,min(p,q)) for p,q in rows]==[1,1,0,1]
assert all(not(imp(p,q) and p) or q for p,q in rows)
assert any(imp(p,q) and q and not p for p,q in rows)
assert all(1-min(p,q)==max(1-p,1-q) for p,q in rows)
assert all(imp(min(p,q),p) for p,q in rows)
assert all(not(max(p,q) and not p) or q for p,q in rows)
assert 2**3-1==7
print(f"{len(paths)} published chapter(s); introductory truth-table checks OK")

# 第2章：有限ブール代数をビット集合として全列挙
for n in range(1,5):
    top=(1<<n)-1
    elems=range(top+1)
    for a,b,c in product(elems,repeat=3):
        assert a&(b|c)==(a&b)|(a&c)
        assert a|(b&c)==(a|b)&(a|c)
        assert (top^(a|b))==((top^a)&(top^b))
        assert (a&b==a)==(a&(top^b)==0)
        assert ((top^a)|b==top)==(a&b==a)
        assert a&((top^a)|c)==a&c
    atoms=[a for a in elems if a and not any(b and b!=a and b&a==b for b in elems)]
    assert len(atoms)==n
    assert all(sum(b for b in atoms if b&a==b)==a for a in elems)
# DNFの構成が全ての真理関数を再現する（3変数まで）
for n in range(1,4):
    assignments=list(product([0,1],repeat=n))
    for mask in range(1<<len(assignments)):
        terms=[v for i,v in enumerate(assignments) if mask&(1<<i)]
        values=[int(any(all(x==y for x,y in zip(v,term)) for term in terms)) for v in assignments]
        assert sum(val<<i for i,val in enumerate(values))==mask
A={0,1,3}; B={1,2}; omega=set(range(4))
assert A&B=={1} and A|B==omega and (omega-A)|B=={1,2}
assert 2**(2**4)==65536
print("chapter 2: finite Boolean algebra and DNF checks OK")

# 第3章：有限構造での量化・反例・代入例
D=range(3)
f=lambda x:(x+1)%3
E=lambda x:x in {0,2}
assert f(f(2))==1 and E(f(2))
assert [int(E(x) and E(f(x))) for x in D]==[0,0,1]
assert not all(E(x) for x in D) and any(E(x) for x in D)
assert all(any(x==y for y in D) for x in D)
assert not any(all(x==y for x in D) for y in D)
assert not all(any(x<y for y in D) for x in D)
assert not any(all(x<y for x in D) for y in D)
assert any(all(not(x<y) for y in D) for x in D)
# 三要素集合上の二項関係512種類について量化の法則を検算
for bits in product([False,True],repeat=9):
    R=lambda x,y:bits[3*x+y]
    all_exists=all(any(R(x,y) for y in D) for x in D)
    exists_all=any(all(R(x,y) for x in D) for y in D)
    assert not exists_all or all_exists
    assert (not all_exists)==any(all(not R(x,y) for y in D) for x in D)
    for y in D:
        # 捕獲回避した forall z R(f(y),z) の値
        assert all(R(f(y),z) for z in D)==all(R((y+1)%3,z) for z in D)
# 変数条件を外した誤った推論の反例
assert E(0) and not all(E(x) for x in D)
assert any(E(x) for x in D) and not E(1)
assert all(any(y!=z for z in D) for y in D)
assert not any(y!=y for y in D)
print("chapter 3: 512 finite relations and quantifier examples OK")
