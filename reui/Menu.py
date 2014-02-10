from reui import Box, SGL_LEFT, SGL_RIGHT, SGL_CLICK
from pydispatch import dispatcher

'''
A Box containing a vertical-scrolling menu. Generates event when a menu item is selected. Supports submenus.
'''
class Menu(Box.Box):

    items = [("Item 1",),("Item 2",),("Item 3",)]
    _selidx = 0
    _highlightpos = 1

    '''
    Initialize Menu object
    '''
    def __init__(self, width, height, border_flags = 0):
        Box.Box.__init__(self, width, height, border_flags)
        dispatcher.connect(self.on_left, signal=SGL_LEFT)
        dispatcher.connect(self.on_right, signal=SGL_RIGHT)
        dispatcher.connect(self.on_right, signal=SGL_CLICK)

    def draw(self):
        pos = 1
        for itemIdx in range(len(self.items)):
            if itemIdx = self._selidx
                self.draw_text(2, pos, self.items[itemIdx][0])
                for i in range(Box.arial_16.char_height):
                    self._bitmap.invert_row(2 + i)
                pos += Box.arial_16.char_height
            else:
                self.draw_text(2, pos, self.items[itemIdx][0])
                pos += Box.arial_16.char_height
        self.refresh()
        
    def move_highlight_to(self, x):
        while x > self._highlightpos:
            self._bitmap.invert_row(self._highlightpos)
            self._highlightpos += 1
            self.bitmap.invert_row(self._highlightpos + Box.arial_16.char_height)
            self.refresh()
        while x < self._highlightpos:
            self._bitmap.invert_row(self._highlightpos + Box.arial_16.char_height)
            self._highlightpos -= 1
            self.bitmap.invert_row(self._highlightpos)
            self.refresh()
        
    def on_left(self, **args):
        if self._selidx < len(items):
            self._selidx += 1
            self.move_highlight_to(self._selidx * Box.arial_16.char_height + 1)
            
    def on_right(self, **args):
        if self._selidx > 0:
            self._selidx -= 1
            self.move_highlight_to(self._selidx * Box.arial_16.char_height + 1)
            
    def on_click(self, **args):
        print "Clicked on item: %s" % self.items[self._selidx][0]
