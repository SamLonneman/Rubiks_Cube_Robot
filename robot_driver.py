from constants import SOLVED
from Robot import Robot
from Cube import Cube
from time import sleep
from RPi import GPIO
from os import system

# Initialize Robot
robot = Robot()

while not GPIO.input(robot.shutdown_button):

    # Wait for input
    while not (GPIO.input(robot.shutdown_button) or GPIO.input(robot.solve_button)):
        sleep(0.1)

    # If solve button was pressed, solve
    if not GPIO.input(robot.shutdown_button):

        # Read in cube state (For now a superflip)
        cube = Cube(SOLVED)
        cube.move("M M Ui R R Di S M M U Mi U U F F Di S M M Ui R R Ui", False)

        # Solve cube, abort at any time if necessary
        cube.solve()
        for turn in cube.solution_sequence.split():
            if GPIO.input(robot.abort_button):
                break
            getattr(robot, turn)()

# Shut down
GPIO.cleanup()
system("sudo shutdown -h now")
