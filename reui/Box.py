import reui
from gaugette.bitmap import Bitmap
from gaugette.font5x8 import Font5x8
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
        self.font = Font5x8
        
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

    def draw_text(self, x, y, string):
        font_bytes = self.font.bytes
        font_rows = self.font.rows
        font_cols = self.font.cols
        for c in string:
            p = ord(c) * font_cols
            for col in range(0,font_cols):
                mask = font_bytes[p]
                p+=1
                for row in range(0,8):
                    self._bitmap.draw_pixel(x,y+row,mask & 0x1)
                    mask >>= 1
                x += 1

