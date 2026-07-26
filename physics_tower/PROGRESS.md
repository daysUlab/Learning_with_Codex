# physics_tower 執筆進捗（PROGRESS）

## 運用ルール（このリポジトリ専用）
- ユーザーが **「次をお願いします」** とだけ指示した場合も、このファイルを最初に確認する。
- 優先順位は次の通り。
  1. `status=DOING` の行があれば、そのファイルを最優先で仕上げて `DONE` にする。
  2. `DOING` が無ければ、キュー先頭から最初の `TODO` を1件だけ選んで執筆する。
  3. 1回の実行で本文執筆は **必ず1ファイルのみ**。
- ただし、ユーザーが対象ファイルまたは件数を明示した一括バッチでは指定範囲を優先する。対象・レビュー判定・検査結果を `notes` で区別する。
- 執筆完了後は、この表の対象行を `DONE` に更新し、`last_updated` と `notes` を記録する。
- 次の `TODO` は同一実行内で `DOING` にしない（次回実行時に選ばれるよう `TODO` のまま残す）。
- 対象範囲は `physics_tower/` 配下のみ。
- 数式は原則として文章中に埋め込まず、独立行のブロック数式（`$$...$$`）で記述する。
- 上記ルールは全セクションに適用し、特に演習問題・演習解答・章末まとめでも数式をインライン記法にしない。
- 行列数式は `\begin{pmatrix}...\end{pmatrix}` を必ず同一ブロック数式内で閉じ、途中改行や記号欠落でレンダリング崩れを起こさない。

## 状態定義

- `DRAFT_DONE`：本文と全解答を作成済み。
- `STRUCTURE_QA_PASS`：見出し、navigation、相対link、TeX delimiter、Mermaid構文の構造検査済み。
- `CONTENT_REVIEWED`：物理内容、近似、符号、単位、古典／量子境界をレビュー済み。
- `EXERCISE_REVIEWED`：全設問と解答の対応、途中式、判断理由をレビュー済み。
- `SOURCE_VERIFIED`：現在製品・企業情報を公式一次資料で確認し、確認日を記録済み。
- 旧 `QA_PASS` は当時の構造QAを含む総称であり、上記の各レビューを個別に保証する状態名ではない。

## キュー定義
- 順序規則: `physics_tower/README.md` → `00_physics_math_tools`（`00_overview.md` 優先、その後サブフォルダ）→ 番号順フォルダ → `90_topics_from_conversations`。
- 各フォルダ内はファイル名辞書順。

## 執筆キュー

