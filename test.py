import reui
import reui.Box
import reui.Menu
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

box = reui.Box.Box(128, 10, reui.BORDER_BOTTOM,)
menu = reui.Menu.Menu(128, 50)

box.draw_text(2, 1, "Hello World!")
box.draw_border()
menu.draw()

display.bitmap.replace_rect(0,0,box._bitmap)
display.bitmap.replace_rect(0,10,menu._bitmap)

#menu.refresh()

display.display()

try:
    app.run()
finally:
    display.clear_display()
    display.display()
