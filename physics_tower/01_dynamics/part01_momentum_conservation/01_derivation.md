# 運動量保存の導出（多体系からの標準導出）

## 出発点

粒子

$$
i
$$

に対して

$$
\frac{d\mathbf{p}_i}{dt}=\mathbf{F}_i^{\text{ext}}+\sum_{j\neq i}\mathbf{F}_{ij}
$$

を置きます。

## 全粒子で総和

$$
\frac{d}{dt}\sum_i\mathbf{p}_i=\sum_i\mathbf{F}_i^{\text{ext}}+\sum_i\sum_{j\neq i}\mathbf{F}_{ij}
$$

内部力項は作用反作用

$$
\mathbf{F}_{ij}=-\mathbf{F}_{ji}
$$

により相殺されます。

したがって

$$
\frac{d\mathbf{P}}{dt}=\mathbf{F}_{\text{ext}}
$$

を得ます。

## 保存条件

外力の合力が

$$
\mathbf{F}_{\text{ext}}=\mathbf{0}
$$

なら

$$
\mathbf{P}=\text{const.}
$$

です。

## 積分形

時刻

$$
t_1
$$

から

$$
t_2
$$

まで積分すると

$$
\mathbf{P}(t_2)-\mathbf{P}(t_1)=\int_{t_1}^{t_2}\mathbf{F}_{\text{ext}}\,dt
$$

となり、右辺は外力の力積です。

## 使いどころ

- 衝突問題
- 爆発分裂問題
- 反作用推進問題

で特に有効です。

ただし、外力が大きい長時間過程にはそのまま適用できません。
