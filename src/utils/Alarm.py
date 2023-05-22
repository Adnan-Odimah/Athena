""" Contains the alarm object for athena """
import datetime
import multiprocessing
import time

# Temp
import inputimeout
from playsound import playsound

from src.utils import AUDIO_DIR, ringtone_directories


class Alarm:
    """
    id: Document ID on firestore
    name: name of the alarm
    time: time the alarm goes off
    audio: audio to play
    deleted:Bool


    #
    """

    def __init__(
        self, db_id: str, name: str, time_to_ring: datetime.datetime, audio_code: str
    ):
        self.db_id = db_id
        self.name = name
        self.time_to_ring = time_to_ring
        self.audio_code = (
            audio_code  # Code to indicate which Alarm Ringtone the Alarm is set to
        )

        self.audio = (
            AUDIO_DIR + ringtone_directories[audio_code]
        )  # Gets the Actual file directory of the Audio
        self.deleted = False
        self.audio_process = None

        self.alarm_check()  # Automatically starts the countdown for the alarm one initialisation

    def play_audio(self):
        """Plays the correct audio file"""
        while True:  ## Loops the Audio file
            playsound(self.audio, block=True)

    def alarm_check(self):  # sourcery skip: use-contextlib-suppress
        """
        Starts the Countdown for when the alarm should ring
        """
        difference_int = (
            self.time_to_ring - datetime.datetime.now()
        ).total_seconds()  # Figures out how long is left till the alarm should actually go off

        # time.sleep(difference_int)

        # TODO: Get rid of timeout and update DB if user says delete it

        try:
            inputimeout.inputimeout(
                prompt="Press anything to delete", timeout=difference_int
            )
            self.deleted = True
        except inputimeout.TimeoutOccurred:
            pass

        self.alarm_loop()

    def snooze_check(self):
        """Checks if the user has requested to snooze the alarm"""
        # IF audio detected == snooze:
        self.snooze_current()

    def stop_check(self):
        """Checks if the user requested to stop the alarm"""
        # IF audio detected == stop:

        self.stop_current()

    def snooze_current(self):
        """Snoozes an alarm that is going off"""
        self.audio_process.terminate()
        time.sleep(300)

    def stop_current(self):
        """Stops the current alarm"""
        self.audio_process.terminate()
        self.deleted = True

    def alarm_loop(self):
        """The actual loop for the alarm once it goes off"""
        while not self.deleted:
            self.audio_process = multiprocessing.Process(
                target=self.play_audio
            )  # Creates a multithread for the audio loop
            self.audio_process.start()

            # Replace with Snooze Check
            ask_in = input("s for snooze, d for stop:\n")
            if ask_in == "s":
                self.snooze_current()
            # Replace with Stop Check
            elif ask_in == "d":
                self.stop_current()
