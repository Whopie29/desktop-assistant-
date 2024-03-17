import requests
import json
import os
from PIL import Image
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

Api_Key = "ExWSfhxssd0OCCOFBEXpJp2AoyRefB2BiEPou7Ir"
def NasaNews(Date):

    speak("Extracting data from Nasa .")

    Url="https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

    Params ={'date':str(Date)}

    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']
    
    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)

    Path_1 = ""

    Path_2= ""

    os.rename(Path_1,Path_2)

    img = Image.open(Path_2)
    img.show

    speak(f"Title : {Title}")
    speak(f"According to Nasa :{Info}")


  