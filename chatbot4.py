from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
bot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot using the English corpus
trainer.train("chatterbot.corpus.english")
def get_bot_response(user_input):
    # Convert the user's input into a Statement object
    user_statement = Statement(user_input)

    # Get the bot's response to the user's input
    bot_response = bot.get_response(user_statement)

    return str(bot_response)
while True:
    user_input = input("User: ")

    if user_input.lower() == 'exit':
        break

    bot_response = get_bot_response(user_input)
    print("Bot:", bot_response)
