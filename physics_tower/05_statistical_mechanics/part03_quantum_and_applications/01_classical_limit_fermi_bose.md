# 古典統計の限界とFermi–Dirac・Bose–Einstein統計

## 三つの統計

一粒子stateのenergyを

$$
\varepsilon
$$

とすると平均占有数は

$$
\bar n_{\mathrm{FD}}=\frac1{e^{\beta(\varepsilon-\mu)}+1}
$$

$$
\bar n_{\mathrm{BE}}=\frac1{e^{\beta(\varepsilon-\mu)}-1}
$$

希薄・高温で占有が小さいと

$$
\bar n_{\mathrm{MB}}\simeq e^{-\beta(\varepsilon-\mu)}
$$

へ近づきます。

| 粒子 | 統計 | 占有 |
|---|---|---|
| electron、proton、neutron | Fermi–Dirac | 一つの一粒子stateに0または1 |
| photon、phonon、整数spin atom | Bose–Einstein | 同じstateに多数 |
| 希薄高温gas | Maxwell–Boltzmann近似 | quantum exchangeを無視 |

## 境界の目安

thermal de Broglie wavelength

$$
\lambda_{\mathrm{th}}=\frac{h}{\sqrt{2\pi mk_BT}}
$$

に対し

$$
n\lambda_{\mathrm{th}}^3\ll1
$$

ならclassical近似が有効です。低温、高密度、軽い粒子ほど量子統計が必要です。

## 現象

- Fermi：metal electron、semiconductor carrier、degenerate star。
- Bose：blackbody、phonon、Bose condensation。
- classical破綻：ultraviolet catastrophe、low-temperature heat capacity。

## 演習と全解答

1. electronはどの統計か。
   **解答**：Fermi–Diracです。
2. photonのchemical potentialは平衡で何か。
   **解答**：
   $$
   \mu=0
   $$
3.
   $$
   \varepsilon=\mu
   $$
   でFD占有はいくらか。
   **解答**：
   $$
   \frac12
   $$
4. temperatureを下げるとquantum degeneracyは強まるか。
   **解答**：
   $$
   \lambda_{\mathrm{th}}\propto T^{-1/2}
   $$
   なので強まります。
5. dilute semiconductorで使う近似は何か。
   **解答**：nondegenerateならBoltzmann近似です。
6. band structureを本式だけで導けるか。
   **解答**：できません。許されるstateのenergyは量子力学が与え、統計は占有を与えます。

## ナビゲーション

- 前：[古典例](../part02_classical_ensembles/04_classical_examples_and_equipartition.md)
- 次：[半導体](02_semiconductor_carriers_and_einstein_relation.md)
- 関連：[量子力学](../../07_quantum_mechanics/00_overview.md)
