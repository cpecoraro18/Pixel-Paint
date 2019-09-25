from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import math

class BitCanvas():
    BACKGROUND_COLOR = 'white'
    DEFAULT_COLOR = 'black'
    CANVAS_WIDTH = 500
    CANVAS_HEIGHT = 400
    gridDim = 24


    def init(self, tab):
        #--------------------main canvas---------------------
        self.canvas = Canvas(tab, width = self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT)
        self.canvas.configure(background=self.BACKGROUND_COLOR)
        self.canvas.pack()

        self.canvas.bind('<Button-1>', self.drawLine)
        self.canvas.bind('<B1-Motion>', self.drawLine)
        #--------------------coordinates for drawing lines---------------------
        self.old_x = None
        self.old_y = None
        #--------------------color---------------------
        self.color = self.DEFAULT_COLOR
        #--------------------eraser active---------------------
        self.eraser = False

        self.undoStack = []

        self.drawGrid()

    def drawLine(self, event):
        #draws square based on clock event and grid
        bottom_x = math.floor(event.x/self.CANVAS_WIDTH*self.gridDim)/self.gridDim * self.CANVAS_WIDTH
        bottom_y = math.floor(event.y/self.CANVAS_HEIGHT*self.gridDim)/self.gridDim* self.CANVAS_HEIGHT
        top_x = math.ceil(event.x/self.CANVAS_WIDTH*self.gridDim)/self.gridDim* self.CANVAS_WIDTH
        top_y = math.ceil(event.y/self.CANVAS_HEIGHT*self.gridDim)/self.gridDim* self.CANVAS_HEIGHT
        x = self.canvas.create_rectangle(bottom_x, bottom_y, top_x, top_y, outline="",  fill = self.color)
        self.undoStack.append(x)
        self.canvas.tag_raise('grid')


    def drawGrid(self):
        #top to bottom lines
        for i in range(1,self.gridDim):
            self.canvas.create_line(0, self.CANVAS_HEIGHT/self.gridDim*i, self.CANVAS_WIDTH, self.CANVAS_HEIGHT/self.gridDim*i,
                               width=1, fill='black',
                               capstyle=ROUND, smooth=TRUE, splinesteps=36, tags = 'grid')
        #left to right lines
        for i in range(1,self.gridDim):
            self.canvas.create_line(self.CANVAS_WIDTH/self.gridDim*i, 0, self.CANVAS_WIDTH/self.gridDim*i,self.CANVAS_HEIGHT,
                               width=1, fill='black',
                               capstyle=ROUND, smooth=TRUE, splinesteps=36, tags='grid')

    def removeGrid(self):
        self.canvas.delete('grid')


    def setColor(self, color):
        if color == "White":
            eraser = True
            self.color = "White"
        else:
            eraser = False
            self.color = color
    def getColor(self):
        return self.color

    def getImage(self):
        return

    def clear(self, gridOn):
        self.canvas.delete('all')
        if gridOn:
            self.drawGrid()
    def undo():
        x = self.stack.pop()
        self.canvas.delete(x)
