# 转换清单

> 本清单记录自动转换产物与原 PDF 的对应关系，不代表内容已完成校对。

- 源文件 SHA-256：`aaf536c53b9bf6a1d354b7ea6a4263eb09bc37207c1b2c8a7b187315851e7b0a`
- 原稿页码以只读归档 PDF 的物理页码为准；正文中的 `<!-- source: ... -->` 注释继续使用这一口径。
- 更新版页码由 `work/build_updated_pdf.py` 对当前 Markdown 统一排版后实测，成品为 `outputs/tapeout-beginner-guide-updated.pdf`，共 138 页。

## 更新版成品页码

| 产出文件 | 更新版页码范围 | 原稿页码范围 |
| --- | --- | --- |
| `docs/01-front-matter.md` | 第 1–10 页 | 第 1–12 页 |
| `docs/02-credits-a.md` | 第 11–15 页 | 第 13–19 页 |
| `docs/03-credits-b.md` | 第 16–20 页 | 第 20–26 页 |
| `docs/04-quick-reference.md` | 第 21–24 页 | 第 27–31 页 |
| `docs/05-chapter-01.md` | 第 25–33 页 | 第 32–38 页 |
| `docs/06-chapter-02.md` | 第 34–39 页 | 第 39–44 页 |
| `docs/07-chapter-03.md` | 第 40–45 页 | 第 45–50 页 |
| `docs/08-chapter-04.md` | 第 46–58 页 | 第 51–59 页；另含补充资料 |
| ↳ `TapeOut DeWeb 生态靓号新手指南` | 第 55–57 页（3 页） | 不参与原稿页码 |
| `docs/09-chapter-05-part-1.md` | 第 59–69 页 | 第 60–69 页 |
| `docs/10-chapter-05-part-2.md` | 第 70–71 页 | 第 70 页 |
| `docs/11-chapter-06.md` | 第 72–79 页 | 第 71–77 页 |
| `docs/12-chapter-07-part-1.md` | 第 80–91 页 | 第 78–88 页 |
| `docs/13-chapter-07-part-2.md` | 第 92–94 页 | 第 89–91 页 |
| `docs/14-chapter-08.md` | 第 95–101 页 | 第 92–99 页 |
| `docs/15-chapter-09.md` | 第 102–109 页 | 第 100–107 页 |
| `docs/16-chapter-10.md` | 第 110–113 页 | 第 108–111 页 |
| `docs/17-chapter-11.md` | 第 114–127 页 | 第 112–118 页 |
| `docs/18-chapter-12.md` | 第 128–133 页 | 第 119–124 页 |
| `docs/19-appendices.md` | 第 134–138 页 | 第 125–130 页 |

## Markdown 与仓库文件（原稿溯源）

| 产出文件 | 原 PDF 页码范围 | 涉及图片 |
| --- | --- | --- |
| `source/original.pdf` | 第 1–130 页 | PDF 原样只读归档；图片不单列 |
| `docs/index.md` | 第 1–130 页（导航） | 无 |
| `docs/01-front-matter.md` | 第 1–12 页 | `docs/assets/page-001-cover.png` |
| `docs/02-credits-a.md` | 第 13–19 页 | 无 |
| `docs/03-credits-b.md` | 第 20–26 页 | 无 |
| `docs/04-quick-reference.md` | 第 27–31 页 | `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0027-04.png` |
| `docs/05-chapter-01.md` | 第 32–38 页 | `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0034-02.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0035-01.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0035-02.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0035-03.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0035-04.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0035-07.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0036-01.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0037-01.png` |
| `docs/06-chapter-02.md` | 第 39–44 页 | `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0040-02.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0042-06.png` |
| `docs/07-chapter-03.md` | 第 45–50 页 | `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0045-17.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0046-00.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0047-10.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0048-00.png` |
| `docs/08-chapter-04.md` | 第 51–59 页 | `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0054-01.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0054-02.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0054-13.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0055-05.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0055-07.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0056-00.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0056-07.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0057-00.png` |
| `docs/09-chapter-05-part-1.md` | 第 60–69 页 | `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0060-15.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0061-11.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0062-07.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0064-01.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0065-05.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0067-02.png` |
| `docs/10-chapter-05-part-2.md` | 第 70–70 页 | 无 |
| `docs/11-chapter-06.md` | 第 71–77 页 | `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0073-07.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0074-11.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0075-00.png` |
| `docs/12-chapter-07-part-1.md` | 第 78–88 页 | `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0079-01.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0079-05.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0082-01.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0083-02.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0084-02.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0085-00.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0085-03.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0085-09.png` |
| `docs/13-chapter-07-part-2.md` | 第 89–91 页 | 无 |
| `docs/14-chapter-08.md` | 第 92–99 页 | `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0092-06.png` |
| `docs/15-chapter-09.md` | 第 100–107 页 | `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0101-02.png` |
| `docs/16-chapter-10.md` | 第 108–111 页 | 无 |
| `docs/17-chapter-11.md` | 第 112–118 页 | `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0113-06.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0113-07.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0113-14.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0113-15.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0113-16.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0113-17.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0114-02.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0114-07.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0114-08.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0114-09.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0114-10.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0114-15.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0115-00.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0115-04.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0115-08.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0115-12.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0115-17.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0115-21.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-03.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-08.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-10.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-11.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-18.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-19.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-21.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-25.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0117-02.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0117-04.png`、`docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0117-07.png` |
| `docs/18-chapter-12.md` | 第 119–124 页 | 无 |
| `docs/19-appendices.md` | 第 125–130 页 | 无 |
| `README.md` | 不适用（仓库说明） | 无 |
| `CONTRIBUTING.md` | 不适用（协作说明） | 无 |
| `.gitignore` | 不适用（Git 配置） | 无 |
| `mkdocs.yml` | 不适用（预览配置） | 无 |
| `manifest.md` | 不适用（转换登记） | 无 |
| `work/build_updated_pdf.py` | 不适用（更新版统一排版脚本） | 读取全部 `docs/*.md` 及其图片 |
| `work/updated_page_ranges.json` | 不适用（更新版页码实测记录） | 由统一排版脚本生成 |
| `outputs/tapeout-beginner-guide-updated.pdf` | 更新版第 1–138 页；不参与原稿溯源 | 当前 Markdown 的统一排版成品 |

