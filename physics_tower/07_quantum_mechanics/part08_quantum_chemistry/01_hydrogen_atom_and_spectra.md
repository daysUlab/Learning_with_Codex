# 水素原子――Coulomb potential・量子数・spectra

## 現代量子論から見ると

このページの固有値問題は主に

$$
H_{\rm atom}
$$

を扱います。energy differenceだけではabsorption・emission全過程は決まりません。quantized electromagnetic field、interaction、初期state、photon detectionが必要です。

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

## 原子・field・interaction

全Hamiltonianの見取り図は

$$
H=H_{\rm atom}+H_{\rm field}+H_{\rm int}
$$

です。外場を古典場として扱う近似ではabsorptionとstimulated emissionを記述できますが、真空からphotonが生成されるspontaneous emissionにはfield quantizationが本質的です。transition rateは概略

$$
\Gamma_{i\to f}\propto
|\langle f|H_{\rm int}|i\rangle|^2
\times\text{final-state density}
$$

で、selection ruleはmatrix elementがzeroになる条件です。この構造はlaser、LED、spectroscopyへ接続します。

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
7. 原子のenergy eigenvalueだけでspontaneous emission rateが決まらない理由を述べよ。
   **解答**：
   $$
   H_{\rm int}
   $$
   のmatrix element、photon mode密度、初期field stateが必要で、原子単独Hamiltonianはphoton生成を含まないためです。
8. stimulated emissionとspontaneous emissionの違いを述べよ。
   **解答**：前者は入射fieldの占有により誘起され、後者は初期photonがなくてもquantized fieldとの結合で生じます。

## ナビゲーション

- 前：[角運動量](../part03_angular_momentum_spin/README.md)
- 次：[分子軌道](02_molecular_orbitals_and_bonds.md)
- 歴史：[Bohr模型](../part01_mysteries/02_atomic_spectra_and_matter_waves.md)
- 参考：[原子spectraとHamiltonian（qm大学物理）](https://qmcharge.com/article-spectroscopy-hamiltonian)（確認日：2026-07-27）
