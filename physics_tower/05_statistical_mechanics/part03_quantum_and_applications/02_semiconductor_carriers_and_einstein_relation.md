# 半導体再訪：Fermi準位・状態密度・carrier密度

## 役割分担

- 量子力学：band energy
  $$
  E_c,E_v
  $$
  と状態密度を与える。
- 統計力学：各stateのFermi–Dirac占有を与える。
- 電磁気学・輸送：Poisson方程式、drift、diffusion、電流を与える。

## carrier密度

electron密度は

$$
n=\int_{E_c}^{\infty}g_c(E)f(E)\,dE
$$

hole密度は

$$
p=\int_{-\infty}^{E_v}g_v(E)[1-f(E)]\,dE
$$

です。

$$
f(E)=\frac1{e^{(E-\mu)/(k_BT)}+1}
$$

nondegenerate近似では

$$
n\simeq N_c e^{-(E_c-\mu)/(k_BT)}
$$

$$
p\simeq N_v e^{-(\mu-E_v)/(k_BT)}
$$

したがって

$$
np=n_i^2
$$

を得ます。

## dopingとFermi level

charge neutrality

$$
p+N_D^+=n+N_A^-
$$

とcarrier式を同時に解いてchemical potentialを決めます。dopingが直接electronを古典的に押し込むのではなく、許されたstate、ionization、占有、neutralityの組合せです。

## Einstein関係

nondegenerate equilibriumでdriftとdiffusionが相殺することから

$$
\frac D\mu=\frac{k_BT}{|q|}
$$

です。degenerate carrierではchemical potential勾配を使う一般化が必要です。

## 数値例

300 Kでは

$$
\frac{k_BT}{e}\simeq25.9\ \mathrm{mV}
$$

なので

$$
D\simeq0.0259\,\mu
$$

です。

## 演習と全解答

1. Fermi levelは一粒子energy levelそのものか。
   **解答**：平衡chemical potentialであり、必ず許容stateと一致する必要はありません。
2.
   $$
   E=\mu
   $$
   の占有を求めよ。
   **解答**：
   $$
   f=\frac12
   $$
3. n型でFermi levelは通常どちらへ動くか。
   **解答**：conduction band側へ近づきます。
4. Boltzmann近似の条件は何か。
   **解答**：
   $$
   E-\mu\gg k_BT
   $$
   で占有が小さいことです。
5. mobility
   $$
   0.10\ \mathrm{m^2/(V\,s)}
   $$
   のDを300 Kで求めよ。
   **解答**：
   $$
   D=2.59\times10^{-3}\ \mathrm{m^2/s}
   $$
6. tunneling currentを本ページで説明できるか。
   **解答**：占有は扱えますがtransition probabilityは量子力学が必要です。

## ナビゲーション

- 前：[量子統計](01_classical_limit_fermi_bose.md)
- 次：[応用map](03_modern_applications_map.md)
- 戻る：[半導体bridge](../../02_electromagnetism/part06_semiconductor_bridge/README.md)
