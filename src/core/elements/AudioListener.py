""" Contains class for AudioListener """
import multiprocessing as mp

import speech_recognition as sr


class AudioListener:
    """Class for speech recognition
    Modes:
    Always on = 1
    Athena on-call = 2
    Muted = 3
    """

    def __init__(self, mode: int):
        self.mode = mode

    def main_loop(self):
        """The main loop for listening for speech"""
        while self.mode != 3:
            print(self.mode)
            if self.mode == 3:
                return

            recogniser = sr.Recognizer()
            with sr.Microphone() as src:
                try:
                    audio = recogniser.listen(src, 1)
                    speech = recogniser.recognize_google(audio)
                    self.speech_checker(speech)

                except sr.WaitTimeoutError as err:
                    print(err)
                except sr.UnknownValueError as err:
                    print(err)

    def speech_checker(self, speech: str):
        """checks the speech to see which part was the request and sends it to the processor"""
        if self.mode == 1:
            pass
            # TODO: process what it should say
        elif "athena" in speech.lower() and self.mode == 2:
            speech_split = speech.lower().split("athena")
            request = speech_split[1]
            # TODO: PROCESS request
            print(request)
            if "mute yourself" in request:
                print("muted")
                self.mode = 3


if __name__ == "__main__":
    AudioListener(2).main_loop()
