import os
from os.path import dirname, join
from twilio.rest import Client
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

phone_number = os.getenv('PHONE_NUMBER')
message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=phone_number,
                     to='+2348140506231'
                 )

print(message.sid)

