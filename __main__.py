""" Main File with Script for Athena """

# from _ import _
import datetime

from src.utils import Timer

if __name__ == "__main__":
    Timer.Timer(
        "", "test", datetime.datetime.now() + datetime.timedelta(seconds=3), "Ish", ""
    )
