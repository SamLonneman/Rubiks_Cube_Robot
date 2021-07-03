from RPi import GPIO
from time import sleep


class Motor:

    def __init__(self, step_pin, direction_pin):
        self.step_pin = step_pin
        self.direction_pin = direction_pin
        GPIO.setup(self.direction_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)

    def turn(self, steps=50, clockwise=True, delay=0.0005, other=None):

        # If moving motor alone
        if other is None:

            # Activate direction pin
            GPIO.output(self.direction_pin, clockwise)

            # Step motor accordingly
            for _ in range(steps):
                GPIO.output(self.step_pin, True)
                sleep(delay)
                GPIO.output(self.step_pin, False)
                sleep(delay)

        # If moving two motors simultaneously
        else:

            # Activate direction pin
            GPIO.output(self.direction_pin, clockwise)
            GPIO.output(other.direction_pin, not clockwise)

            # Step motor accordingly
            for _ in range(steps):
                GPIO.output(self.step_pin, True)
                GPIO.output(other.step_pin, True)
                sleep(delay)
                GPIO.output(self.step_pin, False)
                GPIO.output(other.step_pin, False)
                sleep(delay)