| file_path | status | last_updated | notes |
|---|---|---|---|
| `physics_tower/README.md` | DONE | 2026-02-14 | 入口ページを教科書形式へ全面増補。学習目標〜演習・解答まで新設し、直観→導出→確認の流れを明示。 |
| `physics_tower/00_physics_math_tools/00_overview.md` | DONE | 2026-02-14 | 物理数学ツールの全体像を教科書形式で増補。減衰振動を例に直観→導出→確認を実装し、演習10問＋全解答を追加。 |
| `physics_tower/00_physics_math_tools/calculus_techniques/README.md` | DONE | 2026-02-14 | 微積分テクニックの入口を教科書化。連鎖律・部分積分・ヤコビアンを直観→導出→確認で整理し、演習10問＋解答を追加。 |
| `physics_tower/00_physics_math_tools/calculus_techniques/partials_integrals_jacobian.md` | DONE | 2026-02-14 | 偏微分・部分積分・ヤコビアンの実践ページを執筆。境界項と測度変換を含む導出、例題3題、演習10問＋解答を追加。 |
| `physics_tower/00_physics_math_tools/complex_analysis/README.md` | DONE | 2026-02-14 | 複素解析の入口を教科書形式で執筆。コーシー積分公式から留数定理、実積分への適用、演習10問＋解答を追加。 |
| `physics_tower/00_physics_math_tools/complex_analysis/residue_theorem_minimum.md` | DONE | 2026-02-14 | 留数定理の最小実装ページを執筆。積分路選択・留数計算・実積分への復元を途中式で整理し、演習10問＋解答を追加。 |
| `physics_tower/00_physics_math_tools/differential_equations/README.md` | DONE | 2026-02-14 | 微分方程式章の入口を教科書化。1階/2階線形ODEの導出と検算手順を整理し、演習10問＋全解答を追加。 |
| `physics_tower/00_physics_math_tools/differential_equations/ode_methods.md` | DONE | 2026-02-14 | 常微分方程式の解法手順集を執筆。型判別→解法選択→検算を整理し、演習10問＋全解答を追加。 |
| `physics_tower/00_physics_math_tools/experiment/README.md` | DONE | 2026-02-14 | 実験章の入口を教科書化。平均・標準偏差・誤差伝播・有効数字を整理し、演習10問＋全解答を追加。 |
| `physics_tower/00_physics_math_tools/experiment/errors_significant_digits.md` | DONE | 2026-02-14 | 誤差評価と有効数字の実践ページを執筆。統計量・誤差伝播・丸め規則を整理し、演習10問＋全解答を追加。 |
| `physics_tower/00_physics_math_tools/linear_algebra/README.md` | DONE | 2026-02-14 | 線形代数章の入口を教科書化。連立方程式・固有値問題・対角化を整理し、演習10問＋全解答を追加。 |
| `physics_tower/00_physics_math_tools/linear_algebra/basics.md` | DONE | 2026-02-14 | 線形代数基礎実践を執筆。連立・固有値・対角化を途中式で整理し、演習10問＋全解答を追加。 |
| `physics_tower/00_physics_math_tools/vector_analysis/README.md` | DONE | 2026-02-14 | ベクトル解析章の入口を教科書化。勾配・発散・回転と積分定理を整理し、演習10問＋全解答を追加。 |
| `physics_tower/00_physics_math_tools/vector_analysis/nabla_identities.md` | DONE | 2026-02-14 | ナブラ恒等式の実践ページを執筆。3つの恒等式の成分導出、物理接続、演習10問＋解答を追加。 |
| `physics_tower/01_dynamics/00_overview.md` | DONE | 2026-02-14 | EMAN力学章を参考に概要本文を拡充。保存則導出・例題・演習・検算テンプレを整備。 |
| `physics_tower/01_dynamics/columns_and_qa/README.md` | DONE | 2026-02-14 | READMEを概要ページとして整備。目的・読み進め方・子md導線を明確化。 |
| `physics_tower/01_dynamics/columns_and_qa/01_how_to_choose_system.md` | DONE | 2026-02-15 | 系の切り方を高密度に本文化。外力/内力の分類、保存則の判定手順、典型3パターン、例題を追加。 |
| `physics_tower/01_dynamics/columns_and_qa/02_momentum_vs_energy.md` | DONE | 2026-02-15 | 保存則の使い分けページを本文化。区間分割フロー、非弾性/弾性の判定、2段階例題を追加。 |
| `physics_tower/01_dynamics/columns_and_qa/03_gaussian_integral_positioning.md` | DONE | 2026-02-15 | 力学章におけるガウス積分の位置づけを本文化。最小導出、後続章への接続、学習順序を追加。 |
| `physics_tower/01_dynamics/part01_momentum_conservation/README.md` | DONE | 2026-02-14 | README本文を拡充。導出の意味・典型パターン・例題・落とし穴・子md導線を追加。 |
| `physics_tower/01_dynamics/part01_momentum_conservation/01_derivation.md` | DONE | 2026-02-15 | 多粒子系からの運動量保存則導出を本文化。成立条件・方向別適用・例題・検算を追加。 |
| `physics_tower/01_dynamics/part01_momentum_conservation/02_collision_patterns.md` | DONE | 2026-02-15 | 衝突パターン整理を本文化。弾性/非弾性の判定、重心系の使い分け、例題群を追加。 |
| `physics_tower/01_dynamics/part01_momentum_conservation/03_center_of_mass.md` | DONE | 2026-02-15 | 重心系ページを本文化。重心運動方程式、還元質量、衝突変換、典型誤りを追加。 |
| `physics_tower/01_dynamics/part02_energy_conservation/README.md` | DONE | 2026-02-14 | README本文を拡充。保存力/非保存力の整理、例題、誤りポイント、子md導線を追加。 |
| `physics_tower/01_dynamics/part02_energy_conservation/01_work_energy.md` | DONE | 2026-02-15 | 仕事と運動エネルギー定理ページを本文化。導出、複数力分解、仕事率、例題3題、誤り対策を追加。 |
| `physics_tower/01_dynamics/part02_energy_conservation/02_conservative_force.md` | DONE | 2026-02-15 | 保存力とポテンシャルページを本文化。同値条件、判定法、代表例、例題3題、注意点を追加。 |
| `physics_tower/01_dynamics/part02_energy_conservation/03_nonconservative_cases.md` | DONE | 2026-02-15 | 非保存力のエネルギー収支ページを本文化。標準式、散逸解釈、例題3題、誤り対策を追加。 |
| `physics_tower/01_dynamics/part03_angular_momentum/README.md` | DONE | 2026-02-14 | README本文を拡充。角運動量保存の導出、中心力接続、例題、誤りポイントを追加。 |
| `physics_tower/01_dynamics/part03_angular_momentum/01_torque_and_L.md` | DONE | 2026-02-15 | トルクと角運動量の基本式ページを本文化。導出、多粒子拡張、原点依存、例題3題を追加。 |
| `physics_tower/01_dynamics/part03_angular_momentum/02_central_force.md` | DONE | 2026-02-15 | 中心力ページを本文化。角運動量保存、面積速度、極座標式、有効ポテンシャル導入を追加。 |
| `physics_tower/01_dynamics/part03_angular_momentum/03_inertia_change.md` | DONE | 2026-02-15 | 慣性モーメント変化ページを本文化。角運動量保存条件、エネルギー差、実例、例題3題を追加。 |
| `physics_tower/01_dynamics/part04_applications/README.md` | DONE | 2026-02-15 | README本文を拡充。保存則の選択フロー、弾道振り子例題、検算観点、子md導線を追加。 |
| `physics_tower/01_dynamics/part04_applications/01_ballistic_pendulum.md` | DONE | 2026-02-15 | 弾道振り子ページを本文化。2段階解法、エネルギー損失評価、例題3題、誤り対策を追加。 |
| `physics_tower/01_dynamics/part04_applications/02_two_stage_strategy.md` | DONE | 2026-02-15 | 複合問題の一般戦略ページを本文化。段階分解テンプレ、対応表、二段階/三段階例、誤り対策を追加。 |
| `physics_tower/01_dynamics/part04_applications/03_checklist.md` | DONE | 2026-02-15 | 複合保存則問題のチェックリストを本文化。設計/立式/検算の実戦項目と答案テンプレを追加。 |
| `physics_tower/02_electromagnetism/00_overview.md` | CONTENT_REVIEWED | 2026-07-26 | 既存リバイズ。30段階へ拡張し、半導体device・memory・AI hardware・企業・量子準備ルートを追加。数式・link・図検査対象。 |
| `physics_tower/02_electromagnetism/part01_build_maxwell/README.md` | TECH_REVIEWED | 2026-07-26 | 内容リバイズ。章内位置、完成状態、前後ナビゲーションを追加。 |
| `physics_tower/02_electromagnetism/part01_build_maxwell/01_from_coulomb_to_gauss.md` | TECH_REVIEWED | 2026-07-26 | 内容リバイズ。電場定義、Gauss則の微分形、全電荷の条件、演習2問、導線を追加。 |
| `physics_tower/02_electromagnetism/part01_build_maxwell/02_faraday_law.md` | TECH_REVIEWED | 2026-07-26 | 既存リバイズ。固定/移動回路の正本を維持し、L・変圧器・発電機へ接続。演習既存2問、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part01_build_maxwell/03_ampere_maxwell.md` | TECH_REVIEWED | 2026-07-26 | 既存リバイズ。変位電流の正本から端子電流・KCL修正へ接続。演習既存2問、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part02_use_maxwell/README.md` | TECH_REVIEWED | 2026-07-26 | 内容リバイズ。章内位置、完成状態、前後ナビゲーションを追加。 |
| `physics_tower/02_electromagnetism/part02_use_maxwell/01_boundary_conditions.md` | TECH_REVIEWED | 2026-07-26 | 既存リバイズ。場の正本から容量・伝送線路の単位長さ定数へ接続。演習既存2問、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part02_use_maxwell/02_em_waves.md` | TECH_REVIEWED | 2026-07-26 | 既存リバイズ。波動正本から集中定数の限界・伝送線路へ接続。演習既存2問、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part02_use_maxwell/03_poynting_vector.md` | TECH_REVIEWED | 2026-07-26 | 既存リバイズ。Poynting定理正本からVI・抵抗/C/Lの閉曲面収支へ接続。演習既存2問、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part03_phenomenology/README.md` | TECH_REVIEWED | 2026-07-26 | 内容リバイズ。D=εEを条件付き構成方程式として明示し、完成状態と導線を更新。 |
| `physics_tower/02_electromagnetism/part03_phenomenology/01_dielectrics.md` | QA_PASS | 2026-07-26 | 既存リバイズ。分極正本から容量・切替問題へ接続。平行板と固定Q/V例、演習既存8問、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part03_phenomenology/02_conductors_and_skin_effect.md` | QA_PASS | 2026-07-26 | 既存リバイズ。導体正本からρL/Aと交流抵抗へ接続。表皮深さ例、演習既存8問、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part03_phenomenology/03_radiation_basics.md` | QA_PASS | 2026-07-26 | 既存リバイズ。放射正本から放射抵抗・指向性・偏波・給電へ接続。演習既存8問、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part04_from_fields_to_circuits/README.md` | QA_PASS | 2026-07-26 | 新規本文化。場→端子量→RLC→Kirchhoff則の縮約図と9記事導線。演習0、数式・リンク・Mermaid検査通過。 |
| `physics_tower/02_electromagnetism/part04_from_fields_to_circuits/01_voltage_from_electric_field.md` | QA_PASS | 2026-07-26 | 新規本文化。電場線積分から電圧、誘導時の経路依存、電池端子例。演習6問＋全解答、数式・リンク・図検査通過。 |
| `physics_tower/02_electromagnetism/part04_from_fields_to_circuits/02_current_from_current_density.md` | QA_PASS | 2026-07-26 | 新規本文化。電流密度の断面積分、連続の式、ドリフトと信号速度。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part04_from_fields_to_circuits/03_resistance_from_local_ohms_law.md` | QA_PASS | 2026-07-26 | 新規本文化。局所Ohm則から抵抗率・長さ・断面積、銅線例、表皮効果。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part04_from_fields_to_circuits/04_capacitance_from_gauss_and_dielectrics.md` | QA_PASS | 2026-07-26 | 新規本文化。Gauss則・誘電体から容量、固定Q/V、88.5 pF例。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part04_from_fields_to_circuits/05_inductance_from_flux_and_faraday.md` | QA_PASS | 2026-07-26 | 新規本文化。磁束鎖交・Faraday則から自己/相互L、コア損失。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part04_from_fields_to_circuits/06_kirchhoff_laws_from_maxwell.md` | QA_PASS | 2026-07-26 | 新規本文化。連続の式からKCL、Faraday則からKVL、節点蓄積例。演習6問＋全解答、数式・リンク・図検査通過。 |
| `physics_tower/02_electromagnetism/part04_from_fields_to_circuits/07_lumped_element_approximation.md` | QA_PASS | 2026-07-26 | 新規本文化。寸法/波長・遅延/立上り、基板配線例、寄生成分。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part04_from_fields_to_circuits/08_power_and_poynting_flow.md` | QA_PASS | 2026-07-26 | 新規本文化。閉曲面流束からVI、抵抗/C/Lへのエネルギー流、2.5 W例。演習6問＋全解答、数式・リンク・図検査通過。 |
| `physics_tower/02_electromagnetism/part04_from_fields_to_circuits/09_when_circuit_theory_breaks_down.md` | QA_PASS | 2026-07-26 | 新規本文化。反射・放射・クロストーク・EMC・損失から場へ戻る判断。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/README.md` | QA_PASS | 2026-07-26 | 新規本文化。大学受験、工学初年級、高周波・電力・機器の3層と12記事導線。演習0、リンク検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/01_series_parallel_and_equivalent_resistance.md` | QA_PASS | 2026-07-26 | 新規本文化。KCL/KVLから直並列、内部抵抗、6Ω/3Ω例。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/02_voltage_divider_and_current_divider.md` | QA_PASS | 2026-07-26 | 新規本文化。分圧・分流、計器負荷、センサー、10 kΩ例。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/03_capacitors_in_series_and_parallel.md` | QA_PASS | 2026-07-26 | 新規本文化。直並列C、切替、電荷保存、失われる静電エネルギー。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/04_rc_charging_and_discharging.md` | QA_PASS | 2026-07-26 | 新規本文化。RC方程式、時定数、初期/定常、充電エネルギー。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/05_rl_transient_response.md` | QA_PASS | 2026-07-26 | 新規本文化。RL時定数、電流連続、遮断高電圧、フライバック。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/06_lc_and_rlc_oscillation.md` | QA_PASS | 2026-07-26 | 新規本文化。場エネルギー交換、固有振動、減衰、力学対応。演習6問＋全解答、数式・リンク・図検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/07_ac_impedance_and_phasors.md` | QA_PASS | 2026-07-26 | 新規本文化。exp(-iωt)のRLCインピーダンス、過渡/定常、1 kHz例。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/08_resonance_power_and_power_factor.md` | QA_PASS | 2026-07-26 | 新規本文化。共振、Q、半値幅、P/Q/S、力率と送電損失。exp(-iωt)で誘導性Qを正とする複素電力符号を明記。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/09_mutual_inductance_and_transformers.md` | QA_PASS | 2026-07-26 | 新規本文化。相互誘導、巻数比、負荷反映、銅損/鉄損、送電図。演習6問＋全解答、数式・リンク・図検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/10_motors_generators_and_back_emf.md` | QA_PASS | 2026-07-26 | 新規本文化。Lorentzトルク、発電、逆起電力、始動・回生例。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/11_transmission_lines_as_distributed_circuits.md` | QA_PASS | 2026-07-26 | 新規本文化。電信方程式、Z0、反射、終端、Poynting対応。演習6問＋全解答、数式・リンク・図検査通過。 |
| `physics_tower/02_electromagnetism/part05_circuit_applications/12_antennas_and_radiation_connection.md` | QA_PASS | 2026-07-26 | 新規本文化。双極子正本から放射抵抗・指向性・偏波・受信へ接続。演習6問＋全解答、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/qa/README.md` | QA_PASS | 2026-07-26 | 新規本文化。概念・解法選択・計算検算の診断フローと子記事導線を整備。 |
| `physics_tower/02_electromagnetism/qa/01_common_misconceptions.md` | QA_PASS | 2026-07-26 | 既存リバイズ。既存14概念に電圧・電流・RLC・Kirchhoff近似の誤解を追加。演習既存6問、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/qa/02_problem_selection.md` | QA_PASS | 2026-07-26 | 既存リバイズ。直流/過渡/交流と集中/分布の分岐、受験解法導線を追加。演習既存8問、数式・リンク検査通過。 |
| `physics_tower/02_electromagnetism/qa/03_units_and_signs.md` | QA_PASS | 2026-07-26 | 新規本文化。SI単位、面/周回規約、境界条件、exp(-iωt)、演習8問＋全解答を追加。 |
| `physics_tower/02_electromagnetism/qa/04_high_school_circuit_problem_strategy.md` | QA_PASS | 2026-07-26 | 新規本文化。受験頻出12テーマ対応表、モデル選択、捨てた場の情報。演習6問＋全解答、リンク・図検査通過。 |
| `physics_tower/02_electromagnetism/qa/05_engineering_application_map.md` | QA_PASS | 2026-07-26 | 新規本文化。場→回路→機器・送電・高周波の地図と10_circuits境界。演習6問＋全解答、リンク・図検査通過。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/README.md` | STRUCTURE_QA_PASS | 2026-07-26 | ユーザー指定一括batchの新規本文化。場→電荷→deviceの図、古典／量子境界、12記事導線。演習0、link・Mermaid検査対象。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/01_why_semiconductors_need_em_and_quantum.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。電磁気／量子統計の分業、導電率例、演習6問＋全解答。内容・符号・link・TeX検査対象。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/02_electric_potential_and_carrier_control.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。電子energyの符号、gate容量、2.15e16 m^-2例、演習6問＋全解答。量子境界・数式検査対象。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/03_poisson_equation_in_semiconductors.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。固定ion＋carrier、空乏近似、0.70 V例、演習6問＋全解答。Poisson符号・単位検査対象。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/04_drift_diffusion_and_current.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。drift/diffusionと局所Ohm則、1.60e4 A/m2例、演習6問＋全解答。電子／慣用電流検査対象。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/05_doping_depletion_and_junction_fields.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。donor/acceptor・空乏幅・内蔵場、濃度比例、演習6問＋全解答。carrier密度は統計へ保留。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/06_pn_junction_as_an_electrostatic_structure.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。拡散／drift平衡・bias・2.1 pF接合容量、演習6問＋全解答。図・降伏・量子境界検査対象。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/07_diode_from_field_to_terminal_model.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。非線形IV、小信号25.9Ω、整流・保護、演習6問＋全解答。式導出は統計輸送へ保留。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/08_mos_capacitor.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規中心記事。蓄積・空乏・反転、5nm膜2e8 V/m例、演習8問＋全解答。界面・破壊・符号検査対象。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/09_mosfet_as_a_field_controlled_switch.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規中心記事。4端子・channel・長channel式・0.18mA例、演習8問＋全解答。微細化は量子へ保留。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/10_device_capacitance_leakage_and_breakdown.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。gate/接合/配線容量、漏れ・high-k・2.56µW例、演習6問＋全解答。信頼性範囲検査対象。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/11_switching_energy_and_rc_delay.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。CV2、13.8ps、6.4fJ、電圧／漏れtrade-off、演習6問＋全解答。Poynting・RC link検査対象。 |
| `physics_tower/02_electromagnetism/part06_semiconductor_bridge/12_limits_of_the_classical_picture.md` | CONTENT_REVIEWED | 2026-07-26 | 新規。band・tunnel・閉じ込め・ballistic・離散揺らぎの境界。演習6問＋全解答、量子／統計導線検査対象。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/README.md` | STRUCTURE_QA_PASS | 2026-07-26 | 新規。物理→device→system→企業の階層図と13記事導線。演習0、link・Mermaid検査対象。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/01_logic_memory_and_storage.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。register/SRAM/DRAM/HBM/NAND/SSD/HDD比較、100GB転送例、演習6問＋全解答。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/02_cmos_logic_and_gpu_switching.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。MOS→CMOS→GPU、0.167 FLOP/byte例、演習6問＋全解答。Logic Tower相互link・図検査対象。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/03_sram_and_cache.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。6T cell・双安定・cache、32MiBで16.1億T例、演習6問＋全解答。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/04_dram_as_a_transistor_capacitor_cell.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規中心記事。1T1C・sense・refresh、24fC/15万電子例、演習8問＋全解答。図・電荷共有検査対象。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/05_nand_flash_and_floating_gate_or_charge_trap.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。電荷保持・Vt・SLC〜QLC・3D NAND、0.80V例、演習8問＋全解答。tunnelは量子へ保留。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/06_ssd_controller_and_nand_system.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。controller/ECC/FTL/GC、3.2GB/s例、演習6問＋全解答。NAND dieとの差・図検査対象。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/07_hbm_and_vertical_integration.md` | SOURCE_VERIFIED | 2026-07-26 | 新規中心記事。DRAM積層・TSV・1024bit/409.6GB/s例、演習8問＋全解答。Micron公式資料確認、図・熱境界検査対象。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/08_gpu_memory_bandwidth_and_ai.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。roofline・parameter/activation/KV cache、40TFLOP/s例、演習6問＋全解答。data path図検査対象。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/09_interconnects_signal_integrity_and_power.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。反射・crosstalk・PDN・eye、0.5nH/10A/ns例、演習6問＋全解答。伝送線路link検査対象。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/10_packaging_tsv_chiplets_and_thermal_limits.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。die/package/interposer/TSV/2.5D/3D、24K例、演習6問＋全解答。熱は熱力学へ保留。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/11_semiconductor_manufacturing_overview.md` | CONTENT_REVIEWED | 2026-07-26 | 新規。酸化・成膜・露光・etch・implant・anneal・配線・test、膜厚2%例、演習6問＋全解答。化学導線。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/12_company_map_kioxia_micron_skhynix_nvidia.md` | SOURCE_VERIFIED | 2026-07-26 | 新規。4社を製品・役割・物理・device・実装・接続・誤解で整理。演習8問＋全解答。公式一次資料・確認日2026-07-26。 |
| `physics_tower/02_electromagnetism/part07_semiconductor_products/13_from_device_physics_to_ai_datacenter.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規。MOSFET→GPU→HBM/network/SSD→rack、860kW例、演習8問＋全解答。階層図・電力検査対象。 |
| `physics_tower/02_electromagnetism/qa/06_semiconductor_common_misconceptions.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規Q&A。古典／量子、空乏、gate、電子符号、NAND/HBM誤解。演習6問＋全解答。 |
| `physics_tower/02_electromagnetism/qa/07_memory_product_comparison.md` | EXERCISE_REVIEWED | 2026-07-26 | 新規Q&A。SRAM/DRAM/HBM/NAND/SSD選択。固有判断問題8問＋全解答。 |
| `physics_tower/02_electromagnetism/qa/08_semiconductor_company_value_chain.md` | SOURCE_VERIFIED | 2026-07-26 | 新規Q&A。design/fab/package/memory/system分業図。企業配置8問＋全解答、公式一次資料の扱いを明記。 |
| `physics_tower/02_electromagnetism/remedial/README.md` | QA_PASS | 2026-07-26 | 新規本文化。数学の一般論と重複せず、止まった操作から3補習へ戻る診断フローを整備。 |
| `physics_tower/02_electromagnetism/remedial/01_vector_calc_for_em.md` | QA_PASS | 2026-07-26 | 新規本文化。grad/div/curl、Gauss/Stokes、Laplacian、Maxwell使用箇所、演習6問＋全解答。 |
| `physics_tower/02_electromagnetism/remedial/02_ode_pde_refresh.md` | QA_PASS | 2026-07-26 | 新規本文化。Poisson/Laplace/波動/拡散、境界条件、変数分離、平面波、演習6問＋全解答。 |
| `physics_tower/02_electromagnetism/remedial/03_complex_representation_ac.md` | QA_PASS | 2026-07-26 | 新規本文化。複素振幅、位相、インピーダンス、複素誘電率/波数、損失、演習7問＋全解答。 |
| `physics_tower/03_analytical_mechanics/00_overview.md` | TODO | - |  |
| `physics_tower/03_analytical_mechanics/part01_supplements/README.md` | TODO | - |  |
| `physics_tower/03_analytical_mechanics/part02_basics/README.md` | TODO | - |  |
| `physics_tower/03_analytical_mechanics/part03_variational/README.md` | TODO | - |  |
| `physics_tower/03_analytical_mechanics/part04_gateway_to_qm/README.md` | TODO | - |  |
| `physics_tower/03_analytical_mechanics/part05_infinite_dof/README.md` | TODO | - |  |
| `physics_tower/03_analytical_mechanics/part06_canonical_em/README.md` | TODO | - |  |
| `physics_tower/03_analytical_mechanics/part07_constraints/README.md` | TODO | - |  |
| `physics_tower/04_thermodynamics/00_overview.md` | TODO | - |  |
| `physics_tower/04_thermodynamics/part01_laws/README.md` | TODO | - |  |
| `physics_tower/04_thermodynamics/part02_phenomenology/README.md` | TODO | - |  |
| `physics_tower/05_statistical_mechanics/00_overview.md` | TODO | - |  |
| `physics_tower/05_statistical_mechanics/part01_kinetic_theory/README.md` | TODO | - |  |
| `physics_tower/05_statistical_mechanics/part02_classical_ensembles/README.md` | TODO | - |  |
| `physics_tower/06_relativity/00_overview.md` | TODO | - |  |
| `physics_tower/06_relativity/part01_special/README.md` | TODO | - |  |
| `physics_tower/06_relativity/part02_coordinate_transform/README.md` | TODO | - |  |
| `physics_tower/06_relativity/part03_practice/README.md` | TODO | - |  |
| `physics_tower/06_relativity/part04_gr_intro/README.md` | TODO | - |  |
| `physics_tower/06_relativity/part05_riemann_geometry/README.md` | TODO | - |  |
| `physics_tower/06_relativity/part06_tests/README.md` | TODO | - |  |
| `physics_tower/06_relativity/part07_free_study/README.md` | TODO | - |  |
| `physics_tower/06_relativity/qa_special/README.md` | TODO | - |  |
| `physics_tower/07_quantum_mechanics/00_overview.md` | TODO | - |  |
| `physics_tower/07_quantum_mechanics/part01_mysteries/README.md` | TODO | - |  |
| `physics_tower/07_quantum_mechanics/part02_matrix_formalism/README.md` | TODO | - |  |
| `physics_tower/07_quantum_mechanics/part03_angular_momentum_spin/README.md` | TODO | - |  |
| `physics_tower/07_quantum_mechanics/part04_relativistic_qm/README.md` | TODO | - |  |
| `physics_tower/07_quantum_mechanics/part05_many_body/README.md` | TODO | - |  |
| `physics_tower/07_quantum_mechanics/part06_via_analytical_mech/README.md` | TODO | - |  |
| `physics_tower/07_quantum_mechanics/part07_quantum_computing/README.md` | TODO | - |  |
| `physics_tower/07_quantum_mechanics/part08_quantum_chemistry/README.md` | TODO | - |  |
| `physics_tower/07_quantum_mechanics/remedial_room/README.md` | TODO | - |  |
| `physics_tower/08_elementary_particle/00_overview.md` | TODO | - |  |
| `physics_tower/08_elementary_particle/part01_basics/README.md` | TODO | - |  |
| `physics_tower/08_elementary_particle/part02_lagrangian_density/README.md` | TODO | - |  |
| `physics_tower/08_elementary_particle/part03_free_fields/README.md` | TODO | - |  |
| `physics_tower/08_elementary_particle/part04_interaction_perturbation/README.md` | TODO | - |  |
| `physics_tower/08_elementary_particle/part05_qed_intro/README.md` | TODO | - |  |
| `physics_tower/08_elementary_particle/part06_path_integral/README.md` | TODO | - |  |
| `physics_tower/09_fluid_mechanics/00_overview.md` | TODO | - |  |
| `physics_tower/09_fluid_mechanics/part01_basics/README.md` | TODO | - |  |
| `physics_tower/09_fluid_mechanics/part02_ideal_incompressible/README.md` | TODO | - |  |
| `physics_tower/09_fluid_mechanics/part03_ideal_compressible/README.md` | TODO | - |  |
| `physics_tower/09_fluid_mechanics/part04_viscous_incompressible/README.md` | TODO | - |  |
| `physics_tower/09_fluid_mechanics/part05_viscous_compressible/README.md` | TODO | - |  |
| `physics_tower/09_fluid_mechanics/part06_waves/README.md` | TODO | - |  |
| `physics_tower/10_circuits/00_overview.md` | TODO | - |  |
| `physics_tower/10_circuits/part01_basics/README.md` | TODO | - |  |
| `physics_tower/10_circuits/part02_dc/README.md` | TODO | - |  |
| `physics_tower/10_circuits/part03_ac/README.md` | TODO | - |  |
| `physics_tower/10_circuits/part04_semiconductors/README.md` | TODO | - |  |
| `physics_tower/11_chemistry/00_overview.md` | TODO | - |  |
| `physics_tower/11_chemistry/part01_basics_of_matter/README.md` | TODO | - |  |
| `physics_tower/90_topics_from_conversations/README.md` | TODO | - |  |
| `physics_tower/90_topics_from_conversations/brownian_motion_and_clt.md` | TODO | - |  |
| `physics_tower/90_topics_from_conversations/depth_from_binocular_disparity.md` | TODO | - |  |
| `physics_tower/90_topics_from_conversations/meissner_effect.md` | TODO | - |  |
| `physics_tower/PROGRESS.md` | DONE | 2026-02-14 | 進捗管理ルールと全mdキューを新規作成。次回以降は本表を単一の実行基準として利用。 |
