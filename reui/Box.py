import reui
from gaugette.bitmap import Bitmap
from gaugette.fonts import arial_16
from pydispatch import dispatcher

'''
A box is a region of a display that can be drawn to. Boxes can optionally have borders.
'''
class Box:
    '''
    width = width of box
    height = height of box
    '''
    def __init__(self, width, height, border_flags=0):
        self._bitmap = Bitmap(width, height, 'y') 
        self.width = width
        self.height = height
        self.border_flags = border_flags
        
    def draw_border(self):
        if self.border_flags & reui.BORDER_TOP:
            for x in range(self.width - 1):
                self._bitmap.draw_pixel(x, 0)
        if self.border_flags & reui.BORDER_BOTTOM:
            for x in range(self.width - 1):
                self._bitmap.draw_pixel(x, self.height - 1)
        if self.border_flags & reui.BORDER_LEFT:
            for y in range(self.height - 1):
                self._bitmap.draw_pixel(0, y)
        if self.border_flags & reui.BORDER_RIGHT:
            for y in range(self.height - 1):
                self._bitmap.draw_pixel(self.width - 1, y)
    
    def refresh(self):
        dispatcher.send(signal=reui.SGL_BOX_UPDATE, sender=self)

    def draw_text(self, x, y, string, font=arial_16, inverse=False):
        self._bitmap.draw_text(x, y, string, font, inverse)

