import RPi.GPIO as GPIO
from gpiozero import Servo
import random
import time
from PIL import Image
from thermalprinter import *
import subprocess


GPIO.setmode(GPIO.BCM)
servo = Servo(8)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(7, GPIO.OUT) 



def water():
    servo.max()
    time.sleep(1)
    GPIO.output(7, True)
    time.sleep(2)
    GPIO.output(7, False)
    time.sleep(0.5)
    servo.min()

def insults():
    with ThermalPrinter(port='/dev/ttyAMA0') as printer:
        insults = ["Imagine an egg hitting a concrete pavement, that’s how hard-wired, inflexible and brittle your code is.", "Imagine an egg hitting a concrete pavement, that’s how hard-wired, inflexible and brittle your code is.", "Your commit is writing checks your merge can’t cash.", "Your code is so bad your child processes disowned you.", "Your coding methods are so backwards they’ve added it to the school curriculum in Texas!"]
        printer.feed(2)
        randNum = int(random.randrange(0,5))
        insult = insults[randNum]
        printer.out(insult)
        printer.feed(7)

def meme():
    with ThermalPrinter(port='/dev/ttyAMA0') as printer:
        memes =  ["yay.jpeg", "che.jpeg", "pika.png", "stonks.jpeg", "catfish.jpeg", "pepega.jpeg", "uno.png"]
        printer.feed(2)
        randNum = int(random.randrange(0,7))
        meme = memes[randNum]
        printer.image(Image.open("./" + meme))
        printer.feed(7)
        
    
    

def matrix():
    randNum = int(random.randrange(0,2))
    if randNum == 0:
        subprocess.run("sudo ./rpi-rgb-led-matrix/examples-api-use/demo -D0 --led-rows=32 --led-cols=32 --led-slowdown-gpio=3", shell=True, check=False)
    if randNum == 1:
        subprocess.run("sudo ./rpi-rgb-led-matrix/examples-api-use/demo -D8 --led-rows=32 --led-cols=32 --led-slowdown-gpio=3", shell=True, check=False)
    if randNum == 2:
        subprocess.run("sudo ./rpi-rgb-led-matrix/examples-api-use/demo -D9 --led-rows=32 --led-cols=32 --led-slowdown-gpio=3", shell=True, check=False)


def qrCode():
    with ThermalPrinter(port='/dev/ttyAMA0') as printer:
        insults = ["https://dilbert.com/", "http://www.zombo.com/", "http://corndogoncorndog.com/", "http://corndogoncorndog.com/"]
        printer.feed(2)
        randNum = int(random.randrange(0,3))
        insult = insults[randNum]
        printer.out(insult)
        printer.feed(7)


while True:
    button5 = GPIO.input(24)
    button4 = GPIO.input(25)
    button3 = GPIO.input(10)
    button2 = GPIO.input(11)
    button1 = GPIO.input(9)
    if not button1:
        water()
        button1 = True
    if not button2:
        insults()
        button2 = True
    if not button3:
        meme()
        button3 = True
    if not button4:
        matrix()
        button4 = True
    if not button5:
        qrCode()
        button5 = True
    time.sleep(0.1)



