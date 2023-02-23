import speech_recognition as sr
from googletrans import Translator
import uuid
from gtts import gTTS
from io import BytesIO
from playsound import playsound

# obtain audio from microphone:

recog = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()

with mic as source:
    print("what would you like to translate?'")

    recog.adjust_for_ambient_noise(source)
    audio = recog.listen(source)

    print("Converting Speech to Text...")
    try:
        print("You said: " + recog.recognize_google(audio))
    except sr.UnknownValueError:
        print('could not understand the audio')
    except sr.RequestError as e:
        print('google error; {0}'.format(e))

    sentence = recog.recognize_google(audio)

# with sr.Microphone() as source:
#     print('what would you like to translate?')
#     audio = recognize.listen(source)

# # recognize speech with spynx -meow-
# try: 
#     print('audio recognized as: ' + recognize.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

# sentence = recognize.recognize_sphinx(audio)


# translate the audio/text into desired language:
# parameters available in googletrans documentation

translator = Translator()
change_language = translator.translate(sentence, src='en', dest='ja')

# print(change_language.pronunciation, change_language.text)

save_new_sentence = change_language.pronunciation

# define audio file:

mp3_fp = BytesIO()
save_file = gTTS(save_new_sentence, lang='ja')
randomize_filename = str(uuid.uuid4()) + '.mp3'

# create the audiofile with translated sentence:
with open(randomize_filename, 'wb') as f:
    save_file.write_to_fp(f)

# play the audio file: 

playsound(randomize_filename)
# dfkjth