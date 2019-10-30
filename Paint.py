from tkinter import *
from tkinter.ttk import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
import BitCanvas as bc
import io
import os
from PIL import Image, ImageTk

class Paint():
    DEFAULT_COLOR = '#000000'
    BACKGROUND_COLOR = '#afeeee'

    def init(self):
        self.filepath = "C:/Users/Chris/Documents/Paint/images/untitled.jpg"
        self.filenameGiven = False
        self.filetype = "JPEG"

 #--------------------main window---------------------
        self.window = Tk()
        self.window.title("Pixel Paint")
        self.window.geometry('600x550')
        self.window.configure(background=self.BACKGROUND_COLOR)


        titlelabel = Label(self.window, text="Pixel Paint", foreground="black", background = 'white', font = ("Fixedsys", 24))
        titlelabel.pack(side = "top", fill = "both")

        self.top_frame = Frame(self.window, background = "light gray", highlightthickness = 1, highlightbackground="#E6DCDA")
        self.bottom_frame = Frame(self.window, background = self.BACKGROUND_COLOR)
        self.top_frame.pack(side="top", fill="x", expand=False)
        self.bottom_frame.pack(side="bottom", fill="both", expand=True)
 #--------------------File, edit, ect---------------------
        self.menubar = Menu(self.window)

        self.file = Menu(self.menubar, tearoff=0)

        self.file.add_command(label='New')
        self.file.add_command(label="Open")
        self.file.add_command(label="Save", command = self.save)
        self.window.bind_all("<Control-s>", self.save)
        self.file.add_command(label="Save as", command = self.saveAs)
        self.file.add_separator()
        self.file.add_command(label="Exit")
        self.menubar.add_cascade(label='File', menu = self.file)
        self.window.config(menu=self.menubar)

        self.edit=Menu(self.menubar,tearoff=0)
        self.edit.add_command(label="Undo", command = self.undo)
        self.window.bind_all("<Control-z>", self.undo)
        self.menubar.add_cascade(label="Edit", menu=self.edit)
        self.help=Menu(self.menubar,tearoff=0)
        self.help.add_command(label="Help")
        self.menubar.add_cascade(label="Help",menu=self.help)

 #--------------------color selecting tool---------------------
        self.color_selector = Button(self.top_frame, text='Select Color', command= lambda : self.changeColor(askcolor()[1]), highlightthickness = 0, bd = 0, bg = "light gray")
        self.color_selector.pack(side=LEFT, padx=10)
        self.mostRecentColor = self.DEFAULT_COLOR
        self.changedColor = False
        image = Image.open("C:/Users/Chris/Documents/Paint/Button_Images/colorselect.jpg")
        image = image.resize((32, 32), Image.ANTIALIAS)
        colorimg= ImageTk.PhotoImage(image)
        self.color_selector.configure(image=colorimg)

 #--------------------tool buttons---------------------
        self.draw_button = Button(self.top_frame, text="Draw", command = lambda : self.changeColor(self.mostRecentColor), highlightthickness = 0, bd = 0, bg = "light gray")
        self.draw_button.pack(side=LEFT, padx=3)
        image = Image.open("C:/Users/Chris/Documents/Paint/Button_Images/Pencil.png")
        image = image.resize((32, 32), Image.ANTIALIAS)
        pencilimg= ImageTk.PhotoImage(image)
        self.draw_button.configure(image=pencilimg)
        self.eraser_button = Button(self.top_frame, text="Eraser", command = self.setEraser, highlightthickness = 0, bd = 0, bg = "light gray")
        self.eraser_button.pack(side=LEFT, padx=3)
        image = Image.open("C:/Users/Chris/Documents/Paint/Button_Images/Eraser.png")
        image = image.resize((32, 32), Image.ANTIALIAS)
        eraserimg= ImageTk.PhotoImage(image)
        self.eraser_button.configure(image=eraserimg)

