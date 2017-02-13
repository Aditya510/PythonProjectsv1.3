import fbchat
user = fbchat.Client("aditya5@outlook.com","yeeksentenceh")

from chatterbot import ChatBot

charbot = ChatBot('Ron Obvious',trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

charbot.train("chatterbot.corpus.english")

print(charbot.get_response("Hello, how are you today?"))










friends = user.getUsers("nandana")
friend = friends[0]
import time
while True:
    last_messages = user.getThreadInfo(friend.uid,0)
    a= last_messages[0].body
    time.sleep(1)
    last_messages = user.getThreadInfo(friend.uid,0)
    b = last_messages[0].body
    if a != b:
        user.send(friend.uid, charbot.get_response(b))









































