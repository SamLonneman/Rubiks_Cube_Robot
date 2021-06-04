from Cube import Cube
from Helpers import SOLVED, SCRAMBLES
from time import time as current_time

# Start the timer just to flex
start_time = current_time()

# Mega Tester
sum_moves = 0
cubes_tested = 0
for scramble in SCRAMBLES.split("\n")[:150]:
    cube = Cube(SOLVED)
    cube.move(scramble, False)
    cube.solve_color_agnostically()
    sum_moves += cube.move_count
    cubes_tested += 1

    # Test if the cross was successful
    s = cube.cubestring()
    if not (s[49] == s[48] == s[46] == s[50] == s[52] and
            s[22] == s[25] and
            s[31] == s[34] and
            s[40] == s[43] and
            s[13] == s[16]):
        print("Test #", cubes_tested + 1, "failed.")

print(cubes_tested, "tests completed in", round(current_time() - start_time, 3),
      "seconds with an average of", round(sum_moves / cubes_tested, 2), "moves")
