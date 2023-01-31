import serial
import time as timer
import json
from typing import List

class Action(object):
    def __init__(self, action: str, value: float):
        self.action = action
        self.value = value
        
class ActionList(object):
    def __init__(self, actions: List[Action]):
        self.actions = actions


class MBotMovement():
    def __init__(self):
        self.stop_thread = False
        self.arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
        self.dispatch = {
            'move_forward': self.forward,
            'move_backward': self.backward,
            'move_left': self.left,
            'move_right': self.right,
            'move_forwardright': self.forwardRight,
            'move_forwardleft': self.forwardLeft,
            'move_backwardright': self.backwardRight,
            'move_backwardleft': self.backwardLeft,
            'rotate_right': self.rotateRight,
            'rotate_left': self.rotateLeft,
            'set_speed': self.setSpeedLevel,
            'stop': self.stop,
            'color_init': self.color_init,
            'color_change': self.color_change
        }    

    def write_read(self, x):
        self.arduino.write(bytes(x, 'utf-8'))
        timer.sleep(0.01)
        self.arduino.write(bytes('0', 'utf-8'))
        data = self.arduino.readline()
        return data


    def color_init(self, time):
        self.write_read("c")

    def color_change(self, value):
        self.write_read(value)

    def forward(self, time):
        timeout = timer.time() + time
        while timer.time() < timeout:
#             print(timer.time())
            self.write_read("w")
        
    def backward(self, time):
        timeout = timer.time() + time
        while timer.time() < timeout:
#             print(timer.time())
            self.write_read("s")
            
    def left(self, time):
        timeout = timer.time() + time
        while timer.time() < timeout:
#             print(timer.time())
            self.write_read("a")
            
    def right(self, time):
        timeout = timer.time() + time
        while timer.time() < timeout:
#             print(timer.time())
            self.write_read("d")
            
    def forwardLeft(self, time):
        timeout = timer.time() + time
        while timer.time() < timeout:
#             print(timer.time())
            self.write_read("w")
            self.write_read("a")
            
    def forwardRight(self, time):
        timeout = timer.time() + time
        while timer.time() < timeout:
#             print(timer.time())
            self.write_read("w")
            self.write_read("d")
            
    def backwardLeft(self, time):
        timeout = timer.time() + time
        while timer.time() < timeout:
#             print(timer.time())
            self.write_read("s")
            self.write_read("a")
            
    def backwardRight(self, time):
        timeout = timer.time() + time
        while timer.time() < timeout:
#             print(timer.time())
            self.write_read("s")
            self.write_read("d")
            
    def rotateLeft(self, time):
        timeout = timer.time() + time
        while timer.time() < timeout:
#             print(timer.time())
            self.write_read("q")
            
    def rotateRight(self, time):
        timeout = timer.time() + time
        while timer.time() < timeout:
#             print(timer.time())
            self.write_read("e")
            
    def setSpeedLevel(self, speed):
        self.write_read(str(speed))

    def stop(self, value):
        # empty function
        return
        
    def parseJSON(self, actions):
#         self.stop_thread = False
#         print(self.stop_thread)
        actionList = ActionList(**json.loads(actions))
        for actionDict in actionList.actions:
            if self.stop_thread:
                break
            
            action = Action(**actionDict)
            print("Execute action: %s " % action.action)
            
            self.dispatch[action.action](action.value)
        print("--------------------------------")

