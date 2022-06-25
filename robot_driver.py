from Robot import Robot

# Initialize Robot
robot = Robot()

# Proceed until user shuts down
while robot.proceed():

    # Construct a virtual cube, restart on camera input failure
    try:
        virtual_cube = robot.construct_simulation_cube()
    except Exception as e:
        print(repr(e))
        continue

    # Generate solution sequence from virtual cube
    solution_sequence = virtual_cube.generate_solution_sequence()

    # Use generated solution sequence to solve cube
    robot.solve(solution_sequence)
