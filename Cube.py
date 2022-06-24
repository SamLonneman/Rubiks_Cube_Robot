from copy import deepcopy as deep_copy

from constants import create_cubestring, F2L_ALGORITHMS, OLL_ALGORITHMS, PLL_ALGORITHMS, SOLVED


class Piece:

    def __init__(self, xpos, ypos, zpos, xcol, ycol, zcol):
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.xcol = xcol
        self.ycol = ycol
        self.zcol = zcol

    def __repr__(self):
        return "[{}, {}, {}] [{}, {}, {}]".format(self.xpos, self.ypos, self.zpos, self.xcol, self.ycol, self.zcol)

    def pos(self):
        return self.xpos, self.ypos, self.zpos

    def col(self):
        return {self.xcol, self.ycol, self.zcol}


class Cube:

    # Constructs a cube from a cubestring
    def __init__(self, cstr):

        # A cube has two member variables
        self.solution_sequence = str()
        self.pieces = set()

        # Initialize piece set
        self.pieces.add(Piece(-1, -1, 1, cstr[38], cstr[9], cstr[0]))
        self.pieces.add(Piece(-1, 0, 1, cstr[37], None, cstr[1]))
        self.pieces.add(Piece(-1, 1, 1, cstr[36], cstr[29], cstr[2]))
        self.pieces.add(Piece(0, -1, 1, None, cstr[10], cstr[3]))
        self.pieces.add(Piece(0, 0, 1, None, None, cstr[4]))
        self.pieces.add(Piece(0, 1, 1, None, cstr[28], cstr[5]))
        self.pieces.add(Piece(1, -1, 1, cstr[18], cstr[11], cstr[6]))
        self.pieces.add(Piece(1, 0, 1, cstr[19], None, cstr[7]))
        self.pieces.add(Piece(1, 1, 1, cstr[20], cstr[27], cstr[8]))
        self.pieces.add(Piece(-1, -1, 0, cstr[41], cstr[12], None))
        self.pieces.add(Piece(-1, 0, 0, cstr[40], None, None))
        self.pieces.add(Piece(-1, 1, 0, cstr[39], cstr[32], None))
        self.pieces.add(Piece(0, -1, 0, None, cstr[13], None))
        self.pieces.add(Piece(0, 0, 0, None, None, None))
        self.pieces.add(Piece(0, 1, 0, None, cstr[31], None))
        self.pieces.add(Piece(1, -1, 0, cstr[21], cstr[14], None))
        self.pieces.add(Piece(1, 0, 0, cstr[22], None, None))
        self.pieces.add(Piece(1, 1, 0, cstr[23], cstr[30], None))
        self.pieces.add(Piece(-1, -1, -1, cstr[44], cstr[15], cstr[51]))
        self.pieces.add(Piece(-1, 0, -1, cstr[43], None, cstr[52]))
        self.pieces.add(Piece(-1, 1, -1, cstr[42], cstr[35], cstr[53]))
        self.pieces.add(Piece(0, -1, -1, None, cstr[16], cstr[48]))
        self.pieces.add(Piece(0, 0, -1, None, None, cstr[49]))
        self.pieces.add(Piece(0, 1, -1, None, cstr[34], cstr[50]))
        self.pieces.add(Piece(1, -1, -1, cstr[24], cstr[17], cstr[45]))
        self.pieces.add(Piece(1, 0, -1, cstr[25], None, cstr[46]))
        self.pieces.add(Piece(1, 1, -1, cstr[26], cstr[33], cstr[47]))

    # Returns a piece given a position
    def find_by_pos(self, *pos):
        for piece in self.pieces:
            if pos == piece.pos():
                return piece

    # Returns an piece given a color set
    def find_by_col(self, *col):
        for piece in self.pieces:
            if {*col} == piece.col():
                return piece

    # Creates readable printout from Piece objects
    def __repr__(self):
        result = str()
        for x in -1, 0, 1:
            result += "    "
            result += self.find_by_pos(x, -1, 1).zcol
            result += self.find_by_pos(x, 0, 1).zcol
            result += self.find_by_pos(x, 1, 1).zcol
            result += "\n"
        for z in 1, 0, -1:
            result += self.find_by_pos(-1, -1, z).ycol
            result += self.find_by_pos(0, -1, z).ycol
            result += self.find_by_pos(1, -1, z).ycol
            result += " "
            result += self.find_by_pos(1, -1, z).xcol
            result += self.find_by_pos(1, 0, z).xcol
            result += self.find_by_pos(1, 1, z).xcol
            result += " "
            result += self.find_by_pos(1, 1, z).ycol
            result += self.find_by_pos(0, 1, z).ycol
            result += self.find_by_pos(-1, 1, z).ycol
            result += " "
            result += self.find_by_pos(-1, 1, z).xcol
            result += self.find_by_pos(-1, 0, z).xcol
            result += self.find_by_pos(-1, -1, z).xcol
            result += "\n"
        for x in 1, 0, -1:
            result += "    "
            result += self.find_by_pos(x, -1, -1).zcol
            result += self.find_by_pos(x, 0, -1).zcol
            result += self.find_by_pos(x, 1, -1).zcol
            result += "\n"
        return result

    # Returns the cubestring of the cube's current state
    def generate_cubestring(self):
        return create_cubestring(str(self))

    # Regular turns
    def F(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "F "
        for p in self.pieces:
            if p.xpos == 1:
                p.ypos, p.zpos = p.zpos, -p.ypos
                p.ycol, p.zcol = p.zcol, p.ycol

    def Fi(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "Fi "
        for p in self.pieces:
            if p.xpos == 1:
                p.ypos, p.zpos = -p.zpos, p.ypos
                p.ycol, p.zcol = p.zcol, p.ycol

    def B(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "B "
        for p in self.pieces:
            if p.xpos == -1:
                p.ypos, p.zpos = -p.zpos, p.ypos
                p.ycol, p.zcol = p.zcol, p.ycol

    def Bi(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "Bi "
        for p in self.pieces:
            if p.xpos == -1:
                p.ypos, p.zpos = p.zpos, -p.ypos
                p.ycol, p.zcol = p.zcol, p.ycol

    def R(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "R "
        for p in self.pieces:
            if p.ypos == 1:
                p.xpos, p.zpos = -p.zpos, p.xpos
                p.xcol, p.zcol = p.zcol, p.xcol

    def Ri(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "Ri "
        for p in self.pieces:
            if p.ypos == 1:
                p.xpos, p.zpos = p.zpos, -p.xpos
                p.xcol, p.zcol = p.zcol, p.xcol

    def L(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "L "
        for p in self.pieces:
            if p.ypos == -1:
                p.xpos, p.zpos = p.zpos, -p.xpos
                p.xcol, p.zcol = p.zcol, p.xcol

    def Li(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "Li "
        for p in self.pieces:
            if p.ypos == -1:
                p.xpos, p.zpos = -p.zpos, p.xpos
                p.xcol, p.zcol = p.zcol, p.xcol

    def U(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "U "
        for p in self.pieces:
            if p.zpos == 1:
                p.ypos, p.xpos = -p.xpos, p.ypos
                p.ycol, p.xcol = p.xcol, p.ycol

    def Ui(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "Ui "
        for p in self.pieces:
            if p.zpos == 1:
                p.ypos, p.xpos = p.xpos, -p.ypos
                p.ycol, p.xcol = p.xcol, p.ycol

    def D(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "D "
        for p in self.pieces:
            if p.zpos == -1:
                p.ypos, p.xpos = p.xpos, -p.ypos
                p.ycol, p.xcol = p.xcol, p.ycol

    def Di(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "Di "
        for p in self.pieces:
            if p.zpos == -1:
                p.ypos, p.xpos = -p.xpos, p.ypos
                p.ycol, p.xcol = p.xcol, p.ycol

    # Whole cube rotations
    def x(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "x "
        for p in self.pieces:
            p.xpos, p.zpos = -p.zpos, p.xpos
            p.xcol, p.zcol = p.zcol, p.xcol

    def xi(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "xi "
        for p in self.pieces:
            p.xpos, p.zpos = p.zpos, -p.xpos
            p.xcol, p.zcol = p.zcol, p.xcol

    def y(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "y "
        for p in self.pieces:
            p.ypos, p.xpos = -p.xpos, p.ypos
            p.ycol, p.xcol = p.xcol, p.ycol

    def yi(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "yi "
        for p in self.pieces:
            p.ypos, p.xpos = p.xpos, -p.ypos
            p.ycol, p.xcol = p.xcol, p.ycol

    def z(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "z "
        for p in self.pieces:
            p.ypos, p.zpos = p.zpos, -p.ypos
            p.ycol, p.zcol = p.zcol, p.ycol

    def zi(self, include_in_solution=True):
        if include_in_solution:
            self.solution_sequence += "zi "
        for p in self.pieces:
            p.ypos, p.zpos = -p.zpos, p.ypos
            p.ycol, p.zcol = p.zcol, p.ycol

    # Compound turns
    def f(self, include_in_solution=True):
        self.move("z B", include_in_solution)

    def fi(self, include_in_solution=True):
        self.move("Bi zi", include_in_solution)

    def b(self, include_in_solution=True):
        self.move("zi F", include_in_solution)

    def bi(self, include_in_solution=True):
        self.move("Fi z", include_in_solution)

    def r(self, include_in_solution=True):
        self.move("x L", include_in_solution)

    def ri(self, include_in_solution=True):
        self.move("Li xi", include_in_solution)

    def l(self, include_in_solution=True):
        self.move("xi R", include_in_solution)

    def li(self, include_in_solution=True):
        self.move("Ri x", include_in_solution)

    def u(self, include_in_solution=True):
        self.move("y D", include_in_solution)

    def ui(self, include_in_solution=True):
        self.move("Di yi", include_in_solution)

    def d(self, include_in_solution=True):
        self.move("yi U", include_in_solution)

    def di(self, include_in_solution=True):
        self.move("Ui y", include_in_solution)

    def M(self, include_in_solution=True):
        self.move("xi R Li", include_in_solution)

    def Mi(self, include_in_solution=True):
        self.move("L Ri x", include_in_solution)

    def E(self, include_in_solution=True):
        self.move("yi Di U", include_in_solution)

    def Ei(self, include_in_solution=True):
        self.move("Ui D y", include_in_solution)

    def S(self, include_in_solution=True):
        self.move("z Fi B", include_in_solution)

    def Si(self, include_in_solution=True):
        self.move("Bi F zi", include_in_solution)

    # Performs series of turns from a string. Ex: "R Bi x zi f L l"
    def move(self, sequence, count_moves=True):
        for turn in sequence.split():
            getattr(self, turn)(count_moves)

    def cfop(self):
        self.cross()  # 8.05  moves on average
        self.f2l()    # 33.98 moves on average
        self.oll()    # 10.25 moves on average
        self.pll()    # 15.29 moves on average

    def generate_solution_sequence(self):
        scrambled_cube = deep_copy(self)
        self.cfop()
        self.simplify_sequence()
        for orienting_sequence in "x", "x x", "xi", "y xi", "yi xi":
            new_cube = deep_copy(scrambled_cube)
            new_cube.move(orienting_sequence)
            new_cube.cfop()
            new_cube.simplify_sequence()
            if len(new_cube.solution_sequence.split()) < len(self.solution_sequence.split()):
                self.__dict__ = new_cube.__dict__
        return self.solution_sequence

    # Solve a cross on the bottom
    def cross(self):
        bottom_color = self.find_by_pos(0, 0, -1).zcol
        for side in 1, 2, 3, 4:
            front_color = self.find_by_pos(1, 0, 0).xcol
            piece = self.find_by_col(front_color, bottom_color, None)

            # If the piece is properly oriented on top, solve it
            if piece.zpos == 1 and piece.zcol == bottom_color:
                if piece.xpos == -1:
                    self.move("Ui Ui")
                elif piece.ypos == -1:
                    self.Ui()
                elif piece.ypos == 1:
                    self.U()
                self.move("F F")

            # If the piece is improperly oriented on top, solve it
            elif piece.zpos == 1 and piece.zcol == front_color:
                if piece.xpos == -1:
                    self.U()
                if piece.xpos == 1:
                    self.Ui()
                if piece.ypos == -1:
                    self.move("L Fi Li") if side != 1 else self.move("L Fi")
                if piece.ypos == 1:
                    self.move("Ri F R") if side == 4 else self.move("Ri F")

            # If the piece is on the bottom and not solved, move it into the middle layer
            elif piece.zpos == -1:
                if side == 1 and piece.zcol == bottom_color:
                    if piece.xpos == -1:
                        self.move("D D")
                    elif piece.ypos == -1:
                        self.D()
                    elif piece.ypos == 1:
                        self.Di()
                elif piece.ypos == -1:
                    self.Li()
                elif piece.ypos == 1:
                    self.R()
                elif piece.xpos == -1:
                    self.B()
                elif piece.xpos == 1 and piece.xcol == bottom_color:
                    self.F()

            # If the piece is in the middle layer, solve it
            if piece.zpos == 0:
                if piece.xpos == 1 and piece.ypos == 1:
                    if piece.xcol == front_color:
                        self.F()
                    else:
                        self.move("D Ri Di") if side != 1 else self.move("Ri Di")
                if piece.xpos == 1 and piece.ypos == -1:
                    if piece.xcol == front_color:
                        self.Fi()
                    else:
                        self.move("Di L D") if side != 1 else self.move("L D")
                if piece.xpos == -1 and piece.ypos == 1:
                    if piece.xcol == front_color:
                        self.move("D D Bi Di Di") if side == 4 else self.move("R R F")
                    else:
                        self.move("D R Di") if side != 1 else self.move("R Di")
                if piece.xpos == -1 and piece.ypos == -1:
                    if piece.xcol == front_color:
                        self.move("Di Di B D D") if side != 1 else self.move("L L Fi")
                    else:
                        self.move("Di Li D") if side != 1 else self.move("Li D")

            # Rotate the cube to the next side
            self.y()

    # Solve the first two layers
    def f2l(self):

        # Set up variables
        solved_pairs = set()
        unavailable_pairs = set()
        bottom_color = self.find_by_pos(0, 0, -1).zcol

        # Repeat until all four pairs are solved
        while len(solved_pairs) < 4:

            # More setting up variables
            front_color = self.find_by_pos(1, 0, 0).xcol
            right_color = self.find_by_pos(0, 1, 0).ycol
            corner = self.find_by_col(front_color, right_color, bottom_color)
            edge = self.find_by_col(front_color, right_color, None)

            # If the pair is already solved, note this, turn cube, and continue
            if corner.pos() == (1, 1, -1) and corner.zcol == bottom_color and \
                    edge.pos() == (1, 1, 0) and edge.xcol == front_color:
                solved_pairs.add((corner, edge))
                unavailable_pairs.add((corner, edge))
                self.yi()
                continue

            # If at least one member of the pair is tied up somewhere else, turn cube and continue
            if edge.zpos == 0 and edge.pos() != (1, 1, 0) or corner.zpos == -1 and corner.pos() != (1, 1, -1):
                unavailable_pairs.add((corner, edge))
                if len(unavailable_pairs) >= 4:
                    self.move("R U Ri")
                self.yi()
                continue

            # Orient the top face appropriately
            if corner.zpos == -1 and edge.zpos == 1:
                if edge.zcol == right_color:
                    if edge.pos() == (0, -1, 1):
                        self.Ui()
                    elif edge.pos() == (0, 1, 1):
                        self.U()
                    elif edge.pos() == (-1, 0, 1):
                        self.move("U U")
                elif edge.zcol == front_color:
                    if edge.pos() == (1, 0, 1):
                        self.Ui()
                    elif edge.pos() == (-1, 0, 1):
                        self.U()
                    elif edge.pos() == (0, -1, 1):
                        self.move("U U")
            elif corner.zpos == 1:
                if corner.pos() == (1, -1, 1):
                    self.Ui()
                elif corner.pos() == (-1, 1, 1):
                    self.U()
                elif corner.pos() == (-1, -1, 1):
                    self.move("U U")

            # Get the current F2L configuration
            configuration = str()
            configuration += 'u' if corner.zpos == 1 else 'd'
            configuration += 'y' if right_color == corner.ycol else 'x' if right_color == corner.xcol else 'z'
            if edge.zpos == 0:
                configuration += 'm'
            elif edge.xpos == 1:
                configuration += 'f'
            elif edge.ypos == -1:
                configuration += 'l'
            elif edge.xpos == -1:
                configuration += 'b'
            else:
                configuration += 'r'
            configuration += '0' if edge.zcol == right_color or edge.zpos == 0 and edge.xcol == right_color else '1'

            # Perform F2L algorithm for this configuration
            self.move(F2L_ALGORITHMS[configuration])

            # Now that a pair has been placed, add the pair to the solved set
            solved_pairs.add((corner, edge))
            unavailable_pairs.add((corner, edge))

    # Orient the last layer
    def oll(self):

        while True:
            # Determine current OLL configuration
            configuration = str()
            cubestring = self.generate_cubestring()
            top_color = self.find_by_pos(0, 0, 1).zcol
            for i in 38, 37, 36, 9, 0, 1, 2, 29, 10, 3, 4, 5, 28, 11, 6, 7, 8, 27, 18, 19, 20:
                configuration += '1' if cubestring[i] == top_color else '0'

            # If a valid configuration, perform algorithm and break
            if configuration in OLL_ALGORITHMS:
                self.move(OLL_ALGORITHMS[configuration])
                break

            # otherwise, turn the cube and continue
            else:
                self.yi()

    # Permute the last layer
    def pll(self):

        orientations_checked = 0
        while True:

            # Determine current PLL configuration
            configuration = str()
            cubestring = self.generate_cubestring()
            back_color = self.find_by_pos(-1, 0, 0).xcol
            front_color = self.find_by_pos(1, 0, 0).xcol
            left_color = self.find_by_pos(0, -1, 0).ycol
            right_color = self.find_by_pos(0, 1, 0).ycol
            for i in 38, 37, 36, 9, 29, 10, 28, 11, 27, 18, 19, 20:
                if cubestring[i] == back_color:
                    configuration += "-" if i in (36, 37, 38) else "b"
                elif cubestring[i] == left_color:
                    configuration += "-" if i in (9, 10, 11) else "l"
                elif cubestring[i] == front_color:
                    configuration += "-" if i in (18, 19, 20) else "f"
                elif cubestring[i] == right_color:
                    configuration += "-" if i in (27, 28, 29) else "r"

            # If a valid configuration, perform algorithm and break
            if configuration in PLL_ALGORITHMS:
                self.move(PLL_ALGORITHMS[configuration])
                break

            # otherwise, rotate whole cube and continue
            else:
                self.y()

                # If all orientations have been checked, make a U turn
                orientations_checked += 1
                if orientations_checked == 4:
                    self.U()
                    orientations_checked = 0

    # Simplify the sequence, removing full cube rotations, triple turns, and trivial undoings
    def simplify_sequence(self, half_turn_metric=True):
        # Remove any full cube rotations and adjust all other moves accordingly
        defaults = {
            'y': "U",
            'r': "L",
            'g': "F",
            'o': "R",
            'b': "B",
            'w': "D"
        }
        simplified_sequence = ""
        cube = Cube(SOLVED)
        for turn in self.solution_sequence.split():
            if 'y' in turn or 'x' in turn or 'z' in turn:
                cube.move(turn)
            else:
                if 'U' in turn:
                    simplified_sequence += defaults[cube.find_by_pos(0, 0, 1).zcol]
                elif 'L' in turn:
                    simplified_sequence += defaults[cube.find_by_pos(0, -1, 0).ycol]
                elif 'F' in turn:
                    simplified_sequence += defaults[cube.find_by_pos(1, 0, 1).xcol]
                elif 'R' in turn:
                    simplified_sequence += defaults[cube.find_by_pos(0, 1, 0).ycol]
                elif 'B' in turn:
                    simplified_sequence += defaults[cube.find_by_pos(-1, 0, 0).xcol]
                elif 'D' in turn:
                    simplified_sequence += defaults[cube.find_by_pos(0, 0, -1).zcol]
                if 'i' in turn:
                    simplified_sequence += 'i'
                simplified_sequence += ' '
        simplified_sequence = simplified_sequence[:-1]
        self.solution_sequence = simplified_sequence

        # # BROKEN BROKEN BROKEN (probably not worth fixing, only improves sequence by 3 on avg)
        # # Repeatedly perform the two following transformations until they have no effect
        # edit_made = True
        # while edit_made:
        #     edit_made = False
        #
        #     # Replace triple turns with single inverse turns
        #     simplified_sequence = ""
        #     turn_list = self.solution_sequence.split()
        #     i = 0
        #     while i < len(turn_list):
        #         if i < len(turn_list) - 2 and turn_list[i] == turn_list[i + 1] == turn_list[i + 2]:
        #             simplified_sequence += turn_list[i] + "i "
        #             edit_made = True
        #             i += 3
        #         else:
        #             simplified_sequence += turn_list[i] + ' '
        #             i += 1
        #     self.solution_sequence = simplified_sequence[:-1]
        #
        #     # Delete useless trivial "undoing" moves such as "Ri R" or "F Fi"
        #     simplified_sequence = ""
        #     turn_list = self.solution_sequence.split()
        #     i = 0
        #     while i < len(turn_list):
        #         if i < len(turn_list) - 1 and (
        #                 turn_list[i] == turn_list[i + 1] + 'i' or turn_list[i] + 'i' == turn_list[i + 1]):
        #             edit_made = True
        #             i += 2
        #         else:
        #             simplified_sequence += turn_list[i] + ' '
        #             i += 1
        #     self.solution_sequence = simplified_sequence[:-1]

        # Remove any need for U or D turns
        moves = {
            (0, 0, 1): 'U',
            (0, -1, 0): 'L',
            (1, 0, 0): 'F',
            (0, 1, 0): 'R',
            (-1, 0, 0): 'B',
            (0, 0, -1): 'D'
        }
        defaults = {
            'U': 'y',
            'D': 'w',
            'F': 'g',
            'B': 'b',
            'R': 'o',
            'L': 'r',
        }
        cube = Cube(SOLVED)
        simplified_sequence = ""
        for turn in self.solution_sequence.split():
            move = moves[cube.find_by_col(defaults[turn[0]], None, None).pos()]
            if 'U' in move:
                simplified_sequence += "xi F"
                cube.move("xi")
            elif 'D' in move:
                simplified_sequence += "x F"
                cube.move("x")
            else:
                simplified_sequence += move
            if 'i' in turn:
                simplified_sequence += 'i'
            simplified_sequence += ' '
        simplified_sequence = simplified_sequence[:-1]
        self.solution_sequence = simplified_sequence

        # Combine duplicates into double turns if half_turn_metric is true
        if half_turn_metric:
            simplified_sequence = ""
            turn_list = self.solution_sequence.split()
            i = 0
            while i < len(turn_list):
                if i < len(turn_list) - 1 and turn_list[i] == turn_list[i + 1]:
                    simplified_sequence += turn_list[i][0] + "2 "
                    i += 2
                else:
                    simplified_sequence += turn_list[i] + ' '
                    i += 1
            self.solution_sequence = simplified_sequence[:-1]
