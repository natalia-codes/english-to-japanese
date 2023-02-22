import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from io import BytesIO
from playsound import playsound

# obtain audio from microphone:

recognize = sr.Recognizer()

with sr.Microphone() as source:
    print('what would you like to translate?')
    audio = recognize.listen(source)

# recognize speech with spynx -meow-
try: 
    print('audio recognized as: ' + recognize.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

sentence = recognize.recognize_sphinx(audio)
# print(sentence)

# translate the audio/text into desired language:
# parameters available in googletrans documentation

translator = Translator()
change_language = translator.translate(sentence, src='en', dest='ja')

# print(change_language.pronunciation, change_language.text)

save_new_sentence = change_language.pronunciation

# define audio file:

mp3_fp = BytesIO()
save_file = gTTS(save_new_sentence, lang='ja')

# create the audiofile with translated sentence:
with open('test_program.mp3', 'wb') as f:
    save_file.write_to_fp(f)

# play the audio file: 

playsound('test_program.mp3')