from RPi import GPIO
from time import sleep
from Motor import Motor
from Cube import Cube

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Initialize Motors
motorR1 = Motor(15, 18)
motorR2 = Motor(23, 24)
motorL1 = Motor(25, 8)
motorL2 = Motor(7, 1)
motorF1 = Motor(3, 4)
motorF2 = Motor(17, 27)
motorB1 = Motor(10, 9)
motorB2 = Motor(0, 5)

# Grab cube
motorR2.turn(False)
motorF2.turn(False)
motorL2.turn(False)
motorB2.turn(False)
sleep(2000)

# Read in cube state (For now a random scramble)
cube = Cube("ryowyobbrgbrgrgwbyyybrgwboywgyoorgyoggwwbwwbboyrrwroog")

# Generate solution
cube.solve()

# Solve cube
for turn in cube.solution_sequence.split():
    eval(turn + "()")

# Drop cube
motorR2.turn()
motorF2.turn()
motorL2.turn()
motorB2.turn()


# Robot Functions
def R():
    motorR1.turn()
    motorR2.turn()
    motorR1.turn(False)
    motorR2.turn(False)


def Ri():
    motorR1.turn(False)
    motorR2.turn()
    motorR1.turn()
    motorR2.turn(False)


def R2():
    motorR1.turn(True, None, True, 100)


def L():
    motorL1.turn()
    motorL2.turn()
    motorL1.turn(False)
    motorL2.turn(False)


def Li():
    motorL1.turn(False)
    motorL2.turn()
    motorL1.turn()
    motorL2.turn(False)


def L2():
    motorL1.turn(True, None, True, 100)


def F():
    motorF1.turn()
    motorF2.turn()
    motorF1.turn(False)
    motorF2.turn(False)


def Fi():
    motorF1.turn(False)
    motorF2.turn()
    motorF1.turn()
    motorF2.turn(False)


def F2():
    motorF1.turn(True, None, True, 100)


def B():
    motorB1.turn()
    motorB2.turn()
    motorB1.turn(False)
    motorB2.turn(False)


def Bi():
    motorB1.turn(False)
    motorB2.turn()
    motorB1.turn()
    motorB2.turn(False)


def B2():
    motorB1.turn(True, None, True, 100)


def x():
    motorR2.turn()
    motorR1.turn(False)
    motorR2.turn(False)
    motorF2.turn(True, motorB2, True)
    motorR1.turn(True, motorL1, False)
    motorL2.turn()
    motorL1.turn()
    motorL2.turn(False)
    motorF2.turn(False, motorB2, False)


def xi():
    motorR2.turn()
    motorR1.turn(False)
    motorR2.turn(False)
    motorF2.turn(True, motorB2, True)
    motorR1.turn(False, motorL1, True)
    motorL2.turn()
    motorL1.turn()
    motorL2.turn(False)
    motorF2.turn(False, motorB2, False)
