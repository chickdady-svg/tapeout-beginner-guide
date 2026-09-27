# 生态分层与任务路由

本文件帮助跨仓库协作者把 Issue / PR 开到正确的地方。

## 三层

1. **教材（本仓库）** — 《TapeOut 新手完全指南》Markdown + 页码溯源  
   规则：不扩写原文；合并前人工对照原 PDF。
2. **百科** — [BruceLanLan/tapeout-encyclopedia](https://github.com/BruceLanLan/tapeout-encyclopedia)  
   规则：词条 / 图谱 / 多语言 / Agent 协议；可引用本仓章节 URL。
3. **数据** — [tapeout.work](https://tapeout.work)  
   规则：观测与公开 API；百科用 `data_refs` 引用，不把瞬时数字写进教材。

完整串联说明：  
https://github.com/BruceLanLan/tapeout-encyclopedia/blob/main/docs/CROSS_REPO_WORKFLOW.md

## 快速判断

- 「这句话在 PDF 里写错了 / 断行了 / 图裂了」→ 本仓 PR  
- 「我想补充一个新工具 / 日语词条 / 图谱关系」→ 百科仓 Issue  
- 「现在有多少处理器 / BEM 价格」→ tapeout.work，不要改教材数字当现状

## 合并教材修正之后

在百科仓开 Issue，标题建议：`sync(guide): <主题>`，并链接本仓 PR。
