from fastapi import FastAPI, HTTPException
from typing import Dict, List
import requests
import json

app = FastAPI()


@app.post("/predict/")
def predict(data: Dict[str, str]):
    hf_pipeline = data.get("hf_pipeline")
    model_deployed_url = data.get("model_deployed_url")
    inputs = data.get("inputs")
    parameters = data.get("parameters", {})

    if not hf_pipeline or not model_deployed_url or not inputs:
        raise HTTPException(status_code=400, detail="Missing required fields")

    # Prepare the input in V2 inference protocol format
    v2_input = {
        "array_inputs": [inputs],
        "candidate_labels": parameters.get("candidate_labels", []),
        # Add any other keyword arguments accepted by zero-shot-classification
    }
    v2_payload = {
        "task": hf_pipeline,
        "model": model_deployed_url,
        "inputs": v2_input,
        "parameters": {}
    }

    try:
        # Send the request to the model deployment endpoint
        response = requests.post(model_deployed_url, json=v2_payload)
        response.raise_for_status()
        result = response.json()
        return result
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
