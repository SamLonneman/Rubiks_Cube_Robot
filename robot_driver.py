from os import system
from time import sleep

from Cube import Cube
from Robot import Robot

# Initialize Robot
robot = Robot()

# Repeat until shutdown button is pressed
while not robot.shutdown_button_is_depressed():

    # Wait for input
    while not (robot.shutdown_button_is_depressed() or robot.solve_button_is_depressed()):
        sleep(0.1)

    # If solve button was pressed, solve
    if not robot.shutdown_button_is_depressed():

        # Construct a simulation cube and solve it
        cube = robot.construct_simulation_cube()
        solution_sequence = cube.solve()

        # Solve physical cube, abort at any time if necessary
        for turn in solution_sequence.split():
            getattr(robot, turn)()
            if robot.abort_button_is_depressed():
                break

# Shut down
robot.cleanup()
system("sudo shutdown -h now")
