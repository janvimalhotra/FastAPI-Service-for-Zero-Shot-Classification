import argparse
import logging
import requests
from servicefoundry import Build, PythonBuild, Service, Resources, Port, LocalSource
logging.basicConfig(level=logging.INFO)
parser = argparse.ArgumentParser()
parser.add_argument("--workspace_fqn", required=True, type=str)
args = parser.parse_args()
service = Service(
    name="fastapi",
    image=Build(
        build_spec=PythonBuild(
            command="uvicorn app:app --port 8000 --host 0.0.0.0",
            requirements_path="requirements.txt",
        ),
        build_source=LocalSource(local_build=False)
    ),
    ports=[
        Port(
            port=8000,
            host="zero-shot-intern-janvi.demo1.truefoundry.com"
        )
    ],
    resources=Resources(
        cpu_request=0.05,
        cpu_limit=0.05,
        memory_request=500,
        memory_limit=500,
        ephemeral_storage_request=50,
        ephemeral_storage_limit=50
    ),
    env={
        "UVICORN_WEB_CONCURRENCY": "1",
        "ENVIRONMENT": "dev"
    }
)
service.deploy(workspace_fqn=args.workspace_fqn)

# import os
# import joblib
# import pandas as pd
# from fastapi import FastAPI

# model = joblib.load("iris_classifier.joblib")

# app = FastAPI(root_path=os.getenv("TFY_SERVICE_ROOT_PATH"))

# @app.post("/predict")
# def predict(
#     sepal_length: float, sepal_width: float, petal_length: float, petal_width: float
# ):
#     data = dict(
#         sepal_length=sepal_length,
#         sepal_width=sepal_width,
#         petal_length=petal_length,
#         petal_width=petal_width,
#     )
#     prediction = int(model.predict(pd.DataFrame([data]))[0])
#     return {"prediction": prediction}