"""導入補強の代表例を検算する。"""
import math
import numpy as np

def close(a,b):
    np.testing.assert_allclose(a,b,rtol=1e-10,atol=1e-10)

# 偏微分、ばねの初期条件、基底変換、射影測定
close([2*2,6*1],[4,6])
close([.5*math.cos(0)+.3/2*math.sin(0),-.5*2*math.sin(0)+.3*math.cos(0)],[.5,.3])
B=np.array([[1,1],[1,-1]])
close(B@np.array([3.5,-.5]),[3,4])
close(np.linalg.inv(B)@np.diag([2,3])@B,[[2.5,-.5],[-.5,2.5]])
u=np.array([1,1j])
v=np.array([3,2j])
w=v-u*np.vdot(u,v)/np.vdot(u,u)
close(np.vdot(w,w),np.vdot(v,v)-abs(np.vdot(u,v))**2/np.vdot(u,u))
psi=np.array([1,2j])/math.sqrt(5)
P=np.diag([1,0])
close(np.vdot(psi,P@psi),.2)
close(P@psi/math.sqrt(.2),[1,0])
# Fourier成分の抽出
x=np.linspace(0,2*np.pi,2001)
f=np.sin(x)+.5*np.sin(2*x)
integrate=np.trapezoid if hasattr(np,"trapezoid") else np.trapz
close([integrate(f*np.sin(n*x),x)/np.pi for n in [1,2,3]],[1,.5,0])
close(1/math.sqrt(10*(2*math.pi/10)),1/math.sqrt(2*math.pi))
print("introductory review chapters 01-03: checks OK")
