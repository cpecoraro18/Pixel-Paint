from tkinter import *
from tkinter.ttk import *
from tkinter.colorchooser import *
import BitCanvas as bc

class Paint():
    DEFAULT_COLOR = 'Black'

    def init(self):
 #--------------------main window---------------------
        self.window = Tk()
        self.window.title("Pixel Art")
        self.window.geometry('800x500')

 #--------------------File, edit, ect---------------------
        self.menubar = Menu(self.window)

        self.file = Menu(self.menubar, tearoff=0)
        self.file.add_command(label='New')
        self.file.add_command(label="Open")
        self.file.add_command(label="Save")
        self.file.add_command(label="Save as")
        self.file.add_separator()
        self.file.add_command(label="Exit")
        self.menubar.add_cascade(label='File', menu = self.file)
        self.window.config(menu=self.menubar)

        self.edit=Menu(self.menubar,tearoff=0)
        self.edit.add_command(label="Undo")
        self.edit.add_command(label="Copy")
        self.edit.add_command(label="Paste")
        self.menubar.add_cascade(label="Edit", menu=self.edit)

        self.help=Menu(self.menubar,tearoff=0)
        self.help.add_command(label="Help")
        self.menubar.add_cascade(label="Help",menu=self.help)

 #--------------------Top Frame---------------------
        self.top_frame = Frame(self.window)
        self.top_frame.grid(column=0, row=0)

 #--------------------color selecting tool---------------------
        self.color_selector = Button(self.top_frame, text='Select Color', command= lambda : self.changeColor(askcolor()[1]))
        self.color_selector.grid(column=0, row=0)
        self.mostRecentColor = self.DEFAULT_COLOR

 #--------------------tool buttons---------------------
        self.draw_button = Button(self.top_frame, text="Draw", command = lambda : self.changeColor(self.mostRecentColor))
        self.draw_button.grid(column=1, row=0)
        self.eraser_button = Button(self.top_frame, text="Eraser", command = self.setEraser)
        self.eraser_button.grid(column=2, row=0)

#--------------------clear---------------------
        self.clear_button = Button(self.top_frame, text="Clear", command = lambda : self.clear())
        self.clear_button.grid(column=3, row=0)

#--------------------undo---------------------
        #self.undo_button = Button(self.top_frame, text="Clear", command = lambda : self.canvas.undo())
        #self.undo_button.grid(column=4, row=0)



 #--------------------grid checkbox---------------------
        self.chk_state = BooleanVar()
        self.chk_state.set(True) #set check state
        self.show_grid = Checkbutton(self.top_frame, text='Show Grid', var=self.chk_state, command = self.checkGrid)
        self.show_grid.grid(column=5, row=0)


 #--------------------recent colors---------------------
        self.recent_colors = []
        for i in range(4):
            recent_color = Button(self.top_frame,
                command =lambda: self.selectRecent(self))
            recent_color.grid(column=6+i, row=0)
            recent_color
            self.recent_colors.append(recent_color)

 #--------------------tabs---------------------
        self.tab_control = Notebook(self.window)
        self.tab1 = Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='First')
        self.tab_control.grid(column = 0, row = 3)

#--------------------canvas---------------------
        self.canvas = bc.BitCanvas()
        self.canvas.init(self.tab1)
        self.setup()
        self.window.mainloop()

    def setup(self):
        self.eraser = False

    def changeColor(self, color):
        #for c in self.recent_colors:
            #c.configure()
            #if c.cget('bg') == "" or c.cget('bg') == color:
                #c.set(color)
                #break
        self.canvas.setColor(color)

    def selectRecent(self, color):
        self.canvas.setColor(color)

    def setEraser(self):
        self.mostRecentColor = self.canvas.getColor()
        self.canvas.setColor("White")

    def checkGrid(self):
        if self.chk_state.get() == True:
            self.canvas.drawGrid()
        else:
            self.canvas.removeGrid()

    def saveAs(self):
        self.canvas.getImage()

    def clear(self):
        self.canvas.clear(self.chk_state)


def main():
    paint = Paint()
    paint.init()

if __name__ == "__main__":
    main()
