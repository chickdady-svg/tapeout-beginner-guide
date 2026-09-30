# 《TapeOut 新手完全指南》协作仓库

本仓库将指南整理为按章节拆分的 Markdown，便于通过 GitHub Issue、分支和 Pull Request 多人协作。

当前版本已完成独立校对。正文中的 `<!-- source: ... p.N -->` 注释保留原稿物理页码的溯源映射；原始 PDF 未随公开仓库分发，详细验收报告也未公开分发。

## 仓库结构

- `docs/index.md`：Markdown 导航首页。
- `docs/*.md`：按章节拆分并完成校对的正文。
- `docs/assets/`：正文引用的图片资源。
- `outputs/`：公开发布的更新版 PDF。
- `work/build_updated_pdf.py`：统一生成更新版 PDF 的排版脚本。
- `work/updated_page_ranges.json`：构建后实测的章节页码记录。
- `manifest.md`：更新版页码、原稿溯源页码和图片对应关系。
- `mkdocs.yml`：本地网站预览配置。
- `CONTRIBUTING.md`：协作与修改规范。

## 在 GitHub 上阅读

从 [`docs/index.md`](docs/index.md) 进入目录。所有章节均使用 GitHub Flavored Markdown，可直接在 GitHub 网页中预览。

## 最新投稿

- [《TapeUP全链账本白皮书》学习解读之非技术版](docs/submissions/2026-09-30-tapeup-ledger-nontechnical.md) — 洪七公，2026-09-30

## 更新版 PDF 与页码

当前 Markdown 可通过 `work/build_updated_pdf.py` 统一排版为 [`outputs/tapeout-beginner-guide-updated.pdf`](outputs/tapeout-beginner-guide-updated.pdf)。该成品共 138 页，目录中的“更新版页码”以这份实际输出为准；括号内的“原稿页码”与正文中的 source 注释仅用于保留溯源映射，原始 PDF 未随公开仓库分发。补充内容没有改变原稿页码编号。

第 4 章新增的《TapeOut DeWeb 生态靓号新手指南》在更新版第 55–57 页，实际占 3 页，不参与原稿页码。页码明细和双口径映射见 [`manifest.md`](manifest.md)。

使用项目依赖环境运行：

```shell
python work/build_updated_pdf.py
```

## 本地预览

仓库包含最简 `mkdocs.yml`。已有 MkDocs 环境时，在仓库根目录运行：

```shell
mkdocs serve
```

然后访问命令输出的本地地址。也可以直接使用任何支持 GitHub Flavored Markdown 的编辑器查看 `docs/`。

## 协作方式

1. 从主分支创建短期分支。
2. 只修改与任务相关的 `docs/*.md`，新增图片放入 `docs/assets/`。
3. 保留 `<!-- source: ... p.N -->` 页码回溯注释。
4. 提交 Pull Request，说明修改的章节、原 PDF 页码和核对依据。
5. 由另一位参与者独立复核后再合并。

详细规则见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。
