from config import *

class Speech:
    
    def __init__(self):
        pass

    def voicePlay(string):
        myobj = gTTS(text=string, lang='en', slow=False)
        myobj.save("tts.mp3")
        playsound('tts.mp3')


