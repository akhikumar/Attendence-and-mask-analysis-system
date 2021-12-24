# Download the helper library from https://www.twilio.com/docs/python/install
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('sid')
auth_token = os.getenv('tok')
print(account_sid,auth_token)
client = Client(account_sid, auth_token)

def sendMessage(name,number,data):
     message = client.messages \
                .create(
                     body=f'''Hello {name}, you student was present is class
                         for {data['days']} and is presence is {data['presence']}%''',
                     from_='+13867038947',
                     to='+91' + str(number)
                 )


# print(message.sid)