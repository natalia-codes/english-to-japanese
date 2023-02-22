import speech_recognition as sr
from googletrans import Translator

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    # print(r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

sentence = r.recognize_sphinx(audio)
# print(sentence)

translator = Translator()

word1 = translator.translate(sentence, src='en', dest='ja')

# word2 = translator.translate(word1, src='en', dest='ja')

# print(word1.text)
print(word1.pronunciation)


