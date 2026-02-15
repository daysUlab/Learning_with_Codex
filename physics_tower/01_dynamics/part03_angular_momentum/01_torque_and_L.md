# トルクと角運動量の基本式

## 学習目標
- 角運動量とトルクの定義をベクトルで扱える。
- 回転運動の基本方程式を導出できる。

## 1. 定義
位置

$$
\mathbf{r}
$$

運動量

$$
\mathbf{p}=m\mathbf{v}
$$

に対して角運動量は

$$
\mathbf{L}=\mathbf{r}\times\mathbf{p}
$$

トルクは

$$
\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}
$$

で定義される。

## 2. 運動方程式
時間微分すると

$$
\frac{d\mathbf{L}}{dt}
=\frac{d\mathbf{r}}{dt}\times\mathbf{p}+\mathbf{r}\times\frac{d\mathbf{p}}{dt}
$$

第一項は

$$
\mathbf{v}\times m\mathbf{v}=\mathbf{0}
$$

なので消え、

$$
\frac{d\mathbf{L}}{dt}=\mathbf{r}\times\mathbf{F}=\boldsymbol{\tau}
$$

を得る。

## 3. 保存条件
外力トルクがゼロなら

$$
\frac{d\mathbf{L}}{dt}=\mathbf{0}
$$

より

$$
\mathbf{L}=\text{const.}
$$

である。

## 4. 直観
線運動での「力が運動量を変える」に対応し、回転運動では「トルクが角運動量を変える」。
式の形が並行である点を意識すると理解が安定する。

## まとめ
- 回転問題の第一式は

$$
\frac{d\mathbf{L}}{dt}=\boldsymbol{\tau}
$$

である。
- 対称性が高い系では角運動量保存が強力な制約になる。
