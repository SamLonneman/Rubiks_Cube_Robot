from copy import deepcopy as deep_copy
from Helpers import create_cubestring, OLL_ALGORITHMS, PLL_ALGORITHMS


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

        # A cube has three member variables
        self.move_count = 0
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
    def cubestring(self):
        return create_cubestring(str(self))

    # Regular turns
    def F(self, include_in_solution=True):
        if include_in_solution:
            self.move_count += 1
            self.solution_sequence += "F "
        for p in self.pieces:
            if p.xpos == 1:
                p.ypos, p.zpos = p.zpos, -p.ypos
                p.ycol, p.zcol = p.zcol, p.ycol

    def Fi(self, include_in_solution=True):
        if include_in_solution:
            self.move_count += 1
            self.solution_sequence += "Fi "
        for p in self.pieces:
            if p.xpos == 1:
                p.ypos, p.zpos = -p.zpos, p.ypos
                p.ycol, p.zcol = p.zcol, p.ycol

    def B(self, include_in_solution=True):
        if include_in_solution:
            self.move_count += 1
            self.solution_sequence += "B "
        for p in self.pieces:
            if p.xpos == -1:
                p.ypos, p.zpos = -p.zpos, p.ypos
                p.ycol, p.zcol = p.zcol, p.ycol

    def Bi(self, include_in_solution=True):
        if include_in_solution:
            self.move_count += 1
            self.solution_sequence += "Bi "
        for p in self.pieces:
            if p.xpos == -1:
                p.ypos, p.zpos = p.zpos, -p.ypos
                p.ycol, p.zcol = p.zcol, p.ycol

    def R(self, include_in_solution=True):
        if include_in_solution:
            self.move_count += 1
            self.solution_sequence += "R "
        for p in self.pieces:
            if p.ypos == 1:
                p.xpos, p.zpos = -p.zpos, p.xpos
                p.xcol, p.zcol = p.zcol, p.xcol

    def Ri(self, include_in_solution=True):
        if include_in_solution:
            self.move_count += 1
            self.solution_sequence += "Ri "
        for p in self.pieces:
            if p.ypos == 1:
                p.xpos, p.zpos = p.zpos, -p.xpos
                p.xcol, p.zcol = p.zcol, p.xcol

    def L(self, include_in_solution=True):
        if include_in_solution:
            self.move_count += 1
            self.solution_sequence += "L "
        for p in self.pieces:
            if p.ypos == -1:
                p.xpos, p.zpos = p.zpos, -p.xpos
                p.xcol, p.zcol = p.zcol, p.xcol

    def Li(self, include_in_solution=True):
        if include_in_solution:
            self.move_count += 1
            self.solution_sequence += "Li "
        for p in self.pieces:
            if p.ypos == -1:
                p.xpos, p.zpos = -p.zpos, p.xpos
                p.xcol, p.zcol = p.zcol, p.xcol

    def U(self, include_in_solution=True):
        if include_in_solution:
            self.move_count += 1
            self.solution_sequence += "U "
        for p in self.pieces:
            if p.zpos == 1:
                p.ypos, p.xpos = -p.xpos, p.ypos
                p.ycol, p.xcol = p.xcol, p.ycol

    def Ui(self, include_in_solution=True):
        if include_in_solution:
            self.move_count += 1
            self.solution_sequence += "Ui "
        for p in self.pieces:
            if p.zpos == 1:
                p.ypos, p.xpos = p.xpos, -p.ypos
                p.ycol, p.xcol = p.xcol, p.ycol

    def D(self, include_in_solution=True):
        if include_in_solution:
            self.move_count += 1
            self.solution_sequence += "D "
        for p in self.pieces:
            if p.zpos == -1:
                p.ypos, p.xpos = p.xpos, -p.ypos
                p.ycol, p.xcol = p.xcol, p.ycol

    def Di(self, include_in_solution=True):
        if include_in_solution:
            self.move_count += 1
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
        self.move("y U", include_in_solution)

    def di(self, include_in_solution=True):
        self.move("Ui yi", include_in_solution)

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

    def solve(self):
        self.cross()  # 8.05  moves on average
        self.f2l()    # 33.98 moves on average
        self.oll()    # 10.25 moves on average
        self.pll()

    def solve_color_agnostically(self):
        scrambled_cube = deep_copy(self)
        self.solve()
        for orientation in "x", "x x", "xi", "y xi", "yi xi":
            new_cube = deep_copy(scrambled_cube)
            new_cube.move(orientation)
            new_cube.solve()
            if new_cube.move_count < self.move_count:
                self.__dict__ = new_cube.__dict__

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

            # If corner is in front-right-bottom corner
            if corner.pos() == (1, 1, -1):
                # If the corner is white side down
                if corner.zcol == bottom_color:
                    # Case 01
                    if edge.pos() == (1, 1, 0) and edge.ycol == front_color:
                        self.move("R Ui Ri U yi Ri U U R Ui Ui Ri U R")
                    # Case 02
                    elif edge.pos() == (1, 0, 1) and edge.xcol == front_color:
                        self.move("U R Ui Ri Ui yi Ri U R")
                    # Case 03
                    elif edge.pos() == (0, 1, 1) and edge.ycol == right_color:
                        self.move("Ri Fi R U R Ui Ri F yi")
                # If the corner is white side front
                elif corner.xcol == bottom_color:
                    # Case 04
                    if edge.pos() == (1, 1, 0) and edge.xcol == front_color:
                        self.move("R U Ri Ui R U U Ri Ui R U Ri yi")
                    # Case 05
                    elif edge.pos() == (1, 1, 0) and edge.ycol == front_color:
                        self.move("R F U R Ui Ri Fi Ui Ri yi")
                    # Case 06
                    elif edge.pos() == (1, 0, 1) and edge.xcol == front_color:
                        self.move("yi Ri Ui R U Ri Ui R")
                    # Case 07
                    elif edge.pos() == (0, 1, 1) and edge.ycol == right_color:
                        self.move("R Ui Ri U R Ui Ri yi")
                # If the corner is white side right
                elif corner.ycol == bottom_color:
                    # Case 08
                    if edge.pos() == (1, 1, 0) and edge.xcol == front_color:
                        self.move("R Ui Ri U R Ui Ui Ri U R Ui Ri yi")
                    # Case 09
                    elif edge.pos() == (1, 1, 0) and edge.ycol == front_color:
                        self.move("R U F R U Ri Ui Fi Ri yi")
                    # Case 10
                    elif edge.pos() == (1, 0, 1) and edge.xcol == front_color:
                        self.move("yi Ri U R Ui Ri U R")
                    # Case 11
                    elif edge.pos() == (0, 1, 1) and edge.ycol == right_color:
                        self.move("R U Ri Ui R U Ri yi")
            # If corner is in front-right-top corner
            elif corner.pos() == (1, 1, 1):
                # If the corner is white side up
                if corner.zcol == bottom_color:
                    # Case 12
                    if edge.pos() == (1, 1, 0) and edge.xcol == front_color:
                        self.move("R U Ri Ui R U Ri Ui R U Ri yi")
                    # Case 13
                    elif edge.pos() == (1, 1, 0) and edge.ycol == front_color:
                        self.move("R Ui Ri U yi Ri U R")
                    # Case 14
                    elif edge.pos() == (1, 0, 1) and edge.xcol == front_color:
                        self.move("yi Ri U U R U Ri Ui R")
                    # Case 15
                    elif edge.pos() == (0, -1, 1) and edge.ycol == front_color:
                        self.move("yi Ui Ri U U R Ui Ri U R")
                    # Case 16
                    elif edge.pos() == (-1, 0, 1) and edge.xcol == front_color:
                        self.move("yi Ri U R Ui Ui Ri Ui R")
                    # Case 17
                    elif edge.pos() == (0, 1, 1) and edge.ycol == front_color:
                        self.move("F U R Ui Ri Fi R Ui Ri yi")
                    # Case 18
                    elif edge.pos() == (1, 0, 1) and edge.xcol == right_color:
                        self.move("U R Ui Ri Ui R Ui Ri U R Ui Ri yi")
                    # Case 19
                    elif edge.pos() == (0, -1, 1) and edge.ycol == right_color:
                        self.move("R Ui Ri U U R U Ri yi")
                    # Case 20
                    elif edge.pos() == (-1, 0, 1) and edge.xcol == right_color:
                        self.move("U R Ui Ui Ri U R Ui Ri yi")
                    # Case 21
                    elif edge.pos() == (0, 1, 1) and edge.ycol == right_color:
                        self.move("R Ui Ui Ri Ui R U Ri yi")
                # If corner is white side front
                elif corner.xcol == bottom_color:
                    # Case 22
                    if edge.pos() == (1, 1, 0) and edge.xcol == front_color:
                        self.move("Ui R Ui Ri U U R Ui Ri yi")
                    # Case 23
                    elif edge.pos() == (1, 1, 0) and edge.ycol == front_color:
                        self.move("Ui R U Ri yi U Ri Ui R")
                    # Case 24
                    elif edge.pos() == (1, 0, 1) and edge.xcol == front_color:
                        self.move("yi U Ri U R Ui Ri Ui R")
                    # Case 25
                    elif edge.pos() == (0, -1, 1) and edge.ycol == front_color:
                        self.move("yi Ri Ui R")
                    # Case 26
                    elif edge.pos() == (-1, 0, 1) and edge.xcol == front_color:
                        self.move("yi U Ri Ui R Ui Ri Ui R")
                    # Case 27
                    elif edge.pos() == (0, 1, 1) and edge.ycol == front_color:
                        self.move("yi R Ui Ui Ri Ri Ui R R Ui Ri")
                    # Case 28 FUNKY CASE MAYBE FIX LATER
                    elif edge.pos() == (1, 0, 1) and edge.xcol == right_color:
                        self.move("xi R U x L Ui Li xi Ui Ri x")
                    # Case 29
                    elif edge.pos() == (0, -1, 1) and edge.ycol == right_color:
                        self.move("Ui R Ui Ui Ri U U R Ui Ri yi")
                    # Case 30
                    elif edge.pos() == (-1, 0, 1) and edge.xcol == right_color:
                        self.move("Ui R U Ri Ui R Ui Ui Ri yi")
                    # Case 31
                    elif edge.pos() == (0, 1, 1) and edge.ycol == right_color:
                        self.move("U R Ui Ri yi")
                # If corner is white side right
                elif corner.ycol == bottom_color:
                    # Case 32
                    if edge.pos() == (1, 1, 0) and edge.xcol == front_color:
                        self.move("Ui R Ui Ui Ri U R U Ri yi")
                    # Case 33
                    elif edge.pos() == (1, 1, 0) and edge.ycol == front_color:
                        self.move("yi U Ri Ui R y Ui R U Ri")  # y Ui ==  yidi
                    # Case 34
                    elif edge.pos() == (1, 0, 1) and edge.xcol == front_color:
                        self.move("yi Ui Ri U R")
                    # Case 35
                    elif edge.pos() == (0, -1, 1) and edge.ycol == front_color:
                        self.move("yi U Ri Ui R Ui Ui Ri U R")
                    # Case 36
                    elif edge.pos() == (-1, 0, 1) and edge.xcol == front_color:
                        self.move("yi U Ri U U R Ui Ui Ri U R")
                    # Case 37
                    elif edge.pos() == (0, 1, 1) and edge.ycol == front_color:
                        self.move("R Ui Ri U U yi Ri Ui R")
                    # Case 38
                    elif edge.pos() == (1, 0, 1) and edge.xcol == right_color:
                        self.move("R Ui Ri U R Ui Ri U U R Ui Ri yi")
                    # Case 39
                    elif edge.pos() == (0, -1, 1) and edge.ycol == right_color:
                        self.move("Ui R U Ri U R U Ri yi")
                    # Case 40
                    elif edge.pos() == (-1, 0, 1) and edge.xcol == right_color:
                        self.move("R U Ri yi")
                    # Case 41
                    elif edge.pos() == (0, 1, 1) and edge.ycol == right_color:
                        self.move("Ui R Ui Ri U R U Ri yi")

            # Now that a pair has been placed, add the pair to the solved set
            solved_pairs.add((corner, edge))
            unavailable_pairs.add((corner, edge))

    # Orient the last layer
    def oll(self):

        while True:
            # Determine current OLL configuration
            configuration = str()
            cubestring = self.cubestring()
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

    # Return the PLL configuration
    def get_pll_configuration(self):
        # Determine current PLL configuration
        configuration = str()
        cubestring = self.cubestring()
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
        return configuration

    # Permute the last layer
    def pll(self):

        orientations_checked = 0
        while True:
            # Get PLL Configuration
            configuration = self.get_pll_configuration()

            # If a valid configuration, perform algorithm and break
            if configuration in PLL_ALGORITHMS:
                self.move(PLL_ALGORITHMS[configuration])
                break

            # otherwise, turn the cube and continue
            else:
                self.y()
                orientations_checked += 1
                if orientations_checked == 4:
                    self.U()
                    orientations_checked = 0
