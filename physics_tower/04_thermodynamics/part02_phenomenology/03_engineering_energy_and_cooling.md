# 熱力学の工学応用：発電・冷却・電池・GPU

## 応用と必要概念

| 応用 | system boundary | 必要概念 |
|---|---|---|
| turbine・発電 | steady-flow control volume | enthalpy、entropy、効率 |
| refrigerator・heat pump | cycle | COP、第2法則 |
| battery | matterとchargeを含む系 | Gibbs energy、chemical potential |
| 相変化材料 | 二相系 | latent heat、phase equilibrium |
| GPU・semiconductor | chip→package→coolant | power、thermal resistance、entropy生成 |
| data center | rack＋cooling plant | energy balance、COP、exergy |

## turbine

運動・位置energyを無視した断熱steady-flowでは

$$
\dot W_{\mathrm{out}}\simeq\dot m(h_{\mathrm{in}}-h_{\mathrm{out}})
$$

です。

## 冷蔵庫

$$
\mathrm{COP}_{R}=\frac{Q_c}{W}
$$

可逆上限は

$$
\mathrm{COP}_{R,\max}=\frac{T_c}{T_h-T_c}
$$

です。

## chipの熱

発熱

$$
P
$$

thermal resistance

$$
R_\theta
$$

なら定常近似で

$$
\Delta T=PR_\theta
$$

です。

$$
P=400\ \mathrm{W},\quad R_\theta=0.10\ \mathrm{K/W}
$$

なら

$$
\Delta T=40\ \mathrm{K}
$$

です。局所hot spot、transient、temperature-dependent leakageはこのlumped modelの限界です。

## 演習と全解答

1. 300 W、0.2 K/Wの温度上昇を求めよ。
   **解答**：
   $$
   60\ \mathrm{K}
   $$
2. COP 4で8 kW除熱する電力は何か。
   **解答**：
   $$
   W=\frac84=2\ \mathrm{kW}
   $$
3. heat pumpのCOPが1を超えてよい理由は何か。
   **解答**：仕事を熱へ変えるだけでなく外界から熱を移送する比だからです。
4. voltage低下がdynamic powerに効く理由を述べよ。
   **解答**：
   $$
   P_{\mathrm{dyn}}\propto CV^2f
   $$
   だからです。
5. batteryの最大電気仕事と関係する量は何か。
   **解答**：定温定圧ではGibbs free energy変化です。
6. coolingだけでtransistor leakageを説明できるか。
   **解答**：温度収支は扱えますが、carrier統計とband/tunnelは統計・量子が必要です。

## ナビゲーション

- 前：[potential](02_potentials_equilibrium_phase_chemical.md)
- 次：[熱と統計の境界](04_thermodynamics_vs_statistical_mechanics.md)
- 関連：[半導体package熱](../../02_electromagnetism/part07_semiconductor_products/10_packaging_tsv_chiplets_and_thermal_limits.md)
