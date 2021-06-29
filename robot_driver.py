from RPi import GPIO
from Motor import Motor
from time import sleep

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Initialize Motors
motor1 = Motor(2, 3)
motor2 = Motor(4, 17)

# Drive Motors
for _ in range(10):
    motor1.turn(50, 0.0005, True, motor2)
    sleep(.2)

# GPIO Cleanup
GPIO.cleanup()
