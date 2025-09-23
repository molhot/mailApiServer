# Pythonの公式イメージを使用
FROM python:3.11-slim

# 作業ディレクトリを作成
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install requests

# まず requirements.txt だけコピー（app/ の中から）
COPY ./app/requirements.txt ./

COPY ./app /app

# パッケージをインストール（requirements.txtがある場合）
RUN pip install --no-cache-dir -r requirements.txt


