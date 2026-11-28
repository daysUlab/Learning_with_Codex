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
