from RPi import GPIO
from time import sleep
from Robot import Robot
from Cube import Cube

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Initialize Robot
robot = Robot()

# Lets GOOOOO
robot.grab()
sleep(2000)

# # Read in cube state (For now a random scramble)
# cube = Cube("ryowyobbrgbrgrgwbyyybrgwboywgyoorgyoggwwbwwbboyrrwroog")
#
# # Generate solution
# cube.solve()
#
# # Solve cube
# for turn in cube.solution_sequence.split():
#     getattr(robot, turn)()

robot.drop()
