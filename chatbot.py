
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from gtts import gTTS
from pygame import mixer
import speech_recognition as sr
import os

r = sr.Recognizer()
mixer.init()

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)



while True:
    message = input('You: ')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)

        tts = gTTS('' +str(reply), lang = 'en')
        tts.save('kasule.mp3')
        mixer.music.load('kasule.mp3')
        mixer.music.play()

        print('ChatBot :', reply)
    if message.strip() == 'Bye':
        print('ChatBot : Bye')
        break
