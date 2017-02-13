from chatterbot import ChatBot

charbot = ChatBot('Ron Obvious',trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

charbot.train("chatterbot.corpus.english")

print(charbot.get_response("Hello, how are you today?"))
