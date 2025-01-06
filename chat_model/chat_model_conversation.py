import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")


model=ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

chat_history=[]

system_message=SystemMessage(content="You are a helpful assistant.")
chat_history.append(system_message)

while True:
    prompt=input("You:")
    if prompt.lower()=="exit":
        break

    chat_history.append(HumanMessage(content=prompt))
    result=model.invoke(chat_history)
    print(result.content)
    chat_history.append(AIMessage(content=result.content))