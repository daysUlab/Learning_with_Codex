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

# 第3章：量化の順序と変数捕獲
fig,ax=plt.subplots(figsize=(4.6,3.6),layout="constrained")
ax.imshow([[1,0,0],[0,1,0],[0,0,1]],cmap=matplotlib.colors.ListedColormap(["#eef2f7","#2166ac"]),vmin=0,vmax=1)
ax.set_xticks(range(3),["0","1","2"])
ax.set_yticks(range(3),["0","1","2"])
ax.set_xlabel("y")
ax.set_ylabel("x")
for i in range(3):
    for j in range(3):
        ax.text(j,i,str(int(i==j)),ha="center",va="center",color="white" if i==j else "#334155",fontsize=13)
ax.set_title("R(x,y): x = y")
fig.savefig(out/"quantifier_matrix.png",dpi=220)
plt.close(fig)

fig,ax=plt.subplots(figsize=(5.5,3.2),layout="constrained")
ax.set(xlim=(0,10),ylim=(0,5))
ax.axis("off")
nodes=[(5,4.4,r"$\exists y\;(x\ne y)$","#e0eaf7"),(2.4,2.4,r"$\exists y\;(y\ne y)$","#fbe5df"),(7.5,2.8,r"$\exists z\;(x\ne z)$","#e2f2ed"),(7.5,.75,r"$\exists z\;(y\ne z)$","#e2f2ed")]
for x,y,lab,fc in nodes:
    ax.text(x,y,lab,ha="center",va="center",fontsize=12,bbox=dict(boxstyle="round,pad=.4",fc=fc,ec="#64748b"))
for i,j in [(0,1),(0,2),(2,3)]:
    x,y,_,_=nodes[i]; X,Y,_,_=nodes[j]
    ax.annotate("",xy=(X,Y+.35),xytext=(x,y-.35),arrowprops=dict(arrowstyle="->",color="#64748b"))
ax.text(2.4,3.35,"Direct replacement",ha="center",fontsize=9)
ax.text(2.4,1.65,"Captured y",ha="center",fontsize=9,color="#b45309")
ax.text(8,3.75,"Rename bound y",ha="center",fontsize=9)
ax.text(8.25,1.75,"Substitute y",ha="left",fontsize=9)
fig.savefig(out/"substitution_capture.png",dpi=220)
plt.close(fig)

# 第4章：Henkin構成
def diagram(nodes,edges,name,size=(5.4,3.0)):
    fig,ax=plt.subplots(figsize=size,layout="constrained")
    ax.set(xlim=(0,10),ylim=(0,6))
    ax.axis("off")
    for i,j in edges:
        x,y,_=nodes[i]; X,Y,_=nodes[j]
        ax.annotate("",xy=(X,Y),xytext=(x,y),arrowprops=dict(arrowstyle="->",color="#64748b",shrinkA=20,shrinkB=20))
    for x,y,label in nodes:
        ax.text(x,y,label,ha="center",va="center",fontsize=10,bbox=dict(boxstyle="round,pad=.45",fc="#e0eaf7",ec="#2166ac"))
    fig.savefig(out/name,dpi=220)
    plt.close(fig)
diagram([(2.4,4.5,r"$\exists x\,P(x)$"),(7.5,4.5,"Fresh name c"),(5,1.6,r"$\exists x\,P(x)\;\to\;P(c)$")],[(0,2),(1,2)],"henkin_witness.png")
diagram([(2,4.7,"L0, T0"),(5,4.7,"L1, T1"),(8,4.7,"L2, T2"),(5,1.4,"Union of all stages")],[(0,1),(1,2),(0,3),(1,3),(2,3)],"henkin_stages.png")
diagram([(1.4,4.7,"a"),(3.8,4.7,"f(b)"),(6.2,4.7,"b"),(8.6,4.7,"f(a)"),(2.6,1.5,"[a]"),(7.4,1.5,"[b]")],[(0,4),(1,4),(2,5),(3,5)],"term_model.png")
fig,ax=plt.subplots(figsize=(5.6,3.0),layout="constrained")
ax.set(xlim=(-.3,10.8),ylim=(0,4.3))
ax.axis("off")
for y,n,label in [(3.4,2,"h > 2"),(2.4,5,"h > 5"),(1.4,8,"h > 8")]:
    ax.hlines(y,0,10,color="#94a3b8")
    ax.plot(range(11),[y]*11,"|",color="#64748b")
    ax.hlines(y,n+.1,10,color="#16857c",lw=4)
    ax.scatter([n+1],[y],color="#2166ac",zorder=3)
    ax.text(0,y+.22,label,fontsize=9)
