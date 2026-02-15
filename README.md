# 🚀 PyCraft-Gen: Applied AI Code Expert

PyCraft-Gen is a specialized AI coding assistant powered by a fine-tuned **Qwen2.5-Coder-7B** model. Designed for local execution, it utilizes **GGUF quantization** to perform real-time code generation on standard consumer CPUs, bypassing the need for expensive NVIDIA GPUs.

## 🌟 Key Features
* **Custom Fine-Tuned Brain:** Fine-tuned on the `CodeFeedback-Filtered-Instruction` dataset using LoRA (Low-Rank Adaptation).
* **Edge-Ready Inference:** Optimized for CPU via `llama.cpp` and 4-bit GGUF quantization (Q4_K_M).
* **Real-Time Streaming:** Tokens are streamed to the UI as they are generated for a zero-lag user experience.
* **Dark-Mode UI:** Built with Tailwind CSS for a professional developer-centric interface.

## 🏗️ Technical Architecture

1.  **Model Training:** Trained in Google Colab using `Unsloth` to optimize VRAM and training speed.
2.  **Quantization:** Converted from Safetensors to 4-bit GGUF format for memory efficiency.
3.  **Backend:** FastAPI handles the request-response lifecycle and manages the C++ bindings for the model.
4.  **Frontend:** Asynchronous JavaScript Fetch API handles the `ReadableStream` for real-time code typing.

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.10+
* At least 8GB of RAM (16GB recommended)

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/A-B-Ravte/pycraft-gen.git](https://github.com/A-B-Ravte/pycraft-gen.git)
cd pycraft-gen

# Set up virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn jinja2 python-dotenv llama-cpp-python
```

### 3. Model Setup
Download the fine-tuned GGUF model from my Hugging Face:
A-B-Ravte/pycraft-qwen-2.5-7b-adapter

Place the .gguf file in the models/ directory.

### 4. Run the app
python -m app.main

Visit http://127.0.0.1:8000 to start generating code.

📊 Performance Optimization
To run a 7-billion parameter model on a CPU, I implemented 4-bit Medium Quantization (Q4_K_M). This reduces the model size from ~28GB (FP32) to ~4.4GB, allowing for smooth execution on local hardware while maintaining high coding accuracy.

👨‍💻 Author
Aakash Ravte - Senior Software Engineer | Applied AI & Intelligent Automation