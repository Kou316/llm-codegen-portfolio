# llm-codegen-portfolio

LoRAによってファインチューニングした小規模LLM（StarCoderBase）を使って、競技プログラミング問題の模範解答を自動生成するWebアプリです。（製作中）

React + Typescriptでフロントエンドを構築し、Google Colab上のFlask APIと接続しています。

---

##特徴

-LoRAによる軽量なファインチューニング

-自然言語で問題文を入力 → LLMが模範解答を生成

-フロントエンドはReact + Typescript、バックエンドはFlask + Google Colab + pyngrok　　

-python / C++ / Javaなど多言語対応（2025/6/17時点Pythonのみ対応）　　

---

##使用技術
| 分類          | 技術/ライブラリ                        |
|---------------|---------------------------------------|
| フロントエンド  | React, Typescript, fetch              |
| バックエンド    | Flask, pyngrok, Google Colab          |
| モデル          | StarCoderBase-1B（LoRAチューニング）    |
| その他          | Hugging Face Transformers, peft, ngrok |



##起動方法
---

###フロントエンドの起動（React）

```bash
cd frontend
npm install
npm run dev
```
-ブラウザで https://localhost:5173　を開きます。

-フロントエンドからバックエンドの.generateAPIにリクエストを送信します。

###バックエンド（Flask + LoRA）

バックエンドは　Flask　による簡易APIサーバとして構築され、以下のような処理を行います
1.Python環境の準備
```python
cd backend
pip install -r requirements.txt
```

2.モデルの用意（Colab推奨）
-finetuned_model_ex1/　以下にLoRAの　adapter_model.safetensors　などを配置します。
-モデルのロード先は　model.py　の中で指定されます。

3.Flaskサーバの起動
```bash
python app.py
```
-デフォルトで　https://127.0.0.1:5000　に立ち上がります。

-ngrokを使用する場合
```bash
ngrok http 5000
```
-発行されたURLをReact側で使用することで外部からのアクセスも可能です。


