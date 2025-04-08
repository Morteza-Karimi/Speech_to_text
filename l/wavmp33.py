from pydub import AudioSegment
import os







def convert(input_file_name:str,output_file:str):
    if os.path.exists(input_file_name):
        try:
            audio=AudioSegment.from_mp3(input_file_name)
            audio.export(output_file,format='wav')
            print("succesfully happend")
        except Exception as e:
            print(f'an error {e}')
    else:
        print("file does not exist!!!!!")

if __name__=="__main__":
    input_file=input("file name.mp3")
    output_file=input("file name.wav")

    convert(input_file,output_file)



  
