'''
This file contains the code to configure the Raspberry Pi Pico board used in the ESC204 PSA Project

The implementation has 3 buttons represented by the following variables: 'off_button,' 'plant_button,' and 'people_button.' The code ensures that each button activates a unique sequence of LED's when pressed. There is a green, red and blue LED. The respective button sequences are as follows:
    off_button: no LED's on.
    plant_button: red and blue LED's on, green LED off.
    people_button: all LED's on.

The blue, red and green LED's are respectively represented by the 'b_led,' 'r_led' and 'g_led' variables.
'''

# import libaries for blinking external LED
import board
import digitalio

# configure LED pins
    # blue LED at GP18, red LED at GP19, green LED at GP20
    # configure each pin to send an output
b_led = digitalio.DigitalInOut(board.GP18)
b_led.direction = digitalio.Direction.OUTPUT

r_led = digitalio.DigitalInOut(board.GP19)
r_led.direction = digitalio.Direction.OUTPUT

g_led = digitalio.DigitalInOut(board.GP20)
g_led.direction = digitalio.Direction.OUTPUT

# configure buttons:
    # off button at GP13, plant button at GP12 and people button at GP11
    # each pin configured to accept inputs
    # each configured with PULLUP resistors

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

state = [0, 0, 0] # = [r, g, b] - default to all lights off

def set_state(state):
    '''
    Takes in a list button states and returns None
    Sets the value of each led according to the desired case
    '''

    r_led.value = state[0]
    g_led.value = state[1]
    b_led.value = state[2]

    return

while True: # run while the pico is powered
    
    if (not off_button.value) or (not plant_button.value) or (not people_button.value): # check if a button was pressed
        if not off_button.value: # if off_button is pressed: ...
            state = [0, 0, 0] # ...all led's off

        elif not plant_button.value: # if plant button is pressed: ...
            state = [1, 0, 1] # ...turn on red and blue LED's

        elif not people_button.value: # if people button is pressed...
            state = [1, 1, 1] # ...turn on all LED's
    
    set_state(state) # Set the state. Uses previous state if no button is pressed because the "if" block isn't entered