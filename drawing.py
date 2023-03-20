from time import sleep
from os import system, name

#This method is to clear the screen. If it's windows, use cls, otherwise use clear


# for i in range(0, 20):
#     print('\n\n\n')
#     print(' ' * i + '.')
#     sleep(0.1)
#     clear()

# This class it to define the canvas area
class Canvas:
    def __init__(self,width, height):
        self._x = width
        self._y = height
        self._canvas = [['' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >=self._x or point[1]<0 or point[1]>=self._y

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        if name =='nt':
            _=system('cls')
        else:
            _=system('clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print((' '.join([col[y] for col in self._canvas])))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.pos = [0, 0]
        self.framerate=0.2
        self.mark = '*'
        self.trail = '.'

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        #update the position
        self.pos = pos
        self.canvas.setPos(self.pos, self.mark)
        self.canvas.print()
        sleep(self.framerate)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def drawSquare(self, size):
        i = 0
        while i<size:
            self.right()
            i=i+1

        i=0
        while i<size:
            self.down()
            i=i+1

        i=0
        while i<size:
            self.left()
            i=i+1
        
        i=0
        while i<size:
            self.up()
            i=i+1



canvas = Canvas(20,20)
scribe = TerminalScribe(canvas)

# for i in range(0, 10):
    # for j in range(0,10):
        # scribe.draw((i,j))

#Start drawing the square
scribe.drawSquare(6)