# 横断3：microstate・macrostate・熱力学状態

## 三つの解像度

| 解像度 | 指定するもの | 捨てるもの |
|---|---|---|
| mechanical microstate | 全
$$
q_i,p_i
$$ | ほぼなし |
| statistical macrostate | energy・N・magnetization等 | 個別state |
| thermodynamic state | 平衡状態量
$$
T,p,V,N
$$ | micro model自体 |

一つのthermodynamic stateには膨大なmicrostateが対応します。統計力学はその集合へ確率を与え、熱力学は集合の細部を仮定せず状態間の関係を使います。

## 粗視化

粗視化は単なる測定不足ではなく、目的に不要な変数を積分・平均し、再現性の高い量だけを残す操作です。粒子数が大きいと相対揺らぎ

$$
\sim N^{-1/2}
$$

が小さくなります。

## 演習と解答

1. 温度は一粒子の属性か。
   **解答**：通常はensembleまたは局所平衡集団の属性です。
2. 同じmacrostateに複数microstateがあるか。
   **解答**：あります。その数がmultiplicityです。
3. microstateを知らないと予測不能か。
   **解答**：多数系では典型性と小さい相対揺らぎにより巨視量を高精度予測できます。
4. non-equilibrium状態をT一つで表せるか。
   **解答**：一般には不可で、局所平衡などの追加仮定が必要です。
5. macrostateの選び方は一意か。
   **解答**：目的とscaleに依存します。
6. coarse-grainingで保存則は必ず失うか。
   **解答**：energyやparticle numberなどを意図的に残せます。

- 前：[energy](02_mechanical_and_internal_energy.md)
- 次：[不可逆性](04_micro_reversibility_macro_irreversibility.md)
- 関連：[small counting](../05_statistical_mechanics/part01_kinetic_theory/02_microstate_macrostate_small_counting.md)
