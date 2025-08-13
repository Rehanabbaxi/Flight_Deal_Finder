# class NotificationManager:
#     #This class is responsible for sending notifications with the deal flight details.
#     pass
from pandas.core.nanops import bottleneck_switch
from twilio.rest import Client
import os
from dotenv import  load_dotenv
load_dotenv()

twilio_sid = os.getenv("TWILIO_SID")
twilio_auth_tok = os.getenv("TWILIO_AUTH_TOK")


client = Client(twilio_sid , twilio_auth_tok)
message = client.messages.create(
    body="testing",
    from_=+14708767821,
    to=+923155504532
)

print(message.status)