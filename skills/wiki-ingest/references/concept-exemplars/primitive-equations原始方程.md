---
address: c-000010
type: concept
title: "primitive equations（原始方程）"
status: developing
created: 2026-09-24
updated: 2026-09-28
tags:
  - concept
  - model
  - geophysical-fluid-dynamics
complexity: intermediate
domain: 偏微分方程
aliases:
  - Primitive equations
  - 原始方程
  - PE
  - hydrostatic primitive equations
related:
  - "[[Cao-Titi-2007-primitive-equations-3d|Cao–Titi（2007）三维整体适定性]]"
  - "[[Petcu-Temam-Wirosoetisno-2004-primitive-2d|Petcu 等（2004）二维正则性]]"
  - "[[Wang-Jiu-Xu-2021-nonhomogeneous-primitive-2d|Wang–Jiu–Xu（2021）非齐次含真空]]"
  - "[[Jiu-Ma-Wang-2025-nonhomogeneous-primitive-ddv|Jiu–Ma–Wang（2025）密度依赖黏性]]"
  - "[[Jiang-Wang-2025-primitive-bifurcation|Jiang–Wang（2025）稳定性与分岔]]"
  - "[[稳定分层与-rayleigh-taylor-判据|稳定分层与 Rayleigh–Taylor 判据]]"
  - "[[Dong-Li-Sun-2026-IINS-gravity-stability|Dong–Li–Sun（2026）重力驱动 IINS]]"
  - "[[静力近似与静力极限|静力近似与静力极限]]"
  - "[[prandtl方程与crocco变换|Prandtl 方程与 Crocco 变换]]"
  - "[[Bresch-Kazhikhov-Lemoine-2005-hydrostatic-ns-2d|Bresch 等（2005）2D 静水 NS]]"
  - "[[Renardy-2009-hydrostatic-illposedness|Renardy（2009）不适定性]]"
  - "[[Furukawa-2025-three-limits|Furukawa 等（2025）三种极限]]"
  - "[[Guo-Huang-Zhao-2023-free-boundary-PE|Guo–Huang–Zhao（2023）自由边界 PE]]"
sources:
  - "[[Cao-Titi-2007-primitive-equations-3d|Cao–Titi（2007）三维整体适定性]]"
  - "[[Petcu-Temam-Wirosoetisno-2004-primitive-2d|Petcu 等（2004）二维正则性]]"
  - "[[Wang-Jiu-Xu-2021-nonhomogeneous-primitive-2d|Wang–Jiu–Xu（2021）非齐次含真空]]"
  - "[[Jiu-Ma-Wang-2025-nonhomogeneous-primitive-ddv|Jiu–Ma–Wang（2025）密度依赖黏性]]"
  - "[[Jiang-Wang-2025-primitive-bifurcation|Jiang–Wang（2025）稳定性与分岔]]"
  - "[[Bresch-Kazhikhov-Lemoine-2005-hydrostatic-ns-2d|Bresch 等（2005）]]"
  - "[[Renardy-2009-hydrostatic-illposedness|Renardy（2009）]]"
  - "[[Furukawa-2025-three-limits|Furukawa 等（2025）]]"
  - "[[Leung-Wong-Xie-2024-steady-hydrostatic-euler|Leung–Wong–Xie（2024）稳态刚性]]"
  - "[[Bianchini-Duchene-2024-hydrostatic-limit-isopycnal|Bianchini–Duchêne（2024）]]"
---

# primitive equations（原始方程）

## 模型

primitive equations（PE，原始方程）是大尺度海洋/大气动力学的核心模型：对（Boussinesq 型）Navier–Stokes 方程施加**流体静力学近似**——以静力平衡

$$
\partial_z p = -g\rho \quad (\text{或变体，如 } \partial_z p + T = 0)
$$

替换垂直动量方程，再配以不可压条件与（各向异性的）黏性/热扩散。垂直速度 $w$ 不再是独立未知量，而由诊断关系 $w = -\int_{-h}^{z} \nabla\cdot v\,\mathrm{d}\xi$ 给出，从而引入**非局部非线性项** $(\int_0^z \partial_x v\,\mathrm{d}\xi)\partial_z v$（Ladyzhenskaya 不等式失效的根源）。数学理论由 Lions–Temam–Wang（弱解）开创，[[Cao-Titi-2007-primitive-equations-3d|Cao–Titi（2007）]] 的三维整体强解是奠基性结果。

