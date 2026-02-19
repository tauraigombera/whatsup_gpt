import pytest
from unittest.mock import MagicMock, patch
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# Test normal message flow
def test_whats_up_bot_returns_response(client):
    with patch("main.response", return_value="Hello from AI"):
        result = client.post("/", data={"Body": "Hello"})
        assert result.status_code == 200
        assert b"Hello from AI" in result.data

# Test empty message handling
def test_empty_message(client):
    with patch("main.response", return_value="Sorry, I didn't receive any message."):
        result = client.post("/", data={"Body": ""})
        assert result.status_code == 200

# Test OpenAI rate limit error handler
def test_rate_limit_error_handler(client):
    from openai import RateLimitError
    with patch("main.response", side_effect=RateLimitError("rate limit", response=MagicMock(), body={})):
        result = client.post("/", data={"Body": "Hello"})
        assert result.status_code == 200
        assert b"high demand" in result.data

# Test general error handler
def test_general_error_handler(client):
    with patch("main.response", side_effect=Exception("unexpected")):
        result = client.post("/", data={"Body": "Hello"})
        assert result.status_code == 200
        assert b"Something went wrong" in result.data