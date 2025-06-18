from flask import Flask, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods = ["POST"])

def generate():
  data = request.get_json()
  prompt = data.get("prompt", "")
  max_tokens = data.get("max_tokens", 128)

  inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
  outputs = model.generate(
      **inputs,
      max_new_tokens = max_tokens,
      do_sample = True
  )

  output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
  return jsonify({"code": output_text})

from threading import Thread
def run():
  app.run(port=5000)
Thread(target=run).start()

public_url = ngrok.connect(5000)
print("Flask is live at;", public_url)
