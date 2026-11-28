from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parents[1]/"figures"
out.mkdir(exist_ok=True)
fig,ax=plt.subplots(figsize=(5.5,2.5),layout="constrained")
ax.set(xlim=(0,10),ylim=(0,4))
ax.axis("off")
for x,lab in [(2,"Formal proof"),(8,"Semantic truth")]:
    ax.text(x,2,lab,ha="center",va="center",fontsize=12,
            bbox=dict(boxstyle="round,pad=.5",facecolor="#e0eaf7",edgecolor="#2166ac"))
ax.annotate("",xy=(6.65,2.65),xytext=(3.35,2.65),arrowprops=dict(arrowstyle="->",color="#2166ac",lw=2))
ax.text(5,2.9,"Soundness",ha="center",fontsize=10)
ax.annotate("",xy=(3.35,1.35),xytext=(6.65,1.35),arrowprops=dict(arrowstyle="->",color="#16857c",lw=2))
ax.text(5,1.0,"Completeness",ha="center",fontsize=10)
fig.savefig(out/"proof_truth.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.5,3.8),layout="constrained")
ax.axis("off")
ax.set(xlim=(0,8),ylim=(0,4))
nodes=[(1,3.3,"P,Q"),(3,3.3,"P, not Q"),(5,3.3,"not P,Q"),(7,3.3,"not P,not Q"),(2,2,"P"),(6,2,"not P"),(4,.65,"No extra assumption")]
for i,j in [(0,4),(1,4),(2,5),(3,5),(4,6),(5,6)]:
    x,y,_=nodes[i]; X,Y,_=nodes[j]
    ax.annotate("",xy=(X,Y+.24),xytext=(x,y-.24),arrowprops=dict(arrowstyle="->",color="#64748b"))
for x,y,label in nodes:
    ax.text(x,y,label+"\nprove A",ha="center",va="center",fontsize=9,bbox=dict(boxstyle="round,pad=.25",fc="#e2f2ed",ec="#16857c"))
fig.savefig(out/"case_merge.png",dpi=220)
plt.close(fig)

# 第2章：集合としての真理値
from matplotlib.patches import Rectangle
from itertools import product
fig,ax=plt.subplots(figsize=(5.4,3.2),layout="constrained")
ax.set(xlim=(-1.8,3),ylim=(0,6.8))
ax.axis("off")
for j,lab in enumerate(["a","b","c"]):
    ax.text(j+.5,6.5,lab,ha="center",fontsize=11)
for i,(lab,vals) in enumerate([("P",[1,1,0]),("Q",[0,1,1]),("P and Q",[0,1,0]),("P or Q",[1,1,1]),("not P",[0,0,1]),("P implies Q",[0,1,1])]):
    y=5.5-i
    ax.text(-.12,y+.36,lab,ha="right",va="center",fontsize=10)
    for j,v in enumerate(vals):
        ax.add_patch(Rectangle((j+.12,y),.76,.72,facecolor="#2166ac" if v else "#eef2f7",edgecolor="#64748b"))
        ax.text(j+.5,y+.36,str(v),ha="center",va="center",color="white" if v else "#334155")
fig.savefig(out/"boolean_events.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(5.4,3.5),layout="constrained")
ax.axis("off")
ax.set(xlim=(-.5,6.5),ylim=(-.45,3.5))
nodes={0:(3,0),1:(1,1),2:(3,1),4:(5,1),3:(1,2),5:(3,2),6:(5,2),7:(3,3)}
for a,(x,y) in nodes.items():
    for b,(X,Y) in nodes.items():
        if a&b==a and (b^a).bit_count()==1:
            ax.plot([x,X],[y,Y],color="#94a3b8",zorder=0)
for a,(x,y) in nodes.items():
    lab="{"+",".join(c for i,c in enumerate("abc") if a&(1<<i))+"}" if a else "empty"
    ax.text(x,y,lab,ha="center",va="center",fontsize=10,bbox=dict(boxstyle="round,pad=.3",fc="#e2f2ed" if a in (1,2,4) else "#eef2f7",ec="#16857c" if a in (1,2,4) else "#64748b"))
fig.savefig(out/"boolean_lattice.png",dpi=220)
plt.close(fig)
fig,ax=plt.subplots(figsize=(4.1,5),layout="constrained")
vals=list(product([0,1],repeat=4))
ax.imshow(vals,cmap=matplotlib.colors.ListedColormap(["#eef2f7","#2166ac"]),aspect="auto",vmin=0,vmax=1)
ax.set_xticks(range(4),["00","01","10","11"])
ax.xaxis.tick_top()
ax.set_yticks(range(16),[str(i) for i in range(16)])
ax.set_ylabel("Truth function")
for i,row in enumerate(vals):
    for j,v in enumerate(row):
        ax.text(j,i,str(v),ha="center",va="center",fontsize=9,color="white" if v else "#334155")
fig.savefig(out/"boolean_functions.png",dpi=220)
plt.close(fig)
