# 04 熱力学：微視的軌道を捨てて、巨視的予測を得る

## 章を貫く問い

莫大な粒子の位置・速度・衝突履歴を一つずつ追わず、少数の巨視量だけで何を予測できるでしょうか。熱力学は、情報を捨てたため単に粗い理論になるのではありません。微視的詳細を捨てることで、物質の細部に依存しにくい普遍的な収支、平衡条件、最大効率を得ます。

## 前章から何を残し、何を省略するか

| 残す | 省略する | 新たに導入する |
|---|---|---|
| エネルギー保存、仕事、系と外界、境界、力と圧力、状態変化 | 各粒子の位置・速度、衝突履歴、微視的初期条件、詳細な時間発展 | 温度、圧力、体積、内部エネルギー、entropy、粒子数、chemical potential |

```mermaid
flowchart LR
    M["多数粒子の軌道"] -->|粗視化| E["平衡状態"]
    E --> V["少数の状態量"]
    V --> P["可能過程・効率・平衡"]
```

## 本線

1. [系・境界・平衡・第0法則](part01_laws/01_system_equilibrium_and_temperature.md)
2. [第1法則、熱と仕事](part01_laws/02_first_law_heat_and_work.md)
3. [状態方程式、熱容量、enthalpy](part01_laws/03_equations_of_state_heat_capacity_enthalpy.md)
4. [第2法則、entropy、Carnot cycle](part01_laws/04_second_law_entropy_and_engines.md)
5. [可逆・不可逆とentropy生成](part02_phenomenology/01_reversible_irreversible_and_entropy_generation.md)
6. [熱力学potential、平衡、相、chemical potential](part02_phenomenology/02_potentials_equilibrium_phase_chemical.md)
7. [発電・冷却・電池・GPU熱設計](part02_phenomenology/03_engineering_energy_and_cooling.md)
8. [熱力学と統計力学の境界](part02_phenomenology/04_thermodynamics_vs_statistical_mechanics.md)

## 代表例

- 理想気体の等温・断熱過程
- Carnot機関と冷蔵庫
- 相平衡と化学平衡
- GPU・data centerの発熱、熱抵抗、冷却電力

## 読者別ルート

- 初学者：1→2→3→4→5。
- 工学：1→2→3→4→7。
- 化学・材料：2→6→[統計力学](../05_statistical_mechanics/00_overview.md)。
- 半導体：2→5→7→統計力学のcarrier温度依存。

## 適用範囲

平衡または準静的過程を主とし、局所平衡が置ける範囲まで拡張します。熱力学だけで、温度・圧力の微視的起源、比熱の物質差、揺らぎ、相転移の機構、Fermi準位は決まりません。それらを説明するために統計力学へ進みます。

## 完成状態

法則、entropy、potential、相・化学平衡、工学応用、統計力学との境界を8記事で本文化済みです。

## ナビゲーション

- 前：[解析力学](../03_analytical_mechanics/00_overview.md)
- 次：[統計力学](../05_statistical_mechanics/00_overview.md)
- 親：[Physics Tower](../README.md)
