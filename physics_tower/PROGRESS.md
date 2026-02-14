# physics_tower 執筆進捗（PROGRESS）

## 運用ルール（このリポジトリ専用）
- ユーザーが **「次をお願いします」** とだけ指示した場合も、このファイルを最初に確認する。
- 優先順位は次の通り。
  1. `status=DOING` の行があれば、そのファイルを最優先で仕上げて `DONE` にする。
  2. `DOING` が無ければ、キュー先頭から最初の `TODO` を1件だけ選んで執筆する。
  3. 1回の実行で本文執筆は **必ず1ファイルのみ**。
- 執筆完了後は、この表の対象行を `DONE` に更新し、`last_updated` と `notes` を記録する。
- 次の `TODO` は同一実行内で `DOING` にしない（次回実行時に選ばれるよう `TODO` のまま残す）。
- 対象範囲は `physics_tower/` 配下のみ。
- 数式は原則として文章中に埋め込まず、独立行のブロック数式（`$$...$$`）で記述する。

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
| `physics_tower/00_physics_math_tools/linear_algebra/basics.md` | TODO | - |  |
| `physics_tower/00_physics_math_tools/vector_analysis/README.md` | TODO | - |  |
| `physics_tower/00_physics_math_tools/vector_analysis/nabla_identities.md` | TODO | - |  |
| `physics_tower/01_dynamics/00_overview.md` | TODO | - |  |
| `physics_tower/01_dynamics/columns_and_qa/README.md` | TODO | - |  |
| `physics_tower/01_dynamics/part01_momentum_conservation/README.md` | TODO | - |  |
| `physics_tower/01_dynamics/part02_energy_conservation/README.md` | TODO | - |  |
| `physics_tower/01_dynamics/part03_angular_momentum/README.md` | TODO | - |  |
| `physics_tower/01_dynamics/part04_applications/README.md` | TODO | - |  |
| `physics_tower/02_electromagnetism/00_overview.md` | TODO | - |  |
| `physics_tower/02_electromagnetism/part01_build_maxwell/README.md` | TODO | - |  |
| `physics_tower/02_electromagnetism/part02_use_maxwell/README.md` | TODO | - |  |
| `physics_tower/02_electromagnetism/part03_phenomenology/README.md` | TODO | - |  |
| `physics_tower/02_electromagnetism/qa/README.md` | TODO | - |  |
| `physics_tower/02_electromagnetism/remedial/README.md` | TODO | - |  |
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
