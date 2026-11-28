"""第16〜18章の代表的な積分・行列・数値検算。"""
import math
import itertools
import numpy as np
def close(a,b,atol=1e-10,rtol=1e-10):
    np.testing.assert_allclose(a,b,atol=atol,rtol=rtol)
integrate=np.trapezoid if hasattr(np,"trapezoid") else np.trapz
# cutoff integrals
I1=lambda L,m:(L**2-m*m*np.log1p(L**2/m**2))/(16*np.pi**2)
I2=lambda L,m:(np.log1p(L**2/m**2)+m*m/(L**2+m*m)-1)/(16*np.pi**2)
for L in [10,20]:
    k=np.linspace(0,L,200001)
    close(integrate(k**3/(k*k+1),k)/(8*np.pi**2),I1(L,1),atol=1e-8)
    close(integrate(k**3/(k*k+1)**2,k)/(8*np.pi**2),I2(L,1),atol=1e-8)
close([I1(10,1),I1(20,1)],[.6040318056759615,2.4950723869008686])
close([I2(10,1),I2(20,1)],[.022955716863257442,.03164042213498649])
close(.3*I1(10,1),.18120954170278844)
close(.3*I1(20,1),.7485217160702605)
x=np.linspace(0,1,20001)
z=integrate(np.log1p(4*x*(1-x)),x)
close(z,.49290096,atol=1e-7)
close(.36*z/(32*np.pi**2),.00056184,atol=1e-8)
close((2.2**2*(np.log(2.2)-1.5)+1.5)/(64*np.pi**2),-.0030774194069115536)
close(3+np.log((1e7+2)/(1e7+1))-np.log(2),3-np.log(2),atol=2e-7)
# QED gamma traces and spin sums
I=np.eye(2)
O=np.zeros((2,2))
sig=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
g0=np.block([[I,O],[O,-I]])
gamma=[g0]+[np.block([[O,A],[-A,O]]) for A in sig]
eta=np.diag([1,-1,-1,-1])
for i,j in itertools.product(range(4),repeat=2):
    close(np.trace(gamma[i]@gamma[j]),4*eta[i,j])
for i,j,k,l in itertools.product(range(4),repeat=4):
    close(np.trace(gamma[i]@gamma[j]@gamma[k]@gamma[l]),4*(eta[i,j]*eta[k,l]-eta[i,k]*eta[j,l]+eta[i,l]*eta[j,k]))
slash=lambda p:sum(v*g for v,g in zip(eta@p,gamma))
e2=4*np.pi/137
for th in [0,np.pi/3,np.pi/2,np.pi]:
    p1=np.array([5,0,0,5])
    p2=np.array([5,0,0,-5])
    p3=np.array([5,5*np.sin(th),0,5*np.cos(th)])
    p4=np.array([5,-5*np.sin(th),0,-5*np.cos(th)])
    L=np.array([[np.trace(slash(p2)@a@slash(p1)@b) for b in gamma] for a in gamma])
    H=np.array([[np.trace(slash(p3)@a@slash(p4)@b) for b in gamma] for a in gamma])
    close(e2**2*np.sum(L*(eta@H@eta))/(4*100**2),e2**2*(1+np.cos(th)**2))
    close(L@(eta@(p1+p2)),np.zeros(4))
z=np.linspace(-1,1,20001)
close(integrate(1+z*z,z),8/3,atol=1e-8)
close(4*np.pi/(3*100*137**2)*389400,.8690473151173854)
ae=1/(137.035999206*2*np.pi)
close(ae,.001161409731851883)
close((ae-.00115965218059)/.00115965218059,.001515584,atol=1e-7)
# RG and EFT
c=3/(16*np.pi**2)
for r,expected in [(10,.6161722559258466),(100,.6332404674289527)]:
    close(.6/(1-c*.6*np.log(r)),expected)
close(137-2*np.log(100)/(3*np.pi),136.0227525348274,atol=1e-5)
wf=.1/c
close(-.1*wf+c*wf**2,0)
close(-.1+2*c*wf,.1)
close(3-2**2/4,2)
for xx in [-2,0,1,2]:
    yy=np.linspace(-12,12,24001)
    close(integrate(np.exp(-.5*(3*xx**2+4*yy**2+4*xx*yy)),yy),math.sqrt(2*math.pi/4)*math.exp(-xx**2))
close(.6-3*2**2/10**2,.48)
for r in [.04,.64]:
    exact=1/(1-r)
    for n in range(4):
        approx=sum(r**j for j in range(n+1))
        close(abs(exact-approx)/abs(exact),r**(n+1))
print("review chapters 16-18: numerical checks OK")
