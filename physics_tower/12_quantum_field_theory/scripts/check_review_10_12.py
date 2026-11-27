"""第10〜12章の代表的な数値・行列検算。"""
import math
import numpy as np
def close(a,b,atol=1e-10):
    np.testing.assert_allclose(a,b,rtol=1e-10,atol=atol)
rho,T=.02,2.
v=math.sqrt(T/rho)
close(v,10)
close(math.sqrt(4*10/.1)*math.sin(math.pi/4),math.sqrt(200))
for a in [.1,.05,.001]:
    close(((1+a)**2-2+(1-a)**2)/a**2,2,atol=1e-8)
    assert abs(2*math.sin(a/2)/a-1)<a*a/24+1e-12
x=np.linspace(0,1,4001)
integrate=np.trapezoid if hasattr(np,"trapezoid") else np.trapz
for n in range(1,4):
    for m in range(1,4):
        close(integrate(2*np.sin(n*np.pi*x)*np.sin(m*np.pi*x),x),float(n==m))
        close(integrate(2*n*m*np.pi**2*np.cos(n*np.pi*x)*np.cos(m*np.pi*x),x),(n*np.pi)**2*float(n==m))
e=rho*(v*2*np.pi*.01*np.sin(2*np.pi*x))**2
close(integrate(e,x),.0039478417604357436)
close(integrate(v*e,x),.039478417604357436)
E=math.sqrt(13)
ep,pp=1.25*np.array([E-.6*3,3-.6*E])
close(ep**2-pp**2,4)
close(1.25*(1-.6*3/E),ep/E)
close([3.25**2-1.25**2,-4*.5*1.5,-4*1*2],[9,-3,-8])
u,v,x0,y=1.2,3.,.4,.8
b=.7
up,xp,vp=u,x0+b*u,v+2*b*x0+b*b*u
close(up*vp-xp*xp-y*y,u*v-x0*x0-y*y)
close(5/3*(.75-.8*1.25),-5/12)
U=np.array([[1,-1j],[1,1j]])/math.sqrt(2)
close(U@U.conj().T,np.eye(2))
Qc,Qs=1.2,.7
q=(Qc-1j*Qs)/math.sqrt(2)
theta=.9
close(q*np.exp(1j*theta)+q.conjugate()*np.exp(-1j*theta),math.sqrt(2)*(Qc*math.cos(theta)+Qs*math.sin(theta)))
# 有限振動子行列では最上端を除く
a=np.diag(np.sqrt(np.arange(1,9)),1)
omega=2.
Q=(a+a.T)/math.sqrt(2*omega)
P=-1j*math.sqrt(omega/2)*(a-a.T)
close((Q@P-P@Q)[:8,:8],1j*np.eye(8))
close(((P@P+omega**2*Q@Q)/2)[:8,:8],np.diag(omega*(np.arange(8)+.5)))
close((Q@Q)[0,0],.25)
close((P@P)[0,0],1)
close(4+math.sqrt(13),7.60555127546399)
close(np.exp(-1j*omega*np.pi/4)/(2*omega),-.25j)
eta=.5
time=np.linspace(-60,60,240001)
k0=.7
num=integrate(np.exp(1j*k0*time-(eta+1j*omega)*np.abs(time))/(2*omega),time)
exact=1j/(2*omega)*(1/(k0-omega+1j*eta)-1/(k0+omega-1j*eta))
close(num,exact,atol=1e-7)
close((20**4/(16*np.pi**2))/(10**4/(16*np.pi**2)),16)
print("review chapters 10-12: numerical checks OK")
