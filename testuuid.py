import uuid
from gtts import gTTS
from io import BytesIO
from playsound import playsound

filename = str(uuid.uuid4()) + '.mp3'

print(filename)

# define audio file:

mp3_fp = BytesIO()
save_file = gTTS('whats gucccciii', lang='ja')

# create the audiofile with translated sentence:
with open(filename, 'wb') as f:
    save_file.write_to_fp(f)

# play the audio file: 

playsound(filename)