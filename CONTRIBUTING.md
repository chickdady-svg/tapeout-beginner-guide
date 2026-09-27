# 贡献指南

## 任务先分流

| 任务类型 | 去哪里 |
| --- | --- |
| 有原 PDF 依据的错字 / 格式 / 表格 / 图片 / 链接修复 | **本仓库** |
| 翻译、扩写、新工具词条、知识图谱、Agent 共建 | [tapeout-encyclopedia](https://github.com/BruceLanLan/tapeout-encyclopedia) |
| 实时链上数据 / 市场 / PoD 快照 | [tapeout.work](https://tapeout.work) |

说明见 [`ECOSYSTEM.md`](ECOSYSTEM.md)。

## 可以修改什么

- 正文修改限于 `docs/*.md`。
- 新增或替换的图片放在 `docs/assets/`，并使用相对路径引用。
- 如文件与页码或图片的对应关系变化，请同步更新根目录 `manifest.md`。

## 不要修改什么

- 不要修改、覆盖或重新导出 `source/original.pdf`。
- 不要删除 `<!-- source: tapeout-beginner-guide-v1.5-web.pdf p.N -->` 回溯注释。
- 不要把无法确认的内容改成肯定表述；请使用 `<!-- TODO: verify p.N -->`。
- 不要翻译或扩写原文没有的内容。

## Pull Request 流程

1. 一个 Pull Request 尽量只处理一个章节或一种格式问题。
2. PR 描述中列出修改文件和对应的原 PDF 页码。
3. 说明修改属于文字核对、格式清理、表格修复、图片修复还是链接修复。
4. 提交前检查 Markdown 图片和内部链接均使用相对路径。
5. 请求另一位参与者依据原 PDF 独立复核；自动转换或自动检查不能替代人工校对。
6. （可选）若变更会影响百科词条，在 PR 描述里注明，并在百科仓开 `sync(guide)` Issue。

## 文字和格式原则

- 文件编码统一为 UTF-8。
- 保留原有中英文，不做翻译。
- 只修正有原 PDF 依据的错字、断词、标题、列表、表格和公式。
- 表格优先使用 GFM 表格；无法可靠表达时改为列表，并标记对应页码的 TODO。
- 公式优先使用 `$...$` 或 `$$...$$`，但不得凭推断补写公式。
