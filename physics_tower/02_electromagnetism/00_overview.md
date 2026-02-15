# 02_electromagnetism（電磁気学の全体像）

## 学習目標
- 電磁気学を「法則暗記」ではなく、場の方程式として統一的に理解できる。
- クーロン・アンペール・ファラデーの現象法則が、マクスウェル方程式へ統合される流れを説明できる。
- 問題を見るときに、
  $$
  \text{対称性} \rightarrow \text{積分形} \rightarrow \text{微分形}
  $$
  のどこで解くかを判断できる。

## 0. 導入：この章で何が変わるか

力学では「質点の運動」を追っていましたが、電磁気では主役が

$$
\mathbf{E},\ \mathbf{B}
$$

という場（空間に分布する量）へ移ります。

電荷や電流は場の源であり、場は再び電荷へ力を返します。この相互作用を最短でまとめるのがマクスウェル方程式です。

この章の狙いは、

- まず法則を作る（part01）
- 次に法則を使う（part02）
- 最後に現象へ接続する（part03）

という順で、「なぜその式を使うか」まで含めて理解することです。

---

## 1. 学習マップ

## 1.1 part01_build_maxwell（法則を組み立てる）

ここでは、経験法則を統一してマクスウェル方程式へ到達します。

- [part01_build_maxwell/README.md](part01_build_maxwell/README.md)
- [part01_build_maxwell/01_from_coulomb_to_gauss.md](part01_build_maxwell/01_from_coulomb_to_gauss.md)
- [part01_build_maxwell/02_faraday_law.md](part01_build_maxwell/02_faraday_law.md)
- [part01_build_maxwell/03_ampere_maxwell.md](part01_build_maxwell/03_ampere_maxwell.md)

## 1.2 part02_use_maxwell（法則を使う）

境界条件・波動方程式・ポインティングベクトルなど、解法としてのマクスウェルを扱います。

- [part02_use_maxwell/README.md](part02_use_maxwell/README.md)

## 1.3 part03_phenomenology（現象へ接続）

誘電体・導体・回路近似・電磁波など、現実の見え方へつなぎます。

- [part03_phenomenology/README.md](part03_phenomenology/README.md)

## 1.4 qa / remedial

- つまずき整理： [qa/README.md](qa/README.md)
- 補助復習： [remedial/README.md](remedial/README.md)

---

## 2. まず押さえる4本柱（マクスウェル方程式）

SI単位系での微分形は

$$
\nabla\cdot\mathbf{E}=\frac{\rho}{\varepsilon_0}
$$

$$
\nabla\cdot\mathbf{B}=0
$$

$$
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}
$$

$$
\nabla\times\mathbf{B}=\mu_0\mathbf{J}+\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
$$

です。

初心者向けに言い換えると、

1. 電荷は電場の湧き出し源。
2. 磁場は単独磁荷を持たず閉じた線を作る。
3. 時間変化する磁場は渦電場を作る。
4. 電流と時間変化する電場は渦磁場を作る。

という4つの主張です。

---

## 3. 問題の解き方（最短フロー）

電磁気の計算は次の手順に固定すると安定します。

1. 対称性を判定（球・円筒・平面・一様）。
2. 積分形か微分形かを決める。
3. 既知境界条件を列挙する。
4. 単位・次元を検算する。

特にガウスの法則とアンペールの法則は、対称性が高いときに最短で効きます。

---

## 4. 力学との接続ポイント

- 力学での保存則は「運動量・エネルギー」。
- 電磁気ではこれに加えて、場のエネルギーとエネルギー流（ポインティングベクトル）が主役になる。

ローレンツ力

$$
\mathbf{F}=q(\mathbf{E}+\mathbf{v}\times\mathbf{B})
$$

を通じて、力学章との接続が成立します。すなわち、電磁気章は「場を求める章」であり、力学は「その場でどう動くかを見る章」と役割分担できます。

---

## 5. 典型的な誤解

1. 4本の方程式を別々に暗記してしまう。
   - 連続の式や波動方程式で相互整合を見ると理解が定着する。
2. 積分形と微分形を混同する。
   - 局所情報か、領域全体情報かを先に判定する。
3. 記号の単位を追わない。
   -
   $$
   [\mathbf{E}], [\mathbf{B}], [\rho], [\mathbf{J}]
   $$
   を常に確認する。

---

## 6. この章の進め方（実運用）

- 1回の作業で本文は1ファイルずつ本文化する。
- 次ファイルは `physics_tower/PROGRESS.md` の先頭 `TODO` に従う。
- 新章突入時に用意したスケルトンを順番に育て、READMEで導線を維持する。

この運用により、別の担当AIが入っても進行状態を再現しやすくなります。

---

## まとめ

- 電磁気学は「場の方程式」を中心にした統一理論である。
- 本章では、

$$
\text{法則を作る} \rightarrow \text{法則を使う} \rightarrow \text{現象へつなぐ}
$$

の順で学ぶ。

- まずは part01 のスケルトン群から順に本文化し、マクスウェル方程式の成立過程を丁寧に固める。
