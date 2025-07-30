"""Daily report generation."""
from __future__ import annotations

from typing import List, Dict
import pandas as pd
from datetime import date

import os
from langchain_community.llms import OpenAI


def _load_llm() -> OpenAI | None:
    """Return an OpenAI LLM instance if API key is available."""
    if os.getenv("OPENAI_API_KEY"):
        return OpenAI()
    return None

llm = _load_llm()

def generate_report(news: List[str], analysis: pd.DataFrame) -> str:
    """Generate a markdown daily report summarizing news and portfolio."""
    news_md = "\n".join(f"- {item}" for item in news)
    table_md = analysis.to_markdown(index=False)
    tips_prompt = "给情侣俩的理财小提示，结合以上新闻和持仓分析，50字以内。"
    if llm:
        tip = llm.invoke(tips_prompt).strip()
    else:
        tip = "祝投资顺利，谨慎评估风险。"
    report = (
        f"# 情侣日报 {date.today()}\n\n"
        f"## 今日要闻\n{news_md}\n\n"
        f"## 持仓分析\n{table_md}\n\n"
        f"**小提示：{tip}**"
    )
    return report
