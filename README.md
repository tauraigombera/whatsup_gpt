- ![GitHub stars](https://img.shields.io/github/stars/tauraigombera/whatsup_gpt?style=social)
- ![Python](https://img.shields.io/badge/python-3.11-blue)
- ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## whatsup_gpt

Production-ready WhatsApp AI chatbot built with Flask, Twilio and OpenAI model.
This project is lightweight, extensible, and easy to deploy.

---

### Tools and Technologies
- Python 3.11+
- Flask Web Server
- [OpenAI API](https://developers.openai.com/api/docs)
- WhatsApp Business API via [twilio](https://www.twilio.com/docs/whatsapp)

---

### Message Flow

- A user sends a WhatsApp message.
- Twilio forwards the message to your Flask endpoint.
- The app sends the message to OpenAI.
- ChatGPT generates a response.
- The response is returned to the user via Twilio.

### Before running the project, ensure you have:

- A Twilio account
- A Twilio WhatsApp Sandbox with an approved WhatsApp number
- OpenAI API key
- ngrok for exposing your local server to the internet (for development/testing)

---

## Running with Docker (Recommended)

This is the easiest way to run the app locally without installing Python or any dependencies manually.

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [ngrok](https://ngrok.com/download)

### Steps

1. Clone the repository:
```
git clone https://github.com/tauraigombera/whatsup_gpt.git
```

2. Navigate into the project folder:
```
cd whatsup_gpt
```

3. Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=[your_api_key]
```

4. Build and start the app:
```
docker compose up --build -d
```

The app will be running on http://localhost:5000.

5. Expose it to the internet with ngrok:
```
ngrok http 5000
```

---

## Local Setup (Manual)

Use this approach if you prefer not to use Docker.

### Prerequisites
- Python 3.11 or higher
- [ngrok](https://ngrok.com/download)

### Steps

1. Clone the repository:
```
git clone https://github.com/tauraigombera/whatsup_gpt.git
```

2. Navigate into the project folder:
```
cd whatsup_gpt
```

3. Create and activate a virtual environment:
```
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
source .venv/bin/activate     # Mac/Linux
```

4. Install the required packages:
```
pip install -r requirements.txt
```

5. Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=[your_api_key]
```

6. Run the application:
```
python main.py
```

The app should now be running on http://localhost:5000.

---

### Use ngrok to expose it to the internet:

1. Install ngrok if you haven't already: [download and install ngrok](https://ngrok.com/download).
2. Get the auth token from ngrok and set it up:
```
ngrok config add-authtoken [your_auth_token]
```
3. Start ngrok on the same port as your Flask app (default is 5000):
```
ngrok http 5000
```
ngrok will provide you with a forwarding URL
`(e.g., https://9ef7-123.ngrok-free.app).`
This URL will be used as the endpoint URL for Twilio.

---

### Twilio WhatsApp Setup

- Create a Twilio account.
- Activate WhatsApp Sandbox.
- Join the sandbox using the provided join code.
- In sandbox settings, set your endpoint URL to the ngrok URL you obtained in the previous step.
- Start sending messages to test the bot.


