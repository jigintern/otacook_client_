# 仕様書

- 2019年 9月6日
- jig.jpインターンAチーム
- システム名 Otacook


---

# データ管理仕様書
## 概要
### 本システムが利用するデータ
- ユーザーが入力するユーザーデータ
- システムが生成するユーザー管理用IDとセッションID、レート
- システム管理者が入力するコンテスト問題情報
- ユーザーが入力するコンテスト回答データ
- システムが生成するコンテストマッチング用データ
### 情報漏洩リスクを把握するための資料
- 以下の攻撃が予想される
    - JSON形式ファイルを用いることによって予想される攻撃
        - クロスサイト・スクリプティング
        - eval インジェクション
    - セッションハイジャック
### データベース構造
- 本システムは /projects/superdbpi 配下のjson形式ファイルに保存される
- ユーザーに関連するデータは/users　配下に保存される
- コンテストに関連するデータは/contests 配下に保存される
- 
```
    superdbpi/
        |- contests/
        |    └ entry/
        |        └ (contest_id)/
        |            └ (user_id): ユーザーの参加したコンテストの回答情報を記録するjson形式のファイル
        |    └ groops/
        |        └ (contest_id)/
        |            └ (groop_id): コンテスト投票時のマッチングリストを記録するjson形式のファイル
        |    └ groopindexfromid/
        |        └ (contest_id)/
        |            └ (user_id): ユーザーIDとグループIDの紐付けを行うjson形式のファイル
        |    └ info/
        |        └ (contest_id): コンテストの基本情報を記録するjson形式のファイル
        |    └ recipes/
        |        └ (contest_id): コンテスト問題のレシピを記録するjson形式のファイル
        |    └ materials/
        |        └ (contest_id): コンテスト問題の材料リストを記録するjson形式のファイル
        |    └ now: 実行中のコンテストの状態を記録するjson形式のファイル
        |- users/
             └ idindex/
                 └ (user_id): ユーザーの基本情報を記録するjson形式のファイル
             └ maillist: ユーザーが入力したIDと管理用のユーザーIDの紐付けを行うjson形式のファイル
             └ sessionindex/
                 └ (session_id): セッションIDとユーザーIDの紐付けを行うjson形式のファイル
    
    www/files/
        └ images: コンテストでユーザーが投稿した画像ファイル
```
                 
|ファイル(フォルダ)名にしているもの|意味|
|-|-|
|user_id|管理用ユーザーID|
|contest_id|コンテストのID|
|session_id|ログインセション時に生成されるID|

## 内容

### 各データ

|データ名称|取得方法|保存先|利用方法|
|-|-|-|-|-|
||
|ユーザーのデータ|
|ユーザー名|ユーザーが入力|users/idindex/(user_id)|マイページに表示|
|ユーザーID|ユーザーが入力|users/idindex/(user_id)|ログイン時|
|パスワード|ユーザーが入力|users/idindex/(user_id)|ログイン時|
|管理者用ユーザーID(user_id)|APIが生成|users/idindex/(user_id)|システム内でのユーザー判別|
|レート|システムが生成|users/idindex/(user_id)|コンテストの結果によって変動する値|
|セッションID|システムが生成|users/sessioindex/(session_id)|ログインの状態の管理
||
|コンテストのデータ|
|コンテストID|管理者が入力|contests/now|コンテストIDによる判別のためフォルダ(ファイル)名になる|
|レシピ|管理者が入力|contests/recipes/(contest_id)|コンテスト問題用料理のレシピ|
|料理名|ユーザーが入力|contests/entry/(contest_id)/(user_id)|コンテストに提出する料理名|
|コメント|ユーザーが入力|contests/entry/(contest_id)/(user_id)|提出時に料理に対して送るコメント|
|料理写真|ユーザーが入力|contests/entry/(contest_id)/(user_id)|コンテストに提出する料理名|
|実行期間|APIから取得|contests/info(contest_id)|コンテストの投稿可能時間を決める|
|実行状況|APIから取得|contests/now|コンテストの状況を(投稿・投票・結果)から決める|
|参加人数|システムが生成|保存しない|コンテストに参加した人数を管理|
|投票数|システムが生成|contests/groops/(contest_id)/(groop_id)|コンテストの投票数を管理|
|グループID|APIから取得|contests/groopindexfromid/(contest_id)/(user_id)|グループごとにユーザーとの紐付け|

