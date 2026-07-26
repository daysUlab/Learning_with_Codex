# 電磁気学――電荷から場・回路・半導体・AI計算基盤まで

> 完成状態：場の理論から回路・半導体デバイス・memory・AI計算基盤への入口まで本文化済み
> 単位系：SI
> 交流の時間規約：
>
> $$
> e^{-i\omega t}
> $$

## この章を貫く問い

電荷と電流は、離れた場所へどのように力・エネルギー・情報を伝えるのでしょうか。

力学では粒子の運動を追いました。電磁気学では空間の各点に定義された場

$$
\mathbf E,\ \mathbf B
$$

を主役にします。電荷と電流が場を作り、場がLorentz力

$$
\mathbf F=q(\mathbf E+\mathbf v\times\mathbf B)
$$

を通して物質へ作用します。

## 1. 30段階のストーリー

この図は、静的な電荷から場を組み立て、端子量へ縮約し、集中定数の限界で再び波動と放射へ戻る因果順序を示します。

```mermaid
flowchart TD
  A["電荷・Coulomb・Gauss"] --> B["Faraday・Ampère–Maxwell"]
  B --> C["境界・波動・エネルギー"]
  C --> D["物質応答・放射"]
  D --> E["V・I・Q・磁束へ縮約"]
  E --> F["R・C・L・Kirchhoff則"]
  F --> G["直流・過渡・交流・機器"]
  G --> H["伝送線路・アンテナ・限界"]
  H --> I["半導体中の電位・電荷・輸送"]
  I --> J["pn接合・MOSFET"]
  J --> K["logic・DRAM・NAND・HBM"]
  K --> L["GPU・SSD・AI計算基盤"]
  L --> M["量子・統計で再訪"]
```

1. 電荷と電場
2. Coulomb則
3. 対称性とGauss則
4. 時間変化する磁束とFaraday則
5. 電流・磁場とAmpère則
6. 変位電流とMaxwell方程式
7. 境界条件
8. 電磁波
9. エネルギー密度とPoyntingベクトル
10. 誘電体と分極
11. 導体と表皮効果
12. 加速電荷と放射
13. 電圧と電流への縮約
14. 抵抗・容量・インダクタンス
15. Kirchhoff則
16. 集中定数回路
17. 直流回路
18. RC・RL過渡応答
19. 交流・共振・電力
20. 変圧器・モーター・発電機
21. 伝送線路・アンテナ
22. 回路理論の限界
23. 問題選択・誤解整理
24. 数学補習
25. 半導体中の電位・Poisson方程式・ドリフト拡散
26. ドーピング・空乏層・pn接合
27. MOSコンデンサ・MOSFET
28. CMOS・SRAM・DRAM・NAND
29. HBM・GPU・SSD・package
30. AI計算基盤と古典理論の限界

## 2. Maxwell方程式を二つの記述で整理する

### 2.1 真空中・全電荷による微分形

$$
\nabla\cdot\mathbf E=\frac{\rho}{\varepsilon_0}
$$

$$
\nabla\cdot\mathbf B=0
$$

$$
\nabla\times\mathbf E=-\frac{\partial\mathbf B}{\partial t}
$$

$$
\nabla\times\mathbf B=\mu_0\mathbf J
+\mu_0\varepsilon_0
\frac{\partial\mathbf E}{\partial t}
$$

ここで

$$
\rho,\ \mathbf J
$$

は記述対象に含めた全電荷・全電流です。

### 2.2 物質中・自由電荷による巨視的形

$$
\nabla\cdot\mathbf D=\rho_{\mathrm f}
$$

$$
\nabla\cdot\mathbf B=0
$$

$$
\nabla\times\mathbf E=-\frac{\partial\mathbf B}{\partial t}
$$

$$
\nabla\times\mathbf H=\mathbf J_{\mathrm f}
+\frac{\partial\mathbf D}{\partial t}
$$

補助場は

$$
\mathbf D=\varepsilon_0\mathbf E+\mathbf P
$$

$$
\mathbf H=\frac{\mathbf B}{\mu_0}-\mathbf M
$$

で、束縛電荷・束縛電流を物質応答へ整理します。本章の現象論は主に電気分極を扱い、磁化は定義にとどめます。

構成方程式

$$
\mathbf D=\varepsilon\mathbf E
$$

$$
\mathbf B=\mu\mathbf H
$$

$$
\mathbf J_{\mathrm c}=\sigma\mathbf E
$$

は、Maxwell方程式と同じ普遍法則ではありません。線形・等方・局所・一様など、各記事で明示する媒質モデルの条件に依存します。

## 3. 積分形

$$
\oint_{\partial V}\mathbf D\cdot d\mathbf S=Q_{\mathrm f}
$$

$$
\oint_{\partial V}\mathbf B\cdot d\mathbf S=0
$$

