import msal
import os

# MSALの設定
TENAN_ID=os.getenv('TENANT_ID')
authority = f'https://login.microsoftonline.com/{TENAN_ID}'
client_id = os.getenv('CLIENT_ID')
scope = ['https://graph.microsoft.com/.default']
app = msal.ConfidentialClientApplication(
    client_id, 
    authority=authority, 
    client_credential=os.getenv('MY_MICROSOFT_SECRET_VALUE') # クライアントシークレットを指定
)

result = app.acquire_token_silent(scope, account=None)
if not result: # キャッシュされたトークンがない場合、新たにトークンを取得する 
    result = app.acquire_token_for_client(scopes=scope)
if "access_token" in result: # アクセストークンを取得 
    access_token = result["access_token"] # APIのURLを指定 api_url = "https://graph.microsoft.com/v1.0/<resource>" headers = { 'Authorization': 'Bearer ' + access_token, "Content-Type": "application/json" } data={ # APIのクエリ等をここに } response = requests.post(api_url, headers=headers, json=data) if response.status_code == 201: print("成功") else: print(f"◯◯に失敗しました。. Status code: {response.status_code}")
    print("アクセストークン取得")
else:
    print("MSAL での認証に失敗しました。")
