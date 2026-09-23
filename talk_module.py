"""i had a fight with python pip pakage (important)
first of all in 'speech_recognition' there was no function named
'recognize_google()' so i needed to download speech to text module
at first my idea was to install "google-cloud-speech" but it didn't installed
what about "openai-wisper" you mght ask?... didn't installed either
nothing...but i find a way and that was using 'vosk'
and yeah that why i used extra module"""

import wave
from os import name, system, path
from pyttsx3 import init as ttsx
from colorama import Fore, init
from time import sleep
from vosk import Model, KaldiRecognizer, SetLogLevel
from speech_recognition import Recognizer, Microphone
from json import load, loads, dump


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


class JsonStart:
    def __init__(self):
        with open("data.json", "r") as file:
            self.data = load(file)


class Hear(JsonStart):
    def __init__(self):
        print("loading 2/1...")
        super().__init__()
        SetLogLevel(-1)
        self.the_model = self.data["model"]
        self.model = Model(path.abspath(self.the_model))

    def start(
        self,
    ):
        r = Recognizer()
        print(Fore.LIGHTRED_EX + "recording...")
        with Microphone() as source:
            audio = r.listen(source)
        with open("audio_user.wav", "wb") as wav_get:
            wav_get.write(audio.get_wav_data())
        # text to speech

        wf = wave.open(path.abspath("audio_user.wav"), "rb")
        rec = KaldiRecognizer(self.model, wf.getframerate())
        result_text = []
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = loads(rec.Result())
                result_text.append(result.get("text", ""))
        final_result = loads(rec.FinalResult())
        result_text.append(final_result.get("text", ""))
        full_transcript = " ".join(result_text).strip()
        print(Fore.GREEN + full_transcript + Fore.RESET)
        sleep(0.75)
        return full_transcript


class Speak:
    def __init__(self):
        print("loading 2/2...")
        init()
        self.voice = ttsx()

    def start(self, speech, text=None):
        if text == None:
            text = speech
        print(text)
        self.voice.say(speech)
        self.voice.runAndWait()
        print(Fore.RESET, end="")
        sleep(0.2)
