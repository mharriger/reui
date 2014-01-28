'''
reui - rotary encoder user interface

Dependencies: gaugette, PyDispatcher

(c) 2014 Matt Harriger
'''

from pydispatch import dispatcher

import gaugette.rotary_encoder
import gaugette.switch
import gaugette.ssd1306
 
# Set up the pins for gaugette.
RESET_PIN = 15
DC_PIN    = 16
A_PIN  = 7
B_PIN  = 9
SW_PIN = 8


#Configuration constants
LONG_CLICK_LEN = 1.5 #Length of a long click, in seconds. Can be a float.
POS_STEP_DIVISOR = 4 #Number of encoder steps betwwen LEFT and RIGHT events.


#Signals for PyDispatcher

#There are 2 low-level events: one for a change in encoder position, and one for a change in switch state
SGL_POS_CHANGE = 'pos_change'
SGL_SWITCH_CHANGE = 'switch_change'

#Higher-level events, intended to be more convenient than the low-level ones
SGL_LEFT = 'step_left' #Encoder moved one step to the left.
SGL_RIGHT = 'step_right' #Encoder moved one step to the right.
SGL_CLICK = 'click' #Encoder switch pressed and relesed.
SGL_DOWN_LEFT = 'down_left' #Encoder turned one step to left while switch held down
SGL_DOWN_RIGHT = 'down_right' #Encoder turned one step to right while switch held down
SGL_LONG_CLICK = 'long_click' #Button held down for more than LONG_CLICK_LEN seconds

#Border flags
BORDER_TOP = 1
BORDER_BOTTOM = 2
BORDER_LEFT = 4
BORDER_RIGHT = 8
BORDER_ALL = 15

'''
An reui application. Implements the main event loop.
'''
class App:
    '''
    Initialize an App object
    '''
    def __init__(self):
        #Encoder is owned by the app, while display is separate. I think this makes sense, since the UI is
        #entirely based around the encoder
        self.encoder = gaugette.rotary_encoder.RotaryEncoder.Worker(A_PIN, B_PIN)
        self.switch = gaugette.switch.Switch(SW_PIN)
        self.last_switch_state = self.switch.get_state()

        self.accumPosChange = 0

        dispatcher.connect(self.on_pos_change, signal=SGL_POS_CHANGE,
                             sender=self.encoder)

        return

    '''
    Start the event loop
    '''
    def run(self):
        self.encoder.start()
        while True:
            delta = self.encoder.get_delta()
            if delta != 0:
                dispatcher.send(signal=SGL_POS_CHANGE,
                                           sender=self.encoder, delta=delta)
            state = self.switch.get_state()
            if state != self.last_switch_state:
                dispatcher.send(signal=SGL_SWITCH_CHANGE,
                                           sender=self.encoder, state=state)

    def on_pos_change(self, **args):
        if 'delta' in args:
            self.accumPosChange += args['delta']
        if self.accumPosChange % 4 == 0:
            if self.accumPosChange < 0:
                dispatcher.send(signal=SGL_LEFT, sender=self.encoder)
            if self.accumPosChange > 0:
                dispatcher.send(signal=SGL_RIGHT, sender=self.encoder)
            self.accumPosChange = 0
