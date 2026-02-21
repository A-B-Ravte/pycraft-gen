from llama_cpp import Llama
import os

class PyCraftEngine:
    def __init__(self, model_path: str):
        print(f"Loading model from {model_path}... Please wait.")
        # n_ctx: The 'memory' of the conversation (2048 is standard)
        # n_threads: Number of CPU cores to use. 4 is usually a sweet spot for laptops.
        self.llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=4,
            verbose=False # Set to True if you want to see the 'math' in terminal
        )
        print("✅ Model loaded successfully!")

    def generate_stream(self, prompt: str):
        formatted_prompt = f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
        
        # Use stream=True to get a generator
        stream = self.llm(
            formatted_prompt,
            max_tokens=512,
            stop=["<|im_end|>", "<|im_start|>"],
            stream=True, # THIS IS KEY FOR STEAMING 
            temperature=0.2
        )
        
        for chunk in stream:
            token = chunk['choices'][0]['text']
            yield token  # Yield each piece of text as it arrives