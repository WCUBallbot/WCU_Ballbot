from Motor import Motor
import Adafruit_BBIO.GPIO as GPIO

"""
This file is responsible for controlling all interactions with the microcontroller, the beaglebone.
The file is a collection of functions that can be called to make changes to the digitial logic outputs
on the beaglebone board

@author: Brandon Beiler
@version: 9/11/2018 : Created the base file
"""


def setStep(step: int, motor: Motor):
    """Set the step of the motor.
    
    This function sets the motor driver for the given motor so that it steps the motor
    at the desired step. This step is a constant found in the Motor class

    Args:
        step: the constant that represents the desired step
        motor: the motor that will be affected by this change 
    """
    
    if step == Motor.STEP_FULL:
        GPIO.output(Motor.PIN_M1, GPIO.LOW)
        GPIO.output(Motor.PIN_M2, GPIO.LOW)
        GPIO.output(Motor.PIN_M3, GPIO.LOW)
    elif step == Motor.STEP_HALF:
        GPIO.output(Motor.PIN_M1, GPIO.HIGH)
        GPIO.output(Motor.PIN_M2, GPIO.LOW)
        GPIO.output(Motor.PIN_M3, GPIO.LOW)
    elif step == Motor.STEP_QUARTER:
        GPIO.output(Motor.PIN_M1, GPIO.LOW)
        GPIO.output(Motor.PIN_M2, GPIO.HIGH)
        GPIO.output(Motor.PIN_M3, GPIO.LOW)
    elif step == Motor.STEP_8th:
        GPIO.output(Motor.PIN_M1, GPIO.HIGH)
        GPIO.output(Motor.PIN_M2, GPIO.HIGH)
        GPIO.output(Motor.PIN_M3, GPIO.LOW)
    elif step == Motor.STEP_16th:
        GPIO.output(Motor.PIN_M1, GPIO.HIGH)
        GPIO.output(Motor.PIN_M2, GPIO.HIGH)
        GPIO.output(Motor.PIN_M3, GPIO.HIGH)
    else:
        print("Invalid step argument")



def configureOutputPin(pin: str):
    """Sets the given pin to an output type pin.
    
    The microcontroller beaglebone board requires that a pin be set as output or input
    before that pin can be used. 
    
    Args:
        pin: The string code for the pin, normally depicted as P#_##
    
    """
    GPIO.setup(pin, GPIO.OUT)
    
def configureInputPin(pin: str):
    """Sets the given pin to an input type pin.
    
    The microcontroller beaglebone board requires that a pin be set as output or input
    before that pin can be used. 
    
    Args:
        pin: The string code for the pin, normally depicted as P#_##
    
    """
    GPIO.setup(pin, GPIO.IN)
    