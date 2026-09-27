# 第 10 章：延伸阅读

> 本文件由 PDF 自动转换生成，尚未完成独立校对；请结合页码回溯注释核对原文。

<!-- source: tapeout-beginner-guide-v1.5-web.pdf p.108 -->

## 第 10 章深度阅读：精选文章导读

读完本书，如果你还想继续深入，下面这些文章值得一读。我们按“读者阶段”排列，每篇写了一两句导读， 帮你判断要不要点开。

#### 提示

**阅读提示** ：除官方文件外，下面都是社区或媒体作者的观点，不代表本书立场。一些文章标题带有情绪化或行情导向，我们选它们是因为内容有解释价值。遇到具体数字，请回到链上或官网核对。X （Twitter）上的长文需要登录才能完整阅读，可以尝试 TopicDigg 等镜像站。

### 10.1 官方一手文件（必读）

|**编号**|**文件**|**作者 / 平台**|**导读**|
|---|---|---|---|
|O02|TapeOut 链上微处理器宣言<br>（PDF）|TapeOut 官方（Blonskr） /<br>tapeout.net|唯一的白皮书性质文件，讲清<br>了“为什么要在链上造处理<br>器”。注意其中“已放弃所有<br>权限”与链上现状不符（第 9<br>章）|
|O24|PoD 挖矿页的“算法”“公式”<br>标签|TapeOut 官方 / tapeout.net|挖矿规则最权威的出处：权重<br>公式、参数取值、题库和挑战<br>机制|
|O12|tape:// 规范 v0.2|TapeOut Labs / GitHub|链上网站的名字、解析、校验<br>与隔离规则；中文原文|
|O13|TapeSend / TAP-10|TapeOut Labs / GitHub|容器间加密消息的设计与已知<br>限制|
|O03|Blonskr 首发推文|Blonskr（@Blonskr） / X|项目起点：2,251 个 NAND +<br>latch 组成的链上处理器|
|O26|挖矿的核心公式发布！|Blonskr（@Blonskr） / X|PoD“最优首创”规则的原始<br>出处（2026-08-20）。其中<br>“不排除小规模细节调优”是<br>封印前的说法|
|O32|上线 26 天数据汇总通告|Blonskr（@Blonskr） / X|截至 9 月 9 日约 34,054 BNB<br>成交额（官方 26 天数据）等<br>数字的原文，注意统计口径含<br>两个第三方市场|

### 10.2 入门科普（适合读完第 1‒3 章后看）

**M05** 新东西|Something《TapeOut Protocol 小白科普：从与非门到链上挖矿》（PANews，2026-0825）：从 NAND 门讲起，一路讲到挖矿，图多、节奏慢，最适合零基础读者。https://www.panewslab.com/zh/articles/01a03820-6305-75be-9e73-12005316087a

<!-- source: tapeout-beginner-guide-v1.5-web.pdf p.109 -->

- **M01** 深潮 TechFlow《解读 TapeOut：一个小孩在链上造了一台 CPU》（2026-08-17）：最早的几篇媒体 解读之一，讲项目缘起和首日数据。https://www.techflowpost.com/article/33302

- **M04** BruceBlue《从 Mint 到流片：TapeOut 新手第一次上手指南》（2026-08-18）：早期的操作指南， 界面已有变化，思路仍然适用。https://www.panewslab.com/zh/articles/01a00fff-7b7f-70ff-a188-0448b4d31797

- **X14** @cupid_elvis《TapeOut Explained: A Beginner’s Guide to NAND, LATCH…》（英文，2026-0912）：适合转发给英文读者。https://x.com/cupid_elvis/status/2098670687296843777

- **S03** TapeOut日报（编者作品）《五分钟看懂 TapeOut 怎样把逻辑变成电路》：短小的交互式讲解。https://tapeoutdaily.ai/learn/from-nand-to-processor

- **X18** CUPID（@cupid_elvis）《从 Mining 到 Onchain Computing：我眼中的 TapeOut》（2026-0829）：用“乐高城市”打比方讲清 NAND / LATCH → 电路 → 矿机 → BEM 的层级，还纠正了“链上晶体 管是实体零件”的误解。https://x.com/cupid_elvis/status/2093526616257531954