#--------------------clear---------------------
        self.clear_button = Button(self.top_frame, text="Clear", command = lambda : self.clear(), highlightthickness = 0, bd = 0, bg = "light gray")
        self.clear_button.pack(side=LEFT, padx=3)
        image = Image.open("C:/Users/Chris/Documents/Paint/Button_Images/Clear.png")
        image = image.resize((32, 32), Image.ANTIALIAS)
        clearimg= ImageTk.PhotoImage(image)
        self.clear_button.configure(image=clearimg)

 #--------------------grid checkbox---------------------
        self.gridOn = IntVar()
        self.gridOn.set(0)
        self.show_grid = Checkbutton(self.top_frame, text='Grid', variable=self.gridOn, command = self.checkGrid, bg = "light gray")
        self.show_grid.pack(side=LEFT, padx=10)

 #--------------------recent colors---------------------
        self.recent_colors = []
        recent_color1 = Button(self.top_frame,
            command =lambda: self.selectRecent(recent_color1), height = 1, width = 2)
        recent_color1.pack(side=LEFT, padx=5)
        self.recent_colors.append(recent_color1)
        recent_color2 = Button(self.top_frame,
            command =lambda: self.selectRecent(recent_color2), height = 1, width = 2)
        recent_color2.pack(side=LEFT, padx=5)
        self.recent_colors.append(recent_color2)
        recent_color3 = Button(self.top_frame,
            command =lambda: self.selectRecent(recent_color3), height = 1, width = 2)
        recent_color3.pack(side=LEFT, padx=5)
        self.recent_colors.append(recent_color3)
        recent_color4 = Button(self.top_frame,
            command =lambda: self.selectRecent(recent_color4), height = 1, width = 2)
        recent_color4.pack(side=LEFT, padx=5)
        self.recent_colors.append(recent_color4)

 #--------------------tabs---------------------
        self.tab_control = Notebook(self.bottom_frame)
        self.tab1 = Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='First')
        self.tab_control.pack(side=LEFT, anchor="nw")

#--------------------canvas---------------------
        self.canvas = bc.BitCanvas()
        self.canvas.init(self.tab1)
        self.setup()
        self.window.mainloop()

    def setup(self):
        self.eraser = False

    def changeColor(self, color):
        #if color selected is already the color, do nothing
        if(color == self.canvas.getColor()):
            return
        #if eraser is on, turn off and change set color
        if(self.eraser == True):
            self.eraser = False
            self.canvas.setColor(color)
            return
        if(self.eraser == False and color == self.mostRecentColor):
            return
        self.addColortoRecents(self.canvas.getColor())
        self.canvas.setColor(color)
        self.mostRecentColor = color

    def addColortoRecents(self,color):
        print(color)
        for i in range(4):
            if self.recent_colors[i].cget('bg') == color:
                return
        self.recent_colors[3].configure(bg = self.recent_colors[2].cget('bg'))
        self.recent_colors[2].configure(bg = self.recent_colors[1].cget('bg'))
        self.recent_colors[1].configure(bg = self.recent_colors[0].cget('bg'))
        self.recent_colors[0].configure(bg = color)

    def selectRecent(self, recentcolor):
        self.canvas.setColor(recentcolor.cget('bg'))

    def setEraser(self):
        self.mostRecentColor = self.canvas.getColor()
        self.eraser = True
        self.canvas.setColor("White")

    def checkGrid(self):
        if self.gridOn.get() == 1:
            self.canvas.drawGrid()
        else:
            self.canvas.removeGrid()

    def saveAs(self):
        ftypes = [('PNG', '*.png'), ('JPEG', '*.jpg'), ('BMP', '*.bmp')]
        extentionmap = {'.jpg':'JPEG', '.bmp':'BMP', '.png':'PNG'}
        #get raw image
        bitmap = self.canvas.getImage()
        bitmap.delete('grid')
        #get filepath from user
        ps = bitmap.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        self.filepath = asksaveasfilename(initialdir = "C:/Users/Chris/Documents/Paint/images/", title = "Select file", defaultextension=".*", filetypes = ftypes)
        #if no path selected, return
        if(self.filepath == ''):
            return
        #save image
        img.save(self.filepath,extentionmap[self.filepath[-4:]])
        self.filenameGiven = True
        #reset canvas
        if self.gridOn.get() == 1:
            self.canvas.drawGrid()

    def save(self, event=None):
        if(self.filenameGiven):
            #get raw image
            bitmap = self.canvas.getImage()
            bitmap.delete('grid')
            #save image
            ps = bitmap.postscript(colormode='color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            img.save(self.filepath + self.fileextension, self.filetype)
            #reset canvas
            if self.gridOn.get() == 1:
                self.canvas.drawGrid()
        else:
            self.saveAs()

    def clear(self):
        self.canvas.clear(self.gridOn.get())

    def undo(self, event=None):
        self.canvas.undo()



def main():
    paint = Paint()
    paint.init()

if __name__ == "__main__":
    main()
