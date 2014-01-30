import reui

'''
A box is a region of a display that can be drawn to. Boxes can optionally have borders.
'''
class Box:
    '''
    width = width of box
    height = height of box
    '''
    def __init__(self, display, width, height, border_flags=0, x=0, y=0):
        self.display = display
        self.width = width
        self.height = height
        self.border_flags = border_flags
        #Temporary until I decide on how this will be implemented
        self.x = x
        self.y = y

    def draw_text(self, x, y, string):
        self.display.draw_text(x + self.x, y + self.y, string)
        
    def draw_border(self):
        if self.border_flags & reui.BORDER_TOP:
            for x in range(self.x, self.x + self.width - 1):
                self.display.draw_pixel(x, self.y)
        if self.border_flags & reui.BORDER_BOTTOM:
            for x in range(self.x - 1, self.x + self.width - 1):
                self.display.draw_pixel(x, self.y + self.height - 1)
        if self.border_flags & reui.BORDER_LEFT:
            for y in range(self.y, self.y + self.height - 1):
                self.display.draw_pixel(self.x, y)
        if self.border_flags & reui.BORDER_RIGHT:
            for y in range(self.y, self.y + self.height - 1):
                self.display.draw_pixel(self.x + self.width - 1, y)
    
    def refresh(self):
        self.display.display()