- **X20** YW（@ywweb3）《关于 TapeOut 最近的几个热门问题，统一回复一下》（2026-09-23）：6 问 6 答，大白话讲多链、存储、TapeSend、BEM 挖矿；作者也说明其中有些是个人推测。可以和本书的 FAQ 对照读。https://x.com/ywweb3/status/2102762282904375695

- 推荐阅读：[《TapeOut DeWeb 生态靓号新手指南》](08-chapter-04.md#tapeout-deweb-生态靓号新手指南)，介绍 DeWeb 靓号为何受到关注及其价值逻辑、常见靓号分类、新手选择八步走，以及交易前后的链上核验与风险。

### 10.3 挖矿进阶（适合读完第 5 章后看）

- **M06** 新东西|Something《TapeOut 协议 $BEM 初阶挖矿教程》（PANews，2026-08-26）：带截图的实 操教程，公式与官方 PoD 页一致。注意截图来自第三方市场界面。https://www.panewslab.com/zh/articles/01a03e64-8a61-7566-badf-f21a43a5fb35

- **X10** @JiangX68993《BEM 挖矿逻辑是什么样的？与 BTC 的挖矿逻辑到底有什么区别？》（2026-0915）：用比特币做对照，帮你理解“设计证明”和“工作量证明”的不同。https://x.com/JiangX68993/status/2099803662000546246

- **V-93bitmap-7** 93bitmap 科普第 7 集《榜一大哥的秘密》（视频，见第 11 章）：专讲最优设计的计算公式。

- **X24** Benson（@benson_doge）《当 NFT 开始持续产出：一种按日产能定价的 AMM 思路》（2026-0923）：矿机该按“买到 1 BEM/日产能要花多少 BNB”来比价；作者也讨论了没解决的风险。BruceBlue 的回应帖提醒 q 值和验证状态会变。https://x.com/benson_doge/status/2102704047069556837

### 10.4 生态与经济（适合读完第 6、8 章后看）

- **M07** 黑色马里奥《深度纵览 TapeOut 生态图景》（Odaily，2026-09-20；PANews 转载题为《TapeOut 生态全景盘点》）：目前最完整的生态梳理，从元件到应用逐层讲。https://www.odaily.news/zh-CN/post/5213070

- **M08** CoinW 研究院《TapeOut 机制与风险解析》（PANews，2026-09-22）：数据翔实，并系统讨论了 “庞氏”质疑（第 9 章有转述）。https://www.panewslab.com/zh/articles/01a0c86f-6cb0-7373-83a4-d0fbfaa58aae

<!-- source: tapeout-beginner-guide-v1.5-web.pdf p.110 -->

- **M09** Foresight News《CZ 两次点赞、Bonk Guy 买入的 BEM 是什么？》（2026-09-16）：偏叙事的介 绍；原站可能拒绝抓取，可读 BlockWeeks 转载。https://blockweeks.com/view/317967

- **X02** BruceBlue《The Day TapeOut Launchpad Gave BEM a Second Clock》（英文，2026-09-15）：讨 论 TapeHub 发射台对 BEM 的影响。https://x.com/BruceBlue/status/2099774044023542173

- **M20** OOKC Labs（@OOKCLabs）《TapeOut Operability Research Report》（英文，2026-09-24）：机 构署名的英文研究长文，自称独立研究、不构成投资建议，结论是“中性偏正面（Neutral-toPositive）”。英文深度资料不多，值得一看。https://x.com/OOKCLabs/status/2103048027800027151

### 10.5 技术与愿景（适合读完第 4、7 章后看）

- **X05** BruceBlue《当所有人都把计算搬离主网，TapeOut 却把 Linux 塞了回来》（2026-09-08）：解读链 上 Linux 演示的意义。https://x.com/BruceBlue/status/2097177531665481806

- **X04** BruceBlue《当经验可以被烧成电路｜逻辑门神经网络与 TapeOut 的下一条路》（2026-09-11）：讲 V2 预告里的 BNN / LUT 元件可能带来什么。https://x.com/BruceBlue/status/2098315194145657149

- **X03** BruceBlue《C3S: The First Research Object for TapeOut’s Fabrication Layer》（英文，202609-13）：以“果蝇反射”启发的电路为例，展示可被他人检验与挑战的研究对象；配套网页见第 8 章。 https://x.com/BruceBlue/status/2099054412115374165

- **X08** @ywweb3《TapeKit：不只是“一个新工具”，而是互联网底层的一次重新设计》（2026-09-16）： 从普通用戶角度解释 TapeKit。https://x.com/ywweb3/status/2100188153416126908

- **O06** Blonskr《电路是“生产力基建”》（2026-08-25）：创始人对电路设计价值的看法。https://x.com/Blonskr/status/2092153923507540377

- **X19** CUPID（@cupid_elvis）《DeWEB 与 Web 4.0：TapeOut 的下一张蓝图》（2026-09-20）：从“一 个人做的东西能在互联网上留多久”出发讲 DeWEB 的价值。https://x.com/cupid_elvis/status/2101506529786822843

- **X25** BruceBlue（@BruceBlue）《不把 AI 烧进电路：GateCraft 是送给 TapeOut 社区的一次中秋实验》 （2026-09-24）：BruceBlue 研究系列的最新一篇，附一个浏览器里就能玩的电路小工具（作者写明是 个人研究，不代表 TapeOut）。https://x.com/BruceBlue/status/2103027350183215577

- **X26** JayChen（@0xJayChen）《16.67 万个神经元，我把一只果蝇做上了 BNB Chain》（2026-09-20）：把果蝇神经网络编译成 10,419 个电路（目前在测试网），邀请社区一起把它搬上主网。https://x.com/0xJayChen/status/2101539893906387362

### 10.6 观点与争鸣

- **X12** @sciencedegens《很多人没看懂 TapeOut：它可能是一个“矿机版 Pump”》（2026-08-17）：早 期的机制类比，可对照 CoinW 的风险分析一起读。https://x.com/sciencedegens/status/2089356316188008949

- **X06** BruceBlue《当机器开始在链上进化：TapeOut 与一座公共机器文明的诞生》（2026-08-21，新加 坡时间）：偏愿景的长文。https://x.com/BruceBlue/status/2090507223982318077

- **X09** @ywweb3《如果 TapeOut 真的成功，会创造怎样的新世界？》（2026-09-13）：同样是愿景类，适 合了解社区的期待。https://x.com/ywweb3/status/2099039251619000702

<!-- source: tapeout-beginner-guide-v1.5-web.pdf p.111 -->

- **X21** YW（@ywweb3）《比特币、以太坊之后，TapeOut 正在打开的“第三世界”》（2026-09-22）：面 向新人的叙事长文，偏观点。https://x.com/ywweb3/status/2102261091640422646

- **M21** Golem（@web3_golem）《CZ 一键三连后，16 岁少年做的链上 CPU 项目火了》（Odaily 星球日 报原创，2026-08-17）：最早的媒体报道之一，视角偏冷静，担心电路门槛和金融化后的纠纷；可以和 上面的愿景文对照着读。https://www.odaily.news/zh-CN/post/5212520

#### 提示

YW 的《第三世界》一文提到了 TAPQQ。TAPQQ 是本书编者洪七公的作品（见第 8 章“编者的作品”）， 不是 TapeOut 官方产品。

#### 注意

**关于 KuCoin 博客（M13）** ：这篇英文科普流传较广，但有明显的事实错误（例如“供应不足 4 万”），本书不推荐把它当作数据来源。

#### 本章要点

先读官方一手文件：宣言、PoD 公式页、tape:// 规范、TAP-10。 零基础从 M05 开始；想挖矿读 M06 与 93bitmap 第 7 集；看生态读 M07；看风险读 M08。 社区文章是观点，数字要回到链上或官网核对。

#### 延伸阅读

完整来源目录（255 条，含评分与关系标注）见附录 B 与随书的 catalog.csv 。

- [S01] tapeout.link 文章聚合 —— TapeOut 生态导航 / tapeout.link（社区网站）：https://tapeout.link/

- [M18] Blonskr 推文镜像 —— TopicDigg / topicdigg.com：https://topicdigg.com/x/Blonskr
