import mp3play as m
from gtts import gTTS
import os
st = ""
for k in open("read_input.txt","r"):
    st += k
   # print(k)
tts = gTTS(text=st,lang='en')
tts.save("file_read.mp3")

