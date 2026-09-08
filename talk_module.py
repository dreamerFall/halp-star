"""i had a fight with python pip pakage (important)
first of all in 'speech_recognition' there was no function named
'recognize_google()' so i needed to download speech to text module
at first my idea was to install "google-cloud-speech" but it didn't installed
what about "openai-wisper" you mght ask?... didn't installed either
nothing...but i find a way and that was using 'vosk'
and yeah that why i used extra module"""

import pyttsx3, wave, json, os, json
from colorama import Fore, init
from time import sleep
from vosk import Model, KaldiRecognizer, SetLogLevel
import speech_recognition as spreon

with open("data.json", "r") as file:
    data = json.load(file)
the_model = data["model"]  # vosk module
init()
if not __name__ == "__main__":

    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def speak(speech, text=None):
        if text == None:
            text = speech
        print(text)
        voice = pyttsx3.init()
        voice.say(speech)
        voice.runAndWait()
        print(Fore.RESET, end="")
        sleep(0.2)

    def hear():
        # get speech
        r = spreon.Recognizer()
        print(Fore.LIGHTRED_EX + "recording...")
        with spreon.Microphone() as source:
            audio = r.listen(source)
        with open("audio_user.wav", "wb") as wav_get:
            wav_get.write(audio.get_wav_data())
        # text to speech
        SetLogLevel(-1)
        model = Model(os.path.abspath(the_model))
        wf = wave.open(os.path.abspath("audio_user.wav"), "rb")
        rec = KaldiRecognizer(model, wf.getframerate())
        result_text = []
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                result_text.append(result.get("text", ""))
        final_result = json.loads(rec.FinalResult())
        result_text.append(final_result.get("text", ""))
        full_transcript = " ".join(result_text).strip()
        clear()
        print(Fore.GREEN + full_transcript + Fore.RESET)
        sleep(0.75)
        return full_transcript
