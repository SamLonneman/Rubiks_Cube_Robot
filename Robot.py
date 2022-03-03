from Motor import Motor


class Robot:

    def __init__(self):
        self.motorR1 = Motor(15, 18)
        self.motorR2 = Motor(23, 24)
        self.motorL1 = Motor(25, 8)
        self.motorL2 = Motor(7, 1)
        self.motorF1 = Motor(3, 4)
        self.motorF2 = Motor(17, 27)
        self.motorB1 = Motor(10, 9)
        self.motorB2 = Motor(0, 5)

    def grab(self):
        self.motorR2.turn(False)
        self.motorF2.turn(False)
        self.motorL2.turn(False)
        self.motorB2.turn(False)

    def drop(self):
        self.motorR2.turn()
        self.motorF2.turn()
        self.motorL2.turn()
        self.motorB2.turn()

    def R(self):
        self.motorR1.turn()
        self.motorR2.turn()
        self.motorR1.turn(False)
        self.motorR2.turn(False)

    def Ri(self):
        self.motorR1.turn(False)
        self.motorR2.turn()
        self.motorR1.turn()
        self.motorR2.turn(False)

    def R2(self):
        self.motorR1.turn(True, None, True, 100)

    def L(self):
        self.motorL1.turn()
        self.motorL2.turn()
        self.motorL1.turn(False)
        self.motorL2.turn(False)

    def Li(self):
        self.motorL1.turn(False)
        self.motorL2.turn()
        self.motorL1.turn()
        self.motorL2.turn(False)

    def L2(self):
        self.motorL1.turn(True, None, True, 100)

    def F(self):
        self.motorF1.turn()
        self.motorF2.turn()
        self.motorF1.turn(False)
        self.motorF2.turn(False)

    def Fi(self):
        self.motorF1.turn(False)
        self.motorF2.turn()
        self.motorF1.turn()
        self.motorF2.turn(False)

    def F2(self):
        self.motorF1.turn(True, None, True, 100)

    def B(self):
        self.motorB1.turn()
        self.motorB2.turn()
        self.motorB1.turn(False)
        self.motorB2.turn(False)

    def Bi(self):
        self.motorB1.turn(False)
        self.motorB2.turn()
        self.motorB1.turn()
        self.motorB2.turn(False)

    def B2(self):
        self.motorB1.turn(True, None, True, 100)

    def x(self):
        self.motorR2.turn()
        self.motorR1.turn(False)
        self.motorR2.turn(False)
        self.motorF2.turn(True, self.motorB2, True)
        self.motorR1.turn(True, self.motorL1, False)
        self.motorL2.turn()
        self.motorL1.turn()
        self.motorL2.turn(False)
        self.motorF2.turn(False, self.motorB2, False)

    def xi(self):
        self.motorR2.turn()
        self.motorR1.turn(False)
        self.motorR2.turn(False)
        self.motorF2.turn(True, self.motorB2, True)
        self.motorR1.turn(False, self.motorL1, True)
        self.motorL2.turn()
        self.motorL1.turn()
        self.motorL2.turn(False)
        self.motorF2.turn(False, self.motorB2, False)
