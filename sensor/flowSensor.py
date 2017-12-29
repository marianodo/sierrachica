#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#PIN = 4
#GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
import time
import threading
import datetime as DT
import logging
logger = logging.getLogger(__name__)

class FlowSensor(object):
    def __init__(self):
        self.pulse = 0
        self.cond = threading.Condition()
        self.t = threading.Thread(target=self.incrementPulse, args=(self.cond,))
        self.t.daemon = True
        self.t.start()
        self.active = False
        self.t.do_run = False
        print("INIT")
        # GPIO.setmode(GPIO.BCM)
        # PIN = 4
        # GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # GPIO.add_event_detect(PIN, GPIO.RISING, callback=my_callback)
    def incrementPulse(self, cond):
        while True:
            while getattr(self.t, "do_run", True):
                time.sleep(1)
                self.pulse += 1
            time.sleep(1)

    def startPulse(self):
        print ("start pulse")
        self.t.do_run = True

    def stopPulse(self):
        self.t.do_run = False

    def getPulse(self):
        return self.pulse

    def clearPulse(self):
        self.pulse = 0



#GPIO.add_event_detect(PIN, GPIO.RISING, callback=my_callback)
#GPIO.cleanup()