## 静力近似的合法性（2026-09-26 补全）

PE 作为数学对象由**静力极限**的严格化支撑，详见 [[静力近似与静力极限|静力近似与静力极限]]。要点：

- **标度分类学**（[[Furukawa-2025-three-limits|Furukawa 等 2025]]）：垂直黏度 $\nu_z=\varepsilon^\gamma$ 下，$\gamma<2$ 极限是 2D Navier–Stokes、$\gamma=2$（临界）是全黏性 PE、$\gamma>2$ 是仅水平黏性 PE——**全黏性 PE 只是临界情形**。
- **适定性分界**：各向同性黏性下 2D 静水系统 Sobolev 整体适定（[[Bresch-Kazhikhov-Lemoine-2005-hydrostatic-ns-2d|Bresch 等 2005]]，但黏性与渐近标度不一致）；渐近一致的仅垂直黏性情形存在线性 Hadamard 不适定（[[Renardy-2009-hydrostatic-illposedness|Renardy 2009]]）——**水平黏性/扩散是 PE 整体适定性的本质正则化**，凸性+Gevrey（GMV 2020、Paicu–Yu–Zhu 2024）、解析性（Paicu–Zhang–Zhang 2020）、磁场（Wang–Wang 2022）是抑制机制。开放问题见 [[仅垂直黏性静力方程的sobolev适定性|仅垂直黏性静力方程的 Sobolev 适定性]]。
- **无黏端**：稳态 PE 有 Liouville 型刚性（[[Leung-Wong-Xie-2024-steady-hydrostatic-euler|Leung–Wong–Xie 2024]]：条带域远离滞止点的稳态解必为剪切流）；无黏非稳态整体理论不可得。
- **无黏+扩散端**：等密度面坐标 + Gent–McWilliams 扩散的水静系统局部适定、水静极限最优率 $O(\mu)$（[[Bianchini-Duchene-2024-hydrostatic-limit-isopycnal|Bianchini–Duchêne 2024]]）。

## 结构特征

- **正压/斜压分解**：$\overline v = \frac1h\int_{-h}^0 v\,\mathrm{d}\xi$（正压模态，二维系统）、$\widetilde v = v - \overline v$（斜压模态）。**斜压方程不含压力项**（Cao–Titi Remark 2）——这是 PE 相对三维 Navier–Stokes 的决定性结构优势，使 $L^6$ 估计（$|\widetilde v|^4\widetilde v$ 检验函数）可行，进而无小性条件的整体强解成为可能。该分解也被 [[Furukawa-2025-three-limits|Furukawa 等 2025]] 用于证明 $\delta\to\infty$ 时收敛到 2D NS。
- **分层能量链**：$L^2 \to L^6 \to H^1$（或逐导数 $u_z \to u_x \to \cdots$ 的固定次序估计，[[Petcu-Temam-Wirosoetisno-2004-primitive-2d|Petcu 等 2004]]）+ 延拓，是本 vault 所有两类 PE 适定性证明的公共骨架；对照 [[双层能量法与插值衰减|双层能量法]]（后者多一层"插值换衰减"）。
- **hydrostatic Stokes 正则性**：以静力结构下的椭圆系统替代经典 Stokes 估计，是非齐次/变黏性情形（[[Wang-Jiu-Xu-2021-nonhomogeneous-primitive-2d|Wang 2021]]、[[Jiu-Ma-Wang-2025-nonhomogeneous-primitive-ddv|Jiu 2025]]）的线性工具。

## 结果版图（按已摄入来源）

