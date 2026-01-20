'''
Code for Raspberry Pi Pico board of the ESC204 PSA Project
'''

# import libaries for blinking external LED
import board
import digitalio

# configure pins the turn on the LED's for output
b_led = digitalio.DigitalInOut(board.GP18)
b_led.direction = digitalio.Direction.OUTPUT

r_led = digitalio.DigitalInOut(board.GP19)
r_led.direction = digitalio.Direction.OUTPUT

g_led = digitalio.DigitalInOut(board.GP20)
g_led.direction = digitalio.Direction.OUTPUT

# configure buttons to input to the Pico, use PULLUP resistors
off_button = digitalio.DigitalInOut(board.GP13)
off_button.direction = digitalio.Direction.INPUT
off_button.pull = digitalio.Pull.UP

plant_button = digitalio.DigitalInOut(board.GP12)
plant_button.direction = digitalio.Direction.INPUT
plant_button.pull = digitalio.Pull.UP

people_button = digitalio.DigitalInOut(board.GP11)
people_button.direction = digitalio.Direction.INPUT
people_button.pull = digitalio.Pull.UP

# implement functionality

state = [0, 0, 0] # = [r, g, b] - default all lights off

def set_state(state):

    r_led.value = state[0]
    g_led.value = state[1]
    b_led.value = state[2]

    return

while True:
    
    if (not off_button.value) or (not plant_button.value) or (not people_button.value): # check if a button was pressed
        if not off_button.value: # if off_button is pressed: ...
            state = [0, 0, 0] # ...all led's off

        elif not plant_button.value: # if plant button is pressed: ...
            state = [1, 0, 1] # ...turn on red and blue LED's

        elif not people_button.value: # if people button is pressed...
            state = [1, 1, 1] # ...turn on all LED's
    
    set_state(state) # Set the state. Uses previous state if no button is pressed because the "if" block isn't entered
