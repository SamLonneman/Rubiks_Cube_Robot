from time import time as current_time

from VirtualCube import VirtualCube
from constants import SOLVED, SAMPLE_SCRAMBLES

# SEQUENCE VALIDITY CHECKER
start_time = current_time()
sum_moves = 0
sum_rotations = 0
virtual_cubes_tested = 0
for scramble in SAMPLE_SCRAMBLES.split("\n")[:150]:
    virtual_cube = VirtualCube(SOLVED)
    virtual_cube.move(scramble, False)
    virtual_cube.generate_solution_sequence()
    virtual_cubes_tested += 1
    sum_moves += len(virtual_cube.solution_sequence.split())
    sum_rotations += virtual_cube.solution_sequence.count('x')

    # Check if solution sequence is valid (Remove if testing half turn metric)
    virtual_cube_2 = VirtualCube(SOLVED)
    virtual_cube_2.move(scramble, False)
    virtual_cube_2.move(virtual_cube.solution_sequence)
    s = virtual_cube_2.generate_cubestring()
    if s[0:9] == 9*s[0] and s[9:18] == 9*s[9] and s[18:27] == 9*s[18] and s[27:36] == 9*s[27] and s[36:45] == 9*s[36] and s[45:54] == 9*s[45]:
        pass  # print("Cube #", cubes_tested, "solved.")
    else:
        print("Virtual cube #", virtual_cubes_tested, "FAILED.")

# Print results
print(virtual_cubes_tested, "tests completed in", round(current_time() - start_time, 3),
      "seconds with an average of", round(sum_moves / virtual_cubes_tested, 2), "moves, of which",
      round(sum_rotations / virtual_cubes_tested, 2), "were rotations.")
