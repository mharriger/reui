import reui
import reui.Box
import reui.Menu
import reui.Screen
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

pydispatch.dispatcher.connect(hdlr, sender=pydispatch.dispatcher.Any)

display = gaugette.ssd1306.SSD1306(dc_pin=DC_PIN, reset_pin=RESET_PIN,
                                   buffer_rows=64, buffer_cols=128, rows=64, cols=128)
display.clear_display()
display.begin()

screen = reui.Screen(128, 64, display)
box = reui.Box.Box(128, 10, reui.BORDER_BOTTOM,)
menu = reui.Menu.Menu(128, 50)
screen.add_box(0, 0, box)
screen.add_box(0, 10, menu)

box.draw_text(2, 1, "Hello World!")
box.draw_border()
menu.draw()

try:
    app.run()
finally:
    display.clear_display()
    display.display()
