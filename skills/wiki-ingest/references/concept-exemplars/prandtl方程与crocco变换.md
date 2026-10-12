---
address: c-000024
type: concept
title: "Prandtl 方程与 Crocco 变换"
status: developing
created: 2026-09-26
updated: 2026-09-26
tags:
  - concept
  - boundary-layer
  - prandtl
  - crocco-transform
  - hypoellipticity
complexity: advanced
domain: 偏微分方程
aliases:
  - Prandtl equations
  - boundary layer equations
  - Crocco transform
related:
  - "[[Jia-Lei-Yuan-2026-prandtl-global|Jia–Lei–Yuan（2026）整体适定性]]"
  - "[[静力近似与静力极限|静力近似与静力极限]]"
  - "[[primitive-equations原始方程|primitive equations（原始方程）]]"
  - "[[Gerard-Varet-Masmoudi-Vicol-2020-gevrey-hydrostatic|Gérard–Varet–Masmoudi–Vicol（2020）]]"
  - "[[Paicu-Zhang-Zhang-2020-hydrostatic-thin-strip|Paicu–Zhang–Zhang（2020）]]"
sources:
  - "[[Jia-Lei-Yuan-2026-prandtl-global|Jia–Lei–Yuan（2026）]]"
---

# Prandtl 方程与 Crocco 变换

## 模型

非定常 **Prandtl 边界层方程**描述高 Reynolds 数流中固体壁面附近的薄剪切层（Navier–Stokes 黏性消失极限的边界层方程）：

$$
\partial_tu+u\partial_xu+v\partial_yu-\partial_y^2u+\partial_xp=0,\qquad
\partial_xu+\partial_yv=0,\qquad
u|_{y=0}=v|_{y=0}=0,\quad \lim_{y\to\infty}u=U(t,x),
$$

外流满足 Bernoulli 律。与静力系统（见 [[静力近似与静力极限|静力近似与静力极限]]，有限带/周期域）同为"垂直速度非局部恢复 + 切向导数损失"的退化结构，但 Prandtl 定义在半空间、匹配外流。无结构性假设时 Sobolev 适定性不可能（Gérard-Varet–Dormy 病态；有限时间奇性），故理论围绕**Oleinik 单调性** $\partial_yu>0$ 展开。

## Crocco 变换

单调性允许以速度为垂直坐标：$\eta=u(t,x,y)$、$w(\tau,\xi,\eta)=\partial_yu$，逆变换 $y=\int_0^u d\eta/w$。Prandtl 方程等价化为半空间上的**拟线性超抛物方程**

$$
\partial_\tau w+\eta\,\partial_\xi w-w^2\,\partial_\eta^2w=0 ,
$$

（$v:=w^{-1}$ 时为散度型守恒律结构）——消除 $x$ 方向导数损失的关键。线性化模型是 **Kolmogorov 算子** $\mathcal L_0=\partial_t+y\partial_x-\partial_y^2$（Hörmander 亚椭圆；各向异性伸缩 $t\sim L^2$、$x\sim L^3$、$y\sim L$）。

## 结果版图（按已摄入来源）

| 结果 | 内容 | 来源 |
|---|---|---|
| 整体经典适定性（无小性） | 单调数据 + 多项式/指数/Gauss 匹配速率（含 Blasius）⇒ 任意 $T,X$ 的唯一整体经典解；解决 Oleinik–Samokhin Question 4 | [[Jia-Lei-Yuan-2026-prandtl-global|Jia–Lei–Yuan 2026，Theorem 1.2]] |
| 到达边界的光滑化 | 弱解 + 局部一致单调界 ⇒ $C^\infty$ 直达 $y=0$ | [[Jia-Lei-Yuan-2026-prandtl-global|Jia–Lei–Yuan 2026，Theorem 1.1]] |
| 整体弱解与唯一性类 | 相容性降至 3 阶；唯一性在 $(1-y)^k\lesssim w\lesssim(1-y)\log^{1/2}$ 类；推广 Xin–Zhang–Zhao（精确指数速率）到三类速率 | [[Jia-Lei-Yuan-2026-prandtl-global|Jia–Lei–Yuan 2026，Theorem 1.3、Prop 7.1]] |

未摄入的版图（据该文综述）：Oleinik 的局部经典解（先行理论）；Xin–Zhang / Xin–Zhang–Zhao 的整体弱解；Gérard-Varet–Dormy 的无单调性不适定；E–Engquist 的爆破；Gevrey 框架适定性（Li–Masmoudi–Yang 等，最优指数 2）；稳态 Blasius 剖面的 sharp 渐近稳定性（Jia–Lei–Yuan, Adv. Math. 2025）。

## 方法要点

[[Jia-Lei-Yuan-2026-prandtl-global|Jia–Lei–Yuan 2026]] 的工具箱：半空间 Neumann Kolmogorov 基本解的构造与**正性**（$\Gamma>0\iff x>x_0$，单向输运；enhanced dissipation $e^{-c|\xi|^{2/3}t}$ 的 Gearhart–Prüss 预解式估计）；De Giorgi–Nash–Moser/Kruzkov 边界方案；$W^{2,p}_y$ 理论；Hörmander 亚椭圆 bootstrap（指标 $1/3$ 最优）；权 $w^{-2}$ 加权能量 + Beale–Kato–Majda 型延拓准则；逼近系统 $(w^\epsilon+\epsilon)^2$ 的极值原理。

## 与本库其他主题的关系

- **[[静力近似与静力极限|静力近似与静力极限]]**：NS 的两个奇异极限方向——薄域（→PE/静力系统）与黏性消失（→Prandtl/Euler）；"reduced NS"一词即指 Dirichlet 带上的 hydrostatic NS 与 Prandtl 的家族相似性。[[Paicu-Zhang-Zhang-2020-hydrostatic-thin-strip|Paicu–Zhang–Zhang 2020]] 明言 Prandtl 本身的整体结果当时 open（只有 lifespan 下界）——[[Jia-Lei-Yuan-2026-prandtl-global|Jia–Lei–Yuan 2026]] 在单调类中补上这一缺口。
- **[[primitive-equations原始方程|primitive equations]]**：对照哲学——PE 无结构性小性即整体适定（Cao–Titi）；Prandtl 靠单调性换无小性整体适定性；无单调性时 Prandtl 强病态而 PE 无此障碍。
- enhanced dissipation / Gearhart–Prüss 工具与 [[Jiang-Wang-2025-primitive-bifurcation|Jiang–Wang 2025]] 的谱分析、[[Dong-Li-Sun-2026-IINS-gravity-stability|Dong–Li–Sun 2026]] 的衰减分析同源。
