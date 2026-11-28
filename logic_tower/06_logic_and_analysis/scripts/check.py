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
# 変数条件を外した誤った推論の反例
assert E(0) and not all(E(x) for x in D)
assert any(E(x) for x in D) and not E(1)
assert all(any(y!=z for z in D) for y in D)
assert not any(y!=y for y in D)
print("chapter 3: 512 finite relations and quantifier examples OK")

# 捕獲回避代入を構文木の変換として実装し、意味論と比較する。
def term_vars(t):
    if isinstance(t,str):
        return {t}
    return set().union(*(term_vars(u) for u in t[1:]))
def term_sub(t,x,u):
    if isinstance(t,str):
        return u if t==x else t
    return (t[0],*(term_sub(v,x,u) for v in t[1:]))
def vars_all(a):
    op,*args=a
    if op in ("R","eq"):
        return term_vars(args[0])|term_vars(args[1])
    if op in ("forall","exists"):
        return {args[0]}|vars_all(args[1])
    return set().union(*(vars_all(v) for v in args))
def sub(a,x,t):
    op,*args=a
    if op in ("R","eq"):
        return (op,*(term_sub(u,x,t) for u in args))
    if op in ("forall","exists"):
        y,B=args
        if y==x:
            return a
        if y in term_vars(t):
            used=vars_all(B)|term_vars(t)|{x,y}
            z=next("z"+str(i) for i in range(len(used)+1) if "z"+str(i) not in used)
            B=sub(B,y,z)
            y=z
        return (op,y,sub(B,x,t))
    return (op,*(sub(v,x,t) for v in args))
def value(t,s):
    if isinstance(t,str):
        return s[t]
    assert t[0]=="f"
    return (value(t[1],s)+1)%3
def truth(a,s,bits):
    op,*args=a
    if op=="R":
        return bits[3*value(args[0],s)+value(args[1],s)]
    if op=="eq":
        return value(args[0],s)==value(args[1],s)
    if op=="not":
        return not truth(args[0],s,bits)
    if op=="and":
        return all(truth(v,s,bits) for v in args)
    y,B=args
    assert op in ("forall","exists")
    return (all if op=="forall" else any)(truth(B,{**s,y:d},bits) for d in D)
formulas=[
    ("forall","y",("R","x","y")),
    ("exists","y",("not",("eq","x","y"))),
    ("forall","x",("exists","y",("R","x","y"))),
    ("exists","y",("and",("R","x","y"),("forall","z",("R","y","z")))),
]
cases=0
for bits in product([False,True],repeat=9):
    for A in formulas:
        for t in ["y",("f","y"),("f","x"),"z"]:
            B=sub(A,"x",t)
            for x,y,z in product(D,repeat=3):
                s={"x":x,"y":y,"z":z}
                assert truth(B,s,bits)==truth(A,{**s,"x":value(t,s)},bits)
                cases+=1
print(f"chapter 3: substitution lemma checked in {cases} finite cases")

# 第4章：二要素項モデル、証人の例、有限制約の充足
def term_model_value(base,power):
    return (base+power)%2
for base,power in product(range(2),range(10)):
    v=base
    for _ in range(power):
        v=1-v
    assert v==term_model_value(base,power)
assert term_model_value(0,5)==1 and term_model_value(0,6)==0
assert any(x==1 for x in range(2)) and not (0==1)
from fractions import Fraction
for bounds in [(2,10,100),(0,),(1,2,3),(10,1000,2)]:
    h=max(bounds)+1
    assert all(n<h for n in bounds)
    e=Fraction(1,h+1)
    assert e>0 and all(n*e<1 for n in bounds)
# 既存の名前を証人に固定する場合の反例
assert any([False,True]) and not [False,True][0]
print("chapter 4: finite term model and compactness examples OK (not a proof checker)")
