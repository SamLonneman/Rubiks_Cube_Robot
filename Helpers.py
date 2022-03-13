# This helper function converts a writeable file into a cubestring.
def read_file(input_file):
    input_file = open(input_file, "r")
    return create_cubestring(input_file.read())


# Creates a cubestring from a readable string
def create_cubestring(readable_string):
    color_strips = readable_string.split()
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


# Cubestring of a solved cube
SOLVED = "yyyyyyyyyrrrrrrrrrgggggggggooooooooobbbbbbbbbwwwwwwwww"

# Dictionary containing all F2L cases and their algorithms
F2L_ALGORITHMS = {
    # "<F2L Configuration>": "<Corresponding Algorithm>"
    "dym1": "",  # Case 00: F2L skip
    "dym0": "R Ui Ri U yi Ri U U R Ui Ui Ri U R",  # Case 01
    "dyf0": "U R Ui Ri Ui yi Ri U R",  # Case 02
    "dyr1": "Ri Fi R U R Ui Ri F yi",  # Case 03
    "dzm1": "R U Ri Ui R U U Ri Ui R U Ri yi",  # Case 04
    "dzm0": "R F U R Ui Ri Fi Ui Ri yi",  # Case 05
    "dzf0": "yi Ri Ui R U Ri Ui R",  # Case 06
    "dzr1": "R Ui Ri U R Ui Ri yi",  # Case 07
    "dxm1": "R Ui Ri U R Ui Ui Ri U R Ui Ri yi",  # Case 08
    "dxm0": "R U F R U Ri Ui Fi Ri yi",  # Case 09
    "dxf0": "yi Ri U R Ui Ri U R",  # Case 10
    "dxr1": "R U Ri Ui R U Ri yi",  # Case 11
    "uxm1": "R U Ri Ui R U Ri Ui R U Ri yi",  # Case 12
    "uxm0": "R Ui Ri U yi Ri U R",  # Case 13
    "uxf0": "yi Ri U U R U Ri Ui R",  # Case 14
    "uxl0": "yi Ui Ri U U R Ui Ri U R",  # Case 15
    "uxb0": "yi Ri U R Ui Ui Ri Ui R",  # Case 16
    "uxr0": "F U R Ui Ri Fi R Ui Ri yi",  # Case 17
    "uxf1": "U R Ui Ri Ui R Ui Ri U R Ui Ri yi",  # Case 18
    "uxl1": "R Ui Ri U U R U Ri yi",  # Case 19
    "uxb1": "U R Ui Ui Ri U R Ui Ri yi",  # Case 20
    "uxr1": "R Ui Ui Ri Ui R U Ri yi",  # Case 21
    "uym1": "Ui R Ui Ri U U R Ui Ri yi",  # Case 22
    "uym0": "Ui R U Ri yi U Ri Ui R",  # Case 23
    "uyf0": "yi U Ri U R Ui Ri Ui R",  # Case 24
    "uyl0": "yi Ri Ui R",  # Case 25
    "uyb0": "yi U Ri Ui R Ui Ri Ui R",  # Case 26
    "uyr0": "yi R Ui Ui Ri Ri Ui R R Ui Ri",  # Case 27
    "uyf1": "xi R U x L Ui Li xi Ui Ri x",  # Case 28
    "uyl1": "Ui R Ui Ui Ri U U R Ui Ri yi",  # Case 29
    "uyb1": "Ui R U Ri Ui R Ui Ui Ri yi",  # Case 30
    "uyr1": "U R Ui Ri yi",  # Case 31
    "uzm1": "Ui R Ui Ui Ri U R U Ri yi",  # Case 32
    "uzm0": "yi U Ri Ui R y Ui R U Ri",  # Case 33
    "uzf0": "yi Ui Ri U R",  # Case 34
    "uzl0": "yi U Ri Ui R Ui Ui Ri U R",  # Case 35
    "uzb0": "yi U Ri U U R Ui Ui Ri U R",  # Case 36
    "uzr0": "R Ui Ri U U yi Ri Ui R",  # Case 37
    "uzf1": "R Ui Ri U R Ui Ri U U R Ui Ri yi",  # Case 38
    "uzl1": "Ui R U Ri U R U Ri yi",  # Case 39
    "uzb1": "R U Ri yi",  # Case 40
    "uzr1": "Ui R Ui Ri U R U Ri yi",  # Case 41
}

