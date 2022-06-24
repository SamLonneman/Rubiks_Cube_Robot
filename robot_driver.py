from Robot import Robot

# Initialize Robot
robot = Robot()

# Proceed until user shuts down
while robot.proceed():

    # Construct a virtual cube
    simulation_cube = robot.construct_simulation_cube()

    # Generate solution sequence from virtual cube
    solution_sequence = simulation_cube.solve()

    # Use generated solution sequence to solve cube
    robot.solve(solution_sequence)
