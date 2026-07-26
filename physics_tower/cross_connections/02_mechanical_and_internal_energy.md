# 横断2：力学的energyと内部energy

## 境界を変えると「失われたenergy」が戻る

blockが摩擦で停止すると、blockのmechanical energy

$$
E_{\mathrm{mech}}=K+V
$$

は減ります。しかしblock＋床を系にすれば、deformationや分子運動へ移ったenergyを内部energy

$$
U
$$

として残せます。

$$
\Delta(K+V+U)=Q_{\mathrm{in}}+W_{\mathrm{external}}
$$

内部energyは「目に見えないkinetic energyだけ」ではなく、分子の並進・回転・振動・相互作用・電子状態などを粗視化した状態量です。

## 比較

| 量 | 対象 | 保存条件 |
|---|---|---|
| mechanical energy | 選んだ巨視座標 | 保存力のみ |
| internal energy | 微視自由度をまとめる | 熱・仕事を含む第1法則 |
| total energy | 系と外界を十分含む | 時間並進対称性 |

## 演習と解答

1. 摩擦で全energyは消えるか。
   **解答**：消えず、主にinternal energyへ移ります。
2. 熱は状態量か。
   **解答**：いいえ。境界を横切るenergy移送です。
3. ideal gasのUは分子運動と関係するか。
   **解答**：古典単原子気体では平均並進energyの和です。
4. springのelastic energyは常にUか。
   **解答**：巨視的自由度として明示すればpotential energy、粗視化すればUへ含め得ます。
5. system boundaryが重要な理由は何か。
   **解答**：外部work・heatと内部変換の分類が変わるためです。
6. GPUのelectric energyは最後に何になるか。
   **解答**：計算中の一時的field energyを経て主にheat/internal energyへ散逸します。

- 前：[三形式](01_newton_lagrange_hamilton.md)
- 次：[状態の階層](03_micro_macro_thermodynamic_state.md)
- 関連：[第1法則](../04_thermodynamics/part01_laws/02_first_law_heat_and_work.md)