# Dictionary containing all OLL cases and their algorithms
OLL_ALGORITHMS = {
    # "<OLL Configuration>": "<Corresponding Algorithm>"
    "000011100111001110000": "",  # Case 00: OLL skip
    "010100011010110001010": "R Ui Ui Ri Ri F R Fi U U Ri F R Fi",  # Case 01
    "011100001010110000011": "F R U Ri Ui Fi f R U Ri Ui fi",  # Case 02
    "110000011010110010010": "f R U Ri Ui fi Ui F R U Ri Ui Fi",  # Case 03
    "010100101010100001110": "f R U Ri Ui fi U F R U Ri Ui Fi",  # Case 04
    "110000011011010110000": "ri U U R U Ri U r",  # Case 05
    "000101101011000001110": "r Ui Ui Ri Ui R Ui ri",  # Case 06
    "100001010110101000011": "r U Ri U R Ui Ui ri",  # Case 07
    "011010000110100101100": "ri Ui R Ui Ri U U r",  # Case 08
    "001101000110100010110": "R U Ri Ui Ri F R R U Ri Ui Fi",  # Case 09
    "110000100110110100001": "R U Ri U Ri F R Fi R Ui Ui Ri",  # Case 10
    "110000011011001100001": "ri R R U Ri U R Ui Ui Ri U Mi",  # Case 11
    "001011001011000001110": "Mi Ri Ui R Ui Ri U U R Ui M",  # Case 12
    "110000100111010000011": "f R U R R Ui Ri U R Ui fi",  # Case 13
    "011100000111000010110": "Ri F R U Ri Fi R F Ui Fi",  # Case 14
    "110000010111010010010": "ri Ui r Ri Ui R U ri U r",  # Case 15
    "010100100111000001110": "r U ri R U Ri Ui r Ui ri",  # Case 16
    "011010001010110010010": "l Ui li f R R B Ri U Ri Ui fi",  # Case 17
    "010010101010100000111": "r U Ri U R Ui Ui ri ri Ui R Ui Ri U U r",  # Case 18
    "010010101010110001010": "ri R U R U Ri Ui r Ri Ri F R Fi",  # Case 19
    "010010101010101010010": "r U Ri Ui Mi Mi U R Ui Ri Ui Mi",  # Case 20
    "101001000111000100101": "R Ui Ui Ri Ui R U Ri Ui R Ui Ri",  # Case 21
    "001101000111010100001": "R Ui Ui Ri Ri Ui R R Ui Ri Ri Ui Ui R",  # Case 22
    "101001000111001110000": "R R Di R Ui Ui Ri D R Ui Ui R",  # Case 23
    "100001100111000110100": "r U Ri Ui ri F R Fi",  # Case 24
    "000101100111001100001": "Fi r U Ri Ui ri F R",  # Case 25
    "000101100111000101100": "R Ui Ui Ri Ui R Ui Ri",  # Case 26
    "100001010111001100001": "R U Ri U R Ui Ui Ri",  # Case 27
    "000011100110101010010": "r U Ri Ui ri R U R Ui Ri",  # Case 28
    "100001100110100010110": "R U Ri Ui R Ui Ri Fi Ui F R U Ri",  # Case 29
    "010010101011010101000": "f R U R R Ui Ri U R R Ui Ri fi",  # Case 30
    "011010000110101100001": "ri Fi U F r Ui ri Ui r",  # Case 31
    "110000101011000110100": "R U Bi Ui Ri U R B Ri",  # Case 32
    "110000100111000010110": "R U Ri Ui Ri F R Fi",  # Case 33
    "010100010111001010010": "R U R R Ui Ri F R U R Ui Fi",  # Case 34
    "010010011011000110100": "R Ui Ui Ri Ri F R Fi R Ui Ui Ri",  # Case 35
    "010010010110100110100": "Ri Ui R Ui Ri U R U R Bi Ri B",  # Case 36   #Last four moves edited by me
    "000011010110100010110": "F R Ui Ri Ui R U Ri Fi",  # Case 37
    "100001100110101001010": "R U Ri U R Ui Ri Ui Ri F R Fi",  # Case 38
    "010100100111001000011": "R U Ri Fi Ui F U R U U Ri",  # Case 39
    "011010000111010010010": "Ri F R U Ri Ui Fi U R",  # Case 40
    "101001000110101010010": "R U Ri U R Ui Ui Ri F R U Ri Ui Fi",  # Case 41
    "010010100110100100101": "Ri Ui R Ui Ri U U R F R U Ri Ui Fi",  # Case 42
    "010010010110101101000": "Bi Ui Ri U R B",  # Case 43
    "010100101011010110000": "f R U Ri Ui fi",  # Case 44
    "010100100111010010010": "F R U Ri Ui Fi",  # Case 45
    "000011011010101101000": "Ri Ui Ri F R Fi U R",  # Case 46
    "100001011011000001110": "bi Ui Ri U R Ui Ri U R b",  # Case 47
    "001101000110110000011": "F R U Ri Ui R U Ri Ui Fi",  # Case 48
    "110000010110100101100": "R Bi Ri Ri F R R B Ri Ri Fi R",  # Case 49
    "011100001011010100001": "ri U r r Ui ri ri Ui r r U ri",  # Case 50
    "011100000111010000011": "f R U Ri Ui R U Ri Ui fi",  # Case 51
    "001101001010110100001": "Ri Fi Ui F Ui R U Ri U R",  # Case 52
    "111000000110100100101": "ri U U R U Ri Ui R U Ri U r",  # Case 53
    "101001000110100000111": "r Ui Ui Ri Ui R U Ri Ui R Ui ri",  # Case 54
    "111000000111000000111": "r Ui Ui Ri Ui ri R R U Ri Ui r Ui ri",  # Case 55
    "010100010111010001010": "r U ri U R Ui Ri U R Ui Ri r Ui ri",  # Case 56
    "010010100111001010010": "R U Ri Ui Mi U R Ui ri"  # Case 57
}

