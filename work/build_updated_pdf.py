from __future__ import annotations

import html
import json
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    Image,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "tapeout-beginner-guide-updated.pdf"
RANGES = ROOT / "work" / "updated_page_ranges.json"
FILES = [
    "01-front-matter.md",
    "02-credits-a.md",
    "03-credits-b.md",
    "04-quick-reference.md",
    "05-chapter-01.md",
    "06-chapter-02.md",
    "07-chapter-03.md",
    "08-chapter-04.md",
    "09-chapter-05-part-1.md",
    "10-chapter-05-part-2.md",
    "11-chapter-06.md",
    "12-chapter-07-part-1.md",
    "13-chapter-07-part-2.md",
    "14-chapter-08.md",
    "15-chapter-09.md",
    "16-chapter-10.md",
    "17-chapter-11.md",
    "18-chapter-12.md",
    "19-appendices.md",
]


class Marker(Flowable):
    def __init__(self, key: str, sink: dict[str, int]):
        super().__init__()
        self.key = key
        self.sink = sink
        self.width = 0
        self.height = 0

    def draw(self):
        self.sink[self.key] = self.canv.getPageNumber()


class UpdatedGuideDoc(BaseDocTemplate):
    def __init__(self, filename: str):
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=18 * mm,
            rightMargin=18 * mm,
            topMargin=18 * mm,
            bottomMargin=18 * mm,
            title="TapeOut 新手完全指南（更新版）",
            author="TapeOut 社区协作稿",
        )
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="main")
        self.addPageTemplates(PageTemplate(id="body", frames=[frame], onPage=self._footer))

    def _footer(self, canvas, _doc):
        canvas.saveState()
        canvas.setFont("NotoSansSC", 8)
        canvas.setFillColor(colors.HexColor("#666666"))
        canvas.drawCentredString(A4[0] / 2, 9 * mm, f"更新版  ·  第 {canvas.getPageNumber()} 页")
        canvas.restoreState()


