from backend.services.model_loader import PyCraftEngine
from backend.services.config_service import get_model_by_name


def generate_inference(model_name: str, prompt: str):
    model_details = get_model_by_name(model_name)
    model_config = model_details['model_config']

    llm = PyCraftEngine.get_instance(
        model_details["model_path"]
    )
    # Use stream=True to get a generator
    stream = llm(
        prompt,
        max_tokens=model_config['max_tokens'],
        stream=True, # THIS IS KEY FOR STEAMING 
        temperature=model_config['temperature'],
        top_p = model_config['top_p']
    )
    
    for chunk in stream:
        token = chunk['choices'][0]['text']
        yield token  # Yield each piece of text as it arrives

 