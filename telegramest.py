from telethon import TelegramClient

api_id = 154619
api_hash = '08bb150b2b470c7fb7311c015587cc1e'
phone = '+919811868656'

client = TelegramClient('session_name', api_id, api_hash)
client.connect()

#client.send_code_request(phone)
##myself = client.sign_in(phone, input('Enter code: '))
#print(myself.stringify())
print(client.is_user_authorized() )
from telethon.tl.functions.contacts import ResolveUsernameRequest

##client.send_message('nanothemotorgadi', 'Hello! Talking to you from Telethon')

total, messages, senders = client.get_message_history('nanothemotorgadi')
for message in messages:
    try:
        print(message)
    except:
        continue
