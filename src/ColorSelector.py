from tkinter import *
from tkinter.ttk import *

class ColorSelector():
    DEFAULT_COLOR = 'Black'

    def init(self):
 #--------------------main window---------------------
        window = Tk()
        window.title("Pixel Art")
        window.geometry('600x500')

 #--------------------File, edit, ect---------------------

        file = Menu(window)
        new_item = Menu(file)
        new_item.add_command(label='New')
        file.add_cascade(label = 'File', menu = new_item)
        window.config(menu=file)

 #--------------------Top Frame---------------------
        top_frame = Frame(window)
        top_frame.grid(column=0, row=0)
 #--------------------color selecting tool---------------------
        color_selector = Combobox(top_frame)
        color_selector['values'] = ("Black", "Red", "Blue", "Yellow")
        color_selector.current(0)
        color_selector.grid(column=0, row=0)
 #--------------------eraser button---------------------
        eraser_button = Button(top_frame, text="Eraser")
        eraser_button.grid(column=1, row=0)
 #--------------------grid checkbox---------------------
        chk_state = BooleanVar()
        chk_state.set(True) #set check state
        show_grid = Checkbutton(top_frame, text='Show Grid', var=chk_state)
        show_grid.grid(column=2, row=0)
 #--------------------recent colors---------------------
        recent_color1 = Button(top_frame, text="Color1")
        recent_color1.grid(column=4, row=0)
        recent_color2 = Button(top_frame, text="Color2")
        recent_color2.grid(column=5, row=0)
        recent_color3 = Button(top_frame, text="Color3")
        recent_color3.grid(column=6, row=0)
        recent_color4 = Button(top_frame, text="Color4")
        recent_color4.grid(column=7, row=0)
 #--------------------tabs---------------------
        tab_control = Notebook(window)
        tab1 = Frame(tab_control)
        tab_control.add(tab1, text='First')
        tab_control.grid(column = 0, row = 3)
        canvas = Canvas(tab1, width = 500, height = 400)
        canvas.create_rectangle(0, 0,500, 500, fill="white")
        canvas.pack()
        window.mainloop()

def main():
    paint = Paint()
    paint.init()

if __name__ == "__main__":
    main()
