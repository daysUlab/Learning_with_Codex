# 水素原子――Coulomb potential・量子数・spectra

## 中心問題

固定したprotonを原点に置く近似では

$$
\hat H=-\frac{\hbar^2}{2\mu}\nabla^2
-\frac{e^2}{4\pi\varepsilon_0r}
$$

です。

$$
\mu=\frac{m_em_p}{m_e+m_p}
$$

はreduced massです。球対称性により

$$
\psi_{nlm}(r,\theta,\varphi)=R_{nl}(r)Y_l^m(\theta,\varphi)
$$

と変数分離し、

$$
E_n=-\frac{\mu e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac1{n^2}
\simeq-\frac{13.6\ \mathrm{eV}}{n^2}
$$

を得ます。

| 量子数 | 値 | 主な意味 |
|---|---|---|
| $$n$$ | $$1,2,\ldots$$ | energy・size |
| $$l$$ | $$0,\ldots,n-1$$ | 軌道角運動量 |
| $$m$$ | $$-l,\ldots,l$$ | 選んだ軸の成分 |
| spin | $$\pm1/2$$ | 内部自由度 |

同じ

$$
n
$$

の縮退はCoulomb potentialの高い対称性によります。spin、相対論、Lamb shift、外場で細かく分裂します。

electric dipole遷移の入口では

$$
\Delta l=\pm1,\qquad\Delta m=0,\pm1
$$

がselection ruleです。energy差だけでなく遷移matrix elementが強度を決めます。

## 演習と全解答

1.
   $$
   n=3
   $$
   のenergyを求めよ。
   **解答**：
   $$
   E_3=-13.6/9\simeq-1.51\ \mathrm{eV}
   $$
2.
   $$
   n=2
   $$
   で可能な
   $$
   l
   $$
   は何か。
   **解答**：
   $$
   0,1
   $$
3.
   $$
   l=1
   $$
   の
   $$
   m
   $$
   を列挙せよ。
   **解答**：
   $$
   -1,0,1
   $$
4. 1s orbitalに古典的軌道半径が一つあるか。
   **解答**：ありません。位置はradial確率分布で予測します。
5.
   $$
   2s\to1s
   $$
   がelectric dipole selection ruleで許されるか。
   **解答**：
   $$
   \Delta l=0
   $$
   なので単一photon E1遷移としては禁止です。
6. Bohr模型とSchrödinger解のenergyが一致しても同じmodelでない理由を述べよ。
   **解答**：Bohrは量子化した周回軌道、Schrödingerは波動関数・演算子・確率を用い、角度分布や遷移も記述するためです。

## ナビゲーション

- 前：[角運動量](../part03_angular_momentum_spin/README.md)
- 次：[分子軌道](02_molecular_orbitals_and_bonds.md)
- 歴史：[Bohr模型](../part01_mysteries/02_atomic_spectra_and_matter_waves.md)
