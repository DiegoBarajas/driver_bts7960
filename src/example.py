from driver_bts7960 import Bts7960
from time import sleep

motor = Bts7960(15, 14, 19, 21)
"""
Declaration of the class with pins:
    15 - RPWM
    14 - LPWM
    19 - R_EN
    21 - L_EN
"""

motor.start(10) # advances clockwise to 10% of capacity
sleep(1) # Wait 1 sec

motor.start(100) # advances clockwise to 100% of capacity
sleep(2) # Wait 1 sec

motor.stop() # Stops motor

motor.start(-45) # counterclockwise at 10% of capacity
sleep(5) # Wait 5 secs

motor.stop() # Stops motor
