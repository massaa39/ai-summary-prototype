import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from dotenv import load_dotenv
from app.routers.prediction import router as pred_router

# .env をロード
load_dotenv(dotenv_path=".env")

# FastAPI アプリケーション生成
app = FastAPI(title="プレスリリース要約生成API")

# API ルーター登録
app.include_router(pred_router, prefix="/api")

# 静的ファイルを /static にマウント
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# テンプレート設定
templates = Jinja2Templates(directory="app/static")

# ルートエンドポイント（UI）
@app.get("/", include_in_schema=False)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# デモエンドポイント（UI）
@app.get("/demo", include_in_schema=False)
async def demo(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
