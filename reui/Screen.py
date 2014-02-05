"""
A screen object contains a collection of boxes to be displayed on a
physical display device.
"""

from pydispatch import dispatcher
from reui import SGL_BOX_UPDATE

class Screen:

    _boxes = []
    _boxMap = {}
    _bitmap = None

    def __init__(self, width, height):
        self._bitmap = Bitmap(width, height, 'y')

    def addBox(self, x, y, box):
        self._boxes.append((x, y, box))
        self._boxM[box] = (x, y)
        dispatcher.connect(self.on_box_update, signal=reui.SGL_BOX_UPDATE,
                             sender=box)

    def draw(self):
        for x, y, box in self._boxes:
            self._bitmap.replace_rect(x, y, box._bitmap)

    def on_box_update(self, **args):
        if 'sender' in args:
            sender = args['sender']
            if sender in self._boxMap:
                (x, y) = self._boxMa[sender]
                self._bitmap.replace_rect(x, y, sender._bitmap)

