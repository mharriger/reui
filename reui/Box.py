'''
A box is a region of a display that can be drawn to. Boxes can optionally have borders.
'''
class Box:
    '''
    width = width of box
    height = height of box
    '''
    def __init__(self, width, height, border_flags):
        self.width = width
        self.height = height
        self.border_flags = border_flags
