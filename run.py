

# from flask import Flask
# import os

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     PORT = int(os.environ.get("PORT", 5000))
#     # DEBUG = "NO_DEBUG" not in os.environ

#     app.run(host="0.0.0.0", port=PORT, debug=True)


from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = MessagingResponse().message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)