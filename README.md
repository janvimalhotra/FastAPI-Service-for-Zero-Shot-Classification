# huggingFacetoV2
This is a FastAPI service that provides an endpoint for performing zero-shot classification using a Hugging Face model on truefoundry.

# Installation
Clone the repository to your local machine.<br>
Navigate to the project directory.<br>
##### Prerequisites
Python 3.7 or higher<br>

# Setup
Create a virtual environment (optional but recommended).<br>
Install the required dependencies by running pip install -r requirements.txt.

# Usage
Open Postman<br>
Endpoint<br>
POST /<service-endpoint>/predict/<br>
Request Body: JSON<br>
Example Request Body<br>
json<br>
### Code Snippet
{
  "hf_pipeline": "zero-shot-classification",<br>
  "model_deployed_url": "from-truefoundary-dashboard",<br>
  "inputs": "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!",<br>
  "parameters": {<br>
    "candidate_labels": ["refund", "legal", "faq"]<br>
  }<br>
}<br>
### Post request
Send a POST request to the /predict/ endpoint with the desired input.<br>
#### Response
The response will be a JSON object containing the prediction result.<br>

### Customization
###### You can customize the code to fit your specific requirements. Here are some points to consider:<br>

Modify the predict function to handle different types of Hugging Face models or pipelines.<br>
Update the endpoint URL and request body structure as needed.<br>
Add additional parameters or keyword arguments based on the requirements of your specific model.<br>
Feel free to explore and adapt the code according to your use case.<br>

That's it! You can now run the FastAPI service, send POST requests to the /predict/ endpoint, and get predictions for zero-shot classification using your Hugging Face model.<br>
