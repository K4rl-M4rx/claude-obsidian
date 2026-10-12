---
address: c-000039
type: concept
title: "Couette 流增强耗散与转捩阈值（enhanced dissipation and transition threshold）"
status: developing
created: 2026-09-26
updated: 2026-09-28
tags:
  - concept
  - couette-flow
  - enhanced-dissipation
  - inviscid-damping
  - transition-threshold
complexity: advanced
domain: 偏微分方程
aliases:
  - enhanced dissipation
  - inviscid damping
  - transition threshold
  - Orr echo chains
related:
  - "[[Grenier-2000-nonlinear-instability-euler-prandtl|Grenier（2000）非线性不稳定]]"
  - "[[Li-Masmoudi-Zhao-2025-couette-gevrey-threshold|Li–Masmoudi–Zhao（2025）阈值曲线]]"
  - "[[Masmoudi-Said-Houari-Zhao-2022-boussinesq-couette|MSZ（2022）无热扩散]]"
  - "[[Masmoudi-Zhai-Zhao-2023-boussinesq-finite-channel|MZZ（2023）有限通道]]"
  - "[[Masmoudi-Said-Houari-Zhao-2025-richardson-linear|MSZ（2025）线性 Richardson]]"
  - "[[Bian-Pu-2022-boussinesq-shear-threshold|Bian–Pu（2022）近 Couette 阈值]]"
  - "[[Ren-Wei-2026-stability-threshold-half|Ren–Wei（2026a）阈值 α=1/2]]"
  - "[[Ren-Wei-2026-transition-threshold-third|Ren–Wei（2026b）转捩阈值 α=1/3]]"
  - "[[Liang-Wu-Zhai-2026-general-viscosity-threshold|Liang–Wu–Zhai（2026）一般黏性]]"
  - "[[Zillinger-2023-echo-chains-traveling-waves|Zillinger（2023a）回声链]]"
  - "[[Zillinger-2023-inviscid-stability-traveling-waves|Zillinger（2023b）无黏估计]]"
  - "[[Niu-Wu-2025-tropical-climate-couette|Niu–Wu（2025）热带气候系统]]"
  - "[[Ding-Lin-2022-poiseuille-resolvent|Ding–Lin（2022）Poiseuille ν^{3/4}]]"
  - "[[Ding-Lin-2025-poiseuille-nu23-threshold|Ding–Lin（2025）Poiseuille ν^{2/3}]]"
  - "[[Chen-Li-2024-poiseuille-couette|Chen–Li（2024）混合流]]"
  - "[[Li-Luo-Luo-2025-vertical-dissipation|Li–Luo–Luo（2025）仅垂直耗散]]"
  - "[[Hou-Wang-Xing-2026-rotation-instability|Hou–Wang–Xing（2026）旋转失稳]]"
  - "[[Sinambela-Zhao-2025-shear-transition|Sinambela–Zhao（2025）谱阈值 m_*]]"
  - "[[谱判据与几何光学方法|谱判据与几何光学方法]]"
  - "[[双层能量法与插值衰减|双层能量法与插值衰减]]"
  - "[[稳定分层与-rayleigh-taylor-判据|稳定分层与 Rayleigh–Taylor 判据]]"
  - "[[Jia-Lei-Yuan-2026-prandtl-global|Jia–Lei–Yuan（2026）]]"
  - "[[Jiang-Wang-2025-primitive-bifurcation|Jiang–Wang（2025）]]"
  - "[[Li-Zhang-Zhang-2025a-tc-exterior-linear|Li–Zhang–Zhang（2025a）外域线性]]"
  - "[[Li-Zhang-Zhang-2025b-tc-exterior-nonlinear|Li–Zhang–Zhang（2025b）外域非线性]]"
  - "[[Li-Pan-Zhang-2022-slip-boundary|Li–Pan–Zhang（2022）滑移边界]]"
sources:
  - "[[Li-Masmoudi-Zhao-2025-couette-gevrey-threshold|Li–Masmoudi–Zhao（2025）]]"
  - "[[Masmoudi-Said-Houari-Zhao-2022-boussinesq-couette|MSZ（2022）]]"
  - "[[Grenier-2000-nonlinear-instability-euler-prandtl|Grenier（2000）]]"
  - "[[Ren-Wei-2026-transition-threshold-third|Ren–Wei（2026b）]]"
  - "[[Liang-Wu-Zhai-2026-general-viscosity-threshold|Liang–Wu–Zhai（2026）]]"
  - "[[Zillinger-2023-echo-chains-traveling-waves|Zillinger（2023a）]]"
  - "[[Niu-Wu-2025-tropical-climate-couette|Niu–Wu（2025）]]"