$$
\oint_{\partial S}\mathbf E\cdot d\mathbf l=-\frac{d}{dt}\int_S\mathbf B\cdot d\mathbf S
$$

$$
\oint_{\partial S}\mathbf H\cdot d\mathbf l=I_{\mathrm f}
+\frac{d}{dt}\int_S\mathbf D\cdot d\mathbf S
$$

微分形は各点の局所関係、積分形は面・体積・周回路を通した総量関係です。どちらか一方が本物なのではなく、Gaussの定理とStokesの定理で結ばれます。

## 4. 4式の相互整合

- 電荷は電場の発散源です。
- 磁荷を導入しない標準電磁気では、磁場の発散はゼロです。
- 時間変化する磁場は渦電場を作ります。
- 電流と時間変化する電場は渦磁場を作ります。

Ampère–Maxwell則の発散を取ると

$$
\frac{\partial\rho}{\partial t}
+\nabla\cdot\mathbf J=0
$$

が得られ、変位電流が電荷保存と理論を整合させます。

Faraday則とAmpère–Maxwell則を組み合わせると波動方程式が生まれ、Poynting定理

$$
\frac{\partial u}{\partial t}
+\nabla\cdot\mathbf S
+\mathbf J\cdot\mathbf E=0
$$

が場と物質を含むエネルギー保存を表します。Maxwell方程式は4公式の寄せ集めではなく、保存則・波動・境界条件を同時に支える一つの系です。

## 5. 読み方

### 必修ルート

1. [Coulomb則からGauss則](part01_build_maxwell/01_from_coulomb_to_gauss.md)
2. [Faraday則](part01_build_maxwell/02_faraday_law.md)
3. [Ampère–Maxwell則](part01_build_maxwell/03_ampere_maxwell.md)
4. [境界条件](part02_use_maxwell/01_boundary_conditions.md)
5. [電磁波](part02_use_maxwell/02_em_waves.md)
6. [Poyntingベクトル](part02_use_maxwell/03_poynting_vector.md)
7. [誘電体](part03_phenomenology/01_dielectrics.md)
8. [導体と表皮効果](part03_phenomenology/02_conductors_and_skin_effect.md)
9. [放射](part03_phenomenology/03_radiation_basics.md)
10. [場から回路への縮約](part04_from_fields_to_circuits/README.md)
11. [回路応用](part05_circuit_applications/README.md)

### 大学受験ルート

1. [電圧・電流・RLCの由来](part04_from_fields_to_circuits/README.md)
2. [直列・並列とコンデンサ](part05_circuit_applications/01_series_parallel_and_equivalent_resistance.md)
3. [RC・RL・RLC](part05_circuit_applications/04_rc_charging_and_discharging.md)
4. [大学受験回路の解法戦略](qa/04_high_school_circuit_problem_strategy.md)

### 工学接続ルート

1. [集中定数近似](part04_from_fields_to_circuits/07_lumped_element_approximation.md)
2. [交流・共振・力率](part05_circuit_applications/07_ac_impedance_and_phasors.md)
3. [変圧器・モーター・発電機](part05_circuit_applications/09_mutual_inductance_and_transformers.md)
4. [伝送線路・アンテナ](part05_circuit_applications/11_transmission_lines_as_distributed_circuits.md)
5. [10_circuitsで回路解析を深める](../10_circuits/00_overview.md)

### 半導体デバイスルート

1. [電位・Poisson・輸送](part06_semiconductor_bridge/README.md)
2. [pn接合](part06_semiconductor_bridge/06_pn_junction_as_an_electrostatic_structure.md)
3. [MOSコンデンサ](part06_semiconductor_bridge/08_mos_capacitor.md)
4. [MOSFET](part06_semiconductor_bridge/09_mosfet_as_a_field_controlled_switch.md)

### memory技術ルート

1. [SRAM](part07_semiconductor_products/03_sram_and_cache.md)
2. [DRAM](part07_semiconductor_products/04_dram_as_a_transistor_capacitor_cell.md)
3. [NAND](part07_semiconductor_products/05_nand_flash_and_floating_gate_or_charge_trap.md)
4. [SSDとHBM](part07_semiconductor_products/06_ssd_controller_and_nand_system.md)

### AI hardwareルート

1. [CMOSとGPU](part07_semiconductor_products/02_cmos_logic_and_gpu_switching.md)
2. [HBM](part07_semiconductor_products/07_hbm_and_vertical_integration.md)
3. [GPUとmemory帯域](part07_semiconductor_products/08_gpu_memory_bandwidth_and_ai.md)
4. [AIデータセンター](part07_semiconductor_products/13_from_device_physics_to_ai_datacenter.md)

### 企業・産業ルート

1. [製造工程](part07_semiconductor_products/11_semiconductor_manufacturing_overview.md)
2. [企業マップ](part07_semiconductor_products/12_company_map_kioxia_micron_skhynix_nvidia.md)
3. [value chain Q&A](qa/08_semiconductor_company_value_chain.md)

