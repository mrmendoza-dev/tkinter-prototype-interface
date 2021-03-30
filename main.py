from tkinter import *
from PIL import ImageTk, Image
from operator import itemgetter
import tkinter.scrolledtext as st
from tkinter import messagebox, filedialog
import io
import sys
import os
from os import listdir
from os.path import isfile, join

#Change output to save to a variable instead of printing to screen
#Changes output method and switches back after assigning
def save_output():
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout


    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    return output


#Declare window size when called, use parameters of window and screen size to determine centerpoint
def center_window(window, width, height):
    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth()/2 - width/2)
    positionDown = int(window.winfo_screenheight()/2 - height/2)

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
    center_window(root, 1200, 1000)

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
    generic_padx = 10
    generic_pady = 10



    #SIMPLE TEXT
    header_text = "TKinter Test Interface"
    header = Label(root, text=header_text).grid(row=0, column=0)

    #FRAMES
    #Main dashboard, 5 rows x 2 columns
    dashboard = LabelFrame(root, text='Dashboard', padx=30, pady=20)
    dashboard.grid(row=1, column=0)
    #Positioning inside frame is independent from root


    #APPS SECTION
    apps_frame = LabelFrame(dashboard, text='Apps', padx=generic_padx, pady=generic_pady)
    apps_frame.grid(row=0, column=0)

    calculator_button = Button(apps_frame, text='Calculator', command=calculator_app).grid(row=0)
    image_viewer_app_button = Button(apps_frame, text='Image Viewer', command=image_viewer_app).grid(row=1)
    database_button = Button(apps_frame, text='Database', command=database_app).grid(row=2)
    weather_app_button = Button(apps_frame, text='Weather', command=weather_app).grid(row=3)



    #INPUT
    input_frame = LabelFrame(dashboard, text='Input Field', padx=generic_padx, pady=generic_pady)
    input_frame.grid(row=0, column=1)

    Label(input_frame, text="Enter Text:").grid(row=0)
    entry_field = StringVar()
    entry = Entry(input_frame, textvariable=input_frame, width=50).grid(row=1, columnspan=2)
    #entry.insert(1, "Enter a cryptocurrency...") #Placeholder text
    global current
    current = entry_field.get()
    print(current)
    Label(input_frame, text=current).grid(row=2)

    def myClick(text):
        Label(input_frame, text=text).grid(row=4)

    Button(input_frame, text="Click Here!", command=lambda: myClick(current)).grid(row=3)


    #RADIOS
    radio_frame = LabelFrame(dashboard, text='Input Field', padx=generic_padx, pady=generic_pady)
    radio_frame.grid(row=0, column=2)

    MODES = [
        ("Option 1", 1),
        ("Option 2", 2),
        ("Option 3", 3),
        ("Option 4", 4),
        ("Option 5", 5),
    ]

    def clicked_radio(value):
        Label(radio_frame, text=value).grid(row=len(MODES)+1)

    mode = IntVar()
    mode.set(0)

    for text, value in MODES:
        Radiobutton(radio_frame, text=text, variable=mode, value=value).grid(column=0)

    Button(radio_frame, text="Select", command=lambda: clicked_radio(mode.get())).grid(column=0)



    #SCROLL BAR
    scroll_frame = LabelFrame(dashboard, text='Output Console', padx=generic_padx, pady=generic_pady)
    scroll_frame.grid(row=0, column=3)


    text_area = st.ScrolledText(scroll_frame, width=30, height=8, font=("Times New Roman", 15))
    text_area.grid(row=0, column=6, rowspan=10, pady=10, padx=10)

    # Inserting Text which is read only
    scrollbar_text = "Test"
    text_area.insert(INSERT, scrollbar_text)

    # Making the text read only
    text_area.configure(state='disabled')












    #BUTTONS FRAME
    button_frame = LabelFrame(dashboard, text='Button Depot', padx=generic_padx, pady=generic_pady)
    button_frame.grid(row=0, column=4)

    #Exit Button
    Button(button_frame, text='Quit', command=root.quit).grid(row=0, column=0)

    button_padx = 30
    button_pady = 20
    Button(button_frame, text='1', padx=button_padx, pady=button_pady).grid(row=1, column=0)
    Button(button_frame, text='2', padx=button_padx, pady=button_pady).grid(row=1, column=1)
    Button(button_frame, text='3', padx=button_padx, pady=button_pady).grid(row=1, column=2)
    Button(button_frame, text='4', padx=button_padx, pady=button_pady).grid(row=2, column=0)
    Button(button_frame, text='5', padx=button_padx, pady=button_pady).grid(row=2, column=1)
    Button(button_frame, text='6', padx=button_padx, pady=button_pady).grid(row=2, column=2)
    Button(button_frame, text='7', padx=button_padx, pady=button_pady).grid(row=3, column=0)
    Button(button_frame, text='8', padx=button_padx, pady=button_pady).grid(row=3, column=1)
    Button(button_frame, text='9', padx=button_padx, pady=button_pady).grid(row=3, column=2)


    Button(button_frame, text="Broken", state=DISABLED).grid(row=6, column=0)

    #MESSAGE BOXES
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    def info_popup():
        messagebox.showinfo('Info', 'Testing...')



    def error_popup():
        messagebox.showerror('Error', 'Virus Detected')


    def ask_popup():
        response = messagebox.askquestion('Continue', 'Continue shutting down computer?')
        if response == 'yes':
            Label(button_frame, text='Shutting Down...').grid(row=10, column=3)
        else:
            Label(button_frame, text='Wrong Choice').grid(row=10, column=3)

    Button(button_frame, text='INFO', command=info_popup).grid(row=10, column=0)
    Button(button_frame, text='ERROR', command=error_popup).grid(row=10, column=1)
    Button(button_frame, text='?', command=ask_popup).grid(row=10, column=2)






    #FILE SEARCH FRAME
    #Will only return locatiom of file (c:\\ etc.)
    file_frame = LabelFrame(dashboard, text='File Search', padx=generic_padx, pady=generic_pady)
    file_frame.grid(row=1, column=0)

    def open_explorer():
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(('png files', '*.png'), ('all files', '*.*')))
        upload_label = Label(file_frame, text=root.filename).grid(row=2, column=0)
    Label(file_frame, text='Search for Files').grid(row=0, column=0)
    Button(file_frame, text='Browse', command=open_explorer).grid(row=1, column=0)



    #SLIDER FRAME
    slider_frame = LabelFrame(dashboard, text='Sliders', padx=generic_padx, pady=generic_pady)
    slider_frame.grid(row=1, column=1)

    vh_sum = 0
    Label(slider_frame, text="X + Y = " + str(vh_sum)).grid(row=3, column=3)

    def slide(var):
        vh_sum = vertical.get() + horizontal.get()
        Label(slider_frame, text="X + Y = " + str(vh_sum)).grid(row=3, column=3)

    horizontal = Scale(slider_frame, from_=0, to=1000, orient=HORIZONTAL, command=slide)
    Label(slider_frame, text="X-Slider").grid(row=0, column=0)
    horizontal.grid(row=1, column=0)

    vertical = Scale(slider_frame, from_=0, to=1000, command=slide)
    Label(slider_frame, text="Y-Slider").grid(row=0, column=1)
    vertical.grid(row=1, column=1)


    #CHECKBOXES FRAME
    checkbox_frame = LabelFrame(dashboard, text='Checkbox', padx=generic_padx, pady=generic_pady)
    checkbox_frame.grid(row=1, column=2)

    #DROPDOWN FRAME
    dropdown_frame = LabelFrame(dashboard, text='Dropdown', padx=generic_padx, pady=generic_pady)
    dropdown_frame.grid(row=1, column=3)



