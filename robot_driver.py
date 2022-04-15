from Robot import Robot
from Cube import Cube

# Initialize Robot
robot = Robot()

# Lets GOOOOO
for _ in range(1):
    robot.R()
    robot.L()
    robot.F()
    robot.B()
    robot.x()
    robot.xi()
    robot.Bi()
    robot.Fi()
    robot.Li()
    robot.Ri()


# # Read in cube state (For now a random scramble)
# cube = Cube("ryowyobbrgbrgrgwbyyybrgwboywgyoorgyoggwwbwwbboyrrwroog")
#
# # Generate solution
# cube.solve()
#
# # Solve cube
# for turn in cube.solution_sequence.split():
#     getattr(robot, turn)()
#
# # Drop cube
# robot.drop()
