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
    assert not re.search(r"^\s*\$\s*$",s,re.M),(p,"single dollar delimiter")
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

# 第1〜6章の数列接続例と第9章：有限標本の厳密有理数計算
for n in range(501):
    m=n+1
    e=Fraction(1,m)
    e2=Fraction(1,m+1)
    eta=Fraction(1,10**m)
    assert not (e<Fraction(1,2)) or e<1
    assert (e<Fraction(1,3))==(n>=3)
    assert (e<Fraction(1,3) and n%2==0)==(n>=4 and n%2==0)
    assert e>e2 and e*m==1
    assert e*e*m==e and e*m*m==m
    assert (m+2)*e==1+2*e
    assert Fraction(n,m)==1-e
    assert Fraction(1,2+e)-Fraction(1,2)==-e/(2*(2+e))
    assert 0<eta<e
    if n>=1:
        assert 0<e**3<e**2<e<1
print("chapter 9 and earlier sequence examples: exact rational samples OK")

# 第10章：有限標本の厳密有理数による代表例
for n in range(1,501):
    e=Fraction(1,n+1)
    assert (2+e)*(3-e)==6+e-e*e
    assert (1+e)/(2-e)-Fraction(1,2)==3*e/(2*(2-e))
    assert abs(2+(-1)**n*e-2)==e
    assert 0<e/(2*(2+e))<e/4
print("chapter 10: standard-part rational examples OK")

# 第11章：差商の有限標本検算
for a in map(Fraction,range(-3,4)):
    for n in range(1,101):
        for sign in (-1,1):
            h=Fraction(sign,n+1)
            assert ((a+h)**2-a*a)/h==2*a+h
            assert ((a+h)**3-a**3)/h==3*a*a+3*a*h+h*h
            assert abs(h)/h==sign
            if a and a+h:
                assert (1/(a+h)-1/a)/h==-1/(a*(a+h))
print("chapter 11: finite difference samples OK")

# 第12章：有限和公式、左右の差、区間の拡大を厳密有理数で検算
for m in range(1,151):
    e=Fraction(1,m)
    right=sum(Fraction(k*k,m**3) for k in range(1,m+1))
    left=sum(Fraction(k*k,m**3) for k in range(m))
    assert right==Fraction(1,3)+e/2+e*e/6
    assert left==Fraction(1,3)-e/2+e*e/6
    assert right-left==e
    assert sum(Fraction(k,m*m) for k in range(1,m+1))==Fraction(1,2)+e/2
    assert sum(Fraction(k**3,m**4) for k in range(1,m+1))==Fraction(1,4)+e/2+e*e/4
    assert 8*right==Fraction(8,3)+4*e+4*e*e/3
    assert sum(Fraction((j+1)**3-j**3,m**3) for j in range(m))==1
print("chapter 12: exact finite Riemann sums OK")

# 第13章：四元ブール代数の任意族の上限と分配、有限二進列の円筒
for mask in range(16):
    family=[s for s in range(4) if mask>>s&1]
    join=0
    meet=3
    for s in family:
        join|=s
        meet&=s
    assert all(s&join==s for s in family)
    assert all(join&u==join for u in range(4) if all(s&u==s for s in family))
    assert all(meet&s==meet for s in family)
    assert all(l&meet==l for l in range(4) if all(l&s==l for s in family))
    for a in range(4):
        rhs=0
        for s in family:
            rhs|=a&s
        assert a&join==rhs
for depth in range(1,9):
    words=["".join(bits) for bits in product("01",repeat=depth)]
    cyl=lambda s:{w for w in words if w.startswith(s)}
    for k in range(depth):
        for bits in product("01",repeat=k):
            s="".join(bits)
            assert cyl(s)==cyl(s+"0")|cyl(s+"1")
            assert not cyl(s+"0")&cyl(s+"1")
    parts=[cyl("0"*n+"1") for n in range(depth)]
    assert sum(map(len,parts))==2**depth-1
    assert set().union(*parts)==set(words)-{"0"*depth}
print("chapter 13: finite Boolean families and cylinder samples OK (not infinite completion proof)")

