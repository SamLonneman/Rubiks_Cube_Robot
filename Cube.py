from copy import deepcopy as deep_copy
from Helpers import create_cubestring


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

    def cubestring(self):
        return create_cubestring(str(self))

    # Performs series of turns from a string. Ex: "R Li Di U B"
    def move(self, sequence, count_moves=True):
        for turn in sequence.split():
            getattr(self, turn)(count_moves)

    # The following 12 functions each represent a different turn
    def F(self, count_moves=True):
        self.solution_sequence += "F "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            if p.xpos == 1:
                p.ypos, p.zpos = p.zpos, -p.ypos
                p.ycol, p.zcol = p.zcol, p.ycol

    def Fi(self, count_moves=True):
        self.solution_sequence += "Fi "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            if p.xpos == 1:
                p.ypos, p.zpos = -p.zpos, p.ypos
                p.ycol, p.zcol = p.zcol, p.ycol

    def B(self, count_moves=True):
        self.solution_sequence += "B "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            if p.xpos == -1:
                p.ypos, p.zpos = -p.zpos, p.ypos
                p.ycol, p.zcol = p.zcol, p.ycol

    def Bi(self, count_moves=True):
        self.solution_sequence += "Bi "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            if p.xpos == -1:
                p.ypos, p.zpos = p.zpos, -p.ypos
                p.ycol, p.zcol = p.zcol, p.ycol

    def R(self, count_moves=True):
        self.solution_sequence += "R "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            if p.ypos == 1:
                p.xpos, p.zpos = -p.zpos, p.xpos
                p.xcol, p.zcol = p.zcol, p.xcol

    def Ri(self, count_moves=True):
        self.solution_sequence += "Ri "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            if p.ypos == 1:
                p.xpos, p.zpos = p.zpos, -p.xpos
                p.xcol, p.zcol = p.zcol, p.xcol

    def L(self, count_moves=True):
        self.solution_sequence += "L "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            if p.ypos == -1:
                p.xpos, p.zpos = p.zpos, -p.xpos
                p.xcol, p.zcol = p.zcol, p.xcol

    def Li(self, count_moves=True):
        self.solution_sequence += "Li "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            if p.ypos == -1:
                p.xpos, p.zpos = -p.zpos, p.xpos
                p.xcol, p.zcol = p.zcol, p.xcol

    def U(self, count_moves=True):
        self.solution_sequence += "U "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            if p.zpos == 1:
                p.ypos, p.xpos = -p.xpos, p.ypos
                p.ycol, p.xcol = p.xcol, p.ycol

    def Ui(self, count_moves=True):
        self.solution_sequence += "Ui "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            if p.zpos == 1:
                p.ypos, p.xpos = p.xpos, -p.ypos
                p.ycol, p.xcol = p.xcol, p.ycol

    def D(self, count_moves=True):
        self.solution_sequence += "D "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            if p.zpos == -1:
                p.ypos, p.xpos = p.xpos, -p.ypos
                p.ycol, p.xcol = p.xcol, p.ycol

    def Di(self, count_moves=True):
        self.solution_sequence += "Di "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            if p.zpos == -1:
                p.ypos, p.xpos = -p.xpos, p.ypos
                p.ycol, p.xcol = p.xcol, p.ycol

    def x(self, count_moves=True):
        self.solution_sequence += "x "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            p.xpos, p.zpos = -p.zpos, p.xpos
            p.xcol, p.zcol = p.zcol, p.xcol

    def xi(self, count_moves=True):
        self.solution_sequence += "xi "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            p.xpos, p.zpos = p.zpos, -p.xpos
            p.xcol, p.zcol = p.zcol, p.xcol

    def y(self, count_moves=True):
        self.solution_sequence += "y "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            p.ypos, p.xpos = -p.xpos, p.ypos
            p.ycol, p.xcol = p.xcol, p.ycol

    def yi(self, count_moves=True):
        self.solution_sequence += "yi "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            p.ypos, p.xpos = p.xpos, -p.ypos
            p.ycol, p.xcol = p.xcol, p.ycol

    def z(self, count_moves=True):
        self.solution_sequence += "z "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            p.ypos, p.zpos = p.zpos, -p.ypos
            p.ycol, p.zcol = p.zcol, p.ycol

    def zi(self, count_moves=True):
        self.solution_sequence += "zi "
        if count_moves:
            self.move_count += 1
        for p in self.pieces:
            p.ypos, p.zpos = -p.zpos, p.ypos
            p.ycol, p.zcol = p.zcol, p.ycol

    def solve(self):
        self.cross()
        self.f2l()
        # self.oll()
        # self.pll()

    def solve_color_agnostically(self):
        scrambled_cube = deep_copy(self)
        self.solve()
        for orientation in "x", "x x", "xi", "y xi", "yi xi":
            new_cube = deep_copy(scrambled_cube)
            new_cube.move(orientation, False)
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
            self.y(False)

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
                self.yi(False)
                continue

            # If at least one member of the pair is tied up somewhere else, turn cube and continue
            if edge.zpos == 0 and edge.pos() != (1, 1, 0) or corner.zpos == -1 and corner.pos() != (1, 1, -1):
                unavailable_pairs.add((corner, edge))
                if len(unavailable_pairs) >= 4:
                    self.move("R U Ri")
                self.yi(False)
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
                        self.move("Ri Fi R U R Ui Ri F")
                        self.move("yi")
                # If the corner is white side front
                elif corner.xcol == bottom_color:
                    # Case 04
                    if edge.pos() == (1, 1, 0) and edge.xcol == front_color:
                        self.move("R U Ri Ui R U U Ri Ui R U Ri")
                        self.move("yi")
                    # Case 05
                    elif edge.pos() == (1, 1, 0) and edge.ycol == front_color:
                        self.move("R F U R Ui Ri Fi Ui Ri")
                        self.move("yi")
                    # Case 06
                    elif edge.pos() == (1, 0, 1) and edge.xcol == front_color:
                        self.move("yi Ri Ui R U Ri Ui R")
                    # Case 07
                    elif edge.pos() == (0, 1, 1) and edge.ycol == right_color:
                        self.move("R Ui Ri U R Ui Ri")
                        self.move("yi")
                # If the corner is white side right
                elif corner.ycol == bottom_color:
                    # Case 08
                    if edge.pos() == (1, 1, 0) and edge.xcol == front_color:
                        self.move("R Ui Ri U R Ui Ui Ri U R Ui Ri")
                        self.move("yi")
                    # Case 09
                    elif edge.pos() == (1, 1, 0) and edge.ycol == front_color:
                        self.move("R U F R U Ri Ui Fi Ri")
                        self.move("yi")
                    # Case 10
                    elif edge.pos() == (1, 0, 1) and edge.xcol == front_color:
                        self.move("yi Ri U R Ui Ri U R")
                    # Case 11
                    elif edge.pos() == (0, 1, 1) and edge.ycol == right_color:
                        self.move("R U Ri Ui R U Ri")
                        self.move("yi")
            # If corner is in front-right-top corner
            elif corner.pos() == (1, 1, 1):
                # If the corner is white side up
                if corner.zcol == bottom_color:
                    # Case 12
                    if edge.pos() == (1, 1, 0) and edge.xcol == front_color:
                        self.move("R U Ri Ui R U Ri Ui R U Ri")
                        self.move("yi")
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
                        self.move("F U R Ui Ri Fi R Ui Ri")
                        self.move("yi")
                    # Case 18
                    elif edge.pos() == (1, 0, 1) and edge.xcol == right_color:
                        self.move("U R Ui Ri Ui R Ui Ri U R Ui Ri")
                        self.move("yi")
                    # Case 19
                    elif edge.pos() == (0, -1, 1) and edge.ycol == right_color:
                        self.move("R Ui Ri U U R U Ri")
                        self.move("yi")
                    # Case 20
                    elif edge.pos() == (-1, 0, 1) and edge.xcol == right_color:
                        self.move("U R Ui Ui Ri U R Ui Ri")
                        self.move("yi")
                    # Case 21
                    elif edge.pos() == (0, 1, 1) and edge.ycol == right_color:
                        self.move("R Ui Ui Ri Ui R U Ri")
                        self.move("yi")
                # If corner is white side front
                elif corner.xcol == bottom_color:
                    # Case 22
                    if edge.pos() == (1, 1, 0) and edge.xcol == front_color:
                        self.move("Ui R Ui Ri U U R Ui Ri")
                        self.move("yi")
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
                        self.move("Ui R Ui Ui Ri U U R Ui Ri")
                        self.move("yi")
                    # Case 30
                    elif edge.pos() == (-1, 0, 1) and edge.xcol == right_color:
                        self.move("Ui R U Ri Ui R Ui Ui Ri")
                        self.move("yi")
                    # Case 31
                    elif edge.pos() == (0, 1, 1) and edge.ycol == right_color:
                        self.move("U R Ui Ri")
                        self.move("yi")
                # If corner is white side right
                elif corner.ycol == bottom_color:
                    # Case 32
                    if edge.pos() == (1, 1, 0) and edge.xcol == front_color:
                        self.move("Ui R Ui Ui Ri U R U Ri")
                        self.move("yi")
                    # Case 33
                    elif edge.pos() == (1, 1, 0) and edge.ycol == front_color:
                        self.move("yi U Ri Ui R y Ui R U Ri")  # y Ui == di
                        self.move("yi")
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
                        self.move("R Ui Ri U R Ui Ri U U R Ui Ri")
                        self.move("yi")
                    # Case 39
                    elif edge.pos() == (0, -1, 1) and edge.ycol == right_color:
                        self.move("Ui R U Ri U R U Ri")
                        self.move("yi")
                    # Case 40
                    elif edge.pos() == (-1, 0, 1) and edge.xcol == right_color:
                        self.move("R U Ri")
                        self.move("yi")
                    # Case 41
                    elif edge.pos() == (0, 1, 1) and edge.ycol == right_color:
                        self.move("Ui R Ui Ri U R U Ri")
                        self.move("yi")

            # Now that a pair has been placed, add the pair to the solved set
            solved_pairs.add((corner, edge))
            unavailable_pairs.add((corner, edge))

    def oll(self):
        return

    def pll(self):
        return
