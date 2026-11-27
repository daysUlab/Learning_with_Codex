"""静的図を再生成する。HTML/PDFで同じ物理モデルを使用。"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parents[1] / "figures"
out.mkdir(exist_ok=True)
m, k, A = 2., 8., 0.5
w = np.sqrt(k/m)
t = np.linspace(0, 2*np.pi/w, 400)
x = A*np.cos(w*t)
p = -m*A*w*np.sin(w*t)
fig, ax = plt.subplots(1, 2, figsize=(7.2, 3.0), layout="constrained")
ax[0].plot(t, x, color="#2166ac")
ax[0].set(xlabel="t [s]", ylabel="x [m]", title="Position")
ax[1].plot(x, p, color="#16857c")
ax[1].scatter([A], [0], color="#16857c")
ax[1].set(xlabel="x [m]", ylabel="p [kg m/s]", title="Phase space")
for a in ax:
    a.grid(alpha=.25)
fig.savefig(out/"oscillator.png", dpi=220)
plt.close(fig)
# 離散経路 q(t)=t+a*sin(pi*t), m=T=1, V=0
fig, ax = plt.subplots(figsize=(5.6, 3.2), layout="constrained")
t = np.linspace(0, 1, 300)
for a in [-.3, 0, .3]:
    ax.plot(t, t+a*np.sin(np.pi*t), label=f"a={a:+.1f} m")
ax.set(xlabel="t [s]", ylabel="q [m]", title="Paths with fixed endpoints")
ax.legend()
ax.grid(alpha=.25)
fig.savefig(out/"paths.png", dpi=220)
plt.close(fig)


# 連成振動子の二つの固有モード
fig, ax = plt.subplots(2, 1, figsize=(5.8, 4.2), layout="constrained")
from matplotlib.patches import Rectangle
def spring(a, left, right, y=0):
    xx = np.linspace(left, right, 19)
    yy = np.zeros_like(xx) + y
    yy[1:-1] += .12 * (-1)**np.arange(17)
    a.plot(xx, yy, color="#64748b")
for x0 in [0, 6]:
    ax[0].plot([x0, x0], [-.45,.45], color="#64748b", lw=4)
for x0 in [2,4]:
    ax[0].add_patch(Rectangle((x0-.3,-.23),.6,.46,color="#2166ac"))
    ax[0].text(x0,0,"m",color="white",ha="center",va="center")
for l,r,name in [(0,1.7,"k"),(2.3,3.7,"κ"),(4.3,6,"k")]:
    spring(ax[0],l,r)
    ax[0].text((l+r)/2,.3,name,ha="center")
ax[0].set(xlim=(-.3,6.3),ylim=(-.5,.6),title="Coupled oscillators")
ax[0].axis("off")
t = np.linspace(0,np.pi,400)
ax[1].plot(t,.2*np.cos(2*t),label="In phase: Q+",color="#2166ac")
ax[1].plot(t,.2*np.cos(4*t),label="Out of phase: Q-",color="#16857c")
ax[1].set(xlabel="t [s]",ylabel="Mode amplitude [m]")
ax[1].legend(fontsize=8)
ax[1].grid(alpha=.25)
fig.savefig(out/"coupled.png",dpi=220)
plt.close(fig)
# q,p と Q=2q,P=p/2 は同じ運動を表す
theta=np.linspace(0,2*np.pi,400)
q=.5*np.cos(theta)
p=-2*np.sin(theta)
fig, ax=plt.subplots(1,2,figsize=(6,3),layout="constrained")
for a,xx,yy,xlabel,ylabel in [(ax[0],q,p,"q [m]","p [kg m/s]"),(ax[1],2*q,p/2,"Q [m]","P [kg m/s]")]:
    a.plot(xx,yy,color="#16857c")
    a.set(xlabel=xlabel,ylabel=ylabel,xlim=(-1.1,1.1),ylim=(-2.2,2.2))
    a.grid(alpha=.25)
fig.savefig(out/"canonical.png",dpi=220)
plt.close(fig)
