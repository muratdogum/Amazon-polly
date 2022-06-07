import boto3
import random
from tkinter import *
from pygame import mixer
        
def sorgu():
    
    inp = text.get(1.0, "end-1c")
    polly_client = boto3.Session(
                   aws_access_key_id='access_key', 
                   aws_secret_access_key='secret_access_key',
                   region_name='us-east-1').client('polly')

    response = polly_client.synthesize_speech(
                   VoiceId='Joanna',
                   OutputFormat='mp3',
                   Engine = 'neural', 
                   TextType = "ssml", 
                   Text = "<speak><prosody rate='90%'>"+inp+"</prosody></speak>") 
    new=str(random.randint(45, 500))+".mp3"
    with open('folder/'+new, 'wb') as file: 
       file.write(response['AudioStream'].read())
    mixer.init()
    mixer.music.load('folder/'+new) 
    mixer.music.play()
window = Tk()
window.title("POLLY TEXT TO SPEECH")
window.geometry("1000x500")
window['background']='#856ff8'
frame = Frame(window)
frame['background']='#856ff8'
metin=Label(frame, text= "SESLENDİRİLECEK METNİ GİRİNİZ")
metin.pack(padx=20, pady=20)
text=Text(frame,
                   height = 20,
                   width = 80)
text.pack(pady=10)
cal=Button(frame, text="SESLENDİR",width=18,height=3,bg="yellow",command=sorgu)
cal.pack(pady=10)

metin['background']='#856ff8'

frame.pack()
window.mainloop()
