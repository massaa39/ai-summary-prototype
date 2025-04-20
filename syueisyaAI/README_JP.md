# プレスリリース要約生成プロトタイプ

## 概要
本プロジェクトは、翔泳社様向けにプレスリリース要約をAIで自動生成するデモアプリケーションです。

## 主な機能
- 要約生成API：300〜400字で要約、タイトル自動生成、想定読者分析
- 日本語UI付きWebデモ (`/demo`)
- GitHub Codespaces 対応でワンクリック起動

## 必要環境
- Python 3.10+
- GitHub Codespaces 推奨

## 環境変数設定
1. `.env.example` をコピーして `.env` を作成
2. `OPENAI_API_KEY` にキーを設定

## 起動方法
```bash
# ローカル起動
bash run_demo.sh

# Codespaces
リポジトリを開く → 自動で `run_demo.sh` が実行

## 環境変数
- `OPENAI_API_KEY`: OpenAI API キー

## 開発
```bash
# ローカルで動かす場合
bash run_demo.sh
```
## ディレクトリ構成
ai-summary-prototype/
├─ .devcontainer/
├─ Dockerfile
├─ run_demo.sh
├─ requirements.txt
├─ .env.example
├─ app/
│  ├─ main.py
│  ├─ routers/
│  ├─ components/
│  └─ static/
└─ README_JP.md

動作確認
ブラウザで http://localhost:8000/demo にアクセス