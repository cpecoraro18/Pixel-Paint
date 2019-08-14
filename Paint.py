from tkinter import *
from tkinter.ttk import *
import BitCanvas as bc

class Paint():
    DEFAULT_COLOR = 'Black'

    def init(self):
 #--------------------main window---------------------
        self.window = Tk()
        self.window.title("Pixel Art")
        self.window.geometry('800x500')

 #--------------------File, edit, ect---------------------

        self.file = Menu(self.window)
        self.new_item = Menu(self.file)
        self.new_item.add_command(label='New')
        self.file.add_cascade(label = 'File', menu = self.new_item)
        self.window.config(menu=self.file)

 #--------------------Top Frame---------------------
        self.top_frame = Frame(self.window)
        self.top_frame.grid(column=0, row=0)

 #--------------------color selecting tool---------------------
        self.color_selector = Combobox(self.top_frame)
        self.color_selector['values'] = ("Black", "Red", "Blue", "Yellow")
        self.color_selector.current(0)
        self.color_selector.grid(column=0, row=0)

        self.color_selector.bind("<<ComboboxSelected>>", self.changeColor)

 #--------------------tool buttons---------------------
        self.draw_button = Button(self.top_frame, text="Draw", command = lambda : self.changeColor(None))
        self.draw_button.grid(column=1, row=0)
        self.eraser_button = Button(self.top_frame, text="Eraser", command = self.setEraser)
        self.eraser_button.grid(column=2, row=0)

 #--------------------grid checkbox---------------------
        self.chk_state = BooleanVar()
        self.chk_state.set(True) #set check state
        self.show_grid = Checkbutton(self.top_frame, text='Show Grid', var=self.chk_state, command = self.checkGrid)
        self.show_grid.grid(column=3, row=0)

 #--------------------recent colors---------------------
        self.recent_colors = []
        self.recent_color1text = StringVar()
        self.recent_color1 = Button(self.top_frame, textvariable = self.recent_color1text,
            command =lambda: self.selectRecent(self.recent_color1text))
        self.recent_color1.grid(column=4, row=0)
        self.recent_colors.append(self.recent_color1text)

        self.recent_color2text = StringVar()
        self.recent_color2 = Button(self.top_frame, textvariable = self.recent_color2text,
            command =lambda: self.selectRecent(self.recent_color2text))
        self.recent_color2.grid(column=5, row=0)
        self.recent_colors.append(self.recent_color2text)

        self.recent_color3text = StringVar()
        self.recent_color3 = Button(self.top_frame, textvariable = self.recent_color3text,
            command =lambda: self.selectRecent(self.recent_color3text))
        self.recent_color3.grid(column=6, row=0)
        self.recent_colors.append(self.recent_color3text)

        self.recent_color4text = StringVar()
        self.recent_color4 = Button(self.top_frame, textvariable = self.recent_color4text,
            command =lambda: self.selectRecent(self.recent_color4text))
        self.recent_color4.grid(column=7, row=0)
        self.recent_colors.append(self.recent_color4text)

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

    def changeColor(self, event):
        for color in self.recent_colors:
            if color.get() == "" or color.get() == self.color_selector.get():
                color.set(self.color_selector.get())
                break
        self.canvas.setColor(self.color_selector.get())

    def selectRecent(self, color):
        self.canvas.setColor(color.get())

    def setEraser(self):
        self.canvas.setColor('White')

    def checkGrid(self):
        if self.chk_state.get() == True:
            self.canvas.drawGrid()
        else:
            self.canvas.removeGrid()

def main():
    paint = Paint()
    paint.init()

if __name__ == "__main__":
    main()
