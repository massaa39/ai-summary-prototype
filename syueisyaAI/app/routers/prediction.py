from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import openai

openai.api_key = "${OPENAI_API_KEY}"

class SummarizeRequest(BaseModel):
    text: str

class SummarizeResponse(BaseModel):
    title: str
    summary: str
    audience: str

router = APIRouter()

@router.post("/summarize", response_model=SummarizeResponse)
async def summarize(req: SummarizeRequest):
    prompt = (
        f"以下のプレスリリースを300〜400字で要約し、タイトルを生成してください。"
        f"さらに、想定読者層を分析してその層向けに書いてください。\n\n{req.text}"
    )
    try:
        res = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        content = res.choices[0].message.content.strip()
        # 簡易パース (タイトル|サマリー|読者)
        title, summary, audience = content.split("\n", 2)
        return SummarizeResponse(title=title, summary=summary, audience=audience)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
