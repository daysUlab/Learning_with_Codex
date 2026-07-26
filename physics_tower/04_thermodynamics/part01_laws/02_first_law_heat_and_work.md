# 第1法則：内部energy、熱、仕事

## 問い

力学的energyが摩擦で失われたように見えるとき、何を系に残せばenergy保存を回復できるでしょうか。巨視的な内部自由度をまとめた内部energy

$$
U
$$

を導入します。

本章は「系が受け取る熱と仕事を正」とし

$$
dU=\delta Q+\delta W
$$

を使います。単純圧縮で外圧

$$
p_{\mathrm{ext}}
$$

に逆らって膨張すると

$$
\delta W=-p_{\mathrm{ext}}dV
$$

準静的可逆なら

$$
dU=\delta Q-p\,dV
$$

です。

## 状態量と経路量

$$
dU
$$

は完全微分で、始終状態だけで決まります。一方

$$
\delta Q,\delta W
$$

はpathに依存し、系が「熱を持つ」「仕事を持つ」とは言いません。熱と仕事は境界を横切るenergy移送の分類です。

## 数値例

気体へ

$$
Q=500\ \mathrm{J}
$$

を加え、気体が外界へ

$$
200\ \mathrm{J}
$$

の仕事をしたなら、系が受けた仕事は

$$
W=-200\ \mathrm{J}
$$

なので

$$
\Delta U=300\ \mathrm{J}
$$

です。

## 演習と全解答

1. adiabatic過程で何がゼロか。
   **解答**：
   $$
   Q=0
   $$
   で、温度一定とは限りません。
2. cycleで
   $$
   \Delta U
   $$
   はいくらか。
   **解答**：状態が戻るためゼロです。
3. rigid containerでboundary workはいくらか。
   **解答**：
   $$
   dV=0\Rightarrow W=0
   $$
4. 系へ100 Jの仕事をし、50 J放熱した。
   **解答**：
   $$
   \Delta U=-50+100=50\ \mathrm{J}
   $$
5. 摩擦でmechanical energyが減ると全energy保存は破れるか。
   **解答**：内部energyや外界への熱を含めれば破れません。
6. free expansionで真空への仕事はいくらか。
   **解答**：
   $$
   p_{\mathrm{ext}}=0\Rightarrow W=0
   $$

## 誤解・接続

符号規約は教科書で異なるため最初に宣言します。microscopicな運動energyとpotential energyを統計的に足したものが内部energyへどう結びつくかは次章で扱います。

- 前：[系と温度](01_system_equilibrium_and_temperature.md)
- 次：[状態方程式](03_equations_of_state_heat_capacity_enthalpy.md)
- 関連：[mechanicalとinternal energy](../../cross_connections/02_mechanical_and_internal_energy.md)
