from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")


model = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

template="Write an email in a {tone} email to {company} expressing interest in the {position}, mentioning {skills} as a key strength , keep it 5 lines max"

prompt_template = ChatPromptTemplate.from_template(template)

result = model.invoke(prompt_template.format(tone="excited", company="Google", position="Software Engineer", skills="Python, Machine Learning"))

print(result.content)