### データの保存について
- コンテストに参加した人数のデータのみ、システムの算出時のみ与えられ、保存されない
- その他、すべてのデータは、**平文で**システム終了まで保存される



---

# デプロイ仕様書
### バージョンアップ手順
- デプロイ手順
    - `/opt/project/superdbpi`で`python localserver.py`を実行する。
    - `/opt/project/product/www`に`npm run build`したビルド済みのファイルを配置する
- 動作確認方法
    - `https://t1.intern.jigd.info`に接続し、ログイン画面が表示されるかを確認する


---

# 開発仕様書
## 概要
### 開発に用いたソフトウェアや環境一覧
- ソースコード共有: git
- 連絡: Slack
- フロント開発用フレームワーク: Vue.js 3.11.0
- Vue.js用マテリアルデザインフレームワーク: Vuetify 2.0.0
- パッケージ管理ツール: npm 6.9.3
- サーバー開発用言語: Python 3.6.8
- web開発フレームワーク: flask 1.1.1
- データフォーマット: JSON 

### 開発開始作業の手順などの説明
- コンソールでサーバー作業用ディレクトリ(`otacook_client/superdbpi`)に移動し、`python localserver.py`でlocalhost:8080を起動した状態で、フロント作業用ディレクトリ(`otacook_client/`)で`npm run server`でlocalhost:8081を起動し、開発を行う。
## 内容
### 開発に必要なソフトウェア
- ソースコード共有: git
- フロント開発用フレームワーク: Vue.js 3.11.0
- サーバー開発用言語: Python 3.6.8
- データフォーマット: JSON
### 利用ライブラリ
- Vue.js用マテリアルデザインフレームワーク: Vuetify 2.0.0
- パッケージ管理ツール: npm 6.9.3
- web開発フレームワーク: flask 1.1.1
### 対象端末/OS
- Window
- MacOS
- Linux
### 対象ブラウザ
- Google chrome


---

# テスト仕様書

## テスト手順

### 1.ヘッダー
- どのページにおいてもヘッダーが表示されている
- サインイン、サインアップを行っていない場合は、ヘッダーの右上に「SIGNIN」、「SIGNUP」、左上にシステムのロゴが表示されている
    - 「SIGNIN」を押すと `https://t1.intern.jigd.info/#/signin` で**サインインページ**へ移動
    - 「SIGNUP」を押すと `https://t1.intern.jigd.info/#/signup` で**サインアップページ**へ移動
- サインイン、サインアップを行っている場合は、ヘッダーの右上に「MYPAGE」、「SIGNOUT」、左上にシステムのロゴが表示されている
    - 「MYPAGE」を押すと`https://t1.intern.jigd.info/files/dist/#/mypage`で**マイページ**へ移動
    - 「SINGOUT」を押すとサインイン、サインアップを行っていない状態になる
- ロゴを押すと`https://t1.intern.jigd.info/files/dist/#/`で**トップページ**に移動
### 2.トップページ
- `https://t1.intern.jigd.info/#/`で**トップページ**が表示されている
- /superdbpi/contests/配下のnowというjson形式ファイル内の"status"のvalueが
    - 0のとき、「コンテスト開催前」の状態となり、次回開催予定のコンテストが表示される
    - 1・2のとき、「コンテスト開催中」の状態となり、ページ下の「問題ページへ」を押すと`https://t1.intern.jigd.info/files/dist/#/questionpage`で**問題ページ**へ移動
    - 3のとき、「コンテスト終了」の状態となり、画面下の「結果を見る」を押すと`https://t1.intern.jigd.info/files/dist/#/rankingpage`で**ランキングページ**ヘ移動
