from machine import Pin, PWM

# Exceptions definition
class InvalidSpeedException(Exception):
    """
    Custom exception to indicate an invalid speed value.
    
    Raised when a speed outside the range of -100 to 100 is provided to the motor control.
    """    
    def __init__(self) -> None:
        """
        Initializes the InvalidSpeedException with a default error message.
        """
        message = "Speed must be values between -100 and 100"
        super().__init__(message)
        self.message = message
    
    def __str__(self) -> str:
        """
        Returns a string representation of the exception.
        
        Returns:
            str: A string message indicating the invalid speed error.
        """
        return f"InvalidSpeedException: {self.message}"
    
# Class definition
class Bts7960:
    """
    Represents a motor driver using the BTS7960 H-bridge IC.
    
    Allows for control of motor speed and direction by managing PWM and enable pins.
    """
    
    def __init__(self, rpwm_pin: int, lpwm_pin: int, ren_pin: int, len_pin: int, freq: int = 1000) -> None:
        """
        Initializes the BTS7960 motor driver with specified pins and frequency.
        
        Args:
            rpwm_pin (int): The pin number for the right PWM control.
            lpwm_pin (int): The pin number for the left PWM control.
            ren_pin (int): The pin number for the right enable control.
            len_pin (int): The pin number for the left enable control.
            freq (int, optional): The frequency for the PWM signal. Defaults to 1000 Hz.
        """
        self.r_pwm = PWM(Pin(rpwm_pin), freq)
        self.l_pwm = PWM(Pin(lpwm_pin), freq)
        
        self.r_enable = Pin(ren_pin, Pin.OUT)
        self.l_enable = Pin(len_pin, Pin.OUT)
        
        self._disable() 
        
    def _enable(self) -> None:
        """
        Enables the motor driver by setting the enable pins to high.
        
        This allows the motor to operate.
        """
        self.l_enable.value(1)
        self.r_enable.value(1)   
    
    def _disable(self) -> None:
        """
        Disables the motor driver by setting the enable pins to low.
        
        This stops the motor from operating.
        """
        self.l_enable.value(0)
        self.r_enable.value(0)  
        
    def start(self, speed: float) -> None:
        """
        Starts the motor at the specified speed.
        
        The speed is a float value ranging from -100 to 100, where positive values
        indicate forward motion, negative values indicate reverse motion, and 0 stops the motor.
        
        Args:
            speed (float): The speed to set for the motor, in the range -100 to 100.
            
        Raises:
            InvalidSpeedException: If the speed is outside the allowable range.
        """
        if speed > 100 or speed < -100:
            raise InvalidSpeedException()
        
        if speed > 0:
            self._enable()
            self.l_pwm.duty(511)
            duty = int(511.5 + ((speed / 100) * (1023 - 511.5)))
            self.r_pwm.duty(duty)
            
        elif speed < 0:
            self._enable()
            self.r_pwm.duty(511)
            duty = int(511.5 * (1 - (speed / 100)))
            self.l_pwm.duty(duty)
            
        else:
            self._disable()
            self.r_pwm.duty(511)
            self.l_pwm.duty(511)
            
    def stop(self) -> None:
        """
        Stops the motor by setting the speed to zero.
        
        This is a convenience method that calls `start` with a speed of 0.
        """
        self.start(0)
        
__all__ = ['Bts7960']
