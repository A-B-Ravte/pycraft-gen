from unsloth import FastLanguageModel
import torch

model_name = "your-username/pycraft-qwen-2.5-7b-adapter" # Your HF path

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = model_name,
    max_seq_length = 2048,
    dtype = None,
    load_in_4bit = True,
)
FastLanguageModel.for_inference(model) # 2x faster inference

# Test Prompt
inputs = tokenizer(
    [
        "<|im_start|>user\nWrite a Python function to calculate the Fibonacci sequence.<|im_end|>\n<|im_start|>assistant\n"
    ], return_tensors = "pt").to("cuda")

outputs = model.generate(**inputs, max_new_tokens = 128)
print(tokenizer.batch_decode(outputs))