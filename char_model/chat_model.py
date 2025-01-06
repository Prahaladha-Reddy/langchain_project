from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
chat = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

result=chat.invoke("Hello, i am prahalad")

print(result.content)