"""第4〜6章の一次レビューで追加した有限例の検算。一般定理の機械証明ではない。"""
from itertools import product
from fractions import Fraction as F

# 第4章：古典命題論理による証人公理の否定の展開
for E,A in product([False,True],repeat=2):
    assert (not ((not E) or A)) == (E and not A)
# 異なる命題変数を異なる一項述語で表現する一要素モデル
for n in range(1,5):
    for bits in product([False,True],repeat=n):
        predicates=[{0} if v else set() for v in bits]
        assert tuple(0 in R for R in predicates)==bits
# 有限制約ごとに異なる証人を取る
for N in range(1,101):
    h=N+1
    e=F(1,N+1)
    assert all(n<h and n*e<1 for n in range(1,N+1))

# 第5章：三進列の最初の差が有限の後続項では相殺されない
values={}
for bits in product([0,1],repeat=8):
    x=sum((F(2*b,3**i) for i,b in enumerate(bits,1)),F(0))
    assert x not in values
    values[x]=bits
for a,b in product(values,repeat=2):
    if a!=b:
        k=next(i for i,(u,v) in enumerate(zip(values[a],values[b]),1) if u!=v)
        assert abs(a-b)>=F(1,3**k)
# 有理数切断の積の逆包含で用いた正の証人の公式
cases=0
for r,s in product([F(1,3),F(1,2),F(2),F(5,3),F(7)],repeat=2):
    for k in range(20):
        q=r*s*F(k,20)
        d=min(r/2,s/2,(r*s-q)/(2*(r+s)))
        a,b=r-d,s-d
        assert 0<a<r and 0<b<s and q<a*b
        cases+=1
# 有理数の上限の例
for a,b in product(range(1,31),repeat=2):
    q=1-F(a,b)
    n=b+1
    assert q<1-F(1,n)
# 第6章：分出・置換の有限例と直積の選択関数
A={1,2,3}
assert {x for x in A if x in {2,4}}=={2}
assert {x*x for x in A}=={1,4,9}
choices=list(product([1,2],[3,4,5],[6]))
assert len(set(choices))==6
# 空鎖を含め、実際に上界の存在を確認
P=[frozenset("a"),frozenset("ab"),frozenset("ac")]
for mask in range(8):
    C=[x for i,x in enumerate(P) if mask>>i&1]
    if all(x<=y or y<=x for x,y in product(C,repeat=2)):
        upper=frozenset().union(*C) if C else P[0]
        assert upper in P and all(x<=upper for x in C)
print(f"review 04-06: finite models, 256 ternary codes, {cases} rational products, and chain checks OK")
