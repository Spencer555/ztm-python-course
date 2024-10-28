# from twilio.rest import Client

# # we use the twilio service and read the documentation
# account_sid = 'account_sid'
# auth_token = 'auth_token'
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#     messaging_service_sid='MG80b6127afeaaf37cf979be9e70636c55',
#     body='this is spencer testing out',
#     to='+phonenumber'
# )
# print(message.sid)


import requests

print(requests.post("https://ntfy.sh/mytopic", data="Backup successful 😀".encode(encoding='utf-8')))
