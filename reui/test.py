import reui
import pydispatch

import gaugette.rotary_encoder
import gaugette.switch
import gaugette.ssd1306

# Set up the pins for gaugette.
RESET_PIN = 15
DC_PIN    = 16

app = reui.App()

def hdlr(self, **args):
    print args

pydispatch.dispatcher.connect(hdlr, sender=pydispatch.any)

display = gaugette.ssd1306(dc_pin=DC_PIN, reset_pin=RESET_PIN, buffer_rows=128, buffer_cols=128, rows=64, cols=128)
display.clear_display()
display.begin()

box = reui.Box(display, 128, 54, reui.BORDER_BOTTOM, 0, 10)

box.draw_border()
box.draw_text(2, 2, "Hello World!")
box.refresh()

app.Run()
