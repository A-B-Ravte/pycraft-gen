// frontend/js/app.js

const generateBtn = document.getElementById("generateBtn");
const promptInput = document.getElementById("promptInput");
const outputBox = document.getElementById("outputBox");

if (generateBtn) {
    generateBtn.addEventListener("click", async () => {

        const prompt = promptInput.value.trim();

        if (!prompt) {
            alert("Please enter a prompt");
            return;
        }

        outputBox.textContent = ""; // Clear previous output

        const response = await fetch(
            "http://127.0.0.1:8000/api/generate/pycraft-qwen-2.5-7b",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ prompt: prompt })
            }
        );

        const reader = response.body.getReader();
        const decoder = new TextDecoder("utf-8");

        while (true) {
            const { value, done } = await reader.read();
            if (done) break;

            const chunk = decoder.decode(value);
            outputBox.textContent += chunk;
            outputBox.scrollTop = outputBox.scrollHeight;
        }
    });
}

// ---------- HELPER PAGE LOGIC ----------

const helperBtn = document.getElementById("helperBtn");
const helperInput = document.getElementById("helperInput");
const helperOutput = document.getElementById("helperOutput");

if (helperBtn) {
    helperBtn.addEventListener("click", async () => {

        const code = helperInput.value.trim();

        if (!code) {
            alert("Please paste code");
            return;
        }

        helperOutput.textContent = "";

        const response = await fetch(
            "http://127.0.0.1:8000/api/helper/pycraft-qwen-2.5-7b",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ code: code })
            }
        );

        const reader = response.body.getReader();
        const decoder = new TextDecoder("utf-8");

        while (true) {
            const { value, done } = await reader.read();
            if (done) break;

            const chunk = decoder.decode(value);
            helperOutput.textContent += chunk;
            helperOutput.scrollTop = helperOutput.scrollHeight;
        }
    });
}