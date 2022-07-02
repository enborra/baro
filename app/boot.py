import signal
import sys
import time
from time import strftime
from datetime import date
import calendar

from models.Detector import Detector
from models.HeadsUpDisplay import HeadsUpDisplay


def keyboardHandler(signum, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, keyboardHandler)

if __name__ == "__main__":
    d = Detector()
    d.refresh()

    hud = HeadsUpDisplay()

    cycle_count = 0
    lastRefreshTime = time.time()

    while True:
        time.sleep(2)

        try:
            if time.time() > lastRefreshTime + 10
                print("updating sensors")
                d.refresh()

            if cycle_count > 10:
                cycle_count = 0

            elif cycle_count > 5:
                title_text = "Temp"
                body_text = ('Temp: %0.0f°F' % d.getStat('temp'))
                body_text += ('\nHumidity: %d' % d.getStat('humidity'))
                body_text += ('\nBarometric: %d' % d.getStat('barometric_pressure'))

            else:
                title_text = "Air"
                body_text = ("Small dust: %d" % d.getStat('air_quality_small'))
                body_text += ('\nMedium dust: %d' % d.getStat('air_quality_medium'))
                body_text += ('\nBig dust: %d' % d.getStat('air_quality_large'))

            hud.setText( title=title_text, body=body_text )

            cycle_count += 1

        except Exception as e:
            print(e)

        sys.stdout.flush()
