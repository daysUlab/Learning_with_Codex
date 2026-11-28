"""第13〜15章の代表数値・行列・組合せ検査。"""
import math
import itertools
import numpy as np
def close(a,b,atol=1e-10):
    np.testing.assert_allclose(a,b,rtol=1e-10,atol=atol)
I=np.eye(2)
O=np.zeros((2,2))
sig=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
alpha=[np.block([[O,A],[A,O]]) for A in sig]
beta=np.block([[I,O],[O,-I]])
gamma=[beta]+[beta@A for A in alpha]
eta=np.diag([1,-1,-1,-1])
for i,j in itertools.product(range(4),repeat=2):
    close(gamma[i]@gamma[j]+gamma[j]@gamma[i],2*eta[i,j]*np.eye(4))
m=2.
p=np.array([1.,2.,3.])
E=math.sqrt(m*m+p@p)
B=sum(pi*A for pi,A in zip(p,sig))
H=sum(pi*A for pi,A in zip(p,alpha))+m*beta
close(H@H,E*E*np.eye(4))
u=math.sqrt(E+m)*np.vstack([I,B/(E+m)])
v=math.sqrt(E+m)*np.vstack([B/(E+m),I])
vm=math.sqrt(E+m)*np.vstack([-B/(E+m),I])
gp=E*gamma[0]-sum(pi*A for pi,A in zip(p,gamma[1:]))
close(H@u,E*u)
close((gp+m*np.eye(4))@v,np.zeros((4,2)))
close(u.conj().T@u,2*E*I)
close(u@u.conj().T@beta,gp+m*np.eye(4))
close(v@v.conj().T@beta,gp-m*np.eye(4))
close(u@u.conj().T+vm@vm.conj().T,2*E*np.eye(4))
xi=.7
S=math.cosh(xi/2)*np.eye(4)+math.sinh(xi/2)*alpha[2]
close(S.conj().T@beta@S,beta)
close(np.linalg.inv(S)@gamma[0]@S,math.cosh(xi)*gamma[0]+math.sinh(xi)*gamma[3])
c=np.array([[0,1],[0,0]])
close(-3*c@c.T+3*I,3*c.T@c)
close(np.linalg.det([[2,1],[1,3]]),5)
# Proca偏極、完全性、射影
m,k=3.,4.
E=math.hypot(m,k)
p4=np.array([E,0,0,k])
eps=np.array([[0,1,0,0],[0,0,1,0],[k/m,0,0,E/m]])
close(eps@eta@p4,np.zeros(3))
close(eps@eta@eps.T,-np.eye(3))
close(eps.T@eps,-eta+np.outer(p4,p4)/m**2)
n=np.array([.6,0,.8])
P=np.eye(3)-np.outer(n,n)
close(P@P,P)
close(P@n,np.zeros(3))
close(P@np.array([1,0,0]),[.64,0,-.48])
close(.1/(math.sqrt(1.01)+1),math.sqrt(1.01)*10-10)
# Wick組合せ、Gaussianモーメント、頂点係数
def pairings(xs):
    if not xs:
        yield ()
        return
    for i in range(1,len(xs)):
        for rest in pairings(xs[1:i]+xs[i+1:]):
            yield ((xs[0],xs[i]),)+rest
for n in [2,4,6,8]:
    close(len(list(pairings(list(range(n))))),math.factorial(n)/(2**(n//2)*math.factorial(n//2)))
d=.25
x=np.linspace(-5,5,40001)
rho=np.exp(-x*x/(2*d))/math.sqrt(2*math.pi*d)
integrate=np.trapezoid if hasattr(np,"trapezoid") else np.trapz
close(integrate(x**4*rho,x),3*d*d)
close(integrate(x**6*rho,x),15*d**3)
close(2*(4*3)**2*2/(2*math.factorial(4)**2),.5)
# Mandelstam変数・断面積
m,p,th=1.,2.,math.pi/3
E=math.hypot(m,p)
a=np.array([E,0,0,p])
b=np.array([E,0,0,-p])
c=np.array([E,p*math.sin(th),0,p*math.cos(th)])
d=np.array([E,-p*math.sin(th),0,-p*math.cos(th)])
sq=lambda v:v@eta@v
close([sq(a+b),sq(a-c),sq(a-d)],[20,-4,-12])
close(.6**2/(32*math.pi*20)*389400,69.724,atol=.01)
close(.4**2/(32*math.pi*16),9.94718394324346e-5)
print("review chapters 13-15: numerical checks OK")
