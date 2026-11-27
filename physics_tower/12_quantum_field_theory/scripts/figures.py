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
ax[1].plot(t,.2/np.sqrt(2)*np.cos(2*t),label="In phase: Q+",color="#2166ac")
ax[1].plot(t,.2/np.sqrt(2)*np.cos(4*t),label="Out of phase: Q-",color="#16857c")
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

# 第2章：線形写像と単位正方形
from matplotlib.patches import Polygon
A=np.array([[2,1],[1,1]])
square=np.array([[0,0],[1,0],[1,1],[0,1]])
fig,axs=plt.subplots(1,2,figsize=(6.5,3.3),layout="constrained")
for ax,M,title in zip(axs,[np.eye(2),A],["Original","After A"]):
    ax.add_patch(Polygon(square@M.T,closed=True,facecolor="#2166ac",alpha=.16,edgecolor="#2166ac"))
    for v,col in zip(M.T,["#2166ac","#16857c"]):
        ax.quiver(0,0,*v,angles="xy",scale_units="xy",scale=1,color=col)
    ax.set(xlim=(-.5,3.5),ylim=(-.5,3.5),xlabel="x",ylabel="y",title=title,aspect="equal")
    ax.grid(alpha=.2)
fig.savefig(out/"linear_map.png",dpi=220)
plt.close(fig)
# 複素平面上の位相加算
fig,ax=plt.subplots(figsize=(4,3.6),layout="constrained")
theta=np.linspace(0,2*np.pi,400)
ax.plot(np.cos(theta),np.sin(theta),color="#94a3b8")
for a,label,col in [(np.pi/6,"30°","#2166ac"),(np.pi/3,"60°","#16857c"),(np.pi/2,"30° + 60°","#d97706")]:
    ax.quiver(0,0,np.cos(a),np.sin(a),angles="xy",scale_units="xy",scale=1,color=col,label=label)
ax.axhline(0,color="#94a3b8",lw=.7)
ax.axvline(0,color="#94a3b8",lw=.7)
ax.set(xlim=(-1.15,1.15),ylim=(-1.15,1.15),aspect="equal",xlabel="Re z",ylabel="Im z")
ax.legend(fontsize=8,loc="lower left")
fig.savefig(out/"complex_phase.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.8,3.0),layout="constrained")
ax.plot(theta,(1+np.cos(theta))/2,color="#2166ac")
ax.set(xlabel="Relative phase [rad]",ylabel="Squared amplitude",ylim=(-.04,1.04),xticks=[0,np.pi,2*np.pi],xticklabels=["0","π","2π"])
ax.grid(alpha=.25)
fig.savefig(out/"interference.png",dpi=220)
plt.close(fig)
# 固有方向と一般のベクトルを比較（出力を16で割って描画）
D=np.array([[10,-6],[-6,10]])
fig,ax=plt.subplots(figsize=(4.6,4.2),layout="constrained")
for v,col,label in [(np.array([1.,1.])/np.sqrt(2),"#2166ac","In phase"),(np.array([1.,-1.])/np.sqrt(2),"#16857c","Out of phase"),(np.array([1.,0.]),"#d97706","Other")]:
    dest=D@v/16
    ax.quiver(0,0,*v,angles="xy",scale_units="xy",scale=1,color=col,alpha=.4,width=.013)
    ax.quiver(0,0,*dest,angles="xy",scale_units="xy",scale=1,color=col,label=label,width=.007)
ax.set(xlim=(-1.1,1.2),ylim=(-1.1,1.2),aspect="equal",xlabel="q1",ylabel="q2",title="v (faint), Dv/16 (solid)")
ax.grid(alpha=.2)
ax.legend(fontsize=8)
fig.savefig(out/"eigenvectors.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(4,3.7),layout="constrained")
ax.plot(np.cos(theta),np.sin(theta),color="#94a3b8")
for a,col,label in [(0,"#2166ac","v"),(np.pi/3,"#16857c","Uv")]:
    ax.quiver(0,0,np.cos(a),np.sin(a),angles="xy",scale_units="xy",scale=1,color=col,label=label)
ax.set(xlim=(-1.15,1.15),ylim=(-1.15,1.15),aspect="equal",xlabel="x",ylabel="y",title="Rotation by 60°")
ax.grid(alpha=.2)
ax.legend()
fig.savefig(out/"unitary.png",dpi=220)
plt.close(fig)
