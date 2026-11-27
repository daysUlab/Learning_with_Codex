"""第7〜9章の独立数値検算。全命題の証明ではない。"""
import math
import numpy as np

def close(a,b,atol=1e-10):
    np.testing.assert_allclose(a,b,atol=atol,rtol=1e-10)

# 第7章：境界条件・確率流・角度分布・位相空間
for k,q in [(2,1),(3,1),(5,4)]:
    r=(k-q)/(k+q)
    t=2*k/(k+q)
    close([1+r,k*(1-r)],[t,q*t])
    close(r*r+q/k*t*t,1)
close([1/9,8/9],[((2-1)/(2+1))**2,1/2*(4/3)**2])
close(16*math.pi/100,.5026548245743669)
close(2*2*math.sin(math.pi/6),2)
close(math.exp(-(2*2*math.sin(math.pi/6))**2),math.exp(-4))
close(4*math.pi/2**2,math.pi)
close(1/(16*math.pi*4)*.3894*1000,1.936716714799504,atol=1e-3)
# 一次元Gaussian Fourier変換（実数値の積分）
x=np.linspace(-10,10,20001)
integrate=np.trapezoid if hasattr(np,"trapezoid") else np.trapz
for Q in [0,1,2]:
    close(integrate(np.exp(-x*x/2-1j*Q*x),x),math.sqrt(2*math.pi)*math.exp(-Q*Q/2))
# 黄金律の核の面積（有限区間の打切り誤差込み）
u=np.linspace(-200,200,40001)
close(integrate(np.sinc(u/np.pi)**2,u),math.pi,atol=.006)
# S行列のユニタリ性と光学定理
S=np.diag(np.exp(2j*np.array([.2,.7])))
T=(S-np.eye(2))/1j
close(-1j*(T-T.conj().T),T.conj().T@T)

# 第8章：D4、C4の指標、既約分解
R=np.array([[0,-1],[1,0]])
S=np.diag([1,-1])
close(R@S,[[0,1],[1,0]])
close(S@R,[[0,-1],[-1,0]])
close(S@R@S,R.T)
close(np.linalg.matrix_power(R,4),np.eye(2))
chars=np.exp(2j*np.pi*np.outer(np.arange(4),np.arange(4))/4)
close(chars.conj()@chars.T/4,np.eye(4))
close(chars.conj()@np.array([2,0,-2,0])/4,[0,1,0,1])
U=np.array([[1,1],[-1j,1j]])/math.sqrt(2)
close(U.conj().T@R@U,np.diag([1j,-1j]))
close(U.conj().T@S@U,[[0,1],[1,0]])

# 第9章：Lie代数・二重被覆・角運動量合成
Lx=np.array([[0,0,0],[0,0,-1],[0,1,0]])
Ly=np.array([[0,0,1],[0,0,0],[-1,0,0]])
Lz=np.array([[0,-1,0],[1,0,0],[0,0,0]])
close(Lx@Ly-Ly@Lx,Lz)
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,-1j],[1j,0]])
sz=np.diag([1,-1])
P=np.array([sx,sy,sz])
close(sx@sy,1j*sz)
n=np.array([1,2,3])/math.sqrt(14)
v=np.array([.3,-.5,.7])
theta=.9
N=np.einsum("i,ijk->jk",n,P)
U=math.cos(theta/2)*np.eye(2)-1j*math.sin(theta/2)*N
close(U.conj().T@U,np.eye(2))
close(np.linalg.det(U),1)
v2=v*math.cos(theta)+np.cross(n,v)*math.sin(theta)+n*np.dot(n,v)*(1-math.cos(theta))
close(U@np.einsum("i,ijk->jk",v,P)@U.conj().T,np.einsum("i,ijk->jk",v2,P))
close(math.cos(math.pi/6)**2,.75)
close(math.sqrt(1.5*2.5-.5*1.5),math.sqrt(3))
H=sum(np.kron(A,A) for A in P)/4
close(np.linalg.eigvalsh(H),[-.75,.25,.25,.25])
singlet=np.array([0,1,-1,0])/math.sqrt(2)
for A in P:
    close((np.kron(A,np.eye(2))+np.kron(np.eye(2),A))@singlet,np.zeros(4))
print("review chapters 07-09: numerical checks OK")
