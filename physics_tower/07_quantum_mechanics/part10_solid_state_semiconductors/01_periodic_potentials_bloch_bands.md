# 周期potential・Bloch状態・band構造

## 原子準位から結晶bandへ

結晶では

$$
V(\mathbf r+\mathbf R)=V(\mathbf r)
$$

です。Blochの定理により固有stateは

$$
\psi_{n\mathbf k}(\mathbf r)
=e^{i\mathbf k\cdot\mathbf r}u_{n\mathbf k}(\mathbf r)
$$

$$
u_{n\mathbf k}(\mathbf r+\mathbf R)
=u_{n\mathbf k}(\mathbf r)
$$

と書けます。有限個の原子軌道が重なり、原子数と同数程度の近接準位へ分裂し、巨視的結晶ではbandに見えます。

周期potentialはBrillouin zone境界で進行波を混ぜ、standing wave間のenergy差としてband gapを開きます。

| 物質 | chemical potential近傍のstate |
|---|---|
| conductor | 部分占有bandまたはband重なり |
| insulator | 大きなgapを隔ててvalence満杯・conduction空 |
| semiconductor | 熱・光・dopingでcarrierを作れる比較的小さなgap |

分類はbandの存在だけでなく占有も必要です。占有の正本は統計力学です。

## 演習と全解答

1. Bloch stateは結晶周期と同じ関数か。
   **解答**：周期部分
   $$
   u_{n\mathbf k}
   $$
   は同じですが、全体はphase factorを持ちます。
2. 完全結晶で
   $$
   \mathbf k
   $$
   が何を表すか。
   **解答**：結晶並進の固有値をlabelするcrystal momentumです。
3. 原子を増やすと離散準位がbandに見える理由を述べよ。
   **解答**：相互作用で多数の近接準位へ分裂し、間隔が巨視的に極小になるためです。
4. band gap内に通常のBloch固有stateがあるか。
   **解答**：理想無限結晶のbulk許容stateはありません。欠陥・表面はgap内stateを作り得ます。
5. bandがあるだけでsemiconductorと判定できるか。
   **解答**：できません。gapの大きさ、占有、温度、disorderも必要です。
6. free electronとの違いを一つ述べよ。
   **解答**：周期potentialによりdispersionがzoneでfoldされ、gapと有効質量が生じます。

## ナビゲーション

- 前：[量子化学](../part08_quantum_chemistry/03_many_electron_quantum_chemistry.md)
- 次：[有効質量とcarrier](02_effective_mass_electrons_holes.md)
- 伏線：[古典像の限界](../../02_electromagnetism/part06_semiconductor_bridge/12_limits_of_the_classical_picture.md)
