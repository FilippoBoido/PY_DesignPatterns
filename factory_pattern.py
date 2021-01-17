#-- simple factory pattern

from abc import ABCMeta, abstractmethod


class Motor(metaclass = ABCMeta):
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class ServoMotor(Motor):
    
    def start(self):
        print("Starting servo motor")
        
    def stop(self):
        print("Stopping servo motor")
        
class StepperMotor(Motor):
    
    def start(self):
        print("Starting stepper motor")
        
    def stop(self):
        print("Stopping stepper motor")

class MotorFactory(object):
    
    @staticmethod
    def produce_motor(type):
        return eval(type+"Motor")()
    
if __name__ == '__main__':
    
    try:
        servo = MotorFactory.produce_motor(type="Servoo")
        servo.start()
        
    except NameError:
        print("Motor type not available, no instance produced.")
    
        