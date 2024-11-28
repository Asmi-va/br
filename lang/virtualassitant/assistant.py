import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI


# Initialize OpenAI
openai.api_key = "your_openai_api_key"

# Question Answering
def answer_question(question):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Answer the question:\n{question}",
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Document Summarization
def summarize_document(document):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Summarize the following text:\n{document}",
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# API Interaction Example (for external APIs)
def get_weather(city):
    # Simulate fetching weather data
    return f"The current weather in {city} is sunny with a temperature of 25°C."