## 图片文件

| 图片文件 | 对应原 PDF 页码 | 被引用位置 |
| --- | --- | --- |
| `docs/assets/page-001-cover.png` | 1 | `docs/01-front-matter.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0027-04.png` | 27 | `docs/04-quick-reference.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0034-02.png` | 34 | `docs/05-chapter-01.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0035-01.png` | 35 | `docs/05-chapter-01.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0035-02.png` | 35 | `docs/05-chapter-01.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0035-03.png` | 35 | `docs/05-chapter-01.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0035-04.png` | 35 | `docs/05-chapter-01.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0035-07.png` | 35 | `docs/05-chapter-01.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0036-01.png` | 36 | `docs/05-chapter-01.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0037-01.png` | 37 | `docs/05-chapter-01.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0040-02.png` | 40 | `docs/06-chapter-02.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0042-06.png` | 42 | `docs/06-chapter-02.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0045-17.png` | 45 | `docs/07-chapter-03.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0046-00.png` | 46 | `docs/07-chapter-03.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0047-10.png` | 47 | `docs/07-chapter-03.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0048-00.png` | 48 | `docs/07-chapter-03.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0054-01.png` | 54 | `docs/08-chapter-04.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0054-02.png` | 54 | `docs/08-chapter-04.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0054-13.png` | 54 | `docs/08-chapter-04.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0055-05.png` | 55 | `docs/08-chapter-04.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0055-07.png` | 55 | `docs/08-chapter-04.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0056-00.png` | 56 | `docs/08-chapter-04.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0056-07.png` | 56 | `docs/08-chapter-04.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0057-00.png` | 57 | `docs/08-chapter-04.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0060-15.png` | 60 | `docs/09-chapter-05-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0061-11.png` | 61 | `docs/09-chapter-05-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0062-07.png` | 62 | `docs/09-chapter-05-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0064-01.png` | 64 | `docs/09-chapter-05-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0065-05.png` | 65 | `docs/09-chapter-05-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0067-02.png` | 67 | `docs/09-chapter-05-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0073-07.png` | 73 | `docs/11-chapter-06.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0074-11.png` | 74 | `docs/11-chapter-06.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0075-00.png` | 75 | `docs/11-chapter-06.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0079-01.png` | 79 | `docs/12-chapter-07-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0079-05.png` | 79 | `docs/12-chapter-07-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0082-01.png` | 82 | `docs/12-chapter-07-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0083-02.png` | 83 | `docs/12-chapter-07-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0084-02.png` | 84 | `docs/12-chapter-07-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0085-00.png` | 85 | `docs/12-chapter-07-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0085-03.png` | 85 | `docs/12-chapter-07-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0085-09.png` | 85 | `docs/12-chapter-07-part-1.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0092-06.png` | 92 | `docs/14-chapter-08.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0101-02.png` | 101 | `docs/15-chapter-09.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0113-06.png` | 113 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0113-07.png` | 113 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0113-14.png` | 113 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0113-15.png` | 113 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0113-16.png` | 113 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0113-17.png` | 113 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0114-02.png` | 114 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0114-07.png` | 114 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0114-08.png` | 114 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0114-09.png` | 114 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0114-10.png` | 114 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0114-15.png` | 114 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0115-00.png` | 115 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0115-04.png` | 115 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0115-08.png` | 115 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0115-12.png` | 115 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0115-17.png` | 115 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0115-21.png` | 115 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-03.png` | 116 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-08.png` | 116 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-10.png` | 116 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-11.png` | 116 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-18.png` | 116 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-19.png` | 116 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-21.png` | 116 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0116-25.png` | 116 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0117-02.png` | 117 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0117-04.png` | 117 | `docs/17-chapter-11.md` |
| `docs/assets/tapeout-beginner-guide-v1.5-web.pdf-0117-07.png` | 117 | `docs/17-chapter-11.md` |

## 未被 Markdown 引用的抽取图片

无。
