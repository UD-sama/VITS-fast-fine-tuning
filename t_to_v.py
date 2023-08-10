from gtts import gTTS
import pygame
import os


def text_to_speech( text, lang='en',filename ='example'):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue



if __name__ == "__main__":
    text = "這是一個示範文字轉語音的範例。"
    text_to_speech(text, lang='zh-TW')
