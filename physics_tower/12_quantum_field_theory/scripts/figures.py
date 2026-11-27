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

# 第3章：測定基底と確率
fig,axs=plt.subplots(1,2,figsize=(5.8,2.8),layout="constrained",sharey=True)
for ax,labels,probs,title in [(axs[0],["0","1"],[.75,.25],"Z basis"),(axs[1],["+","-"],[(2+np.sqrt(3))/4,(2-np.sqrt(3))/4],"X basis")]:
    ax.bar(labels,probs,color=["#2166ac","#16857c"])
    ax.set(ylim=(0,1.08),title=title)
    for i,v in enumerate(probs):
        ax.text(i,v+.025,f"{v:.3f}",ha="center",fontsize=9)
axs[0].set_ylabel("Probability")
fig.savefig(out/"measurement.png",dpi=220)
plt.close(fig)
# 二状態系の時間発展
t=np.linspace(0,np.pi,400)
fig,ax=plt.subplots(figsize=(5.6,3),layout="constrained")
ax.plot(t,np.cos(t)**2,label="P(0)",color="#2166ac")
ax.plot(t,np.sin(t)**2,label="P(1)",color="#d97706")
ax.set(xlabel="t [s]",ylabel="Probability",ylim=(-.03,1.03),xticks=[0,np.pi/2,np.pi],xticklabels=["0","π/2","π"])
ax.legend()
ax.grid(alpha=.25)
fig.savefig(out/"two_state.png",dpi=220)
plt.close(fig)
# ガウス波束、hbar=1, p0=0
x=np.linspace(-6,6,700)
p=np.linspace(-4,4,700)
fig,axs=plt.subplots(1,2,figsize=(6.4,3.1),layout="constrained")
for s,col in [(.5,"#2166ac"),(2,"#d97706")]:
    dp=1/(2*s)
    axs[0].plot(x,np.exp(-x*x/(2*s*s))/(np.sqrt(2*np.pi)*s),color=col,label=f"s={s:g}")
    axs[1].plot(p,np.exp(-p*p/(2*dp*dp))/(np.sqrt(2*np.pi)*dp),color=col,label=f"s={s:g}")
for ax,label in zip(axs,["x","p"]):
    ax.set(xlabel=label,ylabel="Probability density")
    ax.grid(alpha=.25)
    ax.legend(fontsize=8)
fig.savefig(out/"gaussian_packet.png",dpi=220)
plt.close(fig)
# 調和振動子：無次元 y=sqrt(m*omega/hbar)*x
y=np.linspace(-3.6,3.6,600)
base=np.pi**(-.25)*np.exp(-y*y/2)
states=[base,np.sqrt(2)*y*base,(2*y*y-1)/np.sqrt(2)*base]
fig,ax=plt.subplots(figsize=(5.8,4.2),layout="constrained")
ax.plot(y,y*y/2,color="#94a3b8",label="Potential")
for n,psi in enumerate(states):
    level=n+.5
    ax.axhline(level,color="#64748b",ls="--",lw=.8)
    ax.plot(y,level+.75*psi**2,color=["#2166ac","#16857c","#d97706"][n])
    ax.text(3.65,level,f"n={n}",va="center",fontsize=9)
ax.set(xlim=(-3.6,4.2),ylim=(0,4.5),xlabel="Dimensionless position",ylabel="Energy / hbar omega")
ax.legend(fontsize=8)
ax.grid(alpha=.15)
fig.savefig(out/"quantum_oscillator.png",dpi=220)
plt.close(fig)

# 第4章：経路積分の候補経路
t=np.linspace(0,1,400)
fig,ax=plt.subplots(figsize=(5.6,3.5),layout="constrained")
for a in [-.5,-.3,-.15,.15,.3,.5]:
    ax.plot(t,t+a*np.sin(np.pi*t),color="#64748b",alpha=.45)
