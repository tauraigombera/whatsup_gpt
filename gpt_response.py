from flask import request
from openai import OpenAI
from dotenv import load_dotenv
import os

# load dotenv library
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Generate response
def response():
    # Get the WhatsApp message sent by the user
    user_msg = request.values.get('Body', '').strip()

    if not user_msg:
        return "Sorry, I didn't receive any message."

    # Generate a response using the Chat API
    chat_response = client.chat.completions.create(
        model="gpt-4o-mini",  # fast, small, good for chatbots
        messages=[
            {"role": "system", "content": "You are a helpful WhatsApp assistant."},
            {"role": "user", "content": user_msg}
        ],
        temperature=0.7,
        max_tokens=256
    )

    # Extract the assistant's reply
    gpt_reply = chat_response.choices[0].message.content.strip()
    return gpt_reply