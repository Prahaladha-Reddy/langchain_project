from tinydb import TinyDB, Query
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")


model = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")


db = TinyDB("chat_history.json")


def load_chat_history():
    return [SystemMessage(content=item['content']) if item['role'] == "system" else
            HumanMessage(content=item['content']) if item['role'] == "human" else
            AIMessage(content=item['content'])
            for item in db.all()]


def save_message(role, content):
    db.insert({"role": role, "content": content})


chat_history = load_chat_history()

if not chat_history:
    # Add a default system message if history is empty
    system_message = SystemMessage(content="You are a helpful assistant.")
    chat_history.append(system_message)
    save_message("system", system_message.content)

# Start chatbot interaction
print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break

    # Add user input to chat history and save it
    chat_history.append(HumanMessage(content=prompt))
    save_message("human", prompt)

    # Get AI response
    result = model.invoke(chat_history)
    print(f"AI: {result.content}")

    # Add AI response to chat history and save it
    chat_history.append(AIMessage(content=result.content))
    save_message("ai", result.content)