### 3.サインアップページ
- `https://t1.intern.jigd.info/#/signup`で**サインアップページ**が表示されている
- 「ユーザー名」が入力できる
- 「ユーザーID」が入力できる
- 「パスワード」が入力できる
- 「サインアップ」ボタンを押すと
    - ユーザー名、ユーザーID、パスワードのどれかが入力されていなければ「入力していない項目があります」の警告が表示され、ページは移動しない
    - すべて入力しているとその直前ページに移動
- 「サインインページへ」ボタンを押すと`https://t1.intern.jigd.info/#/signin`で**サインインページ**に移動
### 4.サインインページ
- `https://t1.intern.jigd.info/#/signin`で**サインインページ**が表示されている
- 「ユーザーID」が入力できる
- 「パスワード」が入力できる
- 「サインイン」を押すと
    - ユーザーID、パスワードが入力されていなければ「入力していない項目があります」の警告が表示され、ページは移動しない
    - 入力したユーザーIDとパスワードがサインアップしたものと異なるときは「ユーザーIDを確認」の警告が表示され、ページは移動しない
    - 入力したユーザーIDとパスワードがサインアップしたものと一致したときは、サインインが完了しその直前のページに移動する
- 「サインアップページへ」を押すと`https://t1.intern.jigd.info/#/signup`で**サインアップページ**に移動する
### 5.マイページ
- `https://t1.intern.jigd.info/#/mypage`で**マイページ**が表示されている
- ユーザー情報として、「ユーザー名」と「ユーザーID」、「レート」が表示されている
### 6.問題ページ
- `https://t1.intern.jigd.info/#/questionpage`で**問題ページ**に移動する
- コンテスト問題の「お題」、「材料リスト」、「レシピ」が表示されている
- サインインを完了していると、
    - 「コンテストに提出する」が表示され、押すと`https://t1.intern.jigd.info/#/answerpage`で**提出ページ**に移動する
- サインインを完了していないと、
    - 「サインイン」が表示され、押すと`https://t1.intern.jigd.info/#/signin`で**サインインページ**に移動する
- コンテストの状態が投票フェーズだと
    - 「投票ページへ」が表示され、押すと`https://t1.intern.jigd.info/#/votepage`で**投票ページ**に移動する
### 7.提出ページ
- `https://t1.intern.jigd.info/#/answerpage`で**提出ページ**が表示されている
- 「料理名」が入力できる
- 「コメント」が入力できる
- 「写真」が選択できる
- 「送信」を押したとき
    - 「料理名」、「コメント」を入力していないと、「すべての項目を入力してから送信してください！」の警告が表示される
    - 「写真」を選択していないと「ファイルが選択されていません」の警告が表示される
    - 「料理名」、「コメント」を入力し、「写真」を選択していると、回答が提出され`https://t1.intern.jigd.info/#/questionpage`で問題ページに移動する
### 8.投票ページ
- `https://t1.intern.jigd.info/#/votepage`で**投票ページ**が表示されている
- 「料理名」、「写真」、「コメント」で構成される各ユーザーの回答が5つ並んで表示されている
- 1位、2位、3位の料理を選ぶことができる
- いずれかの項目を選択したいと「選択していない項目があります」という警告が表示される
- 全ての項目を選択し、「投票する」を押すと、投票が行われ、`https://t1.intern.jigd.info/#/questionpage`で**問題ページ**に移動する
### 9.結果ページ
- `https://t1.intern.jigd.info/#/rankingpage`で**結果ページ**が表示されている
- ユーザーがコンテストに参加し、投稿していれば
    - 1~5位までのユーザーごとの投票による順位が表示される
    - 各「ユーザーの名前」と投稿した料理のデータが表示される
    - 「トップページへ」ボタンを押すと、`https://t1.intern.jigd.info/#/`で**トップページ**へ移動する
- ユーザーがコンテストに参加していなければ
    - 「コンテストに参加していないかマッチング可能人数に達していなかったため表示できません」が表示される
    - 「トップページへ」を押すと、`https://t1.intern.jigd.info/#/`で**トップページ**へ移動する
- サインアップ、サインインを行っていない場合は
    - 「サインインしてください」の警告が出される
    - 「サインイン」を押すと`https://t1.intern.jigd.info/#/signin`で**サインインページ**に移動する