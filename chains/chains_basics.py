from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")


model = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")


prompt_template=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant in thw field {field}"),
        ("human", "Tell me about {topic}"),
    ]
)


chain= prompt_template | model | StrOutputParser()


resul= chain.invoke({"field":"AI", "topic":"Artificial Intelligence"})


print(resul)