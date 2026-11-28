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

# 第7章：フィルターと超フィルター
fig,ax=plt.subplots(figsize=(5.4,2.6),layout="constrained")
ax.set(xlim=(0,6),ylim=(0,4));ax.axis("off")
for y,label,selected in [(3.1,"A",{1,2,3}),(2.1,"B",{3,4,5}),(1.1,"A and B",{3})]:
    ax.text(.55,y,label,ha="right",va="center",fontsize=10)
    for i in range(1,6):
        ax.scatter(i,y,s=240,color="#2166ac" if i in selected else "#e2e8f0")
        ax.text(i,y,str(i),ha="center",va="center",color="white" if i in selected else "#334155")
ax.text(3,.25,"3/5 and 3/5, but intersection = 1/5",ha="center",fontsize=10)
fig.savefig(out/"filter_majority.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(5.2,3.2),layout="constrained")
ax.set(xlim=(-.5,6.5),ylim=(-.5,3.5));ax.axis("off")
nodes={0:(3,0),1:(1,1),2:(3,1),4:(5,1),3:(1,2),5:(3,2),6:(5,2),7:(3,3)}
for a,(x,y) in nodes.items():
    for b,(X,Y) in nodes.items():
        if a&b==a and (a^b).bit_count()==1:
            ax.plot([x,X],[y,Y],color="#16857c" if a&3==3 and b&3==3 else "#cbd5e1")
for a,(x,y) in nodes.items():
    lab="{"+",".join(str(i+1) for i in range(3) if a&(1<<i))+"}" if a else "empty"
    ax.text(x,y,lab,ha="center",va="center",bbox=dict(boxstyle="round,pad=.3",fc="#ccece3" if a&3==3 else "#f1f5f9",ec="#16857c" if a&3==3 else "#94a3b8"))
fig.savefig(out/"principal_filters.png",dpi=220);plt.close(fig)
diagram([(1.3,4.7,"F0"),(3.7,4.7,"F1"),(6.3,4.7,"F2"),(8.7,4.7,"..."),(5,1.4,"Union: upper bound")],[(0,1),(1,2),(2,3),(0,4),(1,4),(2,4),(3,4)],"filter_chain.png")
diagram([(5,4.9,"Cofinite filter"),(2.5,3,"Add even numbers"),(7.5,3,"Add odd numbers"),(2.5,1,"Free ultrafilter U_E"),(7.5,1,"Free ultrafilter U_O")],[(0,1),(0,2),(1,3),(2,4)],"free_filter_choices.png")
fig,ax=plt.subplots(figsize=(5.3,2.9),layout="constrained")
ns=list(range(12))
ax.axhline(1,color="#2166ac",alpha=.4);ax.axhline(-1,color="#d97706",alpha=.4)
ax.scatter(ns[::2],[1]*6,color="#2166ac",label="Even indices")
ax.scatter(ns[1::2],[-1]*6,color="#d97706",label="Odd indices")
ax.set(xlabel="n",ylabel="a_n",xticks=ns,yticks=[-1,0,1],ylim=(-1.5,1.5))
ax.legend(loc="center",fontsize=9,ncol=2);ax.grid(alpha=.15)
fig.savefig(out/"filter_sequence.png",dpi=220);plt.close(fig)

# 第8章：超積・超冪・証人列
fig,ax=plt.subplots(figsize=(5.4,3),layout="constrained")
ns=list(range(10))
ax.plot(ns,[1/(n+1) for n in ns],"o-",color="#2166ac",label=r"$1/(n+1)$")
ax.axhline(0,color="#d97706",ls="--",label="zero sequence")
ax.set(xlabel="Index n",ylabel="Value",xticks=ns,ylim=(-.08,1.1))
ax.legend(fontsize=9);ax.grid(alpha=.2)
fig.savefig(out/"ultrapower_sequences.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(5.4,2.9),layout="constrained")
ax.set(xlim=(-1,6),ylim=(-.4,3.5));ax.axis("off")
for y,lab,row in [(2.7,"a = a'",[1,1,0,1,0,1]),(1.7,"b = b'",[0,1,1,1,0,1]),(.7,"Both",[0,1,0,1,0,1])]:
    ax.text(-.15,y,lab,ha="right",va="center",fontsize=10)
    for j,v in enumerate(row):
        ax.scatter(j+.5,y,s=250,color="#2166ac" if v else "#e2e8f0")
        ax.text(j+.5,y,str(v),ha="center",va="center",color="white" if v else "#334155")
ax.text(3,-.05,"Where both agree, the sums agree",ha="center",fontsize=10)
fig.savefig(out/"ultraproduct_representatives.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(5.4,3),layout="constrained")
ax.set(xlim=(0,7),ylim=(0,4));ax.axis("off")
for j in range(5):
    x=1.1+j*1.2
    ax.text(x,3.25,f"M{j}",ha="center",bbox=dict(boxstyle="round",fc="#e0eaf7",ec="#2166ac"))
    ax.annotate("",xy=(x,2.1),xytext=(x,2.9),arrowprops=dict(arrowstyle="->",color="#64748b"))
    ax.text(x,1.8,f"b{j}",ha="center",color="#16857c")
    ax.annotate("",xy=(3.5,.8),xytext=(x,1.5),arrowprops=dict(arrowstyle="->",color="#16857c",alpha=.65))
ax.text(3.5,.45,"Witness class [b]",ha="center",bbox=dict(boxstyle="round",fc="#e2f2ed",ec="#16857c"))
fig.savefig(out/"los_witnesses.png",dpi=220);plt.close(fig)

# 第9章：超実数の模式図と収束速度
fig,ax=plt.subplots(figsize=(5.5,3.1),layout="constrained")
ax.set(xlim=(0,10),ylim=(0,4));ax.axis("off")
ax.hlines(2.9,1,9,color="#64748b",lw=1.5)
for x,lab in [(2,"0"),(5,"1"),(8,"2")]:
    ax.scatter(x,2.9,color="#2166ac",s=40)
    ax.text(x,3.2,lab,ha="center")
ax.annotate("",xy=(2,1.3),xytext=(2,2.7),arrowprops=dict(arrowstyle="->",color="#16857c"))
ax.hlines(1,1,9,color="#64748b",lw=1.5)
for x,lab in [(2,"0"),(3,r"$\varepsilon^2$"),(4.6,r"$\varepsilon$"),(7,r"$\sqrt{\varepsilon}$")]:
    ax.scatter(x,1,color="#16857c",s=55)
    ax.text(x,.65,lab,ha="center")
ax.text(5,1.65,"Near 0 (schematic, not to scale)",ha="center",fontsize=10)
fig.savefig(out/"hyperreal_zoom.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(5.4,3.2),layout="constrained")
ns=range(1,101)
for power,color in [(0.5,"#d97706"),(1,"#2166ac"),(2,"#16857c")]:
    ax.loglog(ns,[n**(-power) for n in ns],label=f"m^(-{power:g})",color=color)
ax.set(xlabel="m = n + 1",ylabel="Value");ax.legend(fontsize=9);ax.grid(alpha=.2,which="both")
fig.savefig(out/"hyperreal_rates.png",dpi=220);plt.close(fig)
diagram([(5,4.6,"0.9, 0.99, 0.999, ..."),(2.4,2.6,"Real limit"),(7.6,2.6,"Ultrapower class"),(2.4,.8,"1"),(7.6,.8,"1 - eta, less than 1")],[(0,1),(0,2),(1,3),(2,4)],"hyperreal_decimal.png")

# 第10章：標準部の模式図
fig,ax=plt.subplots(figsize=(5.4,2.6),layout="constrained")
ax.set(xlim=(0,10),ylim=(0,3.3));ax.axis("off")
ax.hlines(2.2,1,9,color="#64748b")
for x,lab in [(2,r"$3-\varepsilon^2$"),(5,"3"),(8,r"$3+\varepsilon$")]:
    ax.scatter(x,2.2,color="#16857c",s=50)
    ax.text(x,2.55,lab,ha="center",fontsize=11)
    ax.annotate("",xy=(5,.8),xytext=(x,1.95),arrowprops=dict(arrowstyle="->",color="#2166ac"))
ax.text(5,.48,"standard part = 3",ha="center",fontsize=11)
fig.savefig(out/"standard_part_neighbors.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(5.4,2.8),layout="constrained")
ax.set(xlim=(0,10),ylim=(0,4));ax.axis("off")
for y,closed,lab in [(2.8,False,r"$x=3-\varepsilon$"),(1.3,True,r"$x=3+\varepsilon$")]:
    ax.hlines(y,1,7,color="#2166ac",lw=3)
    ax.scatter(7,y,s=65,facecolor="#2166ac" if closed else "white",edgecolor="#2166ac",zorder=3)
    ax.text(7,y+.32,"3",ha="center")
    ax.text(3,y+.35,lab,ha="center")
    ax.text(8.2,y,"sup = 3",ha="center",fontsize=10)
fig.savefig(out/"standard_part_cuts.png",dpi=220);plt.close(fig)
fig,axs=plt.subplots(2,1,figsize=(5.4,4),layout="constrained")
ns=list(range(12))
axs[0].plot(ns,[2+(-1)**n/(n+1) for n in ns],"o-",color="#2166ac")
axs[0].axhline(2,color="#16857c",ls="--")
axs[0].set(ylabel="Converges to 2")
axs[1].scatter(ns,[(-1)**n for n in ns],c=["#2166ac" if n%2==0 else "#d97706" for n in ns])
axs[1].set(xlabel="Index n",ylabel="Two choices",yticks=[-1,1],ylim=(-1.5,1.5))
fig.savefig(out/"standard_part_limits.png",dpi=220);plt.close(fig)

# 第11章：割線と接線、絶対値、単位円
import math
fig,ax=plt.subplots(figsize=(5.4,3.5),layout="constrained")
xs=[2.3+i/100 for i in range(126)]
ax.plot(xs,[x*x for x in xs],color="#2166ac",lw=2,label="f(x) = x^2")
a=3
for h,col in [(0.5,"#d97706"),(.15,"#16857c")]:
    ax.plot([2.3,3.5],[a*a+(2*a+h)*(x-a) for x in [2.3,3.5]],color=col,label=f"h = {h}")
    ax.scatter([a,a+h],[a*a,(a+h)**2],color=col)
ax.plot([2.3,3.5],[a*a+2*a*(x-a) for x in [2.3,3.5]],"--",color="#64748b",label="Tangent")
ax.set(xlabel="x",ylabel="f(x)",xlim=(2.3,3.55),ylim=(4,13));ax.legend(fontsize=8)
fig.savefig(out/"derivative_secants.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(5.4,3),layout="constrained")
ax.plot([-2,0,2],[2,0,2],color="#2166ac",lw=2)
ax.scatter([-1,0,1],[1,0,1],color="#16857c")
ax.text(-1,1.25,"slope = -1",ha="center");ax.text(1,1.25,"slope = 1",ha="center")
ax.set(xlabel="x",ylabel="|x|",xlim=(-2.2,2.2),ylim=(-.1,2.3));ax.grid(alpha=.2)
fig.savefig(out/"derivative_absolute.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(5,3.7),layout="constrained")
theta=.55
arc=[theta*i/100 for i in range(101)]
ax.fill([0]+[math.cos(t) for t in arc]+[0],[0]+[math.sin(t) for t in arc]+[0],color="#e0eaf7")
ax.plot([0,1,1,0],[0,0,math.tan(theta),0],color="#d97706")
ax.plot([0,1,math.cos(theta),0],[0,0,math.sin(theta),0],color="#16857c",lw=2)
ax.plot([math.cos(t) for t in arc],[math.sin(t) for t in arc],color="#2166ac",lw=2)
ax.text(.21,.065,"t",fontsize=12);ax.text(1.03,.02,"A");ax.text(.79,.54,"B");ax.text(1.03,math.tan(theta),"C");ax.text(-.06,-.05,"O")
ax.set(xlim=(-.12,1.23),ylim=(-.12,.82),aspect="equal");ax.axis("off")
fig.savefig(out/"derivative_trig.png",dpi=220);plt.close(fig)

# 第12章：有限分割・超有限区間・標識点の選択
fig,axs=plt.subplots(1,2,figsize=(5.5,2.8),layout="constrained")
for ax,m in zip(axs,[4,16]):
    xs=[k/m for k in range(m)]
    ax.bar(xs,[(x+1/m)**2 for x in xs],width=1/m,align="edge",color="#b4ddd5",edgecolor="#16857c",linewidth=.6)
    curve=[j/100 for j in range(101)]
    ax.plot(curve,[x*x for x in curve],color="#2166ac",lw=2)
    ax.set(xlim=(0,1.02),ylim=(0,1.05),title=f"m = {m}",xlabel="x")
axs[0].set_ylabel("f(x)")
fig.savefig(out/"integral_rectangles.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(5.5,2.2),layout="constrained")
ax.set(xlim=(0,10),ylim=(0,3));ax.axis("off")
ax.hlines(1.5,.6,9.4,color="#64748b")
for x,lab in [(1,"1"),(2,"2"),(3,"3"),(7,"H-2"),(8,"H-1"),(9,"H")]:
    ax.scatter(x,1.5,color="#16857c",s=45);ax.text(x,1.1,lab,ha="center")
ax.text(5,1.5,"...",ha="center",va="center",fontsize=16)
ax.text(2,2.05,"standard indices",ha="center");ax.text(8,2.05,"nonstandard indices",ha="center")
fig.savefig(out/"integral_hyperfinite.png",dpi=220);plt.close(fig)
fig,axs=plt.subplots(2,1,figsize=(5.4,3.3),layout="constrained")
for ax,v,label in [(axs[0],1,"Rational tags: sum = 1"),(axs[1],0,"Irrational tags: sum = 0")]:
    m=8
    for j in range(m):
        ax.axvline(j/m,color="#94a3b8",lw=.7)
        ax.scatter([(j+.45)/m],[v],color="#2166ac",s=20)
    ax.axvline(1,color="#94a3b8",lw=.7)
    ax.set(xlim=(0,1),ylim=(-.15,1.15),yticks=[0,1],title=label)
fig.savefig(out/"integral_tags.png",dpi=220);plt.close(fig)

# 第13章：四元代数、上界、正則開集合、円筒
diagram([(5,4.5,"{A, B}"),(2.5,2.6,"{A}"),(7.5,2.6,"{B}"),(5,.8,"empty")],[(3,1),(3,2),(1,0),(2,0)],"complete_boolean_four.png")
fig,ax=plt.subplots(figsize=(5.5,2.7),layout="constrained")
ax.set(xlim=(-.5,11.6),ylim=(-.5,3.2));ax.axis("off")
for y,excluded,label in [(2.1,{1},"Upper bound"),(.8,{1,5},"Smaller upper bound")]:
    for k in range(11):
        ax.scatter(k,y,s=44,facecolor="white" if k in excluded else "#16857c" if k%2==0 else "#94a3b8",edgecolor="#64748b")
        if y==.8:ax.text(k,y-.35,str(k),ha="center",fontsize=8)
    ax.text(0,y+.32,label,ha="left",fontsize=10)
    ax.text(11,y,"...",ha="center")
fig.savefig(out/"complete_boolean_missing.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(5.5,2.9),layout="constrained")
ax.set(xlim=(-.15,1.15),ylim=(0,3.5));ax.axis("off")
for y,label in [(2.7,"Open set with a gap"),(1.7,"Closure"),(.7,"Interior of closure")]:
    ax.hlines(y,0,1,color="#2166ac",lw=3)
    ax.scatter([0,1],[y,y],s=48,facecolor="#2166ac" if y==1.7 else "white",edgecolor="#2166ac",zorder=3)
    if y==2.7:ax.scatter(.5,y,s=52,facecolor="white",edgecolor="#2166ac",zorder=3)
    ax.text(.5,y+.26,label,ha="center",fontsize=10)
fig.savefig(out/"regular_open_gap.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(5.5,3.8),layout="constrained")
ax.set(xlim=(-.4,8.4),ylim=(-.4,3.6));ax.axis("off")
for level in range(4):
    for i,bits in enumerate(product("01",repeat=level)):
        x=(i+.5)*8/(2**level)
        y=3-level
        if level:
            xp=(i//2+.5)*8/(2**(level-1))
            ax.plot([xp,x],[y+1,y],color="#94a3b8",lw=1)
        ax.text(x,y,"["+"".join(bits)+"]" if level else "X",ha="center",va="center",fontsize=9,bbox=dict(boxstyle="round,pad=.22",fc="#e0eaf7",ec="#2166ac"),zorder=3)
fig.savefig(out/"cantor_cylinders.png",dpi=220);plt.close(fig)

# 第14章：二つの状況、名前の階層、混合
fig,ax=plt.subplots(figsize=(5.5,3.2),layout="constrained")
ax.set(xlim=(0,10),ylim=(0,6));ax.axis("off")
for x,label,values,col in [(2.5,"A",[1,2],"#2166ac"),(7.5,"B",[2,3],"#16857c")]:
    ax.add_patch(plt.Rectangle((x-1.65,2.1),3.3,3,fc=col,alpha=.10,ec=col,lw=1.4))
    ax.text(x,4.65,"Situation "+label,ha="center",fontsize=11)
    for j,k in enumerate(values):
        ax.text(x,3.85-j*.9,str(k),ha="center",fontsize=15,color=col)
ax.text(5,1.4,"1: p       2: 1       3: q",ha="center",fontsize=11)
ax.text(5,.65,"Boolean membership values",ha="center",fontsize=10)
fig.savefig(out/"bname_membership.png",dpi=220);plt.close(fig)
diagram([(5,4.8,"u"),(2,2.7,"check 1"),(5,2.7,"check 2"),(8,2.7,"check 3"),(5,.7,"Lower-rank names")],[(0,1),(0,2),(0,3),(1,4),(2,4),(3,4)],"bname_hierarchy.png")
fig,ax=plt.subplots(figsize=(5.5,3.2),layout="constrained")
ax.set(xlim=(0,10),ylim=(0,5));ax.axis("off")
for x,lab,col in [(2.5,"p: {1, 2}","#2166ac"),(7.5,"q: {2, 3}","#16857c")]:
    ax.text(x,4.1,lab,ha="center",fontsize=12,bbox=dict(boxstyle="round,pad=.4",fc=col,alpha=.15,ec=col))
    ax.annotate("",xy=(5,2.3),xytext=(x,3.65),arrowprops=dict(arrowstyle="->",color=col,lw=1.8))
ax.text(5,1.8,"Mixed name u",ha="center",fontsize=12)
ax.text(5,1,"1: p    2: 1    3: q",ha="center",fontsize=12,bbox=dict(boxstyle="round,pad=.5",fc="#e0eaf7",ec="#2166ac"))
fig.savefig(out/"bname_mixing.png",dpi=220);plt.close(fig)

# 第15章：成分別演算、有理切断、移行の流れ
fig,ax=plt.subplots(figsize=(5.5,3.2),layout="constrained")
for i,(lab,vals) in enumerate([("x",(2,5)),("y",(3,1)),("x+y",(5,6)),("xy",(6,5))]):
    ax.bar(i-.18,vals[0],width=.33,color="#2166ac",label="A" if i==0 else None)
    ax.bar(i+.18,vals[1],width=.33,color="#16857c",label="B" if i==0 else None)
ax.set_xticks(range(4),["x","y","x+y","xy"]);ax.set_ylabel("Value");ax.legend()
fig.savefig(out/"bva_vectors.png",dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(5.5,3.1),layout="constrained")
xx=[j/100 for j in range(101)]
ax.plot(xx,xx,color="#2166ac",label="f(t) = t")
ax.axhline(.5,color="#64748b",ls="--",label="r = 1/2")
ax.axvspan(.5,1,color="#16857c",alpha=.2,label="Boolean value: r < f")
ax.set(xlabel="t",ylabel="f(t)",xlim=(0,1),ylim=(0,1));ax.legend(fontsize=8)
fig.savefig(out/"bva_cuts.png",dpi=220);plt.close(fig)
diagram([(5,4.6,"Complex polynomial"),(5,3.3,"Root in V^B"),(2.5,1.1,"Measurable root"),(7.5,1.1,"Continuous root on K")],[(0,1),(1,2),(1,3)],"bva_transfer.png")

# 冒頭：三つの数学的な世界と具体例
diagram([(5,4.65,"Mathematical logic"),(1.7,2.7,"Number system"),(5,2.7,"Truth values"),(8.3,2.7,"Set universe"),(1.7,.8,"Infinitesimals"),(5,.8,"Transfer theorems"),(8.3,.8,"Independence")],[(0,1),(0,2),(0,3),(1,4),(2,5),(3,6)],"intro_three_worlds.png")
fig,axs=plt.subplots(1,2,figsize=(5.5,2.8),layout="constrained")
for ax,m,lab in [(axs[0],4,"Finite grid"),(axs[1],32,"Hyperfinite idea")]:
    xx=[k/m for k in range(m)]
    ax.bar(xx,[(x+1/m)**2 for x in xx],width=1/m,align="edge",color="#b4ddd5",edgecolor="#16857c",linewidth=.5)
    xx=[k/100 for k in range(101)]
    ax.plot(xx,[x*x for x in xx],color="#2166ac",lw=1.8)
    ax.set(xlim=(0,1.02),ylim=(0,1.05),title=lab,xlabel="x")
axs[0].set_ylabel("x squared")
fig.savefig(out/"intro_hyperfinite.png",dpi=220);plt.close(fig)
diagram([(5,4.6,"Complex polynomial has a root"),(5,3.1,"Boolean-valued universe"),(2.5,1.1,"Measurable root"),(7.5,1.1,"Continuous root on K")],[(0,1),(1,2),(1,3)],"intro_transfer.png")
diagram([(5,4.6,"ZFC (if consistent)"),(2.5,2.6,"ZFC + CH"),(7.5,2.6,"ZFC + not CH"),(2.5,.8,"Constructible universe"),(7.5,.8,"Forcing extension")],[(0,1),(0,2),(1,3),(2,4)],"intro_forcing.png")
# 第16章：条件の増加・稠密条件列・新しい列
fig,ax=plt.subplots(figsize=(5.5,2.8),layout="constrained")
ax.set(xlim=(-1.2,5.4),ylim=(0,3.6));ax.axis("off")
for i,(label,vals) in enumerate([("p",[1,None,0,None,None]),("q",[1,1,0,None,None]),("r",[1,1,0,1,None])]):
    y=2.7-i
    ax.text(-.6,y+.3,label,ha="center",fontsize=12)
    for k,v in enumerate(vals):
        ax.add_patch(Rectangle((k,y),.78,.6,fc="#e0eaf7" if v is not None else "#f1f5f9",ec="#64748b"))
        ax.text(k+.39,y+.3,"?" if v is None else str(v),ha="center",va="center",fontsize=11)
ax.text(2,.2,"Stronger = more information",ha="center",fontsize=10)
fig.savefig(out/"forcing_conditions.png",dpi=220);plt.close(fig)
diagram([(1.1,4.6,"p0"),(3.7,3.4,"p1 in D0"),(6.3,2.2,"p2 in D1"),(8.8,1,"p3 in D2")],[(0,1),(1,2),(2,3)],"forcing_dense_chain.png")
fig,ax=plt.subplots(figsize=(5.5,3),layout="constrained")
ax.set(xlim=(-1.8,6.6),ylim=(0,4.8));ax.axis("off")
rows=[("a0","000000"),("a1","111111"),("a2","010101"),("r","1010??")]
for i,(lab,word) in enumerate(rows):
    y=3.8-i
    ax.text(-.6,y+.32,lab,ha="center",fontsize=11)
    for k,v in enumerate(word):
        marked=(i<3 and k==i) or (i==3 and k<3)
        ax.add_patch(Rectangle((k,y),.78,.65,fc="#b4ddd5" if marked else "#f1f5f9",ec="#64748b"))
        ax.text(k+.39,y+.32,v,ha="center",va="center",fontsize=10)
ax.text(2.5,.23,"Different at a specified coordinate",ha="center",fontsize=10)
fig.savefig(out/"forcing_new_real.png",dpi=220);plt.close(fig)
