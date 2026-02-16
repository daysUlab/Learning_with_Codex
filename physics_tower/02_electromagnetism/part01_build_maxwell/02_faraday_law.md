# ファラデーの法則と誘導電場

## 学習目標
- 磁束の時間変化と起電力の関係を積分形で説明できる。
- レンツの法則の符号を、エネルギー保存の観点で説明できる。
- ファラデーの法則の積分形と微分形を往復できる。

---

## 0. 導入

静電場では、電場は電荷が作るものでした。
一方、時間的に変化する磁場は、電荷がなくても渦状の電場を作ります。

この現象を定式化したのがファラデーの法則です。

$$
\mathcal{E}=\oint_C \mathbf{E}\cdot d\mathbf{l}=-\frac{d\Phi_B}{dt}
$$

ここで

$$
\Phi_B=\int_S \mathbf{B}\cdot d\mathbf{S}
$$

は回路

$$
C
$$

が張る面

$$
S
$$

を貫く磁束です。

---

## 1. 起電力と線積分

起電力

$$
\mathcal{E}
$$

は、単位電荷あたりに回路一周でなされる仕事として理解できます。
したがって電場の循環で表せます。

$$
\mathcal{E}=\oint_C \mathbf{E}\cdot d\mathbf{l}
$$

静電場では

$$
\oint_C \mathbf{E}\cdot d\mathbf{l}=0
$$

ですが、誘導電場では一般に 0 ではありません。
この違いが「電位差で記述できる電場」と「渦を持つ電場」の違いです。

---

## 2. レンツの法則と負号の意味

ファラデーの法則の負号

$$
-\frac{d\Phi_B}{dt}
$$

はレンツの法則を表します。

- 磁束が増えるなら、それを打ち消す向きの誘導電流が流れる。
- 磁束が減るなら、それを補う向きの誘導電流が流れる。

これはエネルギー保存則と整合しています。
もし増加をさらに増やす向きに流れるなら、外部仕事なしでエネルギーが増えてしまうためです。

---

## 3. 積分形から微分形へ

ストークスの定理

$$
\oint_C \mathbf{E}\cdot d\mathbf{l}=\int_S (\nabla\times\mathbf{E})\cdot d\mathbf{S}
$$

を用いると、ファラデーの法則は

$$
\int_S (\nabla\times\mathbf{E})\cdot d\mathbf{S}=-\int_S \frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{S}
$$

となります。任意の面

$$
S
$$

で成り立つので

$$
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}
$$

を得ます。
これが微分形です。

---

## 4. 例題

## 4.1 一様磁場が時間変化する円形領域

半径

$$
R
$$

の円板領域内で

$$
\mathbf{B}(t)=B(t)\hat{\mathbf{z}}
$$

とし、

$$
r<R
$$

の同心円周上の誘導電場を求めます。

対称性より、電場は接線方向で大きさ一定です。

$$
\oint_C \mathbf{E}\cdot d\mathbf{l}=E(r)\,2\pi r
$$

円周が囲む磁束は

$$
\Phi_B(r)=B(t)\pi r^2
$$

なので

$$
E(r)\,2\pi r=-\frac{d}{dt}\left(B\pi r^2\right)
$$

$$
E(r)=-\frac{r}{2}\frac{dB}{dt}
$$

となります。

## 4.2 回転導体棒の起電力（要点）

長さ

$$
\ell
$$

の導体棒が角速度

$$
\omega
$$

で回転し、

$$
\mathbf{B}=B\hat{\mathbf{z}}
$$

中にあるとき、半径位置

$$
r
$$

の速度は

$$
v=\omega r
$$

です。
ローレンツ力由来の有効電場

$$
|\mathbf{v}\times\mathbf{B}|=\omega r B
$$

を棒に沿って積分すると

$$
\mathcal{E}=\int_0^{\ell} \omega r B\,dr=\frac{1}{2}B\omega \ell^2
$$

を得ます。

---

## 5. よくある誤解

- 磁束が 0 なら常に起電力も 0 と考える。
  - 実際は磁束の時間変化が本質です。
- 負号を「式の暗記記号」として扱う。
  - 変化を打ち消す向きという物理意味で判定します。
- 誘導電場にもスカラー電位を常に定義できると考える。
  - 渦を持つため、一般には単一の電位差だけで表せません。

---

## 6. 演習問題

1. 半径

$$
R
$$

の円ループを貫く一様磁場が

$$
B(t)=B_0+\alpha t
$$

で増加するとき、起電力の大きさを求めよ。

2. 問1で

$$
\alpha>0
$$

のとき、誘導電流の向きをレンツの法則で説明せよ。

3. 微分形

$$
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}
$$

の左辺・右辺の単位が一致することを確認せよ。

4. 半径

$$
r<R
$$

の領域で

$$
E(r)=-\frac{r}{2}\frac{dB}{dt}
$$

となる導出を、面積分から再現せよ。

---

## 7. 演習解答

1. 磁束は

$$
\Phi_B=\pi R^2 B(t)
$$

より

$$
|\mathcal{E}|=\left|\frac{d\Phi_B}{dt}\right|=\pi R^2|\alpha|
$$

です。

2. 磁束が増える向きと反対向きの磁場を作る向きに誘導電流が流れます。
右ねじ則で回路向きを判定します。

3. 左辺は

$$
\nabla\times\mathbf{E}
$$

で

$$
\frac{\mathrm{V}}{\mathrm{m}^2}
$$

右辺は

$$
\frac{\partial\mathbf{B}}{\partial t}
$$

で

$$
\frac{\mathrm{T}}{\mathrm{s}}=\frac{\mathrm{V\,s}}{\mathrm{m}^2\mathrm{s}}=\frac{\mathrm{V}}{\mathrm{m}^2}
$$

となり一致します。

4. 半径

$$
r
$$

の円を積分路に取り、

$$
E(r)\,2\pi r=-\frac{d}{dt}(B\pi r^2)
$$

より

$$
E(r)=-\frac{r}{2}\frac{dB}{dt}
$$

です。

---

## まとめ

- ファラデーの法則は、磁束の時間変化が電場の循環を生む法則である。
- 負号はレンツの法則を表し、エネルギー保存の要請と一致する。
- 積分形と微分形を往復できると、対称性問題と場の局所方程式を同じ視点で扱える。