---

# Couette 流增强耗散与转捩阈值

## 概念

Couette 流 $u_s=(y,0)$ 是谱判据簇的**边界情形**：线性无黏谱稳定（Kelvin 解无增长、无拐点 ⇒ [[Grenier-2000-nonlinear-instability-euler-prandtl|Grenier 2000]] Thm 4.1 的 $\sigma\equiv0$），小黏性下的危险全部来自**非线性 Orr 回声链**而非几何光学增长。Bedrossian–Germain–Masmoudi 的**转捩阈值问题**：求正则性—尺寸配对 $(X,\gamma)$ 使 $\|u_{in}\|_X\lesssim\nu^\gamma\Rightarrow$ 非线性稳定、$\gg\nu^\gamma\Rightarrow$ 不稳定。

## 三个线性机制

- **Enhanced dissipation**：非零模衰减 $e^{-c\nu^{1/3}t}$（时标 $\nu^{-1/3}\ll\nu^{-1}$）；Fourier 侧源于 $\lambda(t)=k^2+(\eta-kt)^2$ 沿轨道 $\eta-kt$ 的暂时放大；能量法实现为 **ghost 权** $\frac{\partial_t\mathfrak m_k}{\mathfrak m_k}=\frac{\nu^{1/3}}{1+\nu^{2/3}(\eta-kt)^2}$（[[Li-Masmoudi-Zhao-2025-couette-gevrey-threshold|Li–Masmoudi–Zhao 2025]] Lemma 3.4）、$M$-乘子（[[Bian-Pu-2022-boussinesq-shear-threshold|Bian–Pu 2022]]）、Niu–Wu 的 $\mathcal M$ 乘子（$k\partial_\xi\mathcal M+\mu\xi^2\ge\tfrac14\mu^{1/3}|k|^{2/3}+\tfrac1{k^2+\xi^2}$，额外给出替代缺失热扩散的 $\|(-\Delta)^{-1/2}f^\neq\|$ 低频通道）、Ren–Wei 的 $\mathcal A=e^{\epsilon\kappa^{1/3}t}$ 与恒等式 (6.15)。与 [[Jia-Lei-Yuan-2026-prandtl-global|Jia–Lei–Yuan 2026]] 的 $e^{-c|\xi|^{2/3}t}$（Gearhart–Prüss 预解式）同族。
- **Inviscid damping**：速度场 $\langle t\rangle^{-1}$ 衰减（Kelvin 混合的椭圆损失）；分层情形 $\langle t\rangle^{-1/2}e^{-\epsilon\kappa^{1/3}t}$（Ren–Wei）。
- **瞬态增长**：分层无黏情形涡量 $\langle t\rangle^{1/2+}$ 增长（[[Masmoudi-Said-Houari-Zhao-2025-richardson-linear|MSZ 2025]]；行波 $\|\omega\|_{L^\infty}\approx f(0)\sqrt t$，[[Zillinger-2023-inviscid-stability-traveling-waves|Zillinger 2023b]]——"similar to the lift-up effect in 3D"）。

## 回声链与正则性—尺寸曲线

Orr 机制使低频被动量经反应项串联放大；**链的步长与临界指数由系统结构决定**：

- **纯 NS**（涡量–速度两步）：单步增益 $\frac{\nu^\beta\eta}{k^2}$；增强耗散在 $t=\nu^{-1/3}$ 截止链 ⇒ 临界频率 $\eta_c=\nu^{-2/3+\beta}$；阈值曲线 $\beta(s)=\frac{1-2s}{3-3s}$（Sobolev $\tfrac13$ ↔ 临界 Gevrey-2 $0$；[[Li-Masmoudi-Zhao-2025-couette-gevrey-threshold|LiMZ 2025]]）。
- **Boussinesq 无热扩散**（温度–速度互作用，两次 $\Delta_t^{-1}$）：单步增益 $c\frac{\eta}{k^3}$ 多一个 $1/k$ ⇒ 临界 **Gevrey-3**；Stirling 增长 $e^{3\eta^{1/3}}$（[[Masmoudi-Said-Houari-Zhao-2022-boussinesq-couette|MSZ 2022]]），线性下界 $e^{\sqrt[3]{c\eta}}$ 由 [[Zillinger-2023-echo-chains-traveling-waves|Zillinger 2023a]] 在行波附近证明（Gevrey-3 临界、速度阻尼在爆破下持续）。
- **无黏分层行波**：[[Zillinger-2023-inviscid-stability-traveling-waves|Zillinger 2023b]] norm-inflation 上界 $\exp(C\min((\epsilon|\xi|^{1+\gamma})^{2/3-2\gamma},\epsilon^{-2}))$，在 $\xi=\epsilon^{-4}$ 匹配 Gevrey 2；猜想最优权 $\exp((\epsilon\xi)^{2/3})$。

