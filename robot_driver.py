from RPi import GPIO
from Motor import Motor
from time import sleep

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Initialize Motors
motor1 = Motor(15, 18)
motor2 = Motor(23, 24)
motor3 = Motor(25, 8)
motor4 = Motor(7, 1)

# Drive Motors
for _ in range(30):
    motor1.turn()
    motor2.turn()
    motor3.turn()
    motor4.turn()
