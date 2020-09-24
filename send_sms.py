from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

# my_message = 'Python is an amazing language!! '

my_message = ''.join(['Lets try this\n' for i in range(5)])

message = client.messages.create(
         to=my_cell,
         from_=my_twilio,
         body=my_message)

print("The message has b   een sent to", my_cell)