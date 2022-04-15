from RPi import GPIO
from time import sleep


class Motor:

    def __init__(self, step_pin, direction_pin):
        self.step_pin = step_pin
        self.direction_pin = direction_pin
        GPIO.setup(self.direction_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)

    def turn(self, clockwise, other, other_cw, steps, delay):
        # If moving motor alone
        if other is None:
            # Activate direction pin
            GPIO.output(self.direction_pin, not clockwise)
            # Step motor accordingly
            for _ in range(steps):
                GPIO.output(self.step_pin, True)
                sleep(delay)
                GPIO.output(self.step_pin, False)
                sleep(delay)
        # If moving two motors simultaneously
        else:
            # Activate direction pins
            GPIO.output(self.direction_pin, not clockwise)
            GPIO.output(other.direction_pin, not other_cw)
            # Step motors accordingly
            for _ in range(steps):
                GPIO.output(self.step_pin, True)
                GPIO.output(other.step_pin, True)
                sleep(delay)
                GPIO.output(self.step_pin, False)
                GPIO.output(other.step_pin, False)
                sleep(delay)

    def cw(self, other=None):
        self.turn(True, other, False, 50, 0.001)

    def ccw(self, other=None):
        self.turn(False, other, True, 50, 0.001)

    def extend(self, other=None):
        self.turn(False, other, False, 450, 0.0003)

    def retract(self, other=None):
        self.turn(True, other, True, 450, 0.0003)
