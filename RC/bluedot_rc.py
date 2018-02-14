#!/usr/bin/env python3
# coding: Latin-1

# Bluedot_rc v1.0
# Written by Bill Harvey Feb 2018
# The program below enables control of motors connected to a PiBorg ThunderBorg
# motor controller board using Martin O'Hanlon's BlueDot app (Andoroid version used for testing)
# Written using python 3
# To use the ThunderBorg you will need to download the Python 3 version of ThunderBorg3.py
# Install on Raspberry Pi using the following command:
# wget -O ThunderBorg3.py http://old.piborg.org/downloads/thunderborg/ThunderBorg3.py.txt

import ThunderBorg3
from time import sleep
import sys
from bluedot import BlueDot
from gpiozero import Robot
from signal import pause

# Setup the ThunderBorg
global TB
TB = ThunderBorg3.ThunderBorg()     # Create a new ThunderBorg object
#TB.i2cAddress = 0x15              # Uncomment and change the value if you have changed the board address
TB.Init()                          # Set the board up (checks the board is connected)
if not TB.foundChip:
    boards = ThunderBorg.ScanForThunderBorg()
    if len(boards) == 0:
        print("No ThunderBorg found, check you are attached :)")
    else:
        print("No ThunderBorg at address %02X, but we did find boards:" % (TB.i2cAddress))
        for board in boards:
            print("    %02X (%d)" % (board, board))
        print("If you need to change the I²C address change the setup line so it is correct, e.g.")
        print("TB.i2cAddress = 0x%02X" % (boards[0]))
    sys.exit()

bd = BlueDot()

def move(pos):
    if pos.top:
        print("Forward", pos.distance)
        TB.SetMotor1(pos.distance)
        TB.SetMotor2(pos.distance)

    elif pos.bottom:
        print("Backwards", pos.distance)
        TB.SetMotor1(-pos.distance)
        TB.SetMotor2(-pos.distance)

    elif pos.left:
        print("Left", pos.distance)
        TB.SetMotor1(pos.distance)
        TB.SetMotor2(-pos.distance)

    elif pos.right:
        print("Right", pos.distance)
        TB.SetMotor1(-pos.distance)
        TB.SetMotor2(pos.distance)
        
    
def stop():
    print("stopping")
    TB.MotorsOff()                 # Turn both motors off

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

pause()




