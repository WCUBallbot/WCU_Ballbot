from MicroControl import *

"""
The Motor class handles all actions related to a single motor. This class handles the abstraction
of interactivity with the hardware components and allows user to simply set motor values and call
motor controls

Imports:


@author: Brandon Beiler
@version: 9/11/2018 : Created the base class

"""
class Motor:
    """
    Attributes:
        acceleration: the current acceleration of the motor (rad/sec^2)
        velocity: the current velocity of the motor (rad/sec)
        position: the current position of the motor (rad)
        targetVelocity: the target motor velocity
        targetPositon: the target motor position
        delayProfile: the list that holds the current delay profile that the motor will use for the next run.
            This profile is updated before every movement operation
        step: the current step state that the motor is in, or will take. 
        ID: the unique identifier for this motor. Used when there are multiple motors being controlled
    """
    
    STEP_FULL = 0 #Full Step
    STEP_HALF = 1 #Half Step
    STEP_QUARTER = 2 #1/4 step
    STEP_8th = 3 #1/8 step
    STEP_16th = 4 #1/16 step
    PIN_STEP = "" #pin for controller step
    PIN_DIR = "" #pin for direction on the controller
    PIN_M1 = "" #pin for m1
    PIN_M2 = "" #pin for m2
    PIN_M3 = "" #pin for m3
    
    def __init__(self,id, step=STEP_FULL):
        """Initialize the Motor.
        
        This initializes the motor class and sets all the motor attributes to zero. Additionally, it takes
        in the identifer for the motor and stores it. Finally, it sets the step rate for the motor
        to full step if the user doesn't provide one.
    
        Args:
            id: the unique identifier for the motor
            step: (optional) the step for the motor
        """
    
        self.__acceleration = 0
        self.__velocity = 0
        self.__position = 0
        self.__targetVelocity = 0
        self.__targetPosition = 0
        self.__delayProfile = []
        self.__step = step
        self.__ID = id;
    
    
    def getAcceleration(self):
        """ This returns the current acceleration of the motor at that instant.
       
        Returns:
            the motors acceleration (rad/sec)
        """
        return self.__acceleration
        
    
    def getVelocity(self):
        """ This returns the current velocity of the motor at that instant.
        
        Returns:
            the motors velocity (rad/sec)
        """
        return self.__velocity
    
    
    def getPosition(self):
        """ This returns the current position of the motor at that instant.
        
        Returns:
            the motors position in (rad)
        """
        return self.__position
    
    
    def getStepType(self):
        """ This returns the current step that the motor takes currently.
    
        Returns:
            the motors step rate
        """
        return self.__step
    
    
    def getID(self):
        """ This returns the motors unique identifier that allows the program to distinguish between motors.
        
        Returns:
            the motors ID
        """
        return self.__ID
    
    
    def getDelayProfile(self):
        """ This returns the delay profile that the motor is going to or just used when conducting a move operation.
    
        Returns:
            A list of delays, depicting the delay profile for motion
        """
        return self.__delayProfile
    
    
    def configurePins(self, step_pin: str, dir_pin: str, m1_pin: str, m2_pin: str, m3_pin: str):
        """This method sets up the connection pins between the motor object and the micro controller
        
        In order to communicate with the board, the various driver pins for the motor are configured
        and stored as variables. Additionally, those pins must be configured as output pins so that
        the beaglebone board can output digital writes to them
        
        Args:
            step_pin: controller pin to step the motor
            dir_pin: controller pin to control motor direction
            m1_pin: controller pin for m1
            m2_pin: controller pin for m2
            m3_pin: controller pin for m3
        """
        
        self.PIN_STEP = step_pin
        self.PIN_DIR = dir_pin
        self.PIN_M1 = m1_pin
        self.PIN_M2 = m2_pin
        self.PIN_M3 = m3_pin
        
        configureOutputPin(self.PIN_STEP)
        configureOutputPin(self.PIN_DIR)
        configureOutputPin(self.PIN_M1)
        configureOutputPin(self.PIN_M2)
        configureOutputPin(self.PIN_M3)
    
    def setStep(self, step: int):
        """ This method allows a user to set the step rate for the motor.
        
        Returns:
            The step rate, as defined by a Motor class constant
        """
        
        if (not self.PIN_M1) and (not self.PIN_M2) and (not self.PIN_M3):
            print("must configure digital pins for motor")
        else:
            self.__step = step
        
            setStep(step, self)
        
    
    def setAcceleration(self, acceleration: int):
        """ This method allows the user to specify an acceleration constant to use for the motor movement.
        
        Returns:
            acceleration: a constant acceleration to use for the motor
        """
        self.__acceleration = acceleration
        
    
    def moveTo(self, position: int, velocity: int):
        """ This method moves the motor to a given position with a certain max velocity. 
        
        It uses the stored acceleration value as the constant motor acceleration.
        
        Args:
            position: the absolute position of the motor in rads
            velocity: the maximum motor velocity 
        """
        
        if (not self.PIN_DIR) and (not self.PIN_STEP):
            print("must configure digital pins for motor")
        else:
            
            self.__targetPosition = position
            self.__targetVelocity = velocity
            
            #NEEDS IMPLIMENTATION
        
    
    def moveBy(self, displacement: int, velocity: int):
        """ This method moves the motor from its current location by a given displacement amount. 
        
        It moves the motor with a max velocity which is provided and the stored constant acceleration value.
        
        Args:
            displacement: the amount to displace the current motors position
            velocity: the maximum motor velocity 
        """
        
        if (not self.PIN_DIR) and (not self.PIN_STEP):
            print("must configure digital pins for motor")
        else:
            
            self.__targetPosition = self.__position + displacement
            self.__targetVelocity = velocity
        
            #NEEDS IMPLIMENTATION
        
    
    
    




    