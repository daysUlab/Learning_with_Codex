"""第4〜6章の数値検算。規制付き積分と有限次元代数の例。"""
import math
import cmath
import itertools
import numpy as np

def close(a, b, atol=1e-10):
    np.testing.assert_allclose(a,b,rtol=1e-10,atol=atol)

# 第4章：自由核の複素位相と規格化、虚時間核の合成
def kernel(x,T):
    return np.exp(1j*x*x/(2*T))/np.sqrt(2j*np.pi*T)
K=kernel(2,1)
close(abs(K),1/math.sqrt(2*math.pi))
close(cmath.phase(K),2-math.pi/4)
close([K.real,K.imag],[.138744163,.374039003],atol=3e-4)
close(math.pi**2*.1**2/(4*.05),.4934802200544679)
close(math.pi**2*.5**2/(4*.05),12.337005501361697)
close((1+math.cos(math.pi/3))/2,.75)
close(math.exp(-4),.01831563888873418)
close(1/math.sqrt(4*math.pi),.28209479177387814)
# 収束する複素時間で自由核を数値合成。T-i eta として eta>0。
x=np.linspace(-25,25,50001)
integrate=np.trapezoid if hasattr(np,"trapezoid") else np.trapz
t1=.7-.4j
t2=1.1-.5j
xi=-.3
xf=1.2
close(integrate(kernel(xf-x,t2)*kernel(x-xi,t1),x),kernel(xf-xi,t1+t2),atol=1e-8)
# 調和振動子核の自由極限
w=1e-4
T=1.3
Kosc=np.sqrt(w/(2j*np.pi*np.sin(w*T)))*np.exp(1j*w*((xf**2+xi**2)*np.cos(w*T)-2*xf*xi)/(2*np.sin(w*T)))
close(Kosc,kernel(xf-xi,T),atol=1e-8)

# 第5章：占有数・交換干渉・CAR
for M,N in [(3,2),(4,3),(2,2)]:
    close(len(list(itertools.combinations_with_replacement(range(M),N))),math.comb(M+N-1,N))
    close(len(list(itertools.combinations(range(M),N))),math.comb(M,N))
U=np.array([[1,1],[1,-1]])/math.sqrt(2)
T=np.kron(U,U)
symmetric=np.array([0,1,1,0])/math.sqrt(2)
antisymmetric=np.array([0,1,-1,0])/math.sqrt(2)
close(T@symmetric,np.array([1,0,0,-1])/math.sqrt(2))
close(T@antisymmetric,-antisymmetric)
close(np.vdot(symmetric,antisymmetric),0)
c=np.array([[0,1],[0,0]])
Z=np.diag([1,-1])
a=np.kron(c,np.eye(2))
b=np.kron(Z,c)
for i,A in enumerate([a,b]):
    for j,B in enumerate([a,b]):
        close(A@B.T+B.T@A,np.eye(4) if i==j else np.zeros((4,4)))
        close(A@B+B@A,np.zeros((4,4)))
vac=np.eye(4)[:,0]
close(a.T@b.T@vac,np.eye(4)[:,3])
close(b.T@a.T@vac,-np.eye(4)[:,3])
close(b@np.eye(4)[:,3],-np.eye(4)[:,2])
close(math.sqrt(2)*math.sqrt(2),2)
close(.2*4*3/2,1.2)
close(np.dot([2,0,3],[1,3,4]),14)

# 第6章：Lorentz変換・四元量・閾値
def boost(beta):
    gamma=1/math.sqrt(1-beta*beta)
    return gamma*np.array([[1,-beta],[-beta,1]])
metric=np.diag([1,-1])
L=boost(.6)
close(L.T@metric@L,metric)
close(L@np.array([5,3]),[4,0])
close(L@np.array([5,1]),[5.5,-2.5])
close(L@np.array([0,10]),[-7.5,12.5])
close(boost(-.6)@L,np.eye(2))
close(L@L,boost(15/17))
close(math.tanh(math.log(4)),15/17)
close(10*math.sqrt(1-.8**2),6)
close((.8+.5)/(1+.8*.5),13/14)
close(math.sqrt(2**2+3**2),math.sqrt(13))
mass=.511
E=mass/math.sqrt(1-.8**2)
mom=.8*E
close(E**2-mom**2,mass**2)
close([E,mom],[.8516666666666667,.6813333333333333])
close(197.327/100,1.97327)
close(math.sqrt(2*.6**2*(1-math.cos(math.pi))),1.2)
close(math.sqrt(2*.6**2),.848528137423857)
assert .848528137423857 < 2*mass < 1.2
print("review chapters 04-06: numerical checks OK")
