import os

from decouple import config
from langchain_community.llms import Replicate

# load in environment variables
REPLICATE_API_TOKEN = config("REPLICATE_API_TOKEN")
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

llm: Replicate = Replicate(
    model="meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
    input={
        "temperature": 0.80,
        "max_length": 500, 
        "top_p": 1
    }
)

prompt: str = """
Human: Answer the following question and show your reasoning to the final answer: who is the king of Morocco ??
AI
"""

response: str = llm(prompt=prompt)

print(response)