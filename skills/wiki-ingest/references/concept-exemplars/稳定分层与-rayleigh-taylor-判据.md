---
address: c-000002
type: concept
title: "稳定分层与 Rayleigh–Taylor 判据"
status: developing
created: 2026-09-23
updated: 2026-09-28
tags:
  - concept
  - hydrodynamic-stability
complexity: intermediate
domain: 偏微分方程
aliases:
  - Stable stratification and the Rayleigh-Taylor criterion
  - Rayleigh–Taylor 稳定性条件
related:
  - "[[Dong-Li-Sun-2026-IINS-gravity-stability|Dong–Li–Sun（2026）重力驱动 IINS 的渐近稳定性]]"
  - "[[双层能量法与插值衰减|双层能量法与插值衰减]]"
  - "[[重力驱动-iins-的衰减率是否最优|重力驱动 IINS 的衰减率是否最优]]"
  - "[[Jiang-Wang-2026-boussinesq-hydrostatic-stability|Jiang–Wang（2026）一般重力势 Boussinesq]]"
  - "[[Jiang-Wang-2025-iins-gravity-latetime|Jiang–Wang（2025）重力势 IINS]]"
sources:
  - "[[Dong-Li-Sun-2026-IINS-gravity-stability|Dong–Li–Sun（2026）重力驱动 IINS 的渐近稳定性]]"
---

# 稳定分层与 Rayleigh–Taylor 判据

## 判据

对密度驱动的流体的静水平衡——$\mathbf{v}_e = \mathbf{0}$，$\nabla \pi_e = -\rho_e \mathbf{e}_3$，$\rho_e = \rho_e(z)$——$\rho_e'$ 的符号决定稳定性：

- **Rayleigh–Taylor 不稳定**：存在 $z_0 \in [0,1]$ 使 $\rho_e'(z_0) > 0$（较轻流体在较重流体之下）。经典线性理论可追溯至 Rayleigh（1883）；非齐次不可压黏性流体的非线性不稳定性由 Jiang–Jiang–Ni（*Sci. China Math.* 2013）与 Jiang–Jiang（*Adv. Math.* 2014）证明。
- **稳定分层**：在 $[0,1]$ 上 $-\infty < \rho_e'(z) < 0$（较重流体在下、较轻流体在上）。这是 Dong–Li–Sun（2026）的条件 (3)；其定理 1.1 给出小扰动的整体存在性与代数衰减——即完整非齐次 Navier–Stokes 系统的 Rayleigh–Taylor **稳定性**现象，见 [[Dong-Li-Sun-2026-IINS-gravity-stability|Dong–Li–Sun（2026）]]。

## 在能量结构中的角色

$\rho_e' < 0$ 有两条贯穿全部能量估计的结构性推论：

1. 权重 $\sigma(z) = -1/\rho_e'(z)$ 在 $[0,1]$ 上为正且有限，低阶能量中的密度部分为 $\int_\Omega \sigma |\nabla_h \varrho|^2\,\mathrm{d}\mathbf{x}$。
2. 浮力项 $-\rho_e' |u_3|^2$ 以有利的符号进入能量：

$$
E^2 \supset \int_\Omega \big(\rho_e |\nabla_h \mathbf{u}|^2 + \sigma |\nabla_h \varrho|^2\big)\,\mathrm{d}\mathbf{x} + \int_\Omega \big((\rho_e + \varrho)\,|\partial_t \mathbf{u}|^2 - \rho_e'\, |u_3|^2\big)\,\mathrm{d}\mathbf{x} + M^{-2} \int_\Omega \sigma |\nabla_h \varrho|^2\,\mathrm{d}\mathbf{x},
$$

其中 $M = \max\{\max_{z} \rho_e,\ \max_{z} |\rho_e'|\}$。若 $\rho_e'$ 变号，该二次型便不再强制——正是产生 Rayleigh–Taylor 不稳定性的同一符号翻转摧毁了能量恒等式。

## Boussinesq 类比

在 Boussinesq 近似下，分层剖面为线性温度 $\theta_e(\mathbf{x}) = x_d$，平衡 $(\mathbf{0}, \tfrac{\gamma}{2}, x_d)$ 的稳定性已有充分研究：Dong–Sun（2D，*J. Differ. Equ.* 2022；3D，*Sci. China Math.* 2024）与 Jang–Kim（*Calc. Var.* 2023，水平周期）在滑移边界条件下用谱分析得到最优衰减 $\|\vartheta(t)\|_{L^2} \lesssim (1+t)^{-(d-1)/4}$。Dong–Li–Sun（2026）的 IINS 结果是无滑移边界下的非 Boussinesq 对应物，此时动量惯性中的变系数 $\rho_e(z)$ 阻断了最优谱路线；见 [[重力驱动-iins-的衰减率是否最优|重力驱动 IINS 的衰减率是否最优]]。

## 一般重力势下的判据（2026-09-28 补全）

Jiang–Wang 三部曲把判据从均匀重力 (0,g) 推广到一般势 f：[[Jiang-Wang-2026-boussinesq-hydrostatic-stability|2502.16226]]（环形域、混合边界）稳态必为 ∇ρ_s=h∇f 型静水平衡，h(x₀,y₀)>0 于某点 ⟺ RT 线性 + Hadamard 不稳定、h<h₀<0 ⟹ 稳定——h 的符号即稳定性分水岭（变分法构造特征值）；[[Jiang-Wang-2025-iins-gravity-latetime|2512.19281]]（2D IINS、Dirichlet）稳态必为 ∇p_s=−ρ_s∇f 静水平衡，RT 不稳定（承 Li 2025）只造成瞬态增长。