# 第14章：有限の名前の再帰計算（四元ブール代数）
from functools import lru_cache
@lru_cache(None)
def bv_check(n):
    return tuple((bv_check(k),3) for k in range(n))
@lru_cache(None)
def bv_member(u,v):
    result=0
    for t,b in v:
        result|=b&bv_equal(u,t)
    return result
@lru_cache(None)
def bv_subset(u,v):
    result=3
    for t,b in u:
        result&=(3^b)|bv_member(t,v)
    return result
@lru_cache(None)
def bv_equal(u,v):
    return bv_subset(u,v)&bv_subset(v,u)
@lru_cache(None)
def bv_eval(u,bit):
    return frozenset(bv_eval(t,bit) for t,b in u if b&bit)
u=tuple((bv_check(k),b) for k,b in [(1,1),(2,3),(3,2)])
v12=tuple((bv_check(k),3) for k in [1,2])
v23=tuple((bv_check(k),3) for k in [2,3])
v123=tuple((bv_check(k),3) for k in [1,2,3])
assert [bv_member(bv_check(k),u) for k in range(1,5)]==[1,3,2,0]
assert bv_equal(u,v12)==1 and bv_equal(u,v23)==2
assert bv_equal(u,v123)==0 and bv_subset(u,v123)==3
assert bv_equal((),(((),0),))==3
names=[tuple((bv_check(k),b) for k,b in enumerate(bs)) for bs in product(range(4),repeat=3)]
for x,y in product(names,repeat=2):
    assert bv_equal(x,y)==sum(bit for bit in [1,2] if bv_eval(x,bit)==bv_eval(y,bit))
    assert bv_member(x,y)==sum(bit for bit in [1,2] if bv_eval(x,bit) in bv_eval(y,bit))
    mixed=tuple((bv_check(k),(x[k][1]&1)|(y[k][1]&2)) for k in range(3))
    assert bv_equal(mixed,x)&1 and bv_equal(mixed,y)&2
print("chapter 14: finite B-name recursion, atomic semantics, mixing samples OK")

# 第15章：成分別演算・順序と複素多項式の有限例
x,y=(2,5),(3,1)
assert tuple(a+b for a,b in zip(x,y))==(5,6)
assert tuple(a*b for a,b in zip(x,y))==(6,5)
assert tuple(max(a,b) for a,b in zip(x,y))==(3,5)
assert sum(bit for bit,a,b in zip([1,2],x,y) if a<=b)==1
assert sum(bit for bit,a,b in zip([1,2],x,y) if b<=a)==2
assert tuple(a*b for a,b in zip((1,0),(0,1)))==(0,0)
assert tuple(z*z for z in (1,1j))==(1,-1)
for a,b in product(range(-3,4),repeat=2):
    import cmath
    roots=(cmath.sqrt(a),cmath.sqrt(b))
    assert all(abs(z*z-v)<1e-12 for z,v in zip(roots,(a,b)))
print("chapter 15: finite component operations and root samples OK")

# 第16章：有限条件の標本全列挙と両立性
conditions=[{k:v for k,v in enumerate(vs) if v!=-1} for vs in product([-1,0,1],repeat=4)]
stronger=lambda q,p:all(q.get(k)==v for k,v in p.items())
for p in conditions:
    assert stronger(p,{})
    for q in conditions:
        compatible=all(p[k]==q[k] for k in p.keys()&q.keys())
        assert compatible==any(stronger(r,p) and stronger(r,q) for r in conditions)
        if compatible:
            union=p|q
            assert stronger(union,p) and stronger(union,q)
    for k in range(4):
        q=p if k in p else p|{k:0}
        assert stronger(q,p) and k in q
    # 有限標本の外側に新しい添字を追加する（稠密性の例）
    for a in product([0,1],repeat=5):
        q=p|{4:1-a[4]}
        assert stronger(q,p) and q[4]!=a[4]
print("chapter 16: finite conditions and dense extension samples OK")
# 冒頭の図の参照も検査
for name in re.findall(r"\]\(figures/([^)]*)\)",(root/"index.qmd").read_text()):
    assert name in (root/"scripts/figures.py").read_text(),name
