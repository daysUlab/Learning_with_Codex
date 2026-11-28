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

# 第5章：集合の構成例
from itertools import combinations
def powerset(s):
    xs=list(s)
    return frozenset(frozenset(c) for k in range(len(xs)+1) for c in combinations(xs,k))
V=frozenset()
sizes=[len(V)]
for _ in range(5):
    V=powerset(V)
    sizes.append(len(V))
assert sizes==[0,1,2,4,16,65536]
pair=lambda a,b:frozenset((frozenset((a,)),frozenset((a,b))))
pairs={(a,b):pair(a,b) for a,b in product(range(4),repeat=2)}
assert len(set(pairs.values()))==16
assert (5+7)%3==0
idx=lambda m,n:(m+n)*(m+n+1)//2+m
assert idx(2,3)==17
assert sorted(idx(m,k-m) for k in range(21) for m in range(k+1))==list(range(231))
f=[{0,2},{0},{1,2}]
Dg={i for i in range(3) if i not in f[i]}
assert Dg=={1} and Dg not in f
# 有理数の平方根切断を有限標本で検算（無限集合の証明ではない）
qs=sorted(set(Fraction(p,q) for p in range(-30,31) for q in range(1,16)))
lower=lambda q:q<0 or q*q<2
assert all(not lower(p) or lower(q) for p in qs for q in qs if q<p)
for r in qs:
    if r>=0 and r*r<2:
        d=min(Fraction(1),(2-r*r)/(2*(2*r+1)))
        assert d>0 and (r+d)**2<2
    if r>0 and r*r>2:
        d=min(r/2,(r*r-2)/(4*r))
        assert r-d>0 and (r-d)**2>2
print("chapter 5: pairs, diagonal enumeration, hierarchy and rational-cut examples OK")

# 第6章：公理の有限例・極大元・モデルによる真偽
A={1,2,3}
assert len(powerset(A))==8
assert {x for x in A if x%2==0}=={2}
assert set.union({1,2},{2,3})==A
assert {x*x for x in A}=={1,4,9}
assert len(list(product(range(2),range(3),range(4))))==24
P=[frozenset(s) for s in [{"a"},{"a","b"},{"a","c"}]]
maximal=[x for x in P if not any(x<y for y in P)]
greatest=[x for x in P if all(y<=x for y in P)]
assert set(maximal)=={frozenset({"a","b"}),frozenset({"a","c"})}
assert not greatest
for C in powerset(P):
    if all(x<=y or y<=x for x,y in product(C,repeat=2)):
        assert any(all(x<=y for x in C) for y in P)
assert any(x in {0} for x in [0]) and not any(x in set() for x in [0])
print("chapter 6: finite axiom examples, choice functions and maximal elements OK")

# 3章単位のレビュー検査
import runpy
runpy.run_path(str(root/"scripts/check_review_04_06.py"))

# 第7章：有限フィルター・超フィルターの全列挙
from itertools import combinations
def finite_filters(n):
    top=(1<<n)-1
    sets=range(top+1)
    result=[]
    for mask in range(1<<(top+1)):
        F={a for a in sets if mask>>a&1}
        if top not in F or 0 in F:
            continue
        if not all(a&b in F for a,b in product(F,repeat=2)):
            continue
        if not all(b in F for a in F for b in sets if a&b==a):
            continue
        result.append(F)
    return result
for n in range(1,5):
    top=(1<<n)-1
    fs=finite_filters(n)
    assert len(fs)==top
    for F in fs:
        K=top
        for a in F:
            K&=a
        assert K and F=={a for a in range(top+1) if a&K==K}
    us=[F for F in fs if not any(F<G for G in fs)]
    assert len(us)==n
    for F in fs:
        assert any(F<=U for U in us)
        assert (F in us)==all((a in F)!=((top^a) in F) for a in range(top+1))
    for U in us:
        for a,b in product(range(top+1),repeat=2):
            assert ((a&b) in U)==(a in U and b in U)
            assert ((a|b) in U)==(a in U or b in U)
        # 有限分割の有限版：各点に三つのラベルを割り当てる
        for labels in product(range(3),repeat=n):
            parts=[sum(1<<i for i,v in enumerate(labels) if v==j) for j in range(3)]
            assert sum(a in U for a in parts)==1
# 有限近似ではなく、有限領域での同値関係の計算例
seqs=list(product(range(2),repeat=4))
for i in range(4):
    for a,b,c in product(seqs,repeat=3):
        if a[i]==b[i] and b[i]==c[i]:
            assert a[i]==c[i]
# 多数決の反例と生成フィルターの例
assert len({1,2,3})>5/2 and len({3,4,5})>5/2
assert len({1,2,3}&{3,4,5})==1
assert {a for a in range(16) if a&6==6}=={6,7,14,15}
print("chapter 7: all filters on 1-4 points, ultrafilter laws and finite partitions OK")

# 第8章：有限主超フィルター上での演算・量化と数列の代表例
for i in range(3):
    seqs=list(product(range(3),repeat=3))
    eq=lambda a,b:a[i]==b[i]
    for a,b,c in product(seqs,repeat=3):
        if eq(a,b):
            assert eq(tuple(x+y for x,y in zip(a,c)),tuple(x+y for x,y in zip(b,c)))
            assert eq(tuple(x*y for x,y in zip(a,c)),tuple(x*y for x,y in zip(b,c)))
    for a in seqs:
        for bits in product([False,True],repeat=9):
            # 三要素領域における存在量化と、列の証人の存在の一致
            left=any(bits[3*a[i]+v] for v in range(3))
            right=any(bits[3*a[i]+b[i]] for b in seqs)
            assert left==right
for n in range(2001):
    e=Fraction(1,n+1)
    h=n+1
    assert e*h==1 and (h+1)*e==1+e
    assert (e<Fraction(1,1000))==(n>=1000)
    assert ((-1)**n)**2==1
print("chapter 8: finite principal ultraproduct and sequence identities OK (not free ultrafilter computation)")
