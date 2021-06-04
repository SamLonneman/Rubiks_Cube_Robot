# This helper function converts a writeable file into a cubestring.
def read_file(input_file):
    input_file = open(input_file, "r")
    return readable_to_cubestring(input_file.read())


def readable_to_cubestring(readable):
    color_strips = readable.split()
    copy = color_strips.copy()
    color_strips[3] = copy[3]
    color_strips[4] = copy[7]
    color_strips[5] = copy[11]
    color_strips[6] = copy[4]
    color_strips[7] = copy[8]
    color_strips[8] = copy[12]
    color_strips[9] = copy[5]
    color_strips[10] = copy[9]
    color_strips[11] = copy[13]
    color_strips[12] = copy[6]
    color_strips[13] = copy[10]
    color_strips[14] = copy[14]
    return ''.join(color_strips)


SOLVED = "yyyyyyyyyrrrrrrrrrgggggggggooooooooobbbbbbbbbwwwwwwwww"

SCRAMBLES = """Fi U B Di F L D B D Li U Bi U Fi Bi Ri B R F L U D B F Ri
U D R B R U L D U R B U R B L Ui D Bi Di Ri U L U D R
R F D U B U D B Li B F Ri D B D L Fi Ui L U Fi D U F L
Bi U D R L Bi R Di U F D F R U L Di F R U Fi D Ui Bi F Ui
U Di B D L B Di L U B Li F Ri F R D R F Li B U D Fi R L
D U L Fi D U Fi L U B R U Bi F R L U R L U Fi B R Fi L
F B Di Fi L R Fi B L U L R Di Ri Di R L D F B R L Di Fi L
R F Ri B U D L Fi D L U L B D F Bi R D L U D Ri Bi U D
D Ri L D Ri D L Di Bi D Ri B L U R U D Li Di L F B R U B
D L Ri B Di U Fi L D L F R U R Di Fi R B F U D B L Ri Di
Di R B Ri L F U L U B F Ui B F D B L Ui L D L Bi D F Di
D Bi Ri Ui F B Ui D Bi U Di Ri Fi Ri Li Bi D B D F Di F B L Ri
L Di Ui F Ri Ui F U Fi U F R Li F L Ri F B R L Bi L D L B
Ri U D F Ui L Bi R Ui L B L U L Bi D Li Ui R U Di Ri U L R
F R L D L Di R F U R Ui Ri Ui R Di B R B F U L U Di F L
R D B Ui Di B F U Di B L Di Ui L Ui Di F L D L F Ui D F Li
Fi D Ui R Fi Di Li D R D F Li U Fi U B Ri B D Ri F R Bi Li F
L D U L U L D R Fi D Fi Bi D Ui Bi F Di Fi U Li Ui R D L D
Ri F Ri U B F R B Li R Di B L Ri Fi B Di Ri L B F Ui B Ui Bi
R U D Fi Di B R Fi Bi R B R B R Bi R B F D U R Ui D F D
D B D Bi F R L U Bi L R U L Bi R D R Ui R Fi L Di L U Li
B U Li R F B Di L D B U Fi L F B Ri L Fi B L Ri D Ui F R
L Di U L B D Fi R Fi L D L D R L D Bi R L Ui R F D B R
R Li Fi Di Ui L Di Ui Fi U L Fi D R F U F U D Fi D U Fi Li Ui
Di F U Ri D U L R F Di B F R D U Ri B Li R Bi U Bi Ri Li U
B Fi Di B Ui B Di F R Fi Di Li Bi D Bi U F Ui Di R B Ui Bi L F
Ui F R D B D F U Ri L F U Fi Bi D F U R Ui F R D B D L
Fi L F Ui Li R Di F B R Ui F L Ri Fi D F R Di Ri Ui L Bi R B
Li R U B Fi Di R Fi Di L R F B U D Fi Di L D L Di F U R Di
F Ri Bi D Li R B Li Ri F D L B U F B Ui Bi Li D L R F D Ui
R F U Di F Bi R D Li R D Ui R Ui Fi Li F Li F B Ri Ui R U D
B L Ui B L B Ui Li Ui Fi U F D Fi R Di L B Ri L Di Bi Di Li U
D F B L D Ri Ui L Ui R L U B D R Di B F Li Di L F Li Di Ri
Fi R Fi L D B R Bi F Ri U D B F Ri Di U F Di Fi B Li Fi U B
Li B U D L B D Fi Ri Fi D L D Li U D Fi D F Ui D Fi Li Bi R
U D L F Bi U D L B F Di R D B Ri L F L D R Bi Li B U Fi
B R B L R Bi R B U Di R D B Fi U B D Li Bi F R Di L F D
L R B Di Li R Di L U F R F U Di B F Ri Li Di Li R B Li F R
L R D F R U L Ri Di U Bi D Fi U B D Bi U B U B U D L Ri
R B Di R L F Ui Bi D B U B D Li U D Fi B L Di F L B Ui R
L F L B F R U Ri B Li R U D F Bi D B D F U Li D R Fi Ri
B L Ri Ui L D R Di L Bi L U L D L Ri Bi U Di R D R Fi B Di
F D F B Di R L F Ui D Ri L F L B L F U Fi U Bi D R F R
D Ui F Di B Li Di R Bi U F Li B D F Ui F R Ui D R Li B R U
U R U Di B Ui L F D Fi U F B L D B Ui L Di F L D Li R Di
U D Ri L D Ri F D B L B D Fi U Ri F Li Fi U Li Ui R B Di Ui
Li B L Ri F R D U B U Di Bi Ri Di U Li Ui Ri B U F L B R Li
D U B D F Di U F Bi L F R U Bi L R Di F U D L B Fi U R
R Bi L U R B R F R Fi Ri U R U D R U D R Bi Di F U D Bi
Fi U L Di Fi L Ui Di B Di U F L Fi U R Li Di F B L Di Ui Li R
Di U Li Ui Di Fi Ui D Li Di L R F U R Ui Di R D B U R U Li R
Ri U Di F D Li F Ri F U Li U Ri U R Di Bi L D F Bi U Bi L U
F B Ui F Ui F Ui Ri U F Ri U Di Ri Di R Li D B L R D B U B
B L B L Bi D U Li B U Bi Fi U Bi L F R Ui F U Fi D Fi Di U
L F B L B R D Ui R U Li Fi L F L R Fi D Ri L Ui B Li Ri F
B D F R D Li Di Ui Bi R F Di Ri D R F Bi L D R Di F U Li Ri
D U L F U Li Fi U L U R Bi Di F Li B R U R U Bi Li Di B Di
L D B L Ui Di Fi R F U B Ri U B F Li U F Di R B Ui B L B
Di L B R D Ui R Fi R Ui F B L U Di L Ri D B Fi L U F R Li
F B Ui F D F Li Ri U F L R D U Ri D B R Li Fi Di F R L U
Bi D Li Di B R L B Ri Ui B Fi U L D Fi Li Bi Li U F B Di U F
Bi R U D F Di L D Bi Ui Fi B L Fi Ri Li D R L B Li U R U D
U L B D L U F L F D Fi U B Ri B D Ui B Ri Bi Fi U R F R
R Fi Ui B Li Fi Li B Ri F Li R D R D B F Ui L F B U R Ui R
Ui R Ui R U Li Ri U L B D U L U L B Fi Li U Di B U B Ri D
Li Ri Di F Ui L B U F R D F R B Li Bi Ui F D Ri Bi Li D U F
U F Di L F Di Ui L D R U D B Li U D L Di F D L F Bi R L
D R F U F B R L U L Fi R D R L Fi R Ui Ri D L R D R B
Bi D F D Ui B Ri Bi D Bi R U D B R F L B L R B D F U B
F Di Fi R F Di Ri Fi B Di Bi D F U Li Di B F D L D B Ri U D
D L Di F D Ri Li F Li F B L Ri F B U Fi D U L F D F Bi L
Li Di Fi D B Ri U D B L Ui R L Ui Li B F R U F R Fi U D Ri
B L D Fi Di B L B F Li U F B R F L Di Ui Li Di Fi Ui Bi U L
R B U Li R Fi Ui L B R F U F Li Di B Fi U Fi L B F Ri U Li
U B F D R U F B Li F Ui Bi Li Di L R B R L D F Di Ui R Di
R D B Ri D Bi R Bi L R Ui R B Li U Ri D Bi Ui F U L F Di R
B R B Ui Fi L Ui R U R U B L B R Bi R Di F R F Di R B Li
R U F L Fi Li Di F Di U Bi U F Di L Bi U L Fi R L B D Ui F
Ui R Bi U D F U D Fi B Li F R F B D R D L Fi L D R Fi L
Bi R B Ri U F D Ri L Bi Li D Ui F Ri Di F U F D Bi L U R D
Bi D R L B U L Ui L U D L R U B F Ui Fi R L Ui Di Fi B Di
Ri D F L Di R Li F Li Fi R B Di B Ri Li F B L D U B F L D
D U Fi Ui F R Ui Bi Ui L Ri Fi R Fi B Li R F Bi D U B R Ui F
R Li Fi Ri Fi B Ri F D Fi Li F Ri B Di Bi L F Ui Ri Ui Ri Ui R D
Bi D L F D Fi U F L Di B Li R D Bi U R B U Di Ri B F Ui F
Li F Ri F B U B U Li Di Ui Li D F R D Fi Ri L F D U R U L
U Ri B Ri L B Li R F B D Ui F D U Ri F D L B Fi U B F R
D R L D Ri U Di B D U Li Fi B Ri B Fi Ri F R Fi R B R L Bi
R Di L F R L U L Ri U Li F Ri Bi Di L F L Ui D F B L B R
L D L Fi Di Ri L Ui D Bi F D L B L Fi B Ui L D R Di L D L
L D L Ui L U R Fi D F Ri B L R U Li B Fi R B Di F Li R D
U Fi D L Ri Fi Li Fi D U L Di F R U B Di F D Li B L D Fi U
R Ui Fi D Fi U F Ui B L B U L U Bi R U D Fi L Ui Li Di R Ui
D U R Bi R F D B D Bi L Di U R L D U Li U F R L B Li D
B Ri L D Ri Di R Fi Bi Ri D Fi R B D B Fi R F L D R U B L
L D Ui Ri Li U Fi D R Di U R F B L Ui F L Ui L R D Ui F B
F U D R L B D Ri L F R L D U Ri B L R Fi L R D B L D
F Ri U B L D B F D U Bi Ri Li Bi D F U Bi R B Di Bi Ui Ri Di
D Fi D Ui F L U Li D F L Ri D L Ui L Fi R F B R L F Ui L
Bi D U Li B Ui Bi L U Bi L F D L U Fi U Fi D R L B Ri Fi Ui
U Bi R F Di F Bi Ri Bi Fi R Fi B Ui Li U Di Li Fi B Di R D L Di
Ri Bi D B U F Ri L F B D Li D B Di Li Ri F R L F R D F Ui
F Ri L U D B F Li Bi L Ri F Di Ui R L F D Ui R F L Fi D Bi
F D R Fi L B Ui B Ri F D B Li D Ui Bi D Bi R L Di F L U Ri
Ri F B Ui Di Li Ri Bi R U F B L D B L D R F R D F R U B
R B F L Ri Di L Bi Ri Ui R F B R U R D Ri U Fi D Ui R U Bi
U Fi B Li Bi L Bi Ui Fi D B L F Li U F D F R L Fi Bi Ri D L
Li B D Ri B Fi D F D Ri B L F D Ui L R Ui Ri U B U D Bi F
D Ri B Fi L D F D Li B Li Fi Bi L Bi F U D Fi U R Di U L B
R Di R L B Fi L B U R Di R F L U Bi Li R Ui Bi U D B F U
D Li B Ri Bi L Ri F D L Fi D Ui Li Ui Bi L F U D Ri B Li R F
Fi Di Bi Fi Ri U B Di L U R U Di B Li Di L F B Di R L F D Li
F B U Fi R D B U Li Di B F D Li B D B U F D Ri L Bi Di R
R F R L F L B Fi L F D F B Ui B R Li B L Bi U F U Fi Bi
Bi F L B F L F Ri L F R Fi B Di B U F Bi R B U B R F Ri
B F D R Ui F Ui F D U Bi D F U F B L D Fi L Fi L D F B
R Ui Bi F U L Ui Ri Ui F Ri L F U D R B U Di Bi U F D R L
Ri L D F D F Di Li Ri F U F R L F Li Ui R D Bi Li R D Bi L
Li F L Fi L R F Li Fi U L U B R Di Li D U Ri B Fi L Ri Bi U
F U F Li U F D U L F L R Di F R Bi D Fi Ri B Ri L D Bi U
R U F R F L Bi L F R Ui Di Ri D Ui Bi R U L F B Ui F L B
L Di U L Bi Ri U B D U R D Li R Di Li D B D Ri B U F Ui Li
B D Ui B Li B L D U L R Bi U F Li R D B U D L F U D Ri
Li D F U Fi L U Di B Di U L U Fi B D L Di Ri F R F Bi U Ri
L Ri B D U Bi Di R B R F U B R U L F B Di Fi D Fi U Fi D
Ui R Li U F Ri Ui Di B Di U Li R B L B F R B D F D F U D
Ui R B D R D B Fi U Di B F D Bi D F Bi R F D U Bi Di B L
Di R F Ri U Li U R Li F L U D F R F Bi R F U F B Di L B
F B Ri L Ui L B Fi Di R U D B D B L F R D F U R U Ri L
Li U F Ri U L D F U L D F Di F L R F Ui R Di B Fi Ri Fi U
Ri U R U D Ri Di F L R B R F Li B R Di Li F Li B Ui Ri F Di
L R Fi U Fi L Fi Ui Ri L Di F D R F Di L D F D L B Ri Li D
B Li D Ui Fi D R U R D F U Ri Li Di Ui B U F B Ri Ui B R F
Ri B U D F B R F Ri F Ri F Ui D R L U R Bi F Di R Bi L U
B R Li F Li B Di U L Ui F R L D F U Li Fi R Di L U B Fi Ri
R L Bi D B D Li Ui D F D Ui Li R Ui L D B U Di F Di B U L
D Bi U F R Li Ui F Ui Ri B Ui B Ri L Di Ri U B Di B D B Di R
F L Bi Li R F U L D R B F Ui D F R Li D B L Ri U D F D
Ri U B D Li U F R Li B Ri L Di Fi Ui L B F Li B F L F U D
Ui Ri Di B R F Ri B D Li F B U Ri B Ui Li Di B Ui L Ui Ri Di B
U D F D Bi R Di Fi Ui L Fi L Di R D U R F Ri L Ui Ri D Ui R
Bi L Bi Ri L F U B L U Li B Di L Ui Li B U F D L Bi R D R
L Ui F Bi L B Di L R F L Ri F R B Di Fi Bi R L F Ui R Li Di
Li F D Ri D Fi Ui R L B D R Bi L R Ui B Li Ri F B R L U Ri
D L Ri Bi L B Di R L Di Ui Ri Bi F D L Bi Ui Di L U L Bi U R
U Li U F Di U Ri L D U L Di R Di L B Di Ui F Di L F U L D
R D R D U Li D R Li B Li Ri Bi L R U R Ui L U F Ui Li U Ri
F L D B D B F D L D R D L R F Ri B D L B L F R Ui Li
U R U D R Li B L B L U B Di L R U R L U B U L R F R
R F D F B Di F U B R Fi Di R U R F Bi L B U Ri D F D F"""
