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
    sensorRefreshSeconds = 5
    lastRefreshTime = time.time()

    while True:
        time.sleep(4)

        try:
            currentTime = time.time()

            if currentTime > lastRefreshTime + sensorRefreshSeconds:
                d.refresh()
                lastRefreshTime = currentTime

            if cycle_count > 2:
                cycle_count = 0

            if cycle_count == 1:
                pmLarge = d.getStat('air_quality_large')
                pmMedium = d.getStat('air_quality_medium')
                pmSmall = d.getStat('air_quality_small')

                title_text = "Air: "

                if pmLarge < 50:
                    title_text += 'Great'

                elif pmLarge <200:
                    title_text += 'Moderate'

                else:
                    title_text += 'Bad'

                body_text = ("Chemicals: %d" % pmSmall)
                body_text += ('\nSmoke & dust: %d' % pmMedium)
                body_text += ('\nPollen: %d' % pmLarge)

            else:
                baroInches = d.getStat('barometric_pressure_inches')

                if baroInches > 32:
                    title_text = 'Very dry.'

                elif baroInches > 31:
                    title_text = 'Dry.'

                elif baroInches > 30:
                    title_text = 'Overcast'

                elif baroInches > 29:
                    title_text = 'Rain'

                elif baroInches > 28:
                    title_text = 'Heavy rain'

                else:
                    title_text = "Storm's comin."

                body_text = ('Temp: %0.0f' % d.getStat('temp')) + '°F'
                body_text += ('\nHumidity: %d' % d.getStat('humidity')) + '%'
                body_text += ('\nBarometric: %d' % d.getStat('barometric_pressure_inches')) + 'in.'

            hud.setText( title=title_text, body=body_text )

            cycle_count += 1

        except Exception as e:
            print(e)

        sys.stdout.flush()
