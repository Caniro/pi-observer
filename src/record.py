from picamera import PiCamera
from datetime import datetime
import RPi.GPIO as GPIO
import time

camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 24
camera.vflip = True
camera.hflip = True

def record():
    for i in range(0, 12):
        current_time = datetime.now()
        filename = current_time.strftime('%Y%m%d_%H%M%S')
        camera.start_recording('/home/pi/Desktop/CCTV/data/' + filename + '.h264')
        camera.wait_recording(5)
        camera.stop_recording()

door_sensor = 14 # pin 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(door_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while 1:
        time.sleep(1)
        if (GPIO.input(door_sensor)):
            record()
#except KeyboardInterrupt:
finally:
    camera.close()
    GPIO.cleanup()
