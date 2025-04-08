import speech_recognition as sr
import os 
from mp3towav.wavmp33 import convert
os.system('cls')
input_file=input("file name.mp3 or adress:\n")
output_file=input("file name.wav:\n")

convert(input_file_name=input_file,output_file=output_file)

recognizer = sr.Recognizer()


audio_file = sr.AudioFile(output_file)

with audio_file as source:
    
    audio_data = recognizer.record(source)

try:
    
    text = recognizer.recognize_google(audio_data)
    print("your text is:\n", text,sep="")
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
