# 🔴 COMPONENT: 要約ロジックサービス
import openai
import os
from app.routers.scraper import ScrapeResponse

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str) -> ScrapeResponse:
    prompt = f"プレスリリースを300～400字で要約し、タイトル・読者を出力してください。\n{text}"  
    res = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7
    )
    content = res.choices[0].message.content.split('\n')
    return ScrapeResponse(
        title=content[0].replace("タイトル：", ""),
        summary=content[1].replace("要約：", ""),
        audience=content[2].replace("対象読者：", "")
    )