import os
import sys
LED_PATH = os.getcwd()
sys.path.append(os.path.join(LED_PATH, 'ws2x'))
from ws2x.led import LEDSim