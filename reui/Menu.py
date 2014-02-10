from reui import Box

'''
A Box containing a vertical-scrolling menu. Generates event when a menu item is selected. Supports submenus.
'''

class Menu(Box.Box):
    '''
    Initialize Menu object
    '''

    items = [("Item 1",),("Item 2",),("Item 3",)]

    def __init__(self, width, height, border_flags = 0):
        Box.Box.__init__(self, width, height, border_flags)

    def draw(self):
        pos = 1
        for item in self.items:
            if item[0] == 'Item 1':
                self.draw_text(2, pos, item[0])
                for i in range(Box.arial_16.char_height):
                    self._bitmap.invert_row(2 + i)
                pos += Box.arial_16.char_height
            else:
                self.draw_text(2, pos, item[0])
                pos += Box.arial_16.char_height
        self.refresh()
