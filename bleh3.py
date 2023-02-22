from  googletrans import Translator

translator = Translator()

word1 = translator.translate('how can i get to the nearest hotel?', src='en', dest='ja')

# word2 = translator.translate(word1, src='en', dest='ja')

# print(word1.text)
print(word1.pronunciation)


