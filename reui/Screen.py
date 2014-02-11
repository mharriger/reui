"""
A screen object contains a collection of boxes to be displayed on a
physical display device.
"""

from pydispatch import dispatcher
from reui import SGL_BOX_UPDATE
from gaugette import bitmap

class Screen:

    _boxes = []
    _boxMap = {}
    _bitmap = None

    def __init__(self, width, height, display):
        #self._bitmap = bitmap.Bitmap(width, height, 'y')
        self._display = display
        #self._display.bitmap = self._bitmap
        self._bitmap = self._display.bitmap

    def add_box(self, x, y, box):
        self._boxes.append((x, y, box))
        self._boxMap[box] = (x, y)
        dispatcher.connect(self.on_box_update, signal=SGL_BOX_UPDATE,
                             sender=box)

    def draw(self):
        for x, y, box in self._boxes:
            self._bitmap.replace_rect(x, y, box._bitmap)

    def on_box_update(self, **args):
        if 'sender' in args:
            sender = args['sender']
            if sender in self._boxMap:
                (x, y) = self._boxMap[sender]
                self._bitmap.replace_rect(x, y, sender._bitmap)
        self._display.display()

    def draw_pixel(self, box, x, y, on=True):
        bx, by = self._boxMap[box]
        self._bitmap.draw_pixel(bx + x, by + y, on)

    def draw_text(self, box, x, y, string, font=box.font):
        bx, by = self._boxMap[box]
        self._bitmap.draw_text(bx + x, by + y, string, font)
        
