from tkinter import *
from tkinter.ttk import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
import BitCanvas as bc
import io
import os
from PIL import Image, ImageTk

class Paint():
    DEFAULT_COLOR = 'Black'
    BACKGROUND_COLOR = '#afeeee'

    def init(self):
        self.filepath = "C:/Users/Chris/Documents/Paint/images/untitled"
        self.filenameGiven = False
 #--------------------main window---------------------
        self.window = Tk()
        self.window.title("Pixel Paint")
        self.window.geometry('600x550')
        self.window.configure(background=self.BACKGROUND_COLOR)
        self.window.columnconfigure(0, weight=1)


        titlelabel = Label(self.window, text="Pixel Paint", foreground="black", background = 'white', font = ("Fixedsys", 24))
        titlelabel.grid(row=0, column=0, sticky='ew')
        titlelabel.configure(anchor=CENTER)
 #--------------------File, edit, ect---------------------
        self.menubar = Menu(self.window)

        self.file = Menu(self.menubar, tearoff=0)

        self.file.add_command(label='New')
        self.file.add_command(label="Open")
        self.file.add_command(label="Save", command = self.save)
        self.file.add_command(label="Save as", command = self.saveAs)
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
        self.top_frame.grid(column=0, row=1)

 #--------------------color selecting tool---------------------
        self.color_selector = Button(self.top_frame, text='Select Color', command= lambda : self.changeColor(askcolor()[1]))
        self.color_selector.grid(column=0, row=0)
        self.mostRecentColor = self.DEFAULT_COLOR
        image = Image.open("C:/Users/Chris/Documents/Paint/Button_Images/colorselect.jpg")
        image = image.resize((25, 25), Image.ANTIALIAS)
        colorimg= ImageTk.PhotoImage(image)
        self.color_selector.configure(image=colorimg)

 #--------------------tool buttons---------------------
        self.draw_button = Button(self.top_frame, text="Draw", command = lambda : self.changeColor(self.mostRecentColor))
        self.draw_button.grid(column=1, row=0)
        image = Image.open("C:/Users/Chris/Documents/Paint/Button_Images/Pencil.jpg")
        image = image.resize((25, 25), Image.ANTIALIAS)
        pencilimg= ImageTk.PhotoImage(image)
        self.draw_button.configure(image=pencilimg)
        self.eraser_button = Button(self.top_frame, text="Eraser", command = self.setEraser)
        self.eraser_button.grid(column=2, row=0)
        image = Image.open("C:/Users/Chris/Documents/Paint/Button_Images/Eraser.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        eraserimg= ImageTk.PhotoImage(image)
        self.eraser_button.configure(image=eraserimg)

#--------------------clear---------------------
        self.clear_button = Button(self.top_frame, text="Clear", command = lambda : self.clear())
        self.clear_button.grid(column=3, row=0)
        image = Image.open("C:/Users/Chris/Documents/Paint/Button_Images/clear.jpg")
        image = image.resize((25, 25), Image.ANTIALIAS)
        clearimg= ImageTk.PhotoImage(image)
        self.clear_button.configure(image=clearimg)

 #--------------------grid checkbox---------------------
        self.gridOn = IntVar()
        self.gridOn.set(0)
        self.show_grid = Checkbutton(self.top_frame, text='Grid', variable=self.gridOn, command = self.checkGrid)
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

        self.canvas.setColor(color)

    def selectRecent(self, color):
        self.canvas.setColor(color)

    def setEraser(self):
        self.mostRecentColor = self.canvas.getColor()
        self.canvas.setColor("White")

    def checkGrid(self):
        if self.gridOn.get() == 1:
            self.canvas.drawGrid()
        else:
            self.canvas.removeGrid()

    def saveAs(self):
        bitmap = self.canvas.getImage()
        bitmap.delete('grid')
        ps = bitmap.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.filepath = asksaveasfilename(initialdir = "C:/Users/Chris/Documents/Paint/images/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        img.save(self.filepath + ".jpg", 'JPEG')
        self.filenameGiven = True
        if self.gridOn.get() == 1:
            self.canvas.drawGrid()

    def save(self):
        if(self.filenameGiven):
            bitmap = self.canvas.getImage()
            bitmap.delete('grid')
            ps = bitmap.postscript(colormode='color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            img.save(self.filepath + ".jpg", 'JPEG')
            if self.gridOn.get() == 1:
                self.canvas.drawGrid()
        else:
            self.saveAs()

    def clear(self):
        self.canvas.clear(self.gridOn.get())



def main():
    paint = Paint()
    paint.init()

if __name__ == "__main__":
    main()
