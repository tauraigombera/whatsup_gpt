from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
from gpt_response import response
from error_handlers import register_error_handlers

app = Flask(__name__)

# Register global error handlers
register_error_handlers(app)

@app.route("/", methods=["POST"])
# chatbot logic
def whats_up_bot():
    # creating object of MessagingResponse
    responses = MessagingResponse()
    msg = responses.message()
    msg.body(response())
    return str(responses)


if __name__ == "__main__":
    app.run()
