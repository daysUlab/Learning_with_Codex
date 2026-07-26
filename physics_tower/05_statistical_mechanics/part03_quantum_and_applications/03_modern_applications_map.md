# 統計力学の現代応用map

## 基礎概念との対応

| 分野 | 現象・技術 | 必要な基礎概念 |
|---|---|---|
| 半導体・電子材料 | carrier、leakage、輸送 | Fermi分布、状態密度、chemical potential |
| 磁性 | paramagnet、ferromagnet | spin、partition function、相互作用、自発的対称性破れ |
| 相転移 | boiling、criticality | order parameter、free energy、fluctuation、correlation、thermodynamic limit |
| 情報・ML | maximum entropy、EBM、annealing | entropy、Boltzmann分布、Monte Carlo |
| 材料・化学 | defect、diffusion、battery、adsorption | chemical potential、phase equilibrium |
| 生物物理 | Brownian motion、folding | fluctuation、diffusion、free-energy landscape |
| 宇宙 | radiation、star、white dwarf | Bose photon、ideal gas、degenerate Fermi gas |
| 計算科学 | MD、Monte Carlo | sampling、ergodicity、finite-size effect |

## 物理entropyと情報entropy

確率分布

$$
p_i
$$

のShannon entropyは

$$
H=-\sum_i p_i\ln p_i
$$

Gibbs entropyは

$$
S=-k_B\sum_i p_i\ln p_i
$$

で数学構造を共有します。しかし物理entropyはmicrostateの定義、energy constraint、物理単位、熱との関係を持ちます。情報entropyはcodingや不確実性の文脈で使われ、意味を無条件に同一視しません。

## maximum entropyとBoltzmann分布

正規化と平均energy固定の下で

$$
-\sum_i p_i\ln p_i
$$

を最大化すると

$$
p_i\propto e^{-\beta E_i}
$$

を得ます。energy-based modelでも同じ形が使われますが、model energyは必ずしも物理energyではありません。

## Monte Carlo

Metropolis acceptanceを

$$
A=\min\left(1,e^{-\beta\Delta E}\right)
$$

とすればcanonical分布を定常分布にできます。equilibration、autocorrelation、rare event、finite-sizeを検査します。

## 演習と全解答

1. magnetic transitionに必要な追加概念は何か。
   **解答**：spin相互作用、order parameter、自発的対称性破れです。
2. simulated annealingでtemperatureを下げる目的は何か。
   **解答**：高energy stateの受理を徐々に抑え、低energy領域を探索するためです。
3. EBMのenergyはJ単位か。
   **解答**：通常はscoreで、物理単位を持つとは限りません。
4. Brownian motionの拡散係数とmobilityの関係を答えよ。
   **解答**：
   $$
   D=\mu k_BT
   $$
   です。charge mobilityとは定義を区別します。
5. white dwarfを支える統計は何か。
   **解答**：electronのFermi degeneracyです。
6. Monte Carloでsample数だけ増やせば十分か。
   **解答**：いいえ。相関、burn-in、mixing、有限size、model誤差を確認します。

## 限界と次

非平衡輸送、glass、active matterは平衡ensembleだけでは不足します。量子stateの構築と時間発展は[量子力学](../../07_quantum_mechanics/00_overview.md)へ進みます。

- 前：[半導体](02_semiconductor_carriers_and_einstein_relation.md)
- 親：[part03](README.md)

## 参考資料

Jaynes (1957), information theory and statistical mechanics.
