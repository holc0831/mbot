import serial
import time as timer
import json
from typing import List

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    timer.sleep(0.01)
    arduino.write(bytes('0', 'utf-8'))
    data = arduino.readline()
    return data

def forward(time):
    timeout = timer.time() + time
    while timer.time() < timeout:
        print(timer.time())
        write_read("w")
        
def backward(time):
    timeout = timer.time() + time
    while timer.time() < timeout:
        print(timer.time())
        write_read("s")
        
def left(time):
    timeout = timer.time() + time
    while timer.time() < timeout:
        print(timer.time())
        write_read("a")
        
def right(time):
    timeout = timer.time() + time
    while timer.time() < timeout:
        print(timer.time())
        write_read("d")
        
def forwardLeft(time):
    timeout = timer.time() + time
    while timer.time() < timeout:
        print(timer.time())
        write_read("w")
        write_read("a")
        
def forwardRight(time):
    timeout = timer.time() + time
    while timer.time() < timeout:
        print(timer.time())
        write_read("w")
        write_read("d")
        
def backwardLeft(time):
    timeout = timer.time() + time
    while timer.time() < timeout:
        print(timer.time())
        write_read("s")
        write_read("a")
        
def backwardRight(time):
    timeout = timer.time() + time
    while timer.time() < timeout:
        print(timer.time())
        write_read("s")
        write_read("d")
        
def rotateLeft(time):
    timeout = timer.time() + time
    while timer.time() < timeout:
        print(timer.time())
        write_read("q")
        
def rotateRight(time):
    timeout = timer.time() + time
    while timer.time() < timeout:
        print(timer.time())
        write_read("e")
        
def setSpeedLevel(speed):
    write_read(str(speed))

    
dispatch = {
    'move_forward': forward,
    'move_backward': backward,
    'move_left': left,
    'move_right': right,
    'move_forwardright': forwardRight,
    'move_forwardleft': forwardLeft,
    'move_backwardright': backwardRight,
    'move_backwardleft': backwardLeft,
    'rotate_right': rotateRight,
    'rotate_left': rotateLeft,
    'set_speed': setSpeedLevel
}    
    
class Action(object):
    def __init__(self, action: str, value: float):
        self.action = action
        self.value = value
        
class ActionList(object):
    def __init__(self, actions: List[Action]):
        self.actions = actions

    
def parseJSON(actions):
    actionList = ActionList(**json.loads(actions))
    for actionDict in actionList.actions:
        action = Action(**actionDict)
        print(action.action)
        dispatch[action.action](action.value)

testJSON = """
{ "actions":[
    {"action" : "move_west", "value" : 0.5},
    {"action" : "move_south", "value" : 0.5},
    {"action" : "set_speed", "value" : 3},
    {"action" : "move_north", "value" : 0.5},
    {"action" : "move_east", "value" : 0.5},
    {"action" : "rotate_left", "value" : 0.5},
    {"action" : "rotate_right", "value" : 0.5}
    
]
}"""