# Dictionary containing all PLL cases and their algorithms
PLL_ALGORITHMS = {
    # "<PLL Configuration>": "<Corresponding Algorithm>"
    "------------": "",  # Case 00: PLL skip
    "-----fl---r-": "R Ui R U R U R Ui Ri Ui Ri Ri",  # Case 01
    "-----rf---l-": "R R U R U Ri Ui Ri Ui Ri U Ri",  # Case 02
    "-f---rl---b-": "Mi Mi U Mi Mi U U Mi Mi U Mi Mi",  # Case 03
    "-r---fb---l-": "Mi U Mi Mi U Mi Mi U Mi U U Mi Mi Ui",  # Case 04
    "--r-f--rfb-l": "xi R R D D Ri Ui R D D Ri U Ri",  # Case 05
    "--f-l--fbr-r": "xi R Ui R D D Ri U R D D Ri Ri",  # Case 06
    "l-rff--bbl-r": "xi R Ui Ri D R U Ri Di R U Ri D R Ui Ri Di",  # Case 07
    "--r-frl-b--r": "R U Ri Ui Ri F R R Ui Ri Ui R U Ri Fi",  # Case 08
    "-fr-f---b-br": "Ri Ui Fi R U Ri Ui Ri F R R Ui Ri Ui R U Ri U R",  # Case 09
    "fr-r--b-l--b": "Ri U Ri di Ri Fi R R Ui Ri U Ri F R F",  # Case 10
    "fl-r-b--l--b": "F R Ui Ri Ui R U Ri Fi R U Ri Ui Ri F R Fi",  # Case 11
    "------fffrrl": "z Ui R Di R R U Ri Ui R R U D Ri",  # Case 12
    "--r-f-f-b-rr": "R U Ri Fi R U Ri Ui Ri F R R Ui Ri Ui",  # Case 13
    "r-lbb-f---r-": "Ri U U R Ui Ui Ri F R U Ri Ui Ri Fi R R Ui",  # Case 14
    "-lr-fb--b--r": "R Ui Ri Ui R U R D Ri Ui R Di Ri U U Ri Ui",  # Case 15
    "l--f-rfflrlb": "Ri Ri ui R Ui R U Ri u R R f Ri fi",  # Case 16
    "rlfblf-b-lb-": "R U Ri yi R R ui R Ui Ri U Ri u R R",  # Case 17
    "rlfblrbb-l--": "R R u Ri U Ri Ui R ui Ri Ri Fi U F",  # Case 18
    "lf-f-b-flrlb": "Ri di F R R u Ri U R Ui R ui Ri Ri",  # Case 19
    "f--r-rl-l--b": "Ri U R Ui Ri Fi Ui F R U Ri F Ri Fi R Ui R",  # Case 20
    "--f-lrlr-b--": "R U Ri U R U Ri Fi R U Ri Ui Ri F R R Ui Ri U U R Ui Ri"  # Case 21
}

# 150 randomly generated turn sequences for scrambling cubes
SAMPLE_SCRAMBLES = """Fi U B Di F L D B D Li U Bi U Fi Bi Ri B R F L U D B F Ri
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
