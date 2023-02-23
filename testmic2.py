import speech_recognition as sr

mic = sr.Microphone()

recog = sr.Recognizer()
sr.Microphone.list_microphone_names()

with mic as audio_file:
    print("Speak Please")

    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)

    print("Converting Speech to Text...")
    print("You said: " + recog.recognize_google(audio))