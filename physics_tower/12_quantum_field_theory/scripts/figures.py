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

