from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAIError, RateLimitError

def register_error_handlers(app):
    """Register global error handlers for Twilio WhatsApp responses."""

    def twilio_reply(message):
        """Helper to return a Twilio-friendly response."""
        resp = MessagingResponse()
        resp.message(message)
        return str(resp)

    @app.errorhandler(RateLimitError)
    def handle_rate_limit_error(e):
        return twilio_reply("Sorry, I am currently experiencing high demand or out of quota. "
                            "Please try again later."), 200

    @app.errorhandler(OpenAIError)
    def handle_openai_error(e):
        return twilio_reply(f"AI API error occurred. Please try again later."), 200

    @app.errorhandler(Exception)
    def handle_general_error(e):
        # Fallback for all other errors
        return twilio_reply("Oops! Something went wrong. Please try again."), 200
