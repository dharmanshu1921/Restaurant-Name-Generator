# !pip install openai
# !pip install langchain
# !pip install langchain-community
# !pip install langchain-chains
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.chains import SequentialChain

load_dotenv()

import os
openai_api_key=os.environ['OPENAI_API_KEY']

##sequential chain
llm=OpenAI(temperature=0.6)

def generate_restaurant_name_and_items(cuisine):
    prompt_template_name=PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restaurant for {cuisine} food, Suggest a fancy name for this"
    )

    name_chain=LLMChain(llm=llm,prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items=PromptTemplate(
    input_variables=['restaurant_name'],
    template="suggest some menu items for {restaurant_name}. Return it as a comma separated string")

    food_items_chain=LLMChain(llm=llm,prompt=prompt_template_items, output_key="menu_items")

    chain2=SequentialChain(
    chains=[name_chain,food_items_chain],
    input_variables=['cuisine'],
    output_variables=['restaurant_name','menu_items']
    )
    response = chain2({'cuisine':cuisine})
    
    return response


# if __name__ == "__main__":
#     response=generate_restaurant_name_and_items("Arabic")
#     print(response)