ax.plot(t,t,color="#2166ac",lw=2.5,label="Classical path")
ax.scatter([0,1],[0,1],color="#2166ac",zorder=5)
ax.set(xlabel="t",ylabel="x(t)")
ax.legend()
ax.grid(alpha=.2)
fig.savefig(out/"path_family.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.6,3.2),layout="constrained")
t=np.linspace(0,1,9)
q=t+.27*np.sin(np.pi*t)-.11*np.sin(3*np.pi*t)
for j in range(1,8):
    ax.axvline(t[j],color="#94a3b8",alpha=.5,ls="--")
    ax.text(t[j],q[j]+.07,f"x{j}",ha="center",fontsize=8)
ax.plot(t,q,"o-",color="#2166ac")
ax.scatter([0,1],[0,1],color="#d97706",zorder=5)
ax.set(xlabel="Time",ylabel="Position",xticks=t,xticklabels=[f"{j}/8" for j in range(9)])
fig.savefig(out/"time_slices.png",dpi=220)
plt.close(fig)
# 自由粒子核：m=hbar=T=1
x=np.linspace(-5,5,1200)
kernel=np.exp(1j*(x*x/2-np.pi/4))/np.sqrt(2*np.pi)
fig,ax=plt.subplots(figsize=(5.6,3.2),layout="constrained")
ax.plot(x,kernel.real,label="Re K",color="#2166ac")
ax.plot(x,kernel.imag,label="Im K",color="#d97706")
ax.set(xlabel="Final position (initial position = 0)",ylabel="Amplitude")
ax.grid(alpha=.2)
ax.legend()
fig.savefig(out/"free_kernel.png",dpi=220)
plt.close(fig)
# 停留位相：第1章と共通の経路族
a=np.linspace(-.6,.6,1600)
S=.5+np.pi**2*a*a/4
fig,axs=plt.subplots(2,1,figsize=(5.6,4.5),layout="constrained",sharex=True)
axs[0].plot(a,S,color="#2166ac")
axs[0].set(ylabel="Action S(a)")
for h,col in [(.2,"#16857c"),(.05,"#d97706")]:
    axs[1].plot(a,np.cos((S-.5)/h),label=f"hbar={h}",color=col)
axs[1].set(xlabel="Path parameter a",ylabel="cos((S-S0)/hbar)")
axs[1].legend(fontsize=8)
for ax in axs:
    ax.axvline(0,color="#64748b",ls="--",alpha=.6)
    ax.grid(alpha=.2)
fig.savefig(out/"stationary_phase.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.6,3.2),layout="constrained")
ax.plot(x,kernel.real,color="#2166ac",label="Real time: Re K")
ax.plot(x,np.exp(-x*x/2)/np.sqrt(2*np.pi),color="#d97706",label="Euclidean kernel")
ax.set(xlabel="Final position (initial position = 0)",ylabel="Kernel")
ax.grid(alpha=.2)
ax.legend(fontsize=8)
fig.savefig(out/"euclidean_kernel.png",dpi=220)
plt.close(fig)

# 第5章：占有数の配置
from matplotlib.patches import Circle, FancyArrowPatch, Polygon
fig,axs=plt.subplots(2,3,figsize=(6.2,3.4),layout="constrained")
for row in range(2):
    for j,(na,nb) in enumerate([(2,0),(1,1),(0,2)]):
        ax=axs[row,j]
        for x0,n,label in [(0,na,"A"),(1,nb,"B")]:
            ax.plot([x0-.3,x0+.3],[0,0],color="#64748b",lw=1.5)
            ax.text(x0,-.25,label,ha="center",fontsize=9)
            for k0 in range(n):
                ax.add_patch(Circle((x0,.16+.27*k0),.11,color="#2166ac" if row==0 else "#16857c"))
        ax.set(xlim=(-.5,1.5),ylim=(-.4,.8),aspect="equal",title=f"({na},{nb})",xticks=[],yticks=[])
        if row==1 and j!=1:
            ax.text(.5,.67,"Forbidden",color="#b91c1c",ha="center",fontsize=9)
        for spine in ax.spines.values():
            spine.set_visible(False)
axs[0,0].set_ylabel("Bosons")
axs[1,0].set_ylabel("Fermions")
fig.savefig(out/"occupation_two_modes.png",dpi=220)
plt.close(fig)
# 交換による干渉
fig,ax=plt.subplots(figsize=(5.8,3.2),layout="constrained")
xx=np.arange(3)
for j,(probs,label,col) in enumerate([([.25,.5,.25],"Distinguishable","#94a3b8"),([.5,0,.5],"Bosons","#2166ac"),([0,1,0],"Fermions","#16857c")]):
    ax.bar(xx+(j-1)*.24,probs,width=.22,label=label,color=col)
ax.set(xticks=xx,xticklabels=["(2,0)","(1,1)","(0,2)"],xlabel="Output occupations",ylabel="Probability",ylim=(0,1.1))
ax.legend(fontsize=8)
ax.grid(axis="y",alpha=.2)
fig.savefig(out/"exchange_interference.png",dpi=220)
plt.close(fig)
# 状態数
from math import comb
ns=np.arange(7)
fig,ax=plt.subplots(figsize=(5.6,3.1),layout="constrained")
ax.plot(ns,[comb(3+int(n),int(n)) for n in ns],"o-",color="#2166ac",label="Bosons")
ax.plot(ns,[comb(4,int(n)) if n<=4 else 0 for n in ns],"s-",color="#16857c",label="Fermions")
ax.set(xlabel="Particle number N (M=4)",ylabel="Number of states",xticks=ns)
ax.grid(alpha=.25)
ax.legend()
fig.savefig(out/"fock_dimensions.png",dpi=220)
plt.close(fig)
# Fockセクターの模式図
fig,ax=plt.subplots(figsize=(5.8,3.0),layout="constrained")
for i in range(4):
    ax.add_patch(Rectangle((i*1.45-.49,-.34),.98,.68,facecolor="#2166ac",alpha=.15,edgecolor="#2166ac"))
    ax.text(i*1.45,0,f"N = {i}",ha="center",va="center")
for i in range(3):
    x0=i*1.45+.49
    ax.add_patch(FancyArrowPatch((x0,.22),(x0+.47,.22),arrowstyle="->",mutation_scale=12,color="#2166ac"))
    ax.add_patch(FancyArrowPatch((x0+.47,-.22),(x0,-.22),arrowstyle="->",mutation_scale=12,color="#d97706"))
ax.text(2.17,.7,"Creation: N + 1",ha="center",color="#2166ac")
ax.text(2.17,-.7,"Annihilation: N - 1",ha="center",color="#d97706")
ax.text(5.05,0,"...",ha="center",va="center")
ax.set(xlim=(-.65,5.35),ylim=(-1,1))
ax.axis("off")
fig.savefig(out/"fock_sectors.png",dpi=220)
plt.close(fig)
# 一モードの梯子
fig,ax=plt.subplots(figsize=(4.6,3.5),layout="constrained")
for n in range(4):
    ax.plot([-.45,.45],[n,n],color="#64748b",lw=1.5)
    ax.text(0,n+.1,f"|{n}>",ha="center")
for n in range(3):
    ax.add_patch(FancyArrowPatch((-.27,n+.14),(-.27,n+.86),arrowstyle="->",mutation_scale=12,color="#2166ac"))
    ax.add_patch(FancyArrowPatch((.27,n+.86),(.27,n+.14),arrowstyle="->",mutation_scale=12,color="#d97706"))
    ax.text(-.35,n+.5,f"√{n+1}",ha="right",va="center",color="#2166ac")
    ax.text(.35,n+.5,f"√{n+1}",ha="left",va="center",color="#d97706")
ax.text(-.4,3.43,"Creation",ha="center",color="#2166ac")
ax.text(.4,3.43,"Annihilation",ha="center",color="#d97706")
ax.set(xlim=(-1,1),ylim=(-.2,3.7))
ax.axis("off")
fig.savefig(out/"boson_ladder.png",dpi=220)
plt.close(fig)
# 生成順序と反交換符号
fig,ax=plt.subplots(figsize=(5.8,3.5),layout="constrained")
points={(0,0):(0,0),(1,0):(-1,1),(0,1):(1,1),(1,1):(0,2)}
for state,(px,py) in points.items():
    ax.text(px,py,f"|{state[0]},{state[1]}>",ha="center",va="center",bbox=dict(boxstyle="round",fc="#e8f2f7",ec="#64748b"),fontsize=11)
for start,end,label,col,dx in [((0,0),(1,0),"cA†: +","#2166ac",-.22),((1,0),(1,1),"cB†: −","#b91c1c",-.22),((0,0),(0,1),"cB†: +","#16857c",.22),((0,1),(1,1),"cA†: +","#16857c",.22)]:
    p0,p1=points[start],points[end]
    ax.add_patch(FancyArrowPatch(p0,p1,arrowstyle="->",shrinkA=18,shrinkB=18,mutation_scale=12,color=col))
    ax.text((p0[0]+p1[0])/2+dx,(p0[1]+p1[1])/2,label,ha="center",va="center",fontsize=9,color=col)
ax.set(xlim=(-1.65,1.65),ylim=(-.3,2.3))
ax.axis("off")
fig.savefig(out/"fermion_sign.png",dpi=220)
plt.close(fig)

# 第6章：Minkowski時空図
fig,ax=plt.subplots(figsize=(4.6,4.6),layout="constrained")
u=np.linspace(-4,4,200)
ax.plot(u,u,"--",color="#d97706",label="Light")
ax.plot(u,-u,"--",color="#d97706")
ax.axhline(0,color="#64748b",lw=.9)
ax.axvline(0,color="#64748b",lw=.9)
ax.plot(.6*u,u,color="#2166ac",label="ct' axis")
ax.plot(u,.6*u,color="#16857c",label="x' axis")
ax.set(xlim=(-4,4),ylim=(-4,4),aspect="equal",xlabel="x [light-s]",ylabel="ct [light-s]")
ax.legend(fontsize=8,loc="upper left")
ax.grid(alpha=.15)
fig.savefig(out/"minkowski_axes.png",dpi=220)
plt.close(fig)
# 時間の遅れ
beta=np.linspace(0,.98,500)
gamma=1/np.sqrt(1-beta**2)
fig,axs=plt.subplots(1,2,figsize=(6.3,3.1),layout="constrained")
axs[0].plot(beta,gamma,color="#2166ac")
axs[1].plot(beta,10/gamma,color="#16857c")
for v0 in [.6,.8]:
    g0=1/np.sqrt(1-v0*v0)
    axs[0].scatter(v0,g0,color="#d97706")
    axs[1].scatter(v0,10/g0,color="#d97706")
axs[0].set(xlabel="v/c",ylabel="Lorentz factor")
axs[1].set(xlabel="v/c",ylabel="Proper time [s]",ylim=(0,10.5))
for ax in axs:
    ax.grid(alpha=.25)
fig.savefig(out/"time_dilation.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.6,3.2),layout="constrained")
beta=np.linspace(0,.99,400)
ax.plot(beta,2*beta,label="Galilean: 2v",color="#94a3b8",ls="--")
ax.plot(beta,2*beta/(1+beta**2),label="Relativistic",color="#2166ac")
ax.axhline(1,color="#d97706",ls=":",label="Speed of light")
ax.set(xlabel="Each input speed / c",ylabel="Combined speed / c",ylim=(0,2))
ax.legend(fontsize=8)
ax.grid(alpha=.25)
fig.savefig(out/"velocity_addition.png",dpi=220)
plt.close(fig)
p=np.linspace(-4,4,500)
fig,ax=plt.subplots(figsize=(5.6,3.3),layout="constrained")
ax.plot(p,np.sqrt(1+p*p),label="Massive (m=1)",color="#2166ac")
ax.plot(p,np.abs(p),label="Massless",color="#d97706",ls="--")
ax.scatter([0],[1],color="#2166ac")
ax.set(xlabel="Momentum p (c=1)",ylabel="Energy E",ylim=(0,4.5))
ax.legend(fontsize=8)
ax.grid(alpha=.2)
fig.savefig(out/"energy_momentum.png",dpi=220)
plt.close(fig)
# 二光子による対生成の閾値（重心系）
fig,ax=plt.subplots(figsize=(5.8,2.8),layout="constrained")
ax.scatter([0],[0],marker="*",s=180,color="#d97706",zorder=4)
for start,end,label,y0 in [((-2.3,0),(-.28,0),"gamma",.22),((2.3,0),(.28,0),"gamma",.22)]:
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="->",mutation_scale=14,color="#2166ac" if label=="gamma" else "#16857c",lw=2))
    ax.text((start[0]+end[0])/2,y0,label,ha="center")
ax.text(0,.65,"Initial total momentum = 0",ha="center")
ax.scatter([-0.65,0.65],[-.8,-.8],s=85,color="#16857c")
ax.text(-.65,-1.05,"e- (p=0)",ha="center",fontsize=9)
ax.text(.65,-1.05,"e+ (p=0)",ha="center",fontsize=9)
ax.text(0,-1.35,"At threshold: final particles at rest",ha="center",fontsize=9)
ax.set(xlim=(-2.7,2.7),ylim=(-1.55,.95))
ax.axis("off")
fig.savefig(out/"pair_threshold.png",dpi=220)
plt.close(fig)

# 第7章：段差散乱
fig,axs=plt.subplots(1,2,figsize=(6.2,3),layout="constrained")
axs[0].step([-3,0,3],[0,3,3],where="post",color="#2166ac",label="V(x)")
axs[0].axhline(4,color="#d97706",ls="--",label="E")
axs[0].set(xlabel="x",ylabel="Energy",ylim=(-.3,4.7))
axs[0].legend(fontsize=8)
axs[1].bar(["R","T"],[1/9,8/9],color=["#2166ac","#16857c"])
axs[1].set(ylabel="Probability",ylim=(0,1.05))
fig.savefig(out/"step_scattering.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.6,3.6),layout="constrained")
for y0 in [-1,-.5,0,.5,1]:
    ax.add_patch(FancyArrowPatch((-2.6,y0),(-.25,y0),arrowstyle="->",mutation_scale=12,color="#2166ac",alpha=.7))
ax.add_patch(Circle((0,0),.22,color="#d97706"))
for theta0 in np.linspace(-1.35,1.35,7):
    ax.add_patch(FancyArrowPatch((.24*np.cos(theta0),.24*np.sin(theta0)),(2*np.cos(theta0),2*np.sin(theta0)),arrowstyle="->",mutation_scale=12,color="#16857c",alpha=.75))
ax.text(-1.5,1.35,"Incident wave",ha="center")
ax.text(1.4,1.6,"Scattered wave",ha="center")
ax.set(xlim=(-2.8,2.4),ylim=(-2,2),aspect="equal")
ax.axis("off")
fig.savefig(out/"scattering_geometry.png",dpi=220)
plt.close(fig)
theta=np.linspace(0,np.pi,500)
fig,ax=plt.subplots(figsize=(5.6,3.2),layout="constrained")
for ka,col in [(.5,"#64748b"),(1,"#2166ac"),(2,"#16857c")]:
    ax.plot(theta*180/np.pi,np.exp(-(2*ka*np.sin(theta/2))**2),label=f"ka={ka}",color=col)
ax.set(xlabel="Scattering angle [deg]",ylabel="Normalized cross section",ylim=(0,1.04))
ax.legend()
ax.grid(alpha=.2)
fig.savefig(out/"born_angles.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.4,3),layout="constrained")
delta=np.linspace(0,np.pi,400)
ax.plot(delta,np.sin(delta)**2,color="#2166ac")
ax.set(xlabel="Phase shift",ylabel="Cross section / (4π/k²)",xticks=[0,np.pi/2,np.pi],xticklabels=["0","π/2","π"])
ax.grid(alpha=.2)
fig.savefig(out/"partial_wave.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.6,3.2),layout="constrained")
de=np.linspace(-12,12,1800)
for T,col in [(1,"#2166ac"),(3,"#16857c")]:
    ax.plot(de,T*T*np.sinc(de*T/(2*np.pi))**2,label=f"T={T}",color=col)
ax.set(xlabel="Energy difference (hbar=1)",ylabel="Probability / |Vfi|²")
ax.legend()
ax.grid(alpha=.2)
fig.savefig(out/"transition_peak.png",dpi=220)
plt.close(fig)

# 第8章：回転と鏡映
fig,axs=plt.subplots(1,4,figsize=(6.4,2.1),layout="constrained")
for j,ax in enumerate(axs):
    ang=j*np.pi/2
    rot=np.array([[np.cos(ang),-np.sin(ang)],[np.sin(ang),np.cos(ang)]])
    sq=np.array([[-1,-1],[1,-1],[1,1],[-1,1]])
    ax.add_patch(Polygon(sq@rot.T,closed=True,fc="#2166ac",alpha=.15,ec="#2166ac"))
    ax.scatter(*(rot@np.array([1.,1.])),color="#d97706",s=55)
    ax.set(xlim=(-1.5,1.5),ylim=(-1.5,1.5),aspect="equal",title=f"r^{j}")
    ax.axis("off")
fig.savefig(out/"cyclic_rotations.png",dpi=220)
plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(5.5,3),layout="constrained")
for ax,dest,title in [(axs[0],(0,1),"RS"),(axs[1],(0,-1),"SR")]:
    ax.axhline(0,color="#94a3b8",lw=.8)
    ax.axvline(0,color="#94a3b8",lw=.8)
    ax.quiver(0,0,1,0,angles="xy",scale_units="xy",scale=1,color="#94a3b8")
    ax.quiver(0,0,*dest,angles="xy",scale_units="xy",scale=1,color="#2166ac")
    ax.set(xlim=(-1.3,1.3),ylim=(-1.3,1.3),aspect="equal",title=title,xlabel="x",ylabel="y")
fig.savefig(out/"noncommuting_symmetry.png",dpi=220)
plt.close(fig)
fig,axs=plt.subplots(2,2,figsize=(5.1,5.0),layout="constrained")
angle=np.linspace(0,2*np.pi,300)
colors=["#2166ac","#16857c","#d97706","#7c3aed"]
for k,ax in enumerate(axs.flat):
    ax.plot(np.cos(angle),np.sin(angle),color="#94a3b8",lw=.8)
    ax.axhline(0,color="#94a3b8",lw=.5)
    ax.axvline(0,color="#94a3b8",lw=.5)
    for j,col in enumerate(colors):
        z=np.exp(2j*np.pi*k*j/4)
        ax.scatter(z.real,z.imag,s=100-20*j,facecolors="none",edgecolors=col,lw=1.5,label=f"r^{j}")
    ax.set(xlim=(-1.3,1.3),ylim=(-1.3,1.3),aspect="equal",title=f"k={k}")
axs[0,0].legend(fontsize=7,loc="lower left")
fig.savefig(out/"cyclic_characters.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.5,3.2),layout="constrained")
j=np.arange(4)
ax.bar(j,2*np.cos(np.pi*j/2),color="#2166ac",label="2D rotation character")
ax.plot(j,2*np.real(np.exp(1j*np.pi*j/2)),"o",color="#d97706",label="k=1 plus k=3")
ax.axhline(0,color="#94a3b8",lw=.7)
ax.set(xticks=j,xticklabels=["e","r","r^2","r^3"],ylabel="Character",ylim=(-2.5,2.5))
ax.legend(fontsize=8)
fig.savefig(out/"character_decomposition.png",dpi=220)
plt.close(fig)

# 第9章：指数写像と回転の接線
fig,ax=plt.subplots(figsize=(4.8,3.4),layout="constrained")
angle=np.linspace(0,np.pi/2,200)
ax.plot(np.cos(angle),np.sin(angle),color="#2166ac",lw=2,label="Exact rotation")
ax.plot([1,1],[0,.65],"--",color="#d97706",label="Tangent")
for a0 in [0,.35,.7,np.pi/2]:
    ax.plot([0,np.cos(a0)],[0,np.sin(a0)],color="#94a3b8",lw=.8)
    ax.scatter(np.cos(a0),np.sin(a0),color="#2166ac",s=22)
ax.set(xlim=(-.1,1.25),ylim=(-.1,1.15),aspect="equal",xlabel="x",ylabel="y")
ax.legend(fontsize=8,loc="upper left")
fig.savefig(out/"lie_tangent.png",dpi=220)
plt.close(fig)
fig=plt.figure(figsize=(6,3.2),layout="constrained")
for i,(end,title) in enumerate([((0,0,-1),"Ry Rx"),((0,1,0),"Rx Ry")],1):
    ax=fig.add_subplot(1,2,i,projection="3d")
    ax.quiver(0,0,0,1,0,0,color="#94a3b8",arrow_length_ratio=.15)
    ax.quiver(0,0,0,*end,color="#2166ac",arrow_length_ratio=.15)
    ax.set(xlim=(-1,1),ylim=(-1,1),zlim=(-1,1),xlabel="x",ylabel="y",zlabel="z",title=title)
    ax.set_box_aspect((1,1,1))
fig.savefig(out/"lie_rotation_order.png",dpi=220)
plt.close(fig)
theta=np.linspace(0,4*np.pi,500)
fig,ax=plt.subplots(figsize=(5.6,3.2),layout="constrained")
ax.plot(theta/np.pi,np.cos(theta),label="Vector x component",color="#64748b",ls="--")
ax.plot(theta/np.pi,np.cos(theta/2),label="Spinor up amplitude",color="#2166ac")
ax.axhline(0,color="#94a3b8",lw=.7)
ax.set(xticks=[0,1,2,3,4],xticklabels=["0","π","2π","3π","4π"],xlabel="Rotation angle",ylabel="Component / amplitude")
ax.legend(fontsize=8)
fig.savefig(out/"spinor_period.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.6,3.2),layout="constrained")
theta=np.linspace(0,2*np.pi,300)
ax.plot(theta/np.pi,np.cos(theta/2)**2,color="#2166ac",label="P(up)")
ax.plot(theta/np.pi,np.sin(theta/2)**2,color="#16857c",label="P(down)")
ax.scatter([1/3,1/3],[.75,.25],color="#d97706")
ax.set(xticks=[0,.5,1,1.5,2],xticklabels=["0","π/2","π","3π/2","2π"],xlabel="Rotation angle",ylabel="Probability",ylim=(-.03,1.03))
ax.legend(fontsize=8)
ax.grid(alpha=.2)
fig.savefig(out/"spin_measurement.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.6,3.4),layout="constrained")
for x0,j in enumerate([0,.5,1,1.5]):
    ms=np.arange(-j,j+.1,1)
    for mm in ms:
        ax.plot([x0-.28,x0+.28],[mm,mm],lw=2,color="#2166ac")
        if mm<j:
            ax.annotate("",xy=(x0,mm+.93),xytext=(x0,mm+.07),arrowprops=dict(arrowstyle="->",color="#d97706",lw=1))
ax.set(xlim=(-.5,3.5),ylim=(-1.8,1.8),xticks=range(4),xticklabels=["j=0","j=1/2","j=1","j=3/2"],ylabel="m")
ax.grid(axis="y",alpha=.15)
fig.savefig(out/"spin_multiplets.png",dpi=220)
plt.close(fig)

# 第10章：連成振動子から連続体へ
fig,axs=plt.subplots(3,1,figsize=(5.8,4.1),layout="constrained")
for ax,n in zip(axs,[6,16,1000]):
    x=np.linspace(0,1,n)
    y=.3*np.sin(2*np.pi*x)
    ax.axhline(0,color="#94a3b8",lw=.7)
    ax.plot(x,y,color="#2166ac",lw=1.5)
    if n<1000:
        ax.scatter(x,y,color="#d97706",s=35 if n==6 else 17,zorder=3)
    ax.set(xlim=(-.03,1.03),ylim=(-.45,.45),yticks=[],xticks=[],ylabel=f"N={n}" if n<1000 else "Field")
    for spine in ax.spines.values():
        spine.set_visible(False)
fig.savefig(out/"field_chain.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.6,3.1),layout="constrained")
ka=np.linspace(0,np.pi,300)
ax.plot(ka,2*np.sin(ka/2),color="#2166ac",label="Discrete chain")
ax.plot(ka,ka,color="#d97706",ls="--",label="Continuum")
ax.set(xlabel="ka",ylabel="omega a / v",xticks=[0,np.pi/2,np.pi],xticklabels=["0","π/2","π"])
ax.legend(fontsize=8)
ax.grid(alpha=.2)
fig.savefig(out/"field_dispersion.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.6,3.3),layout="constrained")
x=np.linspace(0,1,300)
for n,col in [(1,"#2166ac"),(2,"#16857c"),(3,"#d97706")]:
    ax.plot(x,np.sin(n*np.pi*x),label=f"n={n}",color=col)
ax.scatter([0,1],[0,0],color="#64748b",zorder=4)
ax.axhline(0,color="#94a3b8",lw=.8)
ax.set(xlabel="x / length",ylabel="Normalized displacement")
ax.legend(fontsize=8)
ax.grid(alpha=.15)
fig.savefig(out/"field_modes.png",dpi=220)
plt.close(fig)
fig,axs=plt.subplots(2,1,figsize=(5.6,3.8),layout="constrained")
x=np.linspace(0,2,400)
rho=.02
tension=2.
amp=.01
wave_k=2*np.pi
omega=10*wave_k
axs[0].plot(x,amp*np.cos(wave_k*x),color="#2166ac")
axs[0].set(ylabel="u [m]")
energy=rho*(omega*amp*np.sin(wave_k*x))**2
axs[1].plot(x,energy,color="#d97706",label="Energy density")
axs[1].set(xlabel="x [m]",ylabel="Energy [J/m]")
ax2=axs[1].twinx()
ax2.plot(x,10*energy,color="#16857c",ls="--",label="Energy flux")
ax2.set_ylabel("Flux [W]")
axs[1].legend(fontsize=8,loc="upper left")
ax2.legend(fontsize=8,loc="upper right")
fig.savefig(out/"field_energy_flux.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.6,3.1),layout="constrained")
kk=np.linspace(0,5,300)
for mass,col in [(0,"#64748b"),(1,"#2166ac"),(2,"#16857c")]:
    ax.plot(kk,np.sqrt(kk**2+mass**2),color=col,label=f"m={mass}")
ax.set(xlabel="Wave number |k|",ylabel="Frequency omega (c=1)")
ax.grid(alpha=.2)
ax.legend(fontsize=8)
fig.savefig(out/"field_kg_dispersion.png",dpi=220)
plt.close(fig)
