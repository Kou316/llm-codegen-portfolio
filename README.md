# llm-codegen-portfolio

LoRAによってファインチューニングした小規模LLM（StarCoderBase）を使って、競技プログラミング問題の模範解答を自動生成するWebアプリです。（製作中）
React + Typescriptでフロントエンドを構築し、Google Colab上のFlask APIと接続しています。

---

##特徴

-LoRAによる軽量ファインチューニング
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


###フロントエンド（React）

```bash
cd frontend
npm install
npm run dev

```


###バックエンド
バックエンドは　Flask　による簡易APIサーバとして構築され、以下のような処理を行います:

-モデルとトークナイザーを読み込み（StarCoderBase-1B）
-LoRAのadapterを読み込み
-`/generate`エンドポイントでPOSTを受け取り、コード生成して返す

```python
@app.route("/generate", methods=["POST"])
def generate():
  data = request.get_json()
  prompt = data.get("prompt", "")
  max_tokens - data.get("max_tokens", 128)

  inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
  outputs = model.generate(
    **inputs,
    max_new_tokens=max_tokens,
    do_sample=True
  )

  output_text = tokenizer.decode(output[0], skip_special_toknes=True)
  return jsonfy({"code": output_text})
```



