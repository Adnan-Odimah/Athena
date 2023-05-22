""" Contains the Timer object"""
import datetime
import multiprocessing

from src.utils import Alarm


class Timer(Alarm.Alarm):
    """
    Timer Class
    db_id: ID of record in database
    name: name of record
    time_to_ring: when the timer rings
    audio_code: ringtone to be played
    message: message that will be said (not needed)
    """

    def __init__(
        self,
        db_id: str,
        name: str,
        time_to_ring: datetime.datetime,
        audio_code: str,
        message: str,
    ):
        super().__init__(db_id, name, time_to_ring, audio_code)
        self.message = message

    def alarm_loop(self):
        print("t")
        while not self.deleted:
            # TODO: ONCE NLP DONE - SAY Message
            print("h")
            self.audio_process = multiprocessing.Process(target=self.play_audio)
            self.audio_process.start()

            # TODO: Replace with Stop Check
            self.stop_check()

    def snooze_check(self):
        """N/A for timers"""
        return
