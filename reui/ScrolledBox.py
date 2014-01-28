'''
A subclass of the Box class with built-in vertical and horizontal scrolling support. Essentially a large bitmap, of
which a fixed-size portion can be displayed on the screen.
'''

class ScrolledBox(Box):
    '''
    '''
    def __init__(self, width, height, border_flags):
        Box.__init__(self, width, height, border_flags)
