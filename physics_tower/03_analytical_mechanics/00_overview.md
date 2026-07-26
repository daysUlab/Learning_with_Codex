# 03 解析力学：同じ運動を、よりよい変数で見る

## 章を貫く問い

Newton力学で解ける同じ問題を、なぜ Lagrange 形式や Hamilton 形式で書き直すのでしょうか。答えが変わるからではありません。適切な条件では同じ軌道を与えます。違うのは、使う変数、拘束の扱い、対称性の見え方、他分野へ一般化できる範囲です。

```mermaid
flowchart LR
    N["Newton<br/>力と加速度"] --> L["Lagrange<br/>座標・エネルギー"]
    L --> H["Hamilton<br/>位相空間"]
    H --> X["統計・量子・場"]
```

## 前章から受け取るもの

- 運動方程式、運動量、仕事、力学的エネルギー、角運動量
- 系・時間区間・保存則を選ぶ習慣
- 微分方程式、偏微分、座標変換

## 残す情報・省略する情報・導入する構造

| 区分 | 内容 |
|---|---|
| 残す | 自由度、運動エネルギー、相互作用、初期条件、拘束 |
| 省略する | 選んだ自由度に不要な拘束力の成分、冗長なCartesian座標 |
| 導入する | 一般化座標、仮想変位、Lagrangian、作用、共役運動量、Hamiltonian、位相空間 |

## 何が有利で、何が不利か

- 拘束を座標に組み込み、未知の張力・垂直抗力を式から消せる。
- 曲線座標、多自由度、対称性、場への一般化が見通しよくなる。
- cyclic coordinate から保存量を読み取れる。
- Hamilton形式は統計力学・量子力学の共通言語になる。
- ロボット、多リンク機構、制御、symplectic数値計算へつながる。
- 一方、一定力の一次元運動などでは、Newton形式の方が短く直観的である。

## 本線

1. [Newton・Lagrange・Hamiltonの比較](part01_supplements/01_newton_lagrange_hamilton_comparison.md)
2. [自由度・一般化座標・拘束](part01_supplements/02_degrees_of_freedom_and_coordinates.md)
3. [仮想仕事とEuler–Lagrange方程式](part02_basics/01_virtual_work_and_euler_lagrange.md)
4. [斜面・振り子の比較](part02_basics/02_incline_and_pendulum_comparison.md)
5. [Atwood・滑車・連結物体](part02_basics/03_atwood_and_connected_bodies.md)
6. [中心力・回転系](part02_basics/04_central_force_and_rotating_systems.md)
7. [停留作用](part03_variational/01_stationary_action.md)
8. [対称性とNoether](part03_variational/02_symmetry_cyclic_noether.md)
9. [Legendre変換とHamiltonian](part04_gateway_to_qm/01_legendre_transform_and_hamiltonian.md)
10. [位相空間とPoisson括弧](part04_gateway_to_qm/02_phase_space_and_poisson_brackets.md)
11. [連続体・場への拡張](part05_infinite_dof/01_from_particles_to_fields.md)
12. [電磁場中の荷電粒子](part06_canonical_em/01_charged_particle_and_gauge.md)
13. [拘束・robot・数値計算](part07_constraints/01_constraints_robotics_and_simulation.md)

## 比較例題

斜面、単振り子、Atwood装置、滑車・連結物体、中心力・惑星、回転する輪上のbead、電磁場中の荷電粒子を、変数・式・拘束力・計算量・対称性・保存量・有利な形式で比較します。

## 読者別ルート

- 初学者：1→2→3→比較例→7→8。
- 工学：2→3→比較例→13。
- 統計力学：9→10→[統計力学](../05_statistical_mechanics/00_overview.md)。
- 量子・場：7→8→9→10→11→[量子力学](../07_quantum_mechanics/00_overview.md)。
- 電磁気：3→12→[Maxwell方程式](../02_electromagnetism/00_overview.md)。

## 適用範囲と次の限界

この章は主に有限自由度の古典系、holonomic拘束、保存力を中心にします。非保存力は一般化力として拡張できますが、摩擦・熱化・莫大な自由度を一つずつ追うだけでは巨視的不可逆性を説明しにくい。そこで次章は微視的軌道を捨て、[熱力学](../04_thermodynamics/00_overview.md)の状態量へ進みます。

## 完成状態

本線13記事、比較7題、固有演習と全解答を本文化済みです。レビュー状態は [PROGRESS](../PROGRESS.md) を正本とします。

## ナビゲーション

- 前：[Newton力学](../01_dynamics/00_overview.md)
- 次：[熱力学](../04_thermodynamics/00_overview.md)
- 親：[Physics Tower](../README.md)
