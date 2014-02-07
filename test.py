import reui
import reui.Box
import reui.Menu
import reui.Screen
import pydispatch

import gaugette.rotary_encoder
import gaugette.switch
import gaugette.ssd1306

from datetime import datetime

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
box = reui.Box.Box(128, 18, reui.BORDER_BOTTOM)
menu = reui.Menu.Menu(128, 46)
screen.add_box(0, 0, box)
screen.add_box(0, 18, menu)

box.draw_text(0, 0, datetime.today().strftime('%H:%M'))
date_str = datetime.today().strftime('%x')
box.draw_text(127 - box._bitmap.text_width(date_str, reui.Box.arial_16), 0, date_str)
box.draw_border()
menu.draw()

try:
    app.run()
finally:
    display.clear_display()
    display.display()