## Boussinesq/分层阈值版图（按已摄入来源）

| 来源 | 参数角落 | 阈值/结论 |
|---|---|---|
| [[Masmoudi-Said-Houari-Zhao-2022-boussinesq-couette|MSZ 2022]] | $\mu=0$、$\nu=1$、任意 $Ri$ | Gevrey-$\frac1s$（$s>\frac13$）小初值非线性稳定 + 散射；**无 1/4 门槛** |
| [[Masmoudi-Said-Houari-Zhao-2025-richardson-linear|MSZ 2025]] | $\mu=0$、$\nu\to0$、$Ri>1/4$ | 线性：$\nu^{-1/3}$ 增强耗散 + $\langle t\rangle^{1/2}$ 瞬态；$1/4$ 经好 unknowns 能量等价进入 |
| [[Masmoudi-Zhai-Zhao-2023-boussinesq-finite-channel|MZZ 2023]] | $\nu,\mu\to0$、有限通道无滑 | Sobolev 阈 $\min\{\nu,\mu\}^{1/2}$（边界压制；无界域预期 $1/3$，未证） |
| [[Bian-Pu-2022-boussinesq-shear-threshold|Bian–Pu 2022]] | 近 Couette、$\alpha$ 小/大两分支 | Sobolev $\min(\nu,\mu)^{1/2}$；大 $\alpha$ 需 $L^2$-涡量/$H^1$-温度耦合能量 |
| [[Ren-Wei-2026-stability-threshold-half|Ren–Wei 2026a]] | $\gamma^2>\frac14$、全扩散、比值条件 | Sobolev（$s>\frac12$）精确 $\alpha=\frac12$；速度型正定二次型 $D$ |
| [[Ren-Wei-2026-transition-threshold-third|Ren–Wei 2026b]] | 同上 + 回声链乘子 | **$\alpha=\frac13$**（代价 $s>\frac32$）；JFA 290 (2026) 111383 |
| [[Liang-Wu-Zhai-2026-general-viscosity-threshold|Liang–Wu–Zhai 2026]] | 一般黏性 $\mu^3\le\nu\le\mu^{1/3}$ | $\min\{\nu,\mu\}^{1/2+}$；新乘子 $M^4$ 压临界窗瞬态；与 Ren–Wei 2026b 参数互补 |
| [[Niu-Wu-2025-tropical-climate-couette|Niu–Wu 2025]] | 热带气候系统、$\theta$ 无扩散 | $(\alpha,\beta)=(\frac52,\frac94)$ 尖端的 $L^2$-型阈值；$\mathcal M_2$ 低频通道替代热扩散 |
| [[Li-Masmoudi-Zhao-2025-couette-gevrey-threshold|Li–Masmoudi–Zhao 2025]] | 纯 NS、无边界 | Gevrey 曲线 $\beta(s)$ + inviscid damping |
| [[Ding-Lin-2022-poiseuille-resolvent|Ding–Lin 2022]] | 纯 NS、**Poiseuille** 通道 slip | L² 阈值 ν^{3/4}；增强耗散 e^{−c√νt}（预解式/m-accretive） |
| [[Ding-Lin-2025-poiseuille-nu23-threshold|Ding–Lin 2025]] | 同上 + 无粘阻尼 | H^{7/2+} 阈值 ν^{2/3}；自述非最优 |
| [[Chen-Li-2024-poiseuille-couette|Chen–Li 2024]] | **Poiseuille–Couette 混合** U=y²+ay（𝕋×ℝ） | a≤10⁻³ν^{1/4} 时率 ν^{1/2}，a=10⁻³ν^s 时 ν^{1−2s}；阈值 ν^{3/4+2μ}；a∼O(1) open |
| [[Li-Luo-Luo-2025-vertical-dissipation|Li–Luo–Luo 2025]] | Boussinesq **仅垂直耗散**（ν=μ） | ω≤ν^{1/3}、θ≤ν^{5/6}、∂_xθ≤ν^{1/2}；e^{−εν^{1/3}t}；T₀=ν^{−1/6} |
| [[Grenier-2000-nonlinear-instability-euler-prandtl|Grenier 2000]] | Euler 不稳定剖面（不稳定侧标杆） | 线性不稳定 ⇒ 非线性不稳定；无拐点 ⇒ $\sigma\equiv0$ |

## 不稳定侧的三条路线

