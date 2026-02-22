import json

CONFIG_PATH = 'configs/model.json'

def load_models():
    with open(CONFIG_PATH, 'r') as file:
        # Convert the file content to a Python dictionary
        return json.load(file)['Models']
    
def get_model_by_name(name: str):
    models = load_models()
    for m in models:
        if m["model_name"] == name:
            return m
    raise ValueError("Model not found")