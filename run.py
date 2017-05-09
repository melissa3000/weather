


from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os
import urllib2
import json

wunderground_key = os.environ.get("wunderground_key")



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    f = urllib2.urlopen('http://api.wunderground.com/api/' + wunderground_key + '/geolookup/conditions/q/CA/San_Francisco.json')
    json_string = f.read()

    # turn the string into an object
    parsed_json = json.loads(json_string)

    print json_string

    location = parsed_json['location']['city']

    temp_f = parsed_json['current_observation']['temp_f']
    precip = parsed_json['current_observation']['precip_today_in']

    msg = "Current temperature in %s is: %s. Rain in inches: %s" % (location, temp_f, precip)

    f.close()

    resp = MessagingResponse().message(msg)
    return str(resp)

@app.route("/error")
def error():
    raise Exception("Error!")


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)