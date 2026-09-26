# 第 5 章：PoD 挖矿（第 2 部分）

> 本文件由 PDF 自动转换生成，尚未完成独立校对；请结合页码回溯注释核对原文。

<!-- source: tapeout-beginner-guide-v1.5-web.pdf p.70 -->

#### 提示

**λ 和 β 是怎么定的？** 官网写得很实在：λ（=6）和 β（=3）“用现有链上数据标不出来……这两个数是拍的，不是拟合出来的”。参数全部写在链上、可公开复核，出题之后就被锁死。

#### 本章要点

- PoD 挖矿 **不靠硬件** ：算力的基础是“烧掉的晶体管（工本，要花钱）”，每道题的最优设计再额外拿“设计溢价”，溢价可能比基础那份还大。

- 合格矿机：在 **Behemoth / TapeOut** 上、 **不含 REF** 、不超门数闸门。

- 流程：设计 →（承诺）→ 流片 → arm → start（≤64 区块，抽检≥3 条）→ claim。

- **H = (b* + K_task·q) × P** ，溢价只给“最优首创”；Behemoth 系数 6，TapeOut 系数 1。

- 每天 7,200 BEM，99% 给已验证池，约 3.995 年减半。

- 回本 ≈ 成本 ÷（每日 BEM × 币价）；成本含晶体管、流片协议费和 gas。全网算力、币价、最优首创身份都会变，估算留足余量。

挖矿合约 9 月 14 日已封印，规则和参数谁也改不了。

#### 延伸阅读

- [O24] 官网 PoD 挖矿页（含题库、算法、公式） —— TapeOut 官方 / tapeout.net：https://tapeout.net/pod/ 创始人 @Blonskr《挖矿的核心公式发布！》（2026-08-20） —— Blonskr（@Blonskr） / X：https://x.com/Blonskr/status/2090420634094329989

- 创始人 @Blonskr《PoD 新增反例审查》（2026-09-01） —— Blonskr（@Blonskr） / X：https://x.com/Blonskr/status/2094644591425401189

- TapeOut Mining Intelligence 看板 —— ekonomeest / Dune：https://dune.com/ekonomeest/tapeout-mining-intelligence

- [M06] 《TapeOut 协议 $BEM 初阶挖矿教程》 —— 新东西|Something / PANews（专栏）：https://www.panewslab.com/zh/articles/01a03e64-8a61-7566-badf-f21a43a5fb35

- [X10] 《BEM 挖矿逻辑与 BTC 的区别》 —— 墨鑫mox（@JiangX68993） / X：https://x.com/JiangX68993/status/2099803662000546246

- [X16] 《4 步教会你如何挖 BEM》 —— 黄周（@Web32049） / X：https://x.com/Web32049/status/2092397993047789808

- [V-93bitmap-7] 视频：科普第 7 集（最优矿机原理） —— 93.bitmap（@93bitmap） / X（视频）：https://x.com/93bitmap/status/2094365075356393931

- [S11] TapeOutScan 数据浏览器 —— TapeOutScan / tapeoutexplorer.com：https://tapeoutexplorer.com/
