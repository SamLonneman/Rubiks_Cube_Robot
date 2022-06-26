from copy import deepcopy
from io import BytesIO
from os import system
from time import sleep

from PIL import Image
from RPi import GPIO
from picamera import PiCamera

from VirtualCube import VirtualCube
from Motor import Motor


class Robot:

    def __init__(self):
        self.camera = PiCamera()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.SOLVE_BUTTON = 6
        self.ABORT_BUTTON = 13
        self.ENABLE_PINS = 20, 21
        self.HOT_PIN = 26
        GPIO.setup(self.SOLVE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.ABORT_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.ENABLE_PINS, GPIO.OUT, initial=True)
        GPIO.setup(self.HOT_PIN, GPIO.OUT, initial=True)
        system("sudo sh -c \"echo none > /sys/class/leds/led1/trigger\"")
        system("sudo sh -c \"echo none > /sys/class/leds/led0/trigger\"")
        system("sudo sh -c \"echo 0 > /sys/class/leds/led1/brightness\"")
        system("sudo sh -c \"echo 1 > /sys/class/leds/led0/brightness\"")
        self.motorR1 = Motor(18, 15)
        self.motorR2 = Motor(8, 25)
        self.motorL1 = Motor(24, 23)
        self.motorL2 = Motor(1, 7)
        self.motorF1 = Motor(27, 17)
        self.motorF2 = Motor(11, 9)
        self.motorB1 = Motor(10, 22)
        self.motorB2 = Motor(5, 0)
        self.yellow = tuple()
        self.red = tuple()
        self.green = tuple()
        self.orange = tuple()
        self.blue = tuple()
        self.white = tuple()
        self.images = list()
        self.COORDINATES = [
            (941, 584),
            (858, 464),
            (766, 352),
            (1063, 496),
            (967, 375),
            (882, 263),
            (1176, 408),
            (1088, 287),
            (999, 169),
        ]
        self.c = 0

    def proceed(self):
        GPIO.output(self.ENABLE_PINS, True)
        while not GPIO.input(self.SOLVE_BUTTON) and not GPIO.input(self.ABORT_BUTTON):
            sleep(0.1)
        if GPIO.input(self.ABORT_BUTTON):
            sleep(2)
            if GPIO.input(self.ABORT_BUTTON):
                GPIO.cleanup()
                system("sudo sh -c \"echo 1 > /sys/class/leds/led1/brightness\"")
                system("sudo sh -c \"echo 0 > /sys/class/leds/led0/brightness\"")
                system("sudo shutdown -h now")
                return False
            return self.proceed()
        GPIO.output(self.ENABLE_PINS, False)
        return True

    def construct_simulation_cube(self):
        self.capture()
        self.calibrate()
        cubestring = self.construct_cubestring()
        if not self.cubestring_is_valid(cubestring):
            raise Exception(cubestring)
        virtual_cube = VirtualCube(cubestring)
        virtual_cube.move("z x x x z", False)
        return virtual_cube
    
    def cubestring_is_valid(self, cubestring):
        c = cubestring
        return c.count('y') == c.count('r') == c.count('g') == c.count('o') == c.count('b') == c.count('w')

    def capture(self):
        self.images.clear()
        self.capture_side(0)
        self.z()
        self.capture_side(3)
        self.x()
        self.capture_side(3)
        self.x()
        self.capture_side(3)
        self.x()
        self.capture_side(3)
        self.z()
        self.capture_side(1)

    def capture_side(self, num_rotations):
        self.motorL2.retract(self.motorR2)
        image1 = self.take_picture()
        self.motorL2.extend(self.motorR2)
        self.motorF2.retract(self.motorB2)
        image2 = self.take_picture()
        self.motorF2.extend(self.motorB2)
        image1[1], image1[7] = image2[1], image2[7]
        self.images.append(self.rotate_list(image1, num_rotations))

    def take_picture(self):
        stream = BytesIO()
        self.camera.capture(stream, format='jpeg')
        image = Image.open(stream).load()
        stream.close()
        return [image[coordinate] for coordinate in self.COORDINATES]

    def rotate_list(self, image, num_rotations):
        result = deepcopy(image)
        for _ in range(num_rotations):
            result[0] = image[6]
            result[1] = image[3]
            result[2] = image[0]
            result[3] = image[7]
            result[5] = image[1]
            result[6] = image[8]
            result[7] = image[5]
            result[8] = image[2]
            image = deepcopy(result)
        return result

    def calibrate(self):
        self.yellow = self.images[0][4]
        self.red = self.images[1][4]
        self.green = self.images[2][4]
        self.orange = self.images[3][4]
        self.blue = self.images[4][4]
        self.white = self.images[5][4]

    def construct_cubestring(self):
        cubestring = str()
        for image in self.images:
            for pixel in image:
                cubestring += self.pick_color(pixel)
        return cubestring

    def pick_color(self, rgb):
        differences = {
            self.rgb_diff(rgb, self.yellow): 'y',
            self.rgb_diff(rgb, self.red): 'r',
            self.rgb_diff(rgb, self.green): 'g',
            self.rgb_diff(rgb, self.orange): 'o',
            self.rgb_diff(rgb, self.blue): 'b',
            self.rgb_diff(rgb, self.white): 'w',
        }
        return differences[min(differences.keys())]

    def rgb_diff(self, rgb1, rgb2):
        difference = 0
        for i in range(3):
            difference += abs(rgb1[i] - rgb2[i])
        return difference

    def solve(self, solution_sequence):
        solution_sequence += " drop"
        for turn in solution_sequence.split():
            getattr(self, turn)()
            if GPIO.input(self.ABORT_BUTTON):
                break

    def R(self):
        self.motorR1.cw()
        self.motorR2.retract()
        self.motorR1.ccw()
        self.motorR2.extend()

    def Ri(self):
        self.motorR1.ccw()
        self.motorR2.retract()
        self.motorR1.cw()
        self.motorR2.extend()

    def R2(self):
        self.motorR1.cw()
        self.motorR1.cw()

    def L(self):
        self.motorL1.cw()
        self.motorL2.retract()
        self.motorL1.ccw()
        self.motorL2.extend()

    def Li(self):
        self.motorL1.ccw()
        self.motorL2.retract()
        self.motorL1.cw()
        self.motorL2.extend()

    def L2(self):
        self.motorL1.cw()
        self.motorL1.cw()

    def F(self):
        self.motorF1.cw()
        self.motorF2.retract()
        self.motorF1.ccw()
        self.motorF2.extend()

    def Fi(self):
        self.motorF1.ccw()
        self.motorF2.retract()
        self.motorF1.cw()
        self.motorF2.extend()

    def F2(self):
        self.motorF1.cw()
        self.motorF1.cw()

    def B(self):
        self.motorB1.cw()
        self.motorB2.retract()
        self.motorB1.ccw()
        self.motorB2.extend()

    def Bi(self):
        self.motorB1.ccw()
        self.motorB2.retract()
        self.motorB1.cw()
        self.motorB2.extend()

    def B2(self):
        self.motorB1.cw()
        self.motorB1.cw()

    def x(self):
        self.motorR2.retract()
        self.motorR1.ccw()
        self.motorR2.extend()
        self.motorF2.retract(self.motorB2)
        self.motorR1.cw(self.motorL1)
        self.motorF2.extend(self.motorB2)
        self.motorL2.retract()
        self.motorL1.cw()
        self.motorL2.extend()

    def xi(self):
        self.motorR2.retract()
        self.motorR1.ccw()
        self.motorR2.extend()
        self.motorF2.retract(self.motorB2)
        self.motorR1.ccw(self.motorL1)
        self.motorF2.extend(self.motorB2)
        self.motorL2.retract()
        self.motorL1.cw()
        self.motorL2.extend()

    def z(self):
        self.motorF2.retract()
        self.motorF1.ccw()
        self.motorF2.extend()
        self.motorL2.retract(self.motorR2)
        self.motorF1.cw(self.motorB1)
        self.motorL2.extend(self.motorR2)
        self.motorB2.retract()
        self.motorB1.cw()
        self.motorB2.extend()

    def z2(self):
        self.motorF2.retract()
        self.motorF1.ccw()
        self.motorF2.extend()
        self.motorL2.retract(self.motorR2)
        self.motorF1.cw(self.motorB1)
        self.motorF1.cw(self.motorB1)
        self.motorL2.extend(self.motorR2)
        self.motorF2.retract()
        self.motorF1.cw()
        self.motorF2.extend()

    def drop(self):
        self.motorR2.retract(self.motorL2)
        self.motorF2.retract(self.motorB2)

    def cleanup(self):
        GPIO.cleanup()
