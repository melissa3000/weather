# /usr/bin/env python

# When run, sends sms message to mobile with text specified below

from twilio.rest import Client
import os


account_sid = "AC9d7bdbe6dd7141216cbc087c6e837bf3"
auth_token = os.environ.get("auth_token")
client = Client(account_sid, auth_token)


message = client.api.account.messages.create(to="+17708554418",
                                             from_="+16786078732",
                                             body="Hello there!")

