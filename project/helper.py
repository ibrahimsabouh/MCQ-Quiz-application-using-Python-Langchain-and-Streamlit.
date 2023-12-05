from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_Quiz(category, questions):
    llm = OpenAI(temperature=0.7)

    prompt = PromptTemplate(
        input_variables = ['category', 'questions'],

        template = "make a {questions} multiple-choice questions and each question should have \
            4 choices 3 are wrong and one is right and the questions should be in {category} topic."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt, output_key="question_format")

    response = name_chain({'category': category, 'questions':questions})
    return response

if __name__ == "__main__":
    generate_Quiz("sports", 3)