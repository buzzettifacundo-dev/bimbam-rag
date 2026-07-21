import os
from dotenv import load_dotenv
import cohere

load_dotenv()

co = cohere.ClientV2(
    api_key=os.getenv("COHERE_API_KEY")
)

modelos = co.models.list()

print(modelos)
