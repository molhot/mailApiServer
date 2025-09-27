## 動作確認手順書 
 
### docker compose up --build 
これを実行する 
コンテナがこれで立ち上がる 
 
### 別窓にて docker exec -it コンテナID bash を実行 
上記コマンドにてコンテナにbashではいってください 
※ docker psにて立ち上がっているコンテナが存在しているか確認できる 
 
### 擬似的なメールの送信 
echo "Hello from inside container" | mail -s "Test Mail" mailbot@localhost 
上記にてテスト的にメールを送信することができる 