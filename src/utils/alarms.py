""" Contains the alarm object for athena """
import datetime
import multiprocessing
import time

# Temp
import inputimeout
from playsound import playsound

AUDIO_DIR = "extras/Audio"

ringtone_directories = {
     "Ishmael": 'Ishmael Alarm.m4a',
     "Ibz": 'IbzAlarm.m4a',
     "Deafening": 'FireAlarm.mp3'
                        }


class Alarm:
    """
    id: Document ID on firestore
    name: name of the alarm
    time: time the alarm goes off
    audio: audio to play
    deleted:Bool


    # 
    """
    def __init__(self, db_id: str, name: str, time_to_ring: datetime.datetime, audio):
        self.db_id = db_id
        self.name = name
        self.time_to_ring = time_to_ring
        self.audio_code = audio # Code to indicate which Alarm Ringtone the Alarm is set to
        self.audio = AUDIO_DIR + ringtone_directories[audio]  # Gets the Actual file directory of the Audio
        self.deleted = False
        
        self.alarm_check()  # Automatically starts the countdown for the alarm one initialisation 

    def play_audio(self):
        """Plays the correct audio file"""
        while True:   ## Loops the Audio file
            playsound(self.audio, block=True)


    
    def alarm_check(self):  # sourcery skip: use-contextlib-suppress
        """
        Starts the Countdown for when the alarm should ring
        """
        difference_int = (self.time_to_ring - datetime.datetime.now()).total_seconds() # Figures out how long is left till the alarm should actually go off
            
        #time.sleep(difference_int)


        try:
            inputimeout.inputimeout(prompt='Press anything to delete', timeout=difference_int)
            self.deleted = True
        except inputimeout.TimeoutOccurred:
            pass

        while not self.deleted:
            self.audio_process = multiprocessing.Process(target=self.play_audio)
            self.audio_process.start()


            ask_in = input("s for snooze, d for stop:\n")
            if ask_in == "s":
                self.snooze_current()
            elif ask_in == "d":
                self.stop_current()

    def snooze_current(self):
        """Snoozes an alarm that is going off"""
        self.audio_process.terminate()
        time.sleep(300)

    def stop_current(self):
        """ Stops the current alarm """
        self.audio_process.terminate()
        self.deleted = True


