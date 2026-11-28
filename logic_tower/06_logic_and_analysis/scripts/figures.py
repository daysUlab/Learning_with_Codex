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
