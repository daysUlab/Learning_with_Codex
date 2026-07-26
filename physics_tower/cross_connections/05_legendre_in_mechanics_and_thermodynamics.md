# 横断5：解析力学と熱力学のLegendre変換

## 共通構造

Legendre変換は「傾き」を新しい独立変数へ交換します。

### 力学

$$
p_i=\frac{\partial L}{\partial\dot q_i}
$$

$$
H(q,p)=\sum_i p_i\dot q_i-L(q,\dot q)
$$

速度を共役momentumへ交換します。

### 熱力学

$$
T=\left(\frac{\partial U}{\partial S}\right)_{V,N}
$$

$$
F(T,V,N)=U(S,V,N)-TS
$$

entropyをtemperatureへ交換します。

| 分野 | 元の関数 | 交換 | 新しい関数 |
|---|---|---|---|
| mechanics | Lagrangian | velocityとmomentum | Hamiltonian |
| thermo | internal energy | entropyとtemperature | Helmholtz free energy |

## 違い

力学では時間発展の表現を変え、熱力学では外界が制御する自然変数に合わせて平衡problemを変えます。符号と凸性の規約も異なるため、単なる記号対応ではありません。

## 演習と解答

1.
   $$
   G
   $$
   の定義を書け。
   **解答**：
   $$
   G=U-TS+pV
   $$
2. Hの自然変数を答えよ。
   **解答**：mechanicsのHamiltonianなら
   $$
   q,p
   $$
   、thermoのenthalpyなら
   $$
   S,p,N
   $$
   です。
3. 同じH記号の混同を避けるにはどうするか。
   **解答**：文脈と引数を明記します。
4. transformで情報は消えるか。
   **解答**：凸性・可逆性があれば同じ関係を再表現します。
5. 定温定容で選ぶpotentialは何か。
   **解答**：Helmholtz free energyです。
6. velocity Hessianが特異ならどうなるか。
   **解答**：通常のHamiltonianへ一意変換できず、constraint解析が必要です。

- 前：[不可逆性](04_micro_reversibility_macro_irreversibility.md)
- 次：[対称性と相](06_symmetry_conservation_equilibrium_phase.md)
- 詳細：[mechanics](../03_analytical_mechanics/part04_gateway_to_qm/01_legendre_transform_and_hamiltonian.md)、[thermo](../04_thermodynamics/part02_phenomenology/02_potentials_equilibrium_phase_chemical.md)
