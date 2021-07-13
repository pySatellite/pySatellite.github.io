"""인공위성 발사 위한 로켓 모듈"""
import time

COUNTDOWN_START = 10
COUNTDOWN_SLEEP_SECS = 1


class Rocket:
    """인공위성을 궤도에 진입 시키기 위한 로켓"""

    @staticmethod
    def launch():
        """countdown & launch

        To use:

            >>> Rocket.launch()
            9
            ...
            1
            rocket booster ignition and liftoff!

        """
        Rocket.countdown()
        print("rocket booster ignition and liftoff!")

    @staticmethod
    def countdown():
        """로켓 발사 카운트 다운

        Todo:
            * https://www.nasa.gov/mission_pages/shuttle/launch/countdown101.html
        """
        for i in range(COUNTDOWN_START, 0, -1):
            print(i)
            time.sleep(COUNTDOWN_SLEEP_SECS)
