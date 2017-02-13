import fbchat
import time
username = str(input("Username: "))
password = str(input("Password: "))
client = fbchat.Client(username, password)

name = str(input("Name"))
friends = client.getUsers(name)
friend = friends[0]

msg = str(input("Enter message"))
count = 0
while count<30:
    sent = client.send(friend.uid, msg)

    count += 1
    print(count)






















sent = client.send(friend.uid, str(count) + " total messages sent.")
