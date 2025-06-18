from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import torch

base_model = "bigcode/starcoderbase-1b"
tokenizer = AutoTokenizer.from_pretrained(base_model)
model = AutoModelForCausalLM.from_pretrained(
    base_model,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).to("cuda" if torch.cuda.is_available() else "cpu")


adapter_path = "./finetuned_model_ex1/finetuned_model40_ex1"

# LoRAアダプタを適用
model = PeftModel.from_pretrained(model, adapter_path)
model.eval()

def generate_code(prompt: str, max_tokens: int = 128, temperature: float = 0.2) -> str:
  inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
  outputs = model.generate(
      **inputs,
      max_new_tokens = max_tokens,
      temperature = temperature,
      do_sample = True
  )
  return tokenizer.decode(outputs[0], skip_special_tokens=True)
