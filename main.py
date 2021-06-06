from Cube import Cube
from Helpers import SOLVED, SAMPLE_SCRAMBLES
from time import time as current_time

# Start the timer just to flex
start_time = current_time()

# Mega Tester
sum_moves = 0
cubes_tested = 0
for scramble in SAMPLE_SCRAMBLES.split("\n")[:150]:
    cube = Cube(SOLVED)
    cube.move(scramble, False)
    cube.solve_color_agnostically()
    sum_moves += cube.move_count
    cubes_tested += 1

    # Test if oll was successful
    s = cube.cubestring()
    if not (s[0] == s[1] == s[2] == s[3] == s[4] == s[5] == s[6] == s[7] == s[8]):
        print("Test #", cubes_tested + 1, "failed.")

print(cubes_tested, "tests completed in", round(current_time() - start_time, 3),
      "seconds with an average of", round(sum_moves / cubes_tested, 2), "moves")
