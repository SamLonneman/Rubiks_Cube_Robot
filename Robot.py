from RPi import GPIO
from Motor import Motor


class Robot:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.motorR1 = Motor(15, 18)
        self.motorR2 = Motor(23, 24)
        self.motorL1 = Motor(25, 8)
        self.motorL2 = Motor(7, 1)
        self.motorF1 = Motor(3, 4)
        self.motorF2 = Motor(17, 27)
        self.motorB1 = Motor(10, 9)
        self.motorB2 = Motor(0, 5)

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
