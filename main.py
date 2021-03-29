from tkinter import *
from PIL import ImageTk, Image
from operator import itemgetter
import tkinter.scrolledtext as st
import io
import sys





#Change output to save to a variable instead of printing to screen
#Changes output method and switches back after assigning
def save_output():
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout


    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    return output



def center_window(window, width, height):
    # Gets the requested values of the height and width.
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)
    # Positions the window in the center of the page.
    window.geometry("+{}+{}".format(positionRight, positionDown))
    size = "{}x{}".format(width, height)
    window.geometry(size)
    return window


def create_root():
    #Root of all widgets
    root = Tk()
    title_text = "TK Sesh"
    root.title(title_text)
    center_window(root, 1000, 500)

    #Change window icon
    p1 = PhotoImage(file='bitcoin.png')
    root.iconphoto(False, p1)
    return root


def create_sidebar():
    #Root of all widgets
    top = Toplevel()
    top.title('sidebar')
    top.geometry('300x500')
    close_button = Button(top, text='Close Sidebar', command=top.destroy).grid()
    return top



#Homepage function is main window which adds upon root
def homepage(root):
    #Text Widget
    # myLabel2 = Label(root, text=text)
    header_text = "Header Text"
    header = Label(root, text=header_text).grid(row=0, column=0)
    exit_button = Button(root, text='Quit', command=root.quit).grid(row=3, column=1)



    #Input Widget
    entry_field = StringVar()
    entry = Entry(root, textvariable=entry_field, width=50).grid(row=1, column=0, columnspan=2)
    #entry.insert(1, "Enter a cryptocurrency...") #Placeholder text


    #BUTTONS
    #Button Widget
    def myClick(text):
        myLabel = Label(root, text=text)
        myLabel.grid(row=0, column=3)

    button_text = "Click Here"
    button = Button(root, text=button_text, command=lambda: myClick(entry_field.get()), padx=30).grid(row=3, column=0)
    # button_label = Button(root, text=button_text, state=DISABLED)
    current_crypto = entry_field.get()



    calculator_button = Button(root, text='Calculator', command=calculator_app).grid()
    image_viewer_app_button = Button(root, text='Image Viewer', command=image_viewer_app).grid()
    database_button = Button(root, text='Database', command=database_app).grid()



    #Radio Widget
    #Takes in filter as variable, prints out filtered list
    def clicked_radio(value):
        myLabel = Label(root, text=value).grid(row=11, column=5)

    MODES = [
        ("Option 1", 1),
        ("Option 2", 2),
        ("Option 3", 3),
        ("Option 4", 4),
        ("Option 5", 5),
    ]

    mode = IntVar()
    mode.set(0)

    for text, value in MODES:
        Radiobutton(root, text=text, variable=mode, value=value).grid(column=5)

    radio_button = Button(root, text="Select", command=lambda: clicked_radio(mode.get())).grid(row=10, column=5)




    #Text scroll bar
    text_area = st.ScrolledText(root, width=30, height=8, font=("Times New Roman", 15))
    text_area.grid(row=0, column=6, rowspan=10, pady=10, padx=10)

    # Inserting Text which is read only
    scrollbar_text = "Test"
    text_area.insert(INSERT, scrollbar_text)

    # Making the text read only
    text_area.configure(state='disabled')



def calculator_app():
    top = Toplevel()
    top.title('Calculator')
    center_window(top, 300, 600)

    e = Entry(top, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def button_click(number):
        # e.delete(0, END)
        current = e.get()
        new_number = str(current) + str(number)
        e.delete(0, END)
        e.insert(0, new_number)

    def button_clear():
        current = e.get()
        e.delete(0, END)

    def button_equal():
        second_num = e.get()
        e.delete(0, END)

        if math == 'addition':
            e.insert(0, f_num + float(second_num))
        elif math == 'subtraction':
            e.insert(0, f_num - float(second_num))
        elif math == 'multiplication':
            e.insert(0, f_num * float(second_num))
        elif math == 'division':
            e.insert(0, f_num / float(second_num))


    def button_add():
        first_num = e.get()
        global f_num
        global math
        math = 'addition'
        f_num = float(first_num)
        e.delete(0, END)

    def button_subtract():
        first_num = e.get()
        global f_num
        global math
        math = 'subtraction'
        f_num = float(first_num)
        e.delete(0, END)

    def button_multiply():
        first_num = e.get()
        global f_num
        global math
        math = 'multiplication'
        f_num = float(first_num)
        e.delete(0, END)

    def button_divide():
        first_num = e.get()
        global f_num
        global math
        math = 'division'
        f_num = float(first_num)
        e.delete(0, END)


    #lambda: is needed to pass parameters in function
    button_1 = Button(top, text='1', padx=40, pady=20, command=lambda: button_click(1))
    button_2 = Button(top, text='2', padx=40, pady=20, command=lambda: button_click(2))
    button_3 = Button(top, text='3', padx=40, pady=20, command=lambda: button_click(3))
    button_4 = Button(top, text='4', padx=40, pady=20, command=lambda: button_click(4))
    button_5 = Button(top, text='5', padx=40, pady=20, command=lambda: button_click(5))
    button_6 = Button(top, text='6', padx=40, pady=20, command=lambda: button_click(6))
    button_7 = Button(top, text='7', padx=40, pady=20, command=lambda: button_click(7))
    button_8 = Button(top, text='8', padx=40, pady=20, command=lambda: button_click(8))
    button_9 = Button(top, text='9', padx=40, pady=20, command=lambda: button_click(9))
    button_0 = Button(top, text='0', padx=40, pady=20, command=lambda: button_click(0))

    button_add = Button(top, text='+', padx=39, pady=20, command=button_add)
    button_equal = Button(top, text='=', padx=91, pady=20, command=button_equal)
    button_clear = Button(top, text='C', padx=91, pady=20, command=button_clear)

    button_subtract = Button(top, text='-', padx=41, pady=20, command=button_subtract)
    button_multiply = Button(top, text='x', padx=40, pady=20, command=button_multiply)
    button_divide = Button(top, text='/', padx=40, pady=20, command=button_divide)


    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)
    button_clear.grid(row=4, column=1, columnspan=2)

    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)



def image_viewer_app():
    top = Toplevel()
    top.title('Image Viewer')
    center_window(top, 300, 300)


def database_app():
    top = Toplevel()
    top.title('Database')
    center_window(top, 300, 300)



def main():
    root = create_root()
    sidebar = create_sidebar()


    homepage(root)



    root.mainloop()





if __name__ == '__main__':
    main()