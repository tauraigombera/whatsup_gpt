from flask import request
import openai
from dotenv import load_dotenv
import os

# load dotenv library
load_dotenv()

# access openai API key
openai.api_key = os.environ.get("OPENAI_API_KEY")


# generate response
def response():

    user_msg = request.values.get('Body', '').lower()

    # Generate a response using the OpenAI API
    gpt_response = openai.Completion.create(
        model="text-davinci-003",
        prompt="" + user_msg,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the response from the API
    gpt_response = gpt_response["choices"][0]["text"].strip()
    return gpt_response
