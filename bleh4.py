from gtts import gTTS
from io import BytesIO
from playsound import playsound


# create audio file 
mp3_fp = BytesIO()
# tts_en = gTTS('hello', lang='en')
tts_fr = gTTS('Konnichiwa watashinonamaeha Itaria-godesu', lang='ja')

with open('test_japanese.mp3', 'wb') as f:
    # tts_en.write_to_fp(f)
    tts_fr.write_to_fp(f)

# play audio file

playsound('/Users/lemonysnicket/Desktop/speech/test_japanese.mp3')