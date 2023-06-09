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
        "inputs": [
            {
                "name": "array_inputs",
                "shape": [-1],
                "datatype": "BYTES",
                "parameters": {
                    "content_type": "str"
                },
                "data": [inputs]
            },
            {
                "name": "candidate_labels",
                "shape": [-1],
                "datatype": "BYTES",
                "parameters": {
                    "content_type": "str"
                },
                "data": parameters.get("candidate_labels", [])
            }
        ]
    }

    v2_payload = {
        "inputs": v2_input,
        "outputs": []
    }

    try:
        # Send the request to the model deployment endpoint
        response = requests.post(model_deployed_url, json=v2_payload)
        response.raise_for_status()
        result = response.json()
        return result
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