1. **初值正则性轴**：固定 Couette，Gevrey 2⁺ 以下不稳定（Deng–Masmoudi，未入库）；[[Zillinger-2023-echo-chains-traveling-waves|Zillinger 2023a]] 行波 echo chain 范数爆破（Gevrey-3 临界）。
2. **剖面参数轴**：[[Sinambela-Zhao-2025-shear-transition|Sinambela–Zhao 2025]]——临界层局部修改族的精确谱阈值 m_*（δ-势 Dirac 质量穿越 −1），经 [[Grenier-2000-nonlinear-instability-euler-prandtl|Grenier 2000]] 提升为非线性不稳定；Lin–Zeng H^{5/2⁻} 阈值由 m 调节的一般化。
3. **物理参数轴（谱符号）**：[[Hou-Wang-Xing-2026-rotation-instability|Hou–Wang–Xing 2026]]——Rayleigh–Taylor 型分层符号（δ>0）+ 旋转不足（f+a₀<0）的谱失稳与 Hadamard 非线性失稳。

关键结构性发现：**好未知量/交叉能量**把浮力项接入增强耗散框架——MSZ 2022 的 $K=-\gamma^2\partial_z\rho+\Delta_Lf$、[[Wang-Wang-2022-hydrostatic-mhd|Wang–Wang 2022]] 的仿积 good unknowns、Bian–Pu 的 $\alpha$-耦合能量、Ren–Wei 的速度型 $D$ 与 Liang–Wu–Zhai 的对称变量 $(Z,Q)$ 交叉能量（正定性均恰在 $Ri>1/4$）。

## Richardson/Miles–Howard 门槛的黏性形态

$\nu=1$ 时非线性稳定对一切 $Ri>0$（MSZ 2022——混合 + 黏性机制）；小黏性 $\mu=0$ 线性理论中 $Ri>1/4$ 门槛**重新出现**（MSZ 2025）；非线性端 $Ri>1/4$ 以交叉能量正定性的判别式形式进入（Ren–Wei 2026a、Liang–Wu–Zhai 2026）；行波无黏振幅阈值 $\alpha=\tfrac14$ 即 Miles–Howard（Zillinger 2023a Lemma 2.2）。这为 [[稳定分层与-rayleigh-taylor-判据|RT/Miles–Howard 判据]] 页提供"判据的黏性修正"时间线，并与 [[Bianchini-Duchene-2024-hydrostatic-limit-isopycnal|Bianchini–Duchêne 2024]] 的 $Ri>1/4$ 无黏非线性适定 open problem 相衔接。

## 与本库其他主题的关系

- **[[谱判据与几何光学方法|谱判据]]**：Couette = "谱稳定但非线性亚临界转捩"分支；Grenier 2000 提供不稳定侧对偶；增强耗散的 Gearhart–Prüss 实现是谱方法的耗散版。
- **[[双层能量法与插值衰减|双层能量法]]**：时变 Fourier 乘子 + ghost 权 + 多层 bootstrap（MZZ 的 $(E_k,H_k)$、Niu–Wu 的四层）是该概念页在 Fourier 侧的实现；[[Jiang-Wang-2025-primitive-bifurcation|Jiang–Wang 2025]] 的谱阈值是"精确阈值"版对照。
- 未摄入的相关节点（文献揭示）：Bedrossian–Germain–Masmoudi / Bedrossian–Vicol–Wang、Bedrossian–Masmoudi、Deng–Wu–Zhang、Zhai–Zhao SIAM 2023（$\nu^{1/2}$，被多篇引用为直接前身）、Knobel（$\mu=\nu$ 最优 $\nu^{1/3}$）、Wei–Zhang Tunis. J. Math. 2023、Deng–Masmoudi、Yang–Lin。

## 外域 Taylor–Couette 与滑移边界（2026-09-28 补全）

外域（r→∞ 剪切 r^{−2} 无穷阶退化）上 GP 机制失效：[[Li-Zhang-Zhang-2025a-tc-exterior-linear|2025a]] 证明任意时空耦合指数权下输入–输出估计不成立（X₁≠X₂ 伪谱断链 + 核非零构造），增强耗散仅有空间加权多项式率 Φ=ν^{1/3}|kB|^{2/3}；续篇 [[Li-Zhang-Zhang-2025b-tc-exterior-nonlinear|2025b]] 用含时权 Λ_k=log(Ĉr²+κ_kt) 的预解式估计在 M(0)≤C|νB|^{1/2} 下恢复非线性稳定（阈值 β=1/2 不变、耗散降为对数型）。[[Li-Pan-Zhang-2022-slip-boundary|Li–Pan–Zhang 2022]] 则给出有界域 Navier 滑移边界的显式常数判据 ζ≷−C_rμ（C_r=κ₁/λ₁+4κ₂）：同一"符号阈值"范式在一般边界的常数化。
