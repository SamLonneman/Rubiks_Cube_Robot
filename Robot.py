from io import BytesIO
from os import system

from PIL import Image
from RPi import GPIO
from picamera import PiCamera

from Motor import Motor


class Robot:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.solve_button = 6
        self.abort_button = 13
        self.shutdown_button = 19
        self.hot_pin = 26
        GPIO.setup(self.solve_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.abort_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.shutdown_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.hot_pin, GPIO.OUT)
        GPIO.output(self.hot_pin, True)
        system("sudo sh -c \"echo none > /sys/class/leds/led1/trigger\"")
        system("sudo sh -c \"echo 0 > /sys/class/leds/led1/brightness\"")
        system("sudo sh -c \"echo none > /sys/class/leds/led0/trigger\"")
        system("sudo sh -c \"echo 1 > /sys/class/leds/led0/brightness\"")
        self.motorR1 = Motor(18, 15)
        self.motorR2 = Motor(8, 25)
        self.motorL1 = Motor(24, 23)
        self.motorL2 = Motor(1, 7)
        self.motorF1 = Motor(27, 17)
        self.motorF2 = Motor(11, 9)
        self.motorB1 = Motor(10, 22)
        self.motorB2 = Motor(5, 0)
        self.camera = PiCamera()
        self.yellow = (117, 142, 0)
        self.red = (132, 17, 14)
        self.green = (0, 109, 2)
        self.orange = (178, 70, 8)
        self.blue = (0, 31, 53)
        self.white = (156, 151, 109)
        self.PIXELS = [
            (951, 720),
            (887, 571),
            (755, 495),
            (1042, 586),
            (967, 511),
            (902, 433),
            (1177, 519),
            (1053, 444),
            (979, 303),
        ]

    def rgb_diff(self, rgb1, rgb2):
        difference = 0
        for i in range(3):
            difference += abs(rgb1[i] - rgb2[i])
        return difference

    def take_picture(self):
        stream = BytesIO()
        self.camera.capture(stream, format='jpeg')
        return Image.open(stream).load()

    def calibrate(self):
        self.yellow = self.take_picture()[self.PIXELS[4]]
        self.z()
        self.red = self.take_picture()[self.PIXELS[4]]
        self.x()
        self.green = self.take_picture()[self.PIXELS[4]]
        self.x()
        self.orange = self.take_picture()[self.PIXELS[4]]
        self.x()
        self.blue = self.take_picture()[self.PIXELS[4]]
        self.x()
        self.z()
        self.white = self.take_picture()[self.PIXELS[4]]
        self.z2()

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

    def get_cubestring_segment(self, order):
        cubestring = str()
        image = self.take_picture()
        for i in order:
            cubestring += self.pick_color(image[self.PIXELS[i]])
        return cubestring

    def read_cube(self):
        cubestring = str()
        cubestring += self.get_cubestring_segment((0, 1, 2, 3, 4, 5, 6, 7, 8))
        self.z()
        cubestring += self.get_cubestring_segment((2, 5, 8, 1, 4, 7, 0, 3, 6))
        self.x()
        cubestring += self.get_cubestring_segment((2, 5, 8, 1, 4, 7, 0, 3, 6))
        self.x()
        cubestring += self.get_cubestring_segment((2, 5, 8, 1, 4, 7, 0, 3, 6))
        self.x()
        cubestring += self.get_cubestring_segment((2, 5, 8, 1, 4, 7, 0, 3, 6))
        self.x()
        self.z()
        cubestring += self.get_cubestring_segment((6, 3, 0, 7, 4, 1, 8, 5, 2))
        self.z2()
        return cubestring

    def drop(self):
        self.motorR2.retract(self.motorL2)
        self.motorF2.retract(self.motorB2)

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
