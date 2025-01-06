from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda,RunnableSequence


load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")


model = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

prompt_template=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant in thw field {field}"),
        ("human", "Tell me about {topic}"),
    ]
)


format_prompt=RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model=RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output=RunnableLambda(lambda x: x.content)

chain=RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

resnse=chain.invoke({"field":"AI", "topic":"Artificial Intelligence"})

print(resnse)