from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")


messages =[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is 1+1?"),
    AIMessage(content="2"),
    HumanMessage(content="What is the capital of France?"),
    AIMessage(content="Paris"),
    HumanMessage(content="What is the capital of Italy?"),
    AIMessage(content="Rome"),
    HumanMessage(content="What is the capital of Spain?"),
    AIMessage(content="Madrid"),
    HumanMessage(content="What is the capital of Germany?")
    
]

result=llm.invoke(messages)

print(result.content)