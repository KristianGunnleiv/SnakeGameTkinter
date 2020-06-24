#Game positioning system using a grid
#of defined size with possibilities
#for choosing of height and width.

class grid:

    # Takes in canvas to draw to, and sets gridsize and height, width for boxes in the grid
    def __init__(self, canvas, gridsize=10, boxheight=10, boxwidth=10,):
        self.size = gridsize
        self.bxheight = boxheight
        self.bxwidth = boxwidth
        self.totpxlsize = (self.bxheight * self.bxwidth) * self.size
        self.canvas = canvas

    # Draws in one of the boxes in the grid using location object containing
    #  xy position to draw in, as well as a color object to specify color.
    def draw(loc, c):
        pass