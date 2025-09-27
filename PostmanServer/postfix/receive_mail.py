#!/usr/bin/env python3

import sys
import email
import json
import requests

with open("/tmp/debug.log", "a") as f:
    f.write("スクリプト呼ばれた！\n")

# 読み取り
raw_email = sys.stdin.read()
msg = email.message_from_string(raw_email)

from_addr = msg.get("From")
subject = msg.get("Subject")
to_addr = msg.get("To")

# 本文
body = ""
if msg.is_multipart():
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True).decode()
            break
else:
    body = msg.get_payload(decode=True).decode()

# ローカルAPI (Postman mock server or 自作API) にPOST
api_url = "http://host.docker.internal:3000/test-endpoint"  # PostmanのMock URLに変更可

payload = {
    "from": from_addr,
    "to": to_addr,
    "subject": subject,
    "body": body
}

try:
    res = requests.post(api_url, json=payload)
    print(f"Posted to API. Status: {res.status_code}")
except Exception as e:
    print(f"Failed to call API: {e}")

# ログにも保存
with open("/tmp/received_emails.log", "a") as f:
    f.write(json.dumps(payload, ensure_ascii=False) + "\n")
