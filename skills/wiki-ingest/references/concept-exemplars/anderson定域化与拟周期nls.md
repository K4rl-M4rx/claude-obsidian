---
address: c-000089
type: concept
title: "Anderson 定域化与拟周期 NLS"
status: developing
created: 2026-09-28
updated: 2026-09-28
tags:
  - concept
  - anderson-localization
  - quasi-periodic
  - spectral-theory
complexity: advanced
domain: 数学物理
aliases:
  - Anderson localization
  - 定域化
related:
  - "[[Cong-Shi-Wang-2025-longtime-localization|Cong–Shi–Wang（2025）长时间定域]]"
  - "[[Kirsch-2021-random-schrodinger|Kirsch 讲义]]"
  - "[[Shi-Wang-2026-quasi-periodic-localized-states|Shi–Wang（2026）定域态]]"
sources:
  - "[[Cong-Shi-Wang-2025-longtime-localization|Cong–Shi–Wang（2025）]]"
  - "[[Kirsch-2021-random-schrodinger|Kirsch 讲义]]"
  - "[[Shi-Wang-2026-quasi-periodic-localized-states|Shi–Wang（2026）]]"
---

# Anderson 定域化与拟周期 NLS

## 概念与谱系

Anderson 定域化：随机/拟周期势中波动不扩散（谱纯点 + 特征函数指数衰减；动力学上波包质量不外传）。三条谱系：

1. **线性随机理论**（[[Kirsch-2021-random-schrodinger|Kirsch 讲义]]）：iid Anderson 模型——Pastur 非随机谱、IDS、Wegner 估计、Lifshitz 尾、Combes–Thomas、Fröhlich–Spencer 多尺度分析（good cube 传递 + 初始尺度）；谱底部任意 disorder 定域、任意区间大 disorder 定域；d≥2 离域化与格上 Bernoulli 情形 open。
2. **非线性随机**：Bourgain–Wang（BNF 长时）/ Liu–Wang 等定域态构造。
3. **非线性拟周期**（确定势）：
   - **BNF 路线**（[[Cong-Shi-Wang-2025-longtime-localization|Cong–Shi–Wang 2025]]）：任意 ℓ² 初值多项式长时间定域；新工具 Wronskian 横截性测度估计（替代随机情形的正导数下界）。
   - **CWB/MSA 路线**（[[Shi-Wang-2026-quasi-periodic-localized-states|Shi–Wang 2026]]）：无限时拟周期定域态；d 维相空间无谱分离性 ⇒ 半代数几何（Bourgain 几何引理 + Cartan + Yomdin–Gromov）+ 三尺度 LDT 不可替代。

## 技术对照

| 要素 | 随机（Kirsch） | 拟周期 BNF（CSW） | 拟周期 CWB/MSA（SW） |
|---|---|---|---|
| 消振 | Wegner + 独立性 | nonresonance (1.3) + Cantor 测度 | 二阶 Melnikov Cantor 集 |
| 空间共振 | MSA good cubes | 势垒区 BNF | 半代数集 + Bourgain 引理（衰减 N^{8/9}） |
| 初始尺度 | 大 disorder / Lifshitz 尾 | B₀ 初值界 | Neumann 级数（小尺度） |
| 时间范围 | a.s. 全时刻（线性） | 多项式长时 | 无限时（拟周期态） |

## 与本库其他主题的关系

- 库内主流是**流体稳定性**；本簇是谱理论/数学物理侧枝，但共享"线性机制存活判据"的语言（[[谱判据与几何光学方法|谱判据页]]）：小除子/Melnikov 条件与回声链共振分析同源。
- Shi–Wang 的 Wronskian 测度估计与 [[Ding-Lin-2022-poiseuille-resolvent|预解式路线]]同属"静态量控制动态衰减"。

## 未决问题

- 非线性拟周期系统的整体解/无限时定域；随机与拟周期定域集关系的完全刻画（SW Remark 1.3）。