def calculator_app():
    top = Toplevel()
    top.title('Calculator')
    center_window(top, 290, 435)

    e = Entry(top, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def button_click(number):
        current = e.get()
        new_number = str(current) + str(number)
        e.delete(0, END)
        e.insert(0, new_number)

    def button_clear():
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
    button_equal = Button(top, text='=', padx=90, pady=20, command=button_equal)
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
    global image_label
    top = Toplevel()
    top.title('Image Viewer')

    center_window(top, 850, 900)

    #Check folder for any files and add them to image_list
    folder = 'images'
    image_files = [f for f in listdir(folder) if isfile(join(folder, f))]
    image_list = []

    for filename in image_files:
        file = os.path.join(folder, filename)
        image_object = ImageTk.PhotoImage(Image.open(file))
        image_list.append(image_object)

    status = Label(top, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    image_label = Label(top, image=image_list[0])
    image_label.grid(row=0, column=0, columnspan=3)


    def forward(image_number):
        global image_label
        global button_forward
        global button_back

        image_label.grid_forget()
        image_label = Label(top, image=image_list[image_number-1])

        if image_number == len(image_list):
            button_forward = Button(top, text=">>", state=DISABLED)
        else:
            button_forward = Button(top, text=">>", command=lambda: forward(image_number+1))
        button_back = Button(top, text="<<", command=lambda: back(image_number-1))

        image_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)

        status = Label(top, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    def back(image_number):
        global image_label
        global button_forward
        global button_back

        image_label.grid_forget()
        image_label = Label(top, image=image_list[image_number-1])

        button_forward = Button(top, text=">>", command=lambda: forward(image_number+1))
        if image_number == 1:
            button_back = Button(top, text="<<", state=DISABLED)
        else:
            button_back = Button(top, text="<<", command=lambda: back(image_number-1))

        image_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)

        status = Label(top, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    button_back = Button(top, text="<<", command=back, state=DISABLED)
    button_exit = Button(top, text="Exit", command=top.destroy)
    button_forward = Button(top, text=">>", command=lambda: forward(2))


    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)

    status.grid(row=2, column=0, columnspan=3, sticky=W+E)



def database_app():
    top = Toplevel()
    top.title('Database')
    center_window(top, 300, 300)

def weather_app():
    top = Toplevel()
    top.title('Weather')
    center_window(top, 300, 300)

def main():
    root = create_root()
    #sidebar = create_sidebar()


    homepage(root)



    root.mainloop()





if __name__ == '__main__':
    main()