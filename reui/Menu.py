'''
A Box containing a vertical-scrolling menu. Generates event when a menu item is selected. Supports submenus.
'''

class Menu(ScrolledBox):
    '''
    Initialize Menu object
    '''
    def __init__(self, width, height, border_flags):
        ScrolledBox.__init__(self, width, height, border_flags)