| 情形 | 结果 | 来源 |
|---|---|---|
| 3D 全黏性（柱域，风驱动 + Robin 热） | 任意 $H^1$ 型初值整体唯一强解，无小性 | [[Cao-Titi-2007-primitive-equations-3d|Cao–Titi 2007]] |
| 2D 周期 + 对称（线性分层背景 $N^2 > 0$） | 弱解存在；强解全局唯一；任意 $H^m$ 与 $C^\infty$ 正则性 | [[Petcu-Temam-Wirosoetisno-2004-primitive-2d|Petcu 等 2004]] |
| 2D 非齐次、常黏性、允许真空 | 小 $H^{1/2}$ 速度初值整体唯一强解，$\|\nabla u\| \lesssim t^{-1/2}$ | [[Wang-Jiu-Xu-2021-nonhomogeneous-primitive-2d|Wang 等 2021]] |
| 2D 非齐次、密度依赖非退化黏性、允许真空 | 小 $\|\nabla u_0\|_{L^2}$ 整体唯一强解 + 指数衰减 | [[Jiu-Ma-Wang-2025-nonhomogeneous-primitive-ddv|Jiu–Ma–Wang 2025]] |
| 2D 全扩散、热强迫（滑移边界） | 临界温差 $T_c$ 显式；稳定/临界/不稳定三段式 + 超临界分岔环吸引子 | [[Jiang-Wang-2025-primitive-bifurcation|Jiang–Wang 2025（预印本）]] |
| 2D 静水 NS、各向同性黏性（变深度，底 Dirichlet） | $v_0\in H$、$\partial_zv_0\in L^2$ 整体唯一解；$v_0\in V$ 整体强解无小性 + 指数衰减 | [[Bresch-Kazhikhov-Lemoine-2005-hydrostatic-ns-2d|Bresch 等 2005]] |

来源提及但未摄入的版图（据其文献综述）：部分黏性情形（Cao–Li–Titi：仅垂直涡扩散 / 仅水平黏性——后者已由 [[Furukawa-2025-three-limits|Furukawa 等 2025]] 侧面摄入 PE_H 极限）、间断初值弱解唯一性（Li–Titi）、无黏 PE 的凸积分非唯一（Chiodaroli–Michálek）与三维无黏爆破（Collot–Ibrahim–Lin）、可压 PE、hydrostatic 极限的严格化早期工作（Lions–Temam–Wang、Azérad–Guillén、Li–Titi；Furukawa 等 2025 已入库）。

## 与本 vault 其他主题的关系

- **对 [[Dong-Li-Sun-2026-IINS-gravity-stability|重力驱动 IINS]]**：同一物理家族的不同近似层级——IINS 保留完整垂直动量方程与重力（$\rho \partial_t v_3 + \cdots = -\rho e_3$），PE 以静力平衡替换之。注意已摄入的非齐次 PE（Wang 2021、Jiu 2025）取 $\partial_z P = 0$ 且**无浮力反馈**，密度只通过惯性与黏性起作用，故不描述 Rayleigh–Taylor 型分层不稳定性；含浮力的对应模型（$\partial_z P = -g\rho$，CPE）尚未摄入。
- **对 [[稳定分层与-rayleigh-taylor-判据|稳定分层判据]]**：Petcu 等的背景线性分层 $N^2 > 0$ 与 Jiang–Wang 的边界温差 $T_0 - T_1$ 符号是分层稳定性判据在 PE 中的两种化身；Jiang–Wang 的 $T_c$ 阈值（Rayleigh–Bénard 机制）与 RT 判据（密度梯度符号）互补。无黏端对照见 [[Bianchini-Duchene-2024-hydrostatic-limit-isopycnal|Bianchini–Duchêne 2024]]（Miles–Howard/Richardson 判据下的适定性仍 open）。
- **对 [[双层能量法与插值衰减|双层能量法]]**：Cao–Titi/Petcu 的能量链是"无衰减"适定性路线；Wang 2021 与 Jiu 2025 的小性整体解带显式衰减（$t^{-1/2}$、指数），但由插值/加权得到，未做谱最优性分析——Jiang–Wang 的谱分析正是补足该缺口的一例。
- **对 [[prandtl方程与crocco变换|Prandtl 方程]]**：NS 奇异极限谱系的另一方向（黏性消失 vs 薄域）；两者共享切向导数损失结构，适定性策略（单调/凸性 vs 完全黏性）分道扬镳。

## 自由边界与热绝缘（2026-09-28 补全）

[[Guo-Huang-Zhao-2023-free-boundary-PE|Guo–Huang–Zhao 2023]]（JDE 371）：固定域谱系之外的自由表面版本——上边界 ζ 自由、底固定、热绝缘（N·∇Aθ=0，∂₃θ=0）；小初值（H⁴×|ζ|_{9/2}）唯一整体强解且 E(t)≲e^{−Ct}E(0)。新机制：自由面最高阶范数 |ζ|_{9/2} 由 ζ 的色散方程闭合（对照固定域理论的纯能量闭合）；跨项 ∫J̄wθ 由总温度守恒 + 自由面小性的 Poincaré 型不等式控制。
