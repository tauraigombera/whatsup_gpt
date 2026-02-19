# whatsup_gpt

whatsup_gpt is a WhatsApp chatbot powered by OpenAI’s ChatGPT model.
It listens to incoming WhatsApp messages and generates intelligent, human-like responses in real time.

Built with Python (3.11+) and Flask, this project is lightweight, extensible, and easy to deploy.

### Tools and Technologies
- Python 3.11+
- Flask Web Server
- [OpenAI API](https://developers.openai.com/api/docs)
- WhatsApp Business API via [twilio](https://www.twilio.com/docs/whatsapp)

### Message Flow

- A user sends a WhatsApp message.
- Twilio forwards the message to your Flask endpoint.
- The app sends the message to OpenAI.
- ChatGPT generates a response.
- The response is returned to the user via Twilio.

### Before running the project, ensure you have:

- Python 3.11 or higher
- A Twilio account
- A Twilio WhatsApp Sandbox with an approved WhatsApp number
- OpenAI API key
- Publicly accessible endpoint URL (ngrok for local development)

## Local Setup
1. Clone the repository:
```
git clone https://github.com/tauraigombera/whatsup_gpt.git
```
2. Navigate into the project folder
```
cd whatsup_gpt
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Create .env file and add your OpenAI API key to the environment variables as follows:
```
OPENAI_API_KEY=[your_api_key]
```

5. Run the application:
```
python main.py
```

The app should now be running on http://localhost:5000. 

### Use ngrok to expose it to the internet:
1. Install ngrok if you haven't already: [download and install ngrok](https://ngrok.com/download).
2. get the auth token from ngrok and set it up:
```
ngrok config add-authtoken [your_auth_token]
``` 
3. start ngrok on the same port as your Flask app (default is 5000):
```
ngrok http 5000
```
ngrok will provide you with a forwarding URL 
`(e.g.,  https://9ef7-123.ngrok-free.app ).` 
This URL will be used as the endpoint URL for Twilio.

### Twilio WhatsApp Setup

- Create a Twilio account.
- Activate WhatsApp Sandbox. 
- Join the sandbox using the provided join code. 
- In sandbox settings, set your endpoint URL to the ngrok URL you obtained in the previous step.
- Start sending messages to test the bot.