ax.text(5,.35,"Any finite list: choose a larger integer",ha="center",fontsize=10)
fig.savefig(out/"compactness_numbers.png",dpi=220)
plt.close(fig)

# 第5章
fig,ax=plt.subplots(figsize=(5.5,2.8),layout="constrained")
ax.set(xlim=(-6.6,6.6),ylim=(-.5,3.5));ax.axis("off")
colors=["#2166ac","#16857c","#d97706"]
for r in range(3):
    ax.text(-6.4,2.8-r,f"[{r}]",ha="left",va="center",color=colors[r])
    for n in range(-5,7):
        if n%3==r:
            ax.scatter(n,2.8-r,color=colors[r],s=180)
            ax.text(n,2.8-r,str(n),ha="center",va="center",fontsize=8,color="white")
fig.savefig(out/"modulo_classes.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(4.6,3.6),layout="constrained")
ax.set(xlim=(-.5,4.5),ylim=(-.5,4.5),aspect="equal",xlabel="m",ylabel="n")
ax.set_xticks(range(5));ax.set_yticks(range(5));ax.grid(alpha=.2)
for m,n in product(range(5),repeat=2):
    k=m+n;idx=k*(k+1)//2+m
    ax.scatter(m,n,color=colors[k%3],s=260,zorder=2)
    ax.text(m,n,str(idx),ha="center",va="center",color="white",fontsize=8)
for k in range(1,9):
    pts=[(m,k-m) for m in range(5) if 0<=k-m<5]
    if len(pts)>1:ax.plot(*zip(*pts),color=colors[k%3],alpha=.45)
fig.savefig(out/"countable_pairs.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(4.8,3.5),layout="constrained")
vals=[[0,1,0,1],[1,1,0,0],[0,0,1,0],[1,0,0,0]]
vals.append([1-vals[i][i] for i in range(4)])
ax.imshow(vals,cmap=matplotlib.colors.ListedColormap(["#eef2f7","#2166ac"]),aspect="auto",vmin=0,vmax=1)
ax.set_xticks(range(4),["0","1","2","3"]);ax.set_yticks(range(5),["row 0","row 1","row 2","row 3","new"])
for i,row in enumerate(vals):
    for j,v in enumerate(row):
        ax.text(j,i,str(v),ha="center",va="center",color="white" if v else "#334155")
        if i==j or i==4:ax.add_patch(Rectangle((j-.48,i-.48),.96,.96,fill=False,ec="#d97706",lw=2))
fig.savefig(out/"cantor_diagonal.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(5.4,2.6),layout="constrained")
ax.set(xlim=(0,10),ylim=(0,3));ax.axis("off")
for y,label in [(2,"omega"),(.8,"omega + 1")]:
    ax.text(.2,y+.35,label,fontsize=10)
    ax.hlines(y,.6,7.5,color="#94a3b8")
    for i in range(5):
        ax.scatter(1+i*1.1,y,color="#2166ac")
        ax.text(1+i*1.1,y-.25,str(i),ha="center",fontsize=9)
    ax.text(6.5,y,"...",va="center")
ax.scatter(8.8,.8,color="#d97706",s=70);ax.text(8.8,.48,"last",ha="center",fontsize=10)
fig.savefig(out/"ordinal_order.png",dpi=220);plt.close(fig)
diagram([(1.5,4.5,"V0: 0"),(3.8,4.5,"V1: 1"),(6.2,4.5,"V2: 2"),(8.5,4.5,"V3: 4"),(5,1.4,"V_omega: union of finite stages")],[(0,1),(1,2),(2,3),(0,4),(1,4),(2,4),(3,4)],"cumulative_hierarchy.png")
fig,ax=plt.subplots(figsize=(5.5,2.6),layout="constrained")
ax.set(xlim=(0.8,2.05),ylim=(0,2.8));ax.axis("off")
from math import sqrt
r=sqrt(2)
ax.hlines(1.25,.85,r,color="#2166ac",lw=4)
ax.hlines(1.25,r,2,color="#d97706",lw=4)
for q in [1,1.25,1.4,1.5,1.75,2]:
    ax.scatter(q,1.25,color="#2166ac" if q<r else "#d97706",zorder=3)
    ax.text(q,1.02,str(q),ha="center",fontsize=8)
ax.axvline(r,ymin=.45,ymax=.72,color="#64748b",ls="--")
ax.text(r,2.12,r"$\sqrt{2}$",ha="center",fontsize=12)
ax.text(1.1,.45,"Lower cut",ha="center",fontsize=10,color="#2166ac")
ax.text(1.77,.45,"Complement",ha="center",fontsize=10,color="#d97706")
fig.savefig(out/"dedekind_cut.png",dpi=220);plt.close(fig)

# 第6章：公理とモデル
diagram([(2.5,4.5,"All sets"),(7.5,4.5,"Existing set A"),(2.5,2.5,"Unrestricted collection"),(7.5,2.5,"Select within A"),(2.5,.65,"Contradiction"),(7.5,.65,"Subset of A")],[(0,2),(1,3),(2,4),(3,5)],"russell_separation.png")
fig,ax=plt.subplots(figsize=(5.4,2.8),layout="constrained")
ax.set(xlim=(0,10),ylim=(0,4));ax.axis("off")
for i,x in enumerate([1.2,2.5,3.8]):
    ax.scatter(x,3,color="#2166ac",s=250)
    ax.text(x,3,str(i+1),ha="center",va="center",color="white")
ax.text(2.5,3.65,"Input A",ha="center")
for i,x in enumerate([1.2,2.5,3.8]):
    ax.annotate("",xy=(6.5+i*1.25,1.15),xytext=(x,2.7),arrowprops=dict(arrowstyle="->",color="#16857c"))
    ax.scatter(6.5+i*1.25,1,color="#16857c",s=250)
    ax.text(6.5+i*1.25,1,str((i+1)**2),ha="center",va="center",color="white")
ax.scatter(2.5,1,color="#2166ac",s=250);ax.text(2.5,1,"2",ha="center",va="center",color="white")
ax.annotate("",xy=(2.5,1.3),xytext=(2.5,2.7),arrowprops=dict(arrowstyle="->",color="#2166ac",lw=2))
ax.text(2.5,.35,"Separation",ha="center");ax.text(7.75,.35,"Replacement",ha="center")
fig.savefig(out/"separation_replacement.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(4.8,2.6),layout="constrained")
ax.set(xlim=(0,10),ylim=(0,4));ax.axis("off")
for x in [2.5,7.5]:
    ax.plot([5,x],[1,3],color="#94a3b8")
for x,y,lab in [(5,1,"{a}"),(2.5,3,"{a,b}"),(7.5,3,"{a,c}")]:
    ax.text(x,y,lab,ha="center",va="center",bbox=dict(boxstyle="round,pad=.4",fc="#e2f2ed" if y==3 else "#eef2f7",ec="#16857c"))
ax.text(5,3.75,"Two maximal elements; no greatest element",ha="center",fontsize=10)
fig.savefig(out/"maximal_elements.png",dpi=220);plt.close(fig)
diagram([(5,4.7,"ZFC"),(2.5,2.3,"Model: CH"),(7.5,2.3,"Model: not CH"),(5,.55,"Same axioms, different truth")],[(0,1),(0,2),(1,3),(2,3)],"independence_models.png")
