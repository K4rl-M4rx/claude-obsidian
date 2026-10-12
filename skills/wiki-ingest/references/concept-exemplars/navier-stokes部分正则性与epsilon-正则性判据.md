---
address: c-000051
type: concept
title: "Navier–Stokes 部分正则性与 ε-正则性判据"
status: developing
created: 2026-09-27
updated: 2026-09-27
tags:
  - concept
  - navier-stokes
  - partial-regularity
  - epsilon-regularity
  - millennium-problem
complexity: advanced
domain: 偏微分方程
aliases:
  - partial regularity
  - epsilon-regularity criteria
  - suitable weak solutions
  - CKN theorem
related:
  - "[[Caffarelli-Kohn-Nirenberg-1982-partial-regularity|Caffarelli–Kohn–Nirenberg（1982）]]"
  - "[[Chae-Wolf-2024-vorticity-epsilon-regularity|Chae–Wolf（2024）]]"
  - "[[Ladyzhenskaya-2003-millennium-survey|Ladyzhenskaya（2003）]]"
  - "[[Wang-2025-partial-regularity-new-proof|Wang（2025）]]"
  - "[[Fujii-Tsurumi-Zhang-2025-stationary-ns-decay|Fujii–Tsurumi–Zhang（2025）定常衰减]]"
  - "[[primitive-equations原始方程|primitive equations（原始方程）]]"
  - "[[静力近似与静力极限|静力近似与静力极限]]"
  - "[[couette流增强耗散与转捩阈值|Couette 流增强耗散与转捩阈值]]"
sources:
  - "[[Caffarelli-Kohn-Nirenberg-1982-partial-regularity|Caffarelli–Kohn–Nirenberg（1982）]]"
  - "[[Chae-Wolf-2024-vorticity-epsilon-regularity|Chae–Wolf（2024）]]"
  - "[[Ladyzhenskaya-2003-millennium-survey|Ladyzhenskaya（2003）]]"
  - "[[Wang-2025-partial-regularity-new-proof|Wang（2025）]]"
---

# Navier–Stokes 部分正则性与 ε-正则性判据

## 概念

3D 不可压 NS 在能量类（Leray–Hopf / suitable weak solution）中的整体光滑性未知（千禧年第六问题）。**部分正则性**理论证明：suitable weak solution 的奇异集维数严格小于时空维数——正则性在"除小集合外"处处成立。核心工具是 **ε-正则性判据**：某无量纲量在柱体 $Q_r(x,t)$ 上小于绝对常数 ⇒ 该点正则。

## ε-判据谱系（按已摄入来源）

| 判据 | 量与阈值 | 来源 |
|---|---|---|
| $M(r)\le\epsilon_1$ 且 $F_q(r)\le\epsilon_2$（三次量 + 压力 + 外力） | $r^{-2}\iint(\|u\|^3+\|u\|\|p\|)+\cdots$ | [[Caffarelli-Kohn-Nirenberg-1982-partial-regularity\|CKN 1982, Cor. 1]] |
| $\limsup_{r\to0}r^{-1}\iint_{Q^*_r}\|\nabla u\|^2\le\epsilon_3$（临界指标） | 速度梯度，绝对常数 | [[Caffarelli-Kohn-Nirenberg-1982-partial-regularity\|CKN 1982, Prop. 2]] |
| $r^{-1}\int_{Q(z_0,r)}\|\omega\|^2<\epsilon_\alpha^2$ 于中间尺度区间 $[r_1,r_0]$（$\alpha\to1$ 还原 CKN） | **涡量**，$\epsilon_\alpha=(3-\alpha)^2/(2c)$ | [[Chae-Wolf-2024-vorticity-epsilon-regularity\|Chae–Wolf 2024, Thm 1.5]] |
| 混合判据 ⇒ 奇异集 Minkowski 维数 $\le 15/13$ | $\|\omega\|^2+\|u\|^{10/3}+\|E^*_\Omega(\omega\times u)\|^{5/4}$ | [[Chae-Wolf-2024-vorticity-epsilon-regularity\|Chae–Wolf 2024, Thm 1.8]] |
| $C_1[u,P]\le\delta_0/2^5$（$L^3\times L^{3/2}$） ⇒ $C^\alpha$，$\alpha=-\ln2/\ln\lambda$ | 线性尺度泛函 | [[Wang-2025-partial-regularity-new-proof\|Wang 2025, Thm 1(b)]] |
| $E_r=r^4\int_{Q_r}\|Du\|^2\le\delta_2$ 于所有尺度 | 局域能量 | [[Wang-2025-partial-regularity-new-proof\|Wang 2025, Thm 2]] |

**奇异集维数谱系**：Scheffer 1977（$H^{5/3}<\infty$）→ **CKN 1982**（$P^1=H^1=0$）→ Koh–Yang 2016 / Chae–Wolf 2024（Minkowski $\le15/13$）。

## 证明技术路线（三代）

1. **CKN 原始迭代**：无量纲化 + 压强三分解 + 双尺度交替归纳 + 抛物 Vitali 覆盖（几何测度论框架）。
2. **重证谱系**：Ladyzhenskaya–Seregin 1999、Lin 1998、Choe–Lewis 2000、Vasseur 2007（De Giorgi 类方法）、Wolf 2015（local pressure projection，免除整体压强）。
3. **几何框架**（[[Wang-2025-partial-regularity-new-proof|Wang 2025]]）：调和函数单调性扰动版 + 线性尺度（绕常向量场线性化 NS + Campanato）+ 无压力紧性的紧性引理（压力规范自由度经调和流吸收）+ 小能量几何迭代。

## 千禧年问题的两条路径（与本库其他主题的定位）

- **唯一性类路径**（[[Ladyzhenskaya-2003-millennium-survey|Ladyzhenskaya 2003]]）：Prodi–Serrin–Ladyzhenskaya 临界类 $L_{m,s}$（$\frac3m+\frac2s=1$）的条件正则性与唯一性；整体可解性 ⟺ $\lambda$-凸组合族的一致临界估计（否则 collapse）。$m=3,s=\infty$ 由 ESS 2003 解决。
- **部分正则性路径**（本页）：CKN 表明能量类中奇异集 $P^1=0$，但 CK N 自述 "not strong enough" 以推出唯一性/时间强连续——部分正则性是现状下最强的非端点结果。
- **结构对照**：[[Cao-Titi-2007-primitive-equations-3d|Cao–Titi 2007]] 的 3D PE 整体强解靠静水各向异性结构补回缺失的先验估计——本库的"静力近似与静力极限"簇是"什么结构能恢复整体正则性"的肯定侧，NS 部分正则性是基准障碍侧。
- **定常 NS 定性理论**（[[Fujii-Tsurumi-Zhang-2025-stationary-ns-decay|Fujii–Tsurumi–Zhang 2025]]）：临界 Besov 定常解的适定性与首批逐点衰减率（$\sigma<\tfrac12$）——与谱判据簇的背景流假设之间存在 open gap（衰减是否足够快以落入谱分析框架）。

## 未决问题（承自来源）

- 能量不等式可否取严格不等号 / 弱解时间强连续性 / 唯一性（CKN 遗留）。
- 部分正则性能否强化到 $P^k(S)=0$（$k<1$）或推广到 Hausdorff 维数 1 之下（CKN Theorem D 的方向）。
- 谱判据所需的背景定常流类与临界定常解衰减类的兼容性（本库连接点）。
