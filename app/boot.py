import signal
import sys
import time
from time import strftime
from datetime import date
import calendar

from models.Detector import Detector
from models.HeadsUpDisplay import HeadsUpDisplay
from models.Broadcaster import Broadcaster


def keyboardHandler(signum, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, keyboardHandler)

if __name__ == "__main__":
    d = Detector()
    d.refresh()

    hud = HeadsUpDisplay()
    broadcaster = Broadcaster()

    cycle_count = 0
    sensorRefreshSeconds = 5
    lastRefreshTime = time.time()

    while True:
        time.sleep(4)

        try:
            currentTime = time.time()

            if currentTime > lastRefreshTime + sensorRefreshSeconds:
                d.refresh()
                broadcaster.cycle(
                    values={
                        'temp': d.getStat('temp'),
                        'humidity': d.getStat('humidity'),
                        'barometric': d.getStat('barometric_pressure_inches')
                    }
                )

                lastRefreshTime = currentTime

            if cycle_count > 2:
                cycle_count = 0

            if cycle_count == 1:
                title_text = d.getAirDescription()

                body_text = (" .  %d" % d.getStat('air_quality_small')) + ' ppm'
                body_text += ('\n°  %d' % d.getStat('air_quality_medium')) + ' ppm'
                body_text += ('\no  %d' % d.getStat('air_quality_large')) + ' ppm'

            else:
                title_text = d.getWeatherDescription()

                body_text = ('Temp: %0.0f' % d.getStat('temp')) + '°F'
                body_text += ('\nHumidity: %d' % d.getStat('humidity')) + '%'
                body_text += ('\nBarometric: %0.2f' % d.getStat('barometric_pressure_inches')) + ' in.'

            hud.setText( title=title_text, body=body_text )

            cycle_count += 1

        except Exception as e:
            # print(e)
            pass

        # sys.stdout.flush()
