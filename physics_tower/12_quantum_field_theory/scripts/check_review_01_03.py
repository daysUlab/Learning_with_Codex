"""第1〜3章のレビュー時の独立数値検算。原稿の全命題を証明するテストではない。"""
import math
import numpy as np

def close(a, b):
    np.testing.assert_allclose(a, b, rtol=1e-10, atol=1e-10)

# 第1章：運動・作用・エネルギー・連成振動
close([6/2*2, 0.5*6/2*2**2], [6, 6])
close(math.sqrt(8/2), 2)
close(8*0.5**2/2, 1)
close(.5+.3**2*math.pi**2/4, .7220660990245106)
close((1.01**2+3*1.98**2)-(1+3*2**2), -.2187)
D = np.array([[10,-6],[-6,10]])
close(np.linalg.eigvalsh(D), [4,16])
close(.1*np.array([math.cos(math.pi)+math.cos(2*math.pi),math.cos(math.pi)-math.cos(2*math.pi)]), [0,-.2])
close(.5*4*.2**2+.5*6*.2**2, .2)
close(1**2/(2*2)+8*.25**2/2, .5)
close(2**2*.5**2/(2*2)+8*.5**2/(2*2**2), .5)
close(.5+math.pi**2/16, 1.1168502750680849)
close(4*2*3,24)
close((2-3)/2,-.5)

# 第2章：基底、交換子、内積、固有値、射影、テンソル積
close(np.linalg.solve([[1,1],[1,-1]],[3,4]),[3.5,-.5])
close(np.array([[2,1],[1,1]])@np.array([1,2]),[4,3])
A=np.array([[1,1],[0,1]])
B=np.array([[1,0],[1,1]])
close(A@B-B@A,np.diag([1,-1]))
close(np.linalg.eigvalsh([[2,1j],[-1j,2]]),[1,3])
U=np.array([[1,1],[1,-1]])/math.sqrt(2)
close(U.T@U,np.eye(2))
close(U.T@D@U,np.diag([4,16]))
u=np.array([1,1])/math.sqrt(2)
P=np.outer(u,u)
close(P@P,P)
close(np.linalg.norm(P@np.array([1,0]))**2,.5)
close(np.kron(u,np.array([1,-1])/math.sqrt(2)),[.5,-.5,.5,-.5])
close(np.array([[2,1],[1,2]])@np.array([2,-1]),[3,0])
close(np.abs(np.array([2,1j])/math.sqrt(5))**2,[.8,.2])

# 第3章：測定、Pauli代数、時間発展、Gaussian積分、振動子
psi=np.array([math.sqrt(3)/2,.5])
close(np.abs(U@psi)**2,[(2+math.sqrt(3))/4,(2-math.sqrt(3))/4])
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,-1j],[1j,0]])
sz=np.diag([1,-1])
close(sx@sz-sz@sx,-2j*sy)
psi=np.array([1,1j])/math.sqrt(2)
close(sy@psi,psi)
close(np.vdot(psi,sx@psi),0)
close(np.vdot(psi,sz@psi),0)
close([math.sin(math.pi/4)**2,math.sin(math.pi/2)**2],[.5,1])
x=np.linspace(-12,12,24001)
integrate=np.trapezoid if hasattr(np,"trapezoid") else np.trapz
for s in [.25,.5,2]:
    rho=np.exp(-x*x/(2*s*s))/(math.sqrt(2*math.pi)*s)
    # s=2 では±6標準偏差なので端の残差を考慮する。
    np.testing.assert_allclose(integrate(rho,x),1,atol=1e-8)
    np.testing.assert_allclose(integrate(x*x*rho,x),s*s,atol=1e-6)
    dp=1/(2*s)
    close(s*dp,.5)
close(.2*(np.array([0,4])+.5),[.1,.9])
# 有限行列での梯子演算子の最上端には打切り誤差があるため、内部状態だけ検査。
a=np.diag(np.sqrt(np.arange(1,7)),1)
close((a@a.T-a.T@a)[:6,:6],np.eye(6))
close((a.T@a).diagonal(),np.arange(7))
print("review chapters 01-03: numerical checks OK")
