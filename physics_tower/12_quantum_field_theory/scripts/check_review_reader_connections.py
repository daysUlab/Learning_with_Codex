"""読者コメントに基づく章間接続の代表的数値検算。"""
import math
import numpy as np

A = np.array([[2., -1.], [-1., 2.]])
assert np.allclose(np.linalg.inv(A), np.array([[2., 1.], [1., 2.]])/3)
# 一変数Gaussianの四次相互作用：一次の二点補正
d, lam = 1., .1
assert math.isclose(d-lam*(15*d**3-3*d**3)/24, .95)
# 区別可能な質量ゼロ二体への崩壊幅（GeV）
M, g = 100., 1.
width = g*g/(16*math.pi*M)
assert math.isclose(width*1000, .1989436788648692)
assert math.isclose(width/(width+4*width), .2)
# 階乗型の漸近級数の最小項と増大
terms = [math.factorial(n)*.1**n for n in range(21)]
assert math.isclose(terms[9], terms[10])
assert math.isclose(terms[10], .00036288)
assert terms[20] > terms[10]
print("Reader connections: Gaussian inverse, first-order correction, decay and asymptotic terms: OK")

# 二通りの四点関数と直接の散乱行列要素の係数
from itertools import permutations
assert len(list(permutations(range(4)))) == math.factorial(4)
assert math.comb(4, 2)*math.factorial(2)**2 == math.factorial(4)
# Gaussianの微分：P_{n+1}=d dP_n/dF-F P_n
from numpy.polynomial import Polynomial
d = .7
F = Polynomial([0., 1.])
P = Polynomial([1.])
for _ in range(4):
    P = d*P.deriv()-F*P
assert np.allclose(P.coef, [3*d*d, 0., -6*d, 0., 1.])
# bubbleの一チャネルの対称因子を両形式で比較
den = math.factorial(2)*math.factorial(4)**2
wick = 2*(4*3)**2*math.factorial(2)/den
path = math.comb(4, 2)**2*math.factorial(2)*2*math.factorial(2)**2/den
assert wick == path == .5
print("Two formulations: source derivatives, tree combinatorics and bubble symmetry factor: OK")
