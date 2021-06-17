import RPi.GPIO as GPIO
import time

door_sensor = 14 # pin 8
green_led = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(door_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(green_led, GPIO.OUT)

try:
    while 1:
        time.sleep(0.3)
        if (GPIO.input(door_sensor)):
            GPIO.output(green_led, GPIO.HIGH)
        else:
            GPIO.output(green_led, GPIO.LOW)
#except KeyboardInterrupt:
finally:
    GPIO.cleanup()