def inline_markup(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"!\[([^]]*)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(
        r"\[([^]]+)\]\(([^)]+)\)",
        lambda m: f'<link href="{html.escape(m.group(2), quote=True)}" color="#1259a7">{m.group(1)}</link>',
        text,
    )
    text = re.sub(r"`([^`]+)`", r'<font name="NotoSansSC">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    return text


def styles():
    base = getSampleStyleSheet()
    common = dict(fontName="NotoSansSC", textColor=colors.HexColor("#202124"), leading=16)
    return {
        "h1": ParagraphStyle("h1", parent=base["Heading1"], fontName="NotoSansSC-Bold", fontSize=22, leading=29, spaceAfter=12, textColor=colors.HexColor("#102a43")),
        "h2": ParagraphStyle("h2", parent=base["Heading2"], fontName="NotoSansSC-Bold", fontSize=17, leading=23, spaceBefore=9, spaceAfter=8, textColor=colors.HexColor("#163d66")),
        "h3": ParagraphStyle("h3", parent=base["Heading3"], fontName="NotoSansSC-Bold", fontSize=14, leading=20, spaceBefore=8, spaceAfter=6, textColor=colors.HexColor("#24527a")),
        "h4": ParagraphStyle("h4", parent=base["Heading4"], fontName="NotoSansSC-Bold", fontSize=11.5, leading=17, spaceBefore=6, spaceAfter=4),
        "body": ParagraphStyle("body", parent=base["BodyText"], fontSize=9.8, spaceAfter=5, **common),
        "bullet": ParagraphStyle("bullet", parent=base["BodyText"], fontSize=9.5, leftIndent=13, firstLineIndent=-9, spaceAfter=3, **common),
        "quote": ParagraphStyle("quote", parent=base["BodyText"], fontSize=9.4, leftIndent=10, rightIndent=6, borderColor=colors.HexColor("#8aa4bd"), borderWidth=1, borderPadding=6, backColor=colors.HexColor("#f3f7fa"), spaceAfter=6, **common),
        "table": ParagraphStyle("table", parent=base["BodyText"], fontName="NotoSansSC", fontSize=7.5, leading=10, leftIndent=4, rightIndent=4, spaceAfter=2, textColor=colors.HexColor("#333333")),
    }


def image_flow(path: Path):
    if not path.exists():
        return Paragraph(f"[缺少图片：{html.escape(str(path.name))}]", STYLES["body"])
    img = Image(str(path))
    max_w, max_h = 170 * mm, 190 * mm
    ratio = min(max_w / img.imageWidth, max_h / img.imageHeight, 1)
    img.drawWidth = img.imageWidth * ratio
    img.drawHeight = img.imageHeight * ratio
    img.hAlign = "CENTER"
    return img


def parse_file(filename: str, markers: dict[str, int]):
    path = DOCS / filename
    lines = path.read_text(encoding="utf-8").splitlines()
    story: list[Flowable] = [Marker(f"start:{filename}", markers)]
    in_fence = False
    guide_open = False
    for raw in lines:
        line = raw.strip()
        if line.startswith("<!--") and line.endswith("-->"):
            continue
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not line:
            story.append(Spacer(1, 2.5 * mm))
            continue
        image_match = re.fullmatch(r"!\[[^]]*\]\(([^)]+)\)", line)
        if image_match:
            story.append(image_flow(path.parent / image_match.group(1)))
            story.append(Spacer(1, 3 * mm))
            continue
        heading = re.match(r"^(#{1,4})\s+(.+)$", line)
        if heading:
            level, title = len(heading.group(1)), heading.group(2)
            if title == "TapeOut DeWeb 生态靓号新手指南":
                story.extend([PageBreak(), Marker("guide:start", markers)])
                guide_open = True
            elif filename == "08-chapter-04.md" and title == "本章要点" and guide_open:
                story.extend([Marker("guide:end", markers), PageBreak()])
                guide_open = False
            story.append(Paragraph(inline_markup(title), STYLES[f"h{level}"]))
            continue
        if line.startswith(">"):
            story.append(Paragraph(inline_markup(line.lstrip("> ")), STYLES["quote"]))
            continue
        bullet = re.match(r"^[-*]\s+(.+)$", line)
        numbered = re.match(r"^(\d+)\.\s+(.+)$", line)
        if bullet:
            story.append(Paragraph("• " + inline_markup(bullet.group(1)), STYLES["bullet"]))
        elif numbered:
            story.append(Paragraph(numbered.group(1) + ". " + inline_markup(numbered.group(2)), STYLES["bullet"]))
        elif line.startswith("|"):
            story.append(Paragraph(inline_markup(line), STYLES["table"]))
        elif in_fence:
            story.append(Paragraph(inline_markup(line), STYLES["table"]))
        else:
            story.append(Paragraph(inline_markup(line), STYLES["body"]))
    story.append(Marker(f"end:{filename}", markers))
    return story


pdfmetrics.registerFont(TTFont("NotoSansSC", r"C:\Windows\Fonts\NotoSansSC-VF.ttf"))
pdfmetrics.registerFont(TTFont("NotoSansSC-Bold", r"C:\Windows\Fonts\NotoSansSC-VF.ttf", subfontIndex=0))
STYLES = styles()


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    markers: dict[str, int] = {}
    story: list[Flowable] = []
    for index, filename in enumerate(FILES):
        if index:
            story.append(PageBreak())
        story.extend(parse_file(filename, markers))
    UpdatedGuideDoc(str(OUTPUT)).build(story)
    payload = {
        "pdf": str(OUTPUT.relative_to(ROOT)).replace("\\", "/"),
        "total_pages": max(markers.values()),
        "guide_pages": markers["guide:end"] - markers["guide:start"] + 1,
        "guide_range": [markers["guide:start"], markers["guide:end"]],
        "files": {
            filename: [markers[f"start:{filename}"], markers[f"end:{filename}"]]
            for filename in FILES
        },
    }
    RANGES.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
