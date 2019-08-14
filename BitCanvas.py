from tkinter import *
from tkinter.ttk import *
import math

class BitCanvas():
    BACKGROUND_COLOR = 'white'
    DEFAULT_COLOR = 'black'
    CANVAS_WIDTH = 500
    CANVAS_HEIGHT = 400


    def init(self, tab):
        self.canvas = Canvas(tab, width = self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT)
        self.canvas.configure(background=self.BACKGROUND_COLOR)
        self.canvas.pack()

        self.canvas.bind('<Button-1>', self.drawLine)
        self.canvas.bind('<B1-Motion>', self.drawLine)
        self.old_x = None
        self.old_y = None

        self.color = self.DEFAULT_COLOR

        self.eraser = False

        self.drawGrid()

    def drawLine(self, event):

        bottom_x = math.floor(event.x/self.CANVAS_WIDTH*64)/64 * self.CANVAS_WIDTH
        bottom_y = math.floor(event.y/self.CANVAS_HEIGHT*64)/64* self.CANVAS_HEIGHT
        top_x = math.ceil(event.x/self.CANVAS_WIDTH*64)/64* self.CANVAS_WIDTH
        top_y = math.ceil(event.y/self.CANVAS_HEIGHT*64)/64* self.CANVAS_HEIGHT
        self.canvas.create_rectangle(bottom_x, bottom_y, top_x, top_y, fill = self.color)


    def drawGrid(self):
        for i in range(1,64):
            self.canvas.create_line(0, self.CANVAS_HEIGHT/64*i, self.CANVAS_WIDTH, self.CANVAS_HEIGHT/64*i,
                               width=1, fill='black',
                               capstyle=ROUND, smooth=TRUE, splinesteps=36, tags = 'grid')
        for i in range(1,64):
            self.canvas.create_line(self.CANVAS_WIDTH/64*i, 0, self.CANVAS_WIDTH/64*i,self.CANVAS_HEIGHT,
                               width=1, fill='black',
                               capstyle=ROUND, smooth=TRUE, splinesteps=36, tags='grid')

    def removeGrid(self):
        self.canvas.delete('grid')


    def setColor(self, color):
        self.color = color