### 量子力学への準備ルート

1. [電磁気学と量子論の分業](part06_semiconductor_bridge/01_why_semiconductors_need_em_and_quantum.md)
2. [古典像の限界](part06_semiconductor_bridge/12_limits_of_the_classical_picture.md)
3. [統計力学](../05_statistical_mechanics/00_overview.md)
4. [量子力学](../07_quantum_mechanics/00_overview.md)

### 数学補習ルート

- grad・div・curlで止まった：[ベクトル解析](remedial/01_vector_calc_for_em.md)
- Poisson・波動・拡散で止まった：[ODE・PDE](remedial/02_ode_pde_refresh.md)
- 位相・損失・複素波数で止まった：[複素表示](remedial/03_complex_representation_ac.md)

### 現象から入るルート

1. [誘電体](part03_phenomenology/01_dielectrics.md)
2. [導体と表皮効果](part03_phenomenology/02_conductors_and_skin_effect.md)
3. [放射](part03_phenomenology/03_radiation_basics.md)
4. 分からない式からpart01・part02へ逆向きに戻る

### 問題演習ルート

1. [問題選択](qa/02_problem_selection.md)
2. 対応する本文の演習
3. [頻出誤解](qa/01_common_misconceptions.md)
4. [単位と符号](qa/03_units_and_signs.md)
5. [大学受験回路の解法](qa/04_high_school_circuit_problem_strategy.md)
6. [工学応用マップ](qa/05_engineering_application_map.md)

## 6. 各パートの完成状態

| パート | 役割 | 状態 |
|---|---|---|
| [part01](part01_build_maxwell/README.md) | Maxwell方程式を組み立てる | 完成・技術レビュー済み |
| [part02](part02_use_maxwell/README.md) | 境界・波動・エネルギーへ使う | 完成・技術レビュー済み |
| [part03](part03_phenomenology/README.md) | 物質と放射へつなぐ | 新規本文化・レビュー済み |
| [part04](part04_from_fields_to_circuits/README.md) | 場から端子量・RLC・Kirchhoff則へ縮約 | 本文化・QA済み |
| [part05](part05_circuit_applications/README.md) | 大学受験回路から工学初歩へ接続 | 本文化・QA済み |
| [part06](part06_semiconductor_bridge/README.md) | 電場・電位からpn接合・MOSFETへ接続 | 本文化・内容・演習QA済み |
| [part07](part07_semiconductor_products/README.md) | logic・memory・GPU・AI基盤と企業分業 | 本文化・内容・演習・一次資料QA済み |
| [qa](qa/README.md) | 誤解・問題選択・受験・工学マップ | 本文化済み |
| [remedial](remedial/README.md) | 数学への最短復帰 | 新規本文化済み |

## 7. 回路・量子・統計との役割分担

本章は、回路量が場からどう生まれ、どの近似で有効かを正本とします。[10_circuits](../10_circuits/00_overview.md) はThévenin・Norton、回路網解析、フィルタ、二端子対、オペアンプ、半導体、実装・計測を独立した工学体系として詳しく扱います。

半導体の巨視的な場・電荷・端子モデルは本章、回路網としての詳細は[10_circuits](../10_circuits/00_overview.md)、band・トンネル・量子閉じ込めは[量子力学](../07_quantum_mechanics/00_overview.md)、Fermi準位とcarrier統計は[統計力学](../05_statistical_mechanics/00_overview.md)で再訪します。

解析力学では、場そのものではなく作用・変分・対称性から運動方程式と保存則を統一します。本章で使った

$$
\text{モデル}
\quad
\text{境界条件}
\quad
\text{保存則}
\quad
\text{対称性}
$$

という考え方はそのまま持ち越します。ただし、本バッチでは解析力学の記事には着手しません。

回路への応用は[10_circuits](../10_circuits/00_overview.md)、量子計算と古典回路・論理の違いは[Logic Towerの発展記事](../../logic_tower/90_essays/quantum_computing_and_logic/README.md)へ接続します。

## 8. 章末チェック

- 真空中と物質中のMaxwell方程式を使い分けられる。
- 自由電荷・束縛電荷・分極・電束密度を区別できる。
- 境界条件、波動、エネルギー保存を同じ方程式系から説明できる。
- 良導体近似と遠方場近似の条件を述べられる。
- 問題文から第一候補の道具を選べる。
- 電場・電位・電荷分布からpn接合とMOSの巨視的動作を説明できる。
- DRAM、NAND、HBM、SSD、GPUを異なる階層へ配置できる。
- 古典電磁気学で読める範囲と量子・統計へ保留する範囲を区別できる。

## ナビゲーション

- 前：[力学](../01_dynamics/00_overview.md)
- 次：[part01：Maxwell方程式を組み立てる](part01_build_maxwell/README.md)
- 親：[Physics Tower](../README.md)
