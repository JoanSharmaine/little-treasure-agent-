"""Daily report generation."""

from __future__ import annotations

from typing import List


def generate_markdown_report(news: List[dict], tips: List[str]) -> str:
    """Create a markdown formatted report.

    Parameters
    ----------
    news : List[dict]
        News entries.
    tips : List[str]
        Suggestions for the portfolio.

    Returns
    -------
    str
        Markdown content.
    """
    lines = ["# 情侣日报", "", "## 财经新闻"]
    for item in news:
        lines.append(f"- [{item['title']}]({item['link']})")
    lines.append("\n## 调仓建议")
    for t in tips:
        lines.append(f"- {t}")
    lines.append("\n*小提示：以上内容仅供参考*")
    return "\n".join(lines)
