from gtts import gTTS
import pygame
import os
from docx import Document
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import sql, insert, update, delete

def speak(text):
    
    tts = gTTS(text=text, lang='vi')

    tts.save('voice.mp3')

    pygame.init()

    pygame.mixer.music.load("voice.mp3")

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue

    os.remove('voice.mp3')

document = Document('doctiengfviet.docx')
text = ''
for paragraph in document.paragraphs:
    text += paragraph.text + ' '
    
speak(text)
