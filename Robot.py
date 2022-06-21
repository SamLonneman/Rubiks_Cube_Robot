from RPi import GPIO
from Motor import Motor
from os import system


class Robot:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.solve_button = 6
        self.abort_button = 13
        self.shutdown_button = 19
        self.hot_pin = 26
        GPIO.setup(self.solve_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.abort_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.shutdown_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.hot_pin, GPIO.OUT)
        GPIO.output(self.hot_pin, True)
        system("sudo sh -c \"echo none > /sys/class/leds/led1/trigger\"")
        system("sudo sh -c \"echo 0 > /sys/class/leds/led1/brightness\"")
        system("sudo sh -c \"echo none > /sys/class/leds/led0/trigger\"")
        system("sudo sh -c \"echo 1 > /sys/class/leds/led0/brightness\"")
        self.motorR1 = Motor(18, 15)
        self.motorR2 = Motor(8, 25)
        self.motorL1 = Motor(24, 23)
        self.motorL2 = Motor(1, 7)
        self.motorF1 = Motor(27, 17)
        self.motorF2 = Motor(11, 9)
        self.motorB1 = Motor(10, 22)
        self.motorB2 = Motor(5, 0)

    def grab(self):
        self.motorR2.extend()
        self.motorF2.extend()
        self.motorL2.extend()
        self.motorB2.extend()

    def drop(self):
        self.motorR2.retract()
        self.motorF2.retract()
        self.motorL2.retract()
        self.motorB2.retract()

    def R(self):
        self.motorR1.cw()
        self.motorR2.retract()
        self.motorR1.ccw()
        self.motorR2.extend()

    def Ri(self):
        self.motorR1.ccw()
        self.motorR2.retract()
        self.motorR1.cw()
        self.motorR2.extend()

    def R2(self):
        self.motorR1.cw()
        self.motorR1.cw()

    def L(self):
        self.motorL1.cw()
        self.motorL2.retract()
        self.motorL1.ccw()
        self.motorL2.extend()

    def Li(self):
        self.motorL1.ccw()
        self.motorL2.retract()
        self.motorL1.cw()
        self.motorL2.extend()

    def L2(self):
        self.motorL1.cw()
        self.motorL1.cw()

    def F(self):
        self.motorF1.cw()
        self.motorF2.retract()
        self.motorF1.ccw()
        self.motorF2.extend()

    def Fi(self):
        self.motorF1.ccw()
        self.motorF2.retract()
        self.motorF1.cw()
        self.motorF2.extend()

    def F2(self):
        self.motorF1.cw()
        self.motorF1.cw()

    def B(self):
        self.motorB1.cw()
        self.motorB2.retract()
        self.motorB1.ccw()
        self.motorB2.extend()

    def Bi(self):
        self.motorB1.ccw()
        self.motorB2.retract()
        self.motorB1.cw()
        self.motorB2.extend()

    def B2(self):
        self.motorB1.cw()
        self.motorB1.cw()

    def x(self):
        self.motorR2.retract()
        self.motorR1.ccw()
        self.motorR2.extend()
        self.motorF2.retract(self.motorB2)
        self.motorR1.cw(self.motorL1)
        self.motorF2.extend(self.motorB2)
        self.motorL2.retract()
        self.motorL1.cw()
        self.motorL2.extend()

    def xi(self):
        self.motorR2.retract()
        self.motorR1.ccw()
        self.motorR2.extend()
        self.motorF2.retract(self.motorB2)
        self.motorR1.ccw(self.motorL1)
        self.motorF2.extend(self.motorB2)
        self.motorL2.retract()
        self.motorL1.cw()
        self.motorL2.extend()

    def z(self):
        self.motorF2.retract()
        self.motorF1.ccw()
        self.motorF2.extend()
        self.motorL2.retract(self.motorR2)
        self.motorF1.cw(self.motorB1)
        self.motorL2.extend(self.motorR2)
        self.motorB2.retract()
        self.motorB1.cw()
        self.motorB2.extend()

    def z2(self):
        self.motorF2.retract()
        self.motorF1.ccw()
        self.motorF2.extend()
        self.motorL2.retract(self.motorR2)
        self.motorF1.cw(self.motorB1)
        self.motorF1.cw(self.motorB1)
        self.motorL2.extend(self.motorR2)
        self.motorF2.retract()
        self.motorF1.cw()
        self.motorF2.extend()
