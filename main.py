from Cube import Cube
from Helpers import SOLVED, SAMPLE_SCRAMBLES
from time import time as current_time

# SEQUENCE VALIDITY CHECKER
start_time = current_time()
sum_moves = 0
cubes_tested = 0
for scramble in SAMPLE_SCRAMBLES.split("\n")[:150]:
    cube = Cube(SOLVED)
    cube.move(scramble, False)
    cube.solve()
    cubes_tested += 1
    sum_moves += len(cube.solution_sequence.split())

    # Check if solution sequence is valid (Remove if testing half turn metric)
    cube2 = Cube(SOLVED)
    cube2.move(scramble, False)
    cube2.move(cube.solution_sequence)
    s = cube2.cubestring()
    if s[0:9] == 9*s[0] and s[9:18] == 9*s[9] and s[18:27] == 9*s[18] and s[27:36] == 9*s[27] and s[36:45] == 9*s[36] and s[45:54] == 9*s[45]:
        pass  # print("Cube #", cubes_tested, "solved.")
    else:
        print("Cube #", cubes_tested, "FAILED.")

# Print results
print(cubes_tested, "tests completed in", round(current_time() - start_time, 3),
      "seconds with an average of", round(sum_moves / cubes_tested, 2), "moves")
