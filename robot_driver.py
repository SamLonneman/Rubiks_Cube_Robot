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

        # Construct a simulation cube
        simulation_cube = robot.construct_simulation_cube()

        # Generate solution sequence from simulation cube
        solution_sequence = simulation_cube.solve()

        # Use generated solution sequence to solve physical cube
        robot.solve(solution_sequence)

# Shut down
robot.cleanup()
system("sudo shutdown -h now")
