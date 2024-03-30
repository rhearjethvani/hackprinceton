from gptzero import GPTZeroAPI
from dotenv import load_dotenv
import os

load_dotenv()

def find_ai_human(document):
    api_key = os.getenv("ZERO_AI")
    gptzero_api = GPTZeroAPI(api_key)
    response = gptzero_api.text_predict(document)
    clx = response.get("documents")[0].get("predicted_class")
    return clx
