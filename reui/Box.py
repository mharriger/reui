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
    def __init__(self, screen, width, height, border_flags=0):
        self.width = width
        self.height = height
        self.border_flags = border_flags
        self.font = arial_16
        self._screen = screen
        
    def draw_border(self):
        if self.border_flags & reui.BORDER_TOP:
            for x in range(self.width - 1):
                self._screen.draw_pixel(self, x, 0)
        if self.border_flags & reui.BORDER_BOTTOM:
            for x in range(self.width - 1):
                self._screen.draw_pixel(self, x, self.height - 1)
        if self.border_flags & reui.BORDER_LEFT:
            for y in range(self.height - 1):
                self._screen.draw_pixel(self, 0, y)
        if self.border_flags & reui.BORDER_RIGHT:
            for y in range(self.height - 1):
                self._screen.draw_pixel(self, self.width - 1, y)
    
    def refresh(self):
        dispatcher.send(signal=reui.SGL_BOX_UPDATE, sender=self)

    def draw_text(self, x, y, string, font=arial_16, inverse=False):
        self._screen.draw_text(self, x, y, string, font, inverse)

