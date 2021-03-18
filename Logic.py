#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vaibhav account
#
# Created:     13/12/2020
# Copyright:   (c) vaibhav account 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox

def say(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def intro():
    name = "Vaibhav" #Change to whatever name you want
    top = Tk()
    top.title('Hello')
    label = Label(top, text = f'Hello')
    label.pack()
    say(f'Hello')

    def change():
        label.config(text = "We are setting things up...")
        say("We are setting things up...")

    top.after(3000, change)
    top.after(6000, Notepad)
    top.after(9000, top.destroy)


    mainloop()

def Notepad():

    root = Tk()
    root.title('Untitled - Notepad')
    root.geometry('750x509')
    root.iconbitmap('C:\Vaibhav\CNotepad.ico')
#-----------rft--------------------------------------------------------------------
    global open_status_name
    open_status_name = text_file = False

    global selected
    selected = False

#-------------------------------------------------------------------------------


    def new_file():
        my_text.delete("1.0", END)

        root.title('Untitled - Notepad')
        status_bar.config(text = "New file  ")

        global open_status_name
        open_status_name = text_file = False


    def open_file():
        my_text.delete("1.0", END)

        text_file = filedialog.askopenfilename(initialdir="C:/Vaibhav/Coding/GUI interface with python/Forms/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files", "*.*")))

        if text_file:
            global open_status_name
            open_status_name = text_file

        name = text_file
        status_bar.config(text = f'{name}')
        name = name.replace("C:/Vaibhav/Coding/GUI interface with python/", "")
        root.title(f'{name} - notepad')

        text_file = open(text_file, 'r')
        stuff = text_file.read()

        my_text.insert(END, stuff)
        text_file.close()

    def save_as_file():
        text_file = filedialog.asksaveasfilename(defaultextension = ".*", initialdir = "C:/Vaibhav/Coding/GUI interface with python/", title = "Save file as", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files", "*.*")))
        if text_file:
            name = text_file
            status_bar.config(text = 'New file has been saved.')
            messagebox.showinfo("File saved.", "New file have been saved.")
            name = name.replace("C:/Vaibhav/Coding/GUI interface with python/", "")
            root.title(f'{name} - notepad')

            text_file = open(text_file, 'w')
            text_file.write(my_text.get(1.0, END))

            text_file.close()

            messagebox.showwarning("Effects", "All effects will be deleted. (Underlines, Italics, colours, etc..)")

    def save_file(e):
        global open_status_name
        if e:
            if open_status_name:
                text_file = open(open_status_name, 'w')
                text_file.write(my_text.get(1.0, END))
                text_file.close()

                status_bar.config(text = f'Existing file has been saved: {open_status_name}    ')
                messagebox.showwarning("Effects", "All effects will be deleted. (Underlines, Italics, colours, etc..)")
                messagebox. showinfo("File saved.", "Existing file have been saved.")

            else:
                save_as_file()
                messagebox.showwarning("Effects", "All effects will be deleted. (Underlines, Italics, colours, etc..)")

    def cut_text(e):
        global selected
        if e:
            selected = root.clipboard_get()
        else:
            if my_text.selection_get():
                selected = my_text.selection_get()
                my_text.delete("sel.first", "sel.last")
                root.clipboard_clear()
                root.clipboard_append(selected)

    def copy_text(e):
        global selected
        if e:
            selected = root.clipboard_get()

        if my_text.selection_get():
            selected = my_text.selection_get()
            root.clipboard_clear()
            root.clipboard_append(selected)


    def paste_text(e):
        global selected
        if e:
            selected = root.clipboard_get()
        else:
            if selected:
                position = my_text.index(INSERT)
                my_text.insert(position, selected)


    def bold_it(e):
        if e:
            bold_font = font.Font(my_text, my_text.cget("font"))
            bold_font.configure(weight = "bold")

            my_text.tag_configure("bold", font = bold_font)

            current_tags = my_text.tag_names("sel.first")

            if "bold" in current_tags:
                my_text.tag_remove("bold", "sel.first", "sel.last")

            else:
                my_text.tag_add("bold", "sel.first", "sel.last")

        else:
            bold_font = font.Font(my_text, my_text.cget("font"))
            bold_font.configure(weight = "bold")

            my_text.tag_configure("bold", font = bold_font)

            current_tags = my_text.tag_names("sel.first")

            if "bold" in current_tags:
                my_text.tag_remove("bold", "sel.first", "sel.last")

            else:
                my_text.tag_add("bold", "sel.first", "sel.last")

    def italics_it(e):
        if e:
            italics_font = font.Font(my_text, my_text.cget("font"))
            italics_font.configure(slant = "italic")

            my_text.tag_configure("italic", font = italics_font)

            current_tags = my_text.tag_names("sel.first")

            if "italic" in current_tags:
                my_text.tag_remove("italic", "sel.first", "sel.last")

            else:
                my_text.tag_add("italic", "sel.first", "sel.last")

        else:
            italics_font = font.Font(my_text, my_text.cget("font"))
            italics_font.configure(slant = "italic")

            my_text.tag_configure("italic", font = italics_font)

            current_tags = my_text.tag_names("sel.first")

            if "italic" in current_tags:
                my_text.tag_remove("italic", "sel.first", "sel.last")

            else:
                my_text.tag_add("italic", "sel.first", "sel.last")

    def underline_it(e):
        if e:
            italics_font = font.Font(my_text, my_text.cget("font"))
            italics_font.configure(underline = True)

            my_text.tag_configure("underline", font = italics_font)

            current_tags = my_text.tag_names("sel.first")

            if "underline" in current_tags:
                my_text.tag_remove("underline", "sel.first", "sel.last")

            else:
                my_text.tag_add("underline", "sel.first", "sel.last")

        else:
            italics_font = font.Font(my_text, my_text.cget("font"))
            italics_font.configure(underline = True)

            my_text.tag_configure("underline", font = italics_font)

            current_tags = my_text.tag_names("sel.first")

            if "underline" in current_tags:
                my_text.tag_remove("underline", "sel.first", "sel.last")

            else:
                my_text.tag_add("underline", "sel.first", "sel.last")

    def text_color():

        my_color = colorchooser.askcolor()[1]

        if my_color:

            color_font = font.Font(my_text, my_text.cget("font"))
            #color_font.configure(slant = "italic")

            my_text.tag_configure("colored", font = color_font, foreground = my_color)

            current_tags = my_text.tag_names("sel.first")

            if "colored" in current_tags:
                my_text.tag_remove("colored", "sel.first", "sel.last")

            else:
                my_text.tag_add("colored", "sel.first", "sel.last")

    def bg_color():
        my_color = colorchooser.askcolor()[1]
        if my_color:
            my_text.config(bg=my_color)

    def all_text_color():
        my_color = colorchooser.askcolor()[1]
        if my_color:
            my_text.config(fg=my_color)

    def print_file():
        printer_name = win32print.GetDefaultPrinter()
        status_bar.config(text = printer_name)
        file_to_print = filedialog.askopenfilename(initialdir="C:/Vaibhav/Coding/GUI interface with python/Forms/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files", "*.*")))

        if file_to_print:
            messagebox.showinfo("Printing File.", "Press ok to start printing")
            win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)

    def about_help():
        messagebox.showwarning("Notepad Copyright", "The author of this is Vaibhav Dachavaram. Copyright Protected.")

    #
    def select_all():
        my_text.tag_add('sel', '1.0', 'end')

    def clear_all():
        my_text.delete(1.0, END)

    def dark_mode():
        dark_mode_color = "#373737"

        root.config(bg="black")
        my_text.config(bg=dark_mode_color, fg="white", selectbackground = "yellow", selectforeground = "black", insertbackground="white")
        color_menu.config(bg="black", fg="white")
        file_menu.config(bg="black", fg="white")
        edit_menu.config(bg="black", fg="white")
        font_menu.config(bg="black", fg="white")
        about_menu.config(bg="black", fg="white")
        mode_menu.config(bg="black", fg="white")
        status_bar.config(bg=dark_mode_color, fg="white")
        toolbar_frame.config(bg=dark_mode_color)
        left_button.config(bg="black", fg = "white")
        right_button.config(bg="black", fg = "white")
        middle_button.config(bg="black", fg = "white")
        try:
            top.config(bg="black")

        except:
            pass


    def light_mode():
        main_color = "SystemButtonFace"
        second_color = "SystemButtonFace"
        text_color = "black"
        cursor_color="black"

        root.config(bg=main_color)
        my_text.config(bg="white", fg=text_color, selectbackground = "light grey", selectforeground = "black", insertbackground=cursor_color)
        color_menu.config(bg=main_color, fg="black")
        file_menu.config(bg=main_color, fg="black")
        edit_menu.config(bg=main_color, fg="black")
        font_menu.config(bg=main_color, fg="black")
        about_menu.config(bg=main_color, fg="black")
        mode_menu.config(bg=main_color, fg="black")
        status_bar.config(bg=main_color, fg="black")

        toolbar_frame.config(bg=main_color)
        left_button.config(bg=second_color, fg = text_color)
        right_button.config(bg=second_color, fg = text_color)
        middle_button.config(bg=second_color, fg = text_color)

    def tiwme(e):
        if e:
            status_bar.config(text=time.strftime("%H:%M"))

        status_bar.config(text=time.strftime("%H:%M"))

    def Gmail(e):
        global selected
        warning = messagebox.askokcancel('Warning', "Select text if want to copy into gmail. Press OK to continue, or Cancel to stop")
        if warning == 1:
            try:
                google.open_new_tab('https://mail.google.com/mail/u/0/')
                if e:
                    selected = root.clipboard_get()

                if my_text.selection_get():
                    selected = my_text.selection_get()
                    root.clipboard_clear()
                    root.clipboard_append(selected)
            except:
                pass

    def changefont():
        top = Toplevel()
        fonts = ("Arial", "Courier New", "Comic Sans MS", "Fixedsys", "MS Sans Serif", "MS Serif", "Symbol", "System", "Times New Roman")
        def Arial():
            bold_font = font.Font(my_text, my_text.cget("font"))
            bold_font.configure(family = "Arial")

            my_text.tag_configure("Arial", font = bold_font)

            current_tags = my_text.tag_names("sel.first")

            if "Arial" in current_tags:
                my_text.tag_remove("Arial", "sel.first", "sel.last")

            else:
                my_text.tag_add("Arial", "sel.first", "sel.last")

        def Courier():
            bold_font = font.Font(my_text, my_text.cget("font"))
            bold_font.configure(family = "Courier New")

            my_text.tag_configure(fonts[1], font = bold_font)

            current_tags = my_text.tag_names("sel.first")

            if "bold" in current_tags:
                my_text.tag_remove(fonts[1], "sel.first", "sel.last")

            else:
                my_text.tag_add(fonts[1], "sel.first", "sel.last")

        def Comic():
            bold_font = font.Font(my_text, my_text.cget("font"))
            bold_font.configure(family = fonts[2])

            my_text.tag_configure("Comic Sans MS", font = bold_font)

            current_tags = my_text.tag_names("sel.first")

            if "Comic Sans MS" in current_tags:
                my_text.tag_remove("Comic Sans MS", "sel.first", "sel.last")

            else:
                my_text.tag_add("Comic Sans MS", "sel.first", "sel.last")

        def Fix():
            bold_font = font.Font(my_text, my_text.cget("font"))
            bold_font.configure(family = fonts[3])

            my_text.tag_configure(fonts[3], font = bold_font)

            current_tags = my_text.tag_names("sel.first")

            if "bold" in current_tags:
                my_text.tag_remove(fonts[3], "sel.first", "sel.last")

            else:
                my_text.tag_add(fonts[3], "sel.first", "sel.last")

        def MS():
            bold_font = font.Font(my_text, my_text.cget("font"))
            bold_font.configure(family = fonts[4])

            my_text.tag_configure(fonts[4], font = bold_font)

            current_tags = my_text.tag_names("sel.first")

            if fonts[4] in current_tags:
                my_text.tag_remove(fonts[4], "sel.first", "sel.last")

            else:
                my_text.tag_add(fonts[4], "sel.first", "sel.last")

        def Ms():
            bold_font = font.Font(my_text, my_text.cget("font"))
            bold_font.configure(family = fonts[5])

            my_text.tag_configure(fonts[5], font = bold_font)

            current_tags = my_text.tag_names("sel.first")

            if fonts[5] in current_tags:
                my_text.tag_remove(fonts[5], "sel.first", "sel.last")

            else:
                my_text.tag_add(fonts[5], "sel.first", "sel.last")

        def Sym():
            bold_font = font.Font(my_text, my_text.cget("font"))
            bold_font.configure(family = fonts[6])

            my_text.tag_configure(fonts[6], font = bold_font)

            current_tags = my_text.tag_names("sel.first")

            if fonts[6] in current_tags:
                my_text.tag_remove(fonts[6], "sel.first", "sel.last")

            else:
                my_text.tag_add(fonts[6], "sel.first", "sel.last")

        def Sys():
            bold_font = font.Font(my_text, my_text.cget("font"))
            bold_font.configure(family = fonts[7])

            my_text.tag_configure(fonts[7], font = bold_font)

            current_tags = my_text.tag_names("sel.first")

            if fonts[7] in current_tags:
                my_text.tag_remove(fonts[7], "sel.first", "sel.last")

            else:
                my_text.tag_add(fonts[7], "sel.first", "sel.last")

        def Times():
            bold_font = font.Font(my_text, my_text.cget("font"))
            bold_font.configure(family = fonts[8])

            my_text.tag_configure(fonts[8], font = bold_font)

            current_tags = my_text.tag_names("sel.first")

            if fonts[8] in current_tags:
                my_text.tag_remove(fonts[8], "sel.first", "sel.last")

            else:
                my_text.tag_add(fonts[8], "sel.first", "sel.last")

        button = Button(top, text = fonts[0], command = Arial).pack()
        button = Button(top, text = fonts[1], command = Courier).pack()
        button = Button(top, text = fonts[2], command = Comic).pack()
        button = Button(top, text = fonts[3], command = Fix).pack()
        button = Button(top, text = fonts[4], command = MS).pack()
        button = Button(top, text = fonts[5], command = Ms).pack()
        button = Button(top, text = fonts[6], command = Sym).pack()
        button = Button(top, text = fonts[7], command = Sys).pack()
        button = Button(top, text = fonts[8], command = Times).pack()

    def changefontsize():
        hi = int((input("Font size:")))
        bold_font = font.Font(my_text, my_text.cget("font"))
        bold_font.configure(size = -hi)

        my_text.tag_configure(-hi, font = bold_font)

        current_tags = my_text.tag_names("sel.first")

        if -hi in current_tags:
            my_text.tag_remove(-hi, "sel.first", "sel.last")

        else:
            my_text.tag_add(-hi, "sel.first", "sel.last")

    def reading_mode(e):
        if e:
            my_text.config(state = DISABLED)

        my_text.config(state = DISABLED)

    def editing_mode():
        my_text.config(state =  NORMAL)

    def ask_cortana():
        import Cortana

    def popup(e):
        if e:
            edit_menu.tk_popup(e.x_root, e.y_root)

    def popup2(e):
        if e:
            font_menu.tk_popup(e.x_root, e.y_root)

    def find():

        my_text.tag_remove('found', '1.0', END)

        s = input("Word to find: ")

        if s in my_text.get(1.0, END):
            print("Found")

        if (s):
            idx = '1.0'
            while 1:
                idx = my_text.search(s, idx, nocase = 1,
                                stopindex = END)

                if not idx: break

                lastidx = '% s+% dc' % (idx, len(s))


                my_text.tag_add('found', idx, lastidx)
                idx = lastidx

            my_text.tag_config('found', background = 'Yellow')

    def findNreplace():

        my_text.tag_remove('found', '1.0', END)

        s = input("Word to find: ")
        r = input("Word to replace found word: ")

        if (s and r):
            idx = '1.0'
            while 1:
                idx = my_text.search(s, idx, nocase = 1,
                                stopindex = END)
                print(idx)
                if not idx: break

                lastidx = '% s+% dc' % (idx, len(s))

                my_text.delete(idx, lastidx)
                my_text.insert(idx, r)

                lastidx = '% s+% dc' % (idx, len(r))

                my_text.tag_add('found', idx, lastidx)
                idx = lastidx

            my_text.tag_config('found', background = 'yellow')

    def add_image():
        global my_image
        my_image = PhotoImage(file = 'images\Cortana.png')
        position = my_text.index(INSERT)
        my_text.image_create(position, image=my_image)

    def word_count():
            words = list(my_text.get('1.0', END).split(' '))
            word_count = len(words)
            messagebox.showinfo(title='Word Count', message=f'Word Count: {word_count:,d}')
            status_bar.config(text = f'Word Count: {word_count:,d}')

            print(my_text.cget("height"))

    def right_it():
        my_text.tag_configure("center", justify='right')
        my_text.tag_add("center", 1.0, "end")

    def middle_it():
        my_text.tag_configure("center", justify='center')
        my_text.tag_add("center", 1.0, "end")

    def left_it():
        my_text.tag_configure("center", justify='left')
        my_text.tag_add("center", 1.0, "end")

    def python_mode():
        subprocess.call('C:\Program Files\Git\git-bash.exe')
#-------------------------------------------------------------------------------
    #Specifically for help menu

    def how_cortana():
        top = Toplevel()
        top.title('New Window - Notepad')
        top.iconbitmap('C:\Vaibhav\CNotepad.ico')

        label1 = Label(top, text = "Click on File menu").pack()
        label2 = Label(top, text = "Press \'Ask Cortana\'").pack()

    def lquit():
        choce = messagebox.askyesnocancel("Files", "Make sure your files are saved.")

        if choce == True:
            choice = messagebox.askyesno("Exit?", "Are you sure you want to exit?")
            if choice == 1:
                root.destroy()
                sys.exit()

            else:
                pass

        elif choce == False:
            my_text.config(state = DISABLED)

        else:
            pass

    def why_i_nw():
        messagebox.showinfo("Reason", "You can right click to use the popup menu anywhere on the notepad. This will be fixed shortly.")

#-------------------------------------------------------------------------------
    def new_win():
        top = Toplevel()
        top.title('New Window - Notepad')
        top.iconbitmap('C:\Vaibhav\CNotepad.ico')
        my_frame = Frame(top)
        my_frame.pack(fill = "both" , expand = True)

    #---------------------------------------------------------------------------

        text_scroll = Scrollbar(my_frame)
        text_scroll.pack(side=RIGHT, fill=Y)

        hor_scroll = Scrollbar(my_frame, orient = 'horizontal')
        hor_scroll.pack(side=BOTTOM, fill = X)

    #---------------------------------------------------------------------------

        my_text = Text(my_frame, font = ("Arial", 12), selectbackground = "light grey", selectforeground = "black", undo=True, yscrollcommand = text_scroll.set, wrap = "none", xscrollcommand=hor_scroll.set)
        my_text.pack(fill = "both", expand = True)

    #---------------------------------------------------------------------------

        text_scroll.config(command=my_text.yview)
        hor_scroll.config(command=my_text.xview)

    #---------------------------------------------------------------------------

        my_menu = Menu(top)
        top.config(menu = my_menu)

        file_menu = Menu(my_menu, tearoff = FALSE)
        my_menu.add_cascade(label="File", menu = file_menu)
        file_menu.add_cascade(label="New", command = new_file)
        file_menu.add_cascade(label="Open", command = open_file)
        file_menu.add_cascade(label="Save                   Ctrl S", command = lambda: save_file(False))
        file_menu.add_cascade(label="Save As", command = save_as_file)
        file_menu.add_separator()
        file_menu.add_cascade(label="Print file         Ctrl P", command = print_file)
        file_menu.add_cascade(label="Reading mode           Ctrl R", command = lambda: reading_mode(False))
        file_menu.add_separator()
        file_menu.add_cascade(label="Exit", command=top.quit)
        file_menu.add_separator()
        file_menu.add_cascade(label = "New Window", command = new_win)

        edit_menu = Menu(my_menu, tearoff = FALSE)
        my_menu.add_cascade(label="Edit", menu = edit_menu)
        edit_menu.add_cascade(label="Cut                 Ctrl X", command = lambda: cut_text(False))
        edit_menu.add_cascade(label="Copy              Ctrl C", command = lambda: copy_text(False))
        edit_menu.add_cascade(label="Paste              Ctrl V", command = lambda: paste_text(False))
        edit_menu.add_separator()
        edit_menu.add_cascade(label="Undo              Ctrl Z", command=my_text.edit_undo)
        edit_menu.add_cascade(label="Redo              Ctrl Y", command=my_text.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_cascade(label="Select all        Ctrl A", command=select_all)
        edit_menu.add_cascade(label="Clear all         Ctrl Y", command=clear_all)
        edit_menu.add_separator()
        edit_menu.add_cascade(label="Find", command = find)
        edit_menu.add_cascade(label="Find and Replace", command = findNreplace)
        edit_menu.add_separator()
        edit_menu.add_cascade(label="Time        Ctrl T", command = lambda: tiwme(False))


        font_menu = Menu(my_menu, tearoff = FALSE)
        my_menu.add_cascade(label="Font", menu = font_menu)
        font_menu.add_cascade(label="Bold           Ctrl B",command = lambda: bold_it(False))
        font_menu.add_cascade(label="Italics            Ctrl I", command = lambda: italics_it(False))
        font_menu.add_cascade(label = "Change font", command = changefont)
        font_menu.add_cascade(label = "Change font size", command = changefontsize)
        font_menu.add_cascade(label = "Underline            Ctrl U", command = lambda: underline_it(False))

        color_menu = Menu(my_menu, tearoff = FALSE)
        my_menu.add_cascade(label="Color", menu = color_menu)
        color_menu.add_cascade(label="Change Text ", command = text_color)
        color_menu.add_cascade(label="Change Selected Text", command = text_color)
        color_menu.add_cascade(label="Change All Text", command = all_text_color)
        color_menu.add_cascade(label="Change Background", command = bg_color)

        about_menu = Menu(my_menu, tearoff = FALSE)
        my_menu.add_cascade(label="Help", menu = about_menu)
        about_menu.add_cascade(label="About", command = about_help)
        about_menu.add_cascade(label="Why is Ctrl I not working for italics?", command = why_i_nw)

        mode_menu = Menu(my_menu, tearoff = FALSE)
        my_menu.add_cascade(label="Mode", menu = mode_menu)
        mode_menu.add_cascade(label="Dark mode", command=dark_mode)
        mode_menu.add_cascade(label="Normal mode", command=light_mode)

    #---------------------------------------------------------------------------

        status_bar = Label (top, text = 'Ready   ', anchor = E)
        status_bar.pack(fill = X, side = BOTTOM, ipady = 5)

    #---------------------------------------------------------------------------

        top.bind('<Control-Key-x>', cut_text)
        top.bind('<Control-Key-c>', copy_text)
        top.bind('<Control-Key-v>', paste_text)

        top.bind('<Control-Key-t>', tiwme)

        top.bind('<Control-Key-s>', save_file)


        top.bind('<Control-Key-r>', reading_mode)

        top.bind('<Control-Key-b>', bold_it)
        top.bind('<Control-Key-i>', italics_it)
        top.bind('<Control-Key-u>', underline_it)
        top.bind('<Button-3>', popup)

#-------------------------------------------------------------------------------
    toolbar_frame = Frame(root)
    toolbar_frame.pack(fill = X)
#-------------------------------------------------------------------------------

    my_frame = Frame(root)
    my_frame.pack(fill = "both" , expand = True)

#-------------------------------------------------------------------------------

    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    hor_scroll = Scrollbar(my_frame, orient = 'horizontal')
    hor_scroll.pack(side=BOTTOM, fill = X)

#-------------------------------------------------------------------------------

    my_text = Text(my_frame, font = ("Product Sans", 12), selectbackground = "light grey", selectforeground = "black", undo=True, yscrollcommand = text_scroll.set, wrap = "none", xscrollcommand=hor_scroll.set)
    my_text.pack(fill = "both" , expand = True)

#-------------------------------------------------------------------------------

    text_scroll.config(command=my_text.yview)
    hor_scroll.config(command=my_text.xview)

#-------------------------------------------------------------------------------

    my_menu = Menu(root)
    root.config(menu = my_menu)

    file_menu = Menu(my_menu, tearoff = FALSE)
    my_menu.add_cascade(label="File", menu = file_menu)
    file_menu.add_cascade(label="New", command = new_file)
    file_menu.add_cascade(label="Open", command = open_file)
    file_menu.add_cascade(label="Save                   Ctrl S", command = lambda: save_file(False))
    file_menu.add_cascade(label="Save As", command = save_as_file)
    file_menu.add_separator()
    file_menu.add_cascade(label="Print file         Ctrl P", command = print_file)
    file_menu.add_cascade(label="Reading mode           Ctrl R", command = lambda: reading_mode(False))
    file_menu.add_separator()
    file_menu.add_cascade(label="Exit", command=lquit)
    file_menu.add_separator()
    file_menu.add_cascade(label="Open up Gmail", command = lambda: Gmail(False))
    file_menu.add_cascade(label="Ask Cortana", command = ask_cortana)
    file_menu.add_cascade(label="Open Git Bash Terminal", command = python_mode)
    file_menu.add_separator()
    file_menu.add_cascade(label = "New Window", command = new_win)
    file_menu.add_cascade(label = "Word count", command = word_count)

    edit_menu = Menu(my_menu, tearoff = FALSE)
    my_menu.add_cascade(label="Edit", menu = edit_menu)
    edit_menu.add_cascade(label = "Edit mode", command = editing_mode)
    edit_menu.add_cascade(label="Cut                 Ctrl X", command = lambda: cut_text(False))
    edit_menu.add_cascade(label="Copy              Ctrl C", command = lambda: copy_text(False))
    edit_menu.add_cascade(label="Paste              Ctrl V", command = lambda: paste_text(False))
    edit_menu.add_separator()
    edit_menu.add_cascade(label="Undo              Ctrl Z", command=my_text.edit_undo)
    edit_menu.add_cascade(label="Redo              Ctrl Y", command=my_text.edit_redo)
    edit_menu.add_separator()
    edit_menu.add_cascade(label="Select all        Ctrl A", command=select_all)
    edit_menu.add_cascade(label="Clear all         Ctrl Y", command=clear_all)
    edit_menu.add_separator()
    edit_menu.add_cascade(label="Find", command = find)
    edit_menu.add_cascade(label="Find and Replace", command = findNreplace)
    edit_menu.add_separator()
    edit_menu.add_cascade(label="Time        Ctrl T", command = lambda: tiwme(False))
    edit_menu.add_cascade(label="Add Image", command = add_image)

    font_menu = Menu(my_menu, tearoff = FALSE)
    my_menu.add_cascade(label="Font", menu = font_menu)
    font_menu.add_cascade(label="Bold           Ctrl B",command = lambda: bold_it(False))
    font_menu.add_cascade(label="Italics            Ctrl I", command = lambda: italics_it(False))
    font_menu.add_cascade(label = "Change font", command = changefont)
    font_menu.add_cascade(label = "Change font size", command = changefontsize)
    font_menu.add_cascade(label = "Underline            Ctrl U", command = lambda: underline_it(False))

    color_menu = Menu(my_menu, tearoff = FALSE)
    my_menu.add_cascade(label="Color", menu = color_menu)
    color_menu.add_cascade(label="Change Text ", command = text_color)
    color_menu.add_cascade(label="Change Selected Text", command = text_color)
    color_menu.add_cascade(label="Change All Text", command = all_text_color)
    color_menu.add_cascade(label="Change Background", command = bg_color)

    mode_menu = Menu(my_menu, tearoff = FALSE)
    my_menu.add_cascade(label="Mode", menu = mode_menu)
    mode_menu.add_cascade(label="Dark mode", command=dark_mode)
    mode_menu.add_cascade(label="Normal mode", command=light_mode)

    about_menu = Menu(my_menu, tearoff = FALSE)
    my_menu.add_cascade(label="Help", menu = about_menu)
    about_menu.add_cascade(label="About", command = about_help)
    about_menu.add_cascade(label="How to initiate Cortana from textpad?", command = how_cortana)
    about_menu.add_cascade(label="Why is Ctrl I not working for italics?", command = why_i_nw)

#-------------------------------------------------------------------------------

    status_bar = Label (root, text = 'Ready   ', anchor = E)
    status_bar.pack(fill = X, side = BOTTOM, ipady = 5)

#-------------------------------------------------------------------------------

    right = "Right"
    left = "Left"
    middle = "Middle"

    right_button = Button(toolbar_frame, text=right, command = right_it)
    right_button.grid(row = 0, column = 2, sticky=W)

    left_button = Button(toolbar_frame, text=left, command = left_it)
    left_button.grid(row = 0, column = 0, sticky=W)

    middle_button = Button(toolbar_frame, text=middle, command = middle_it)
    middle_button.grid(row = 0, column = 1, sticky=W)

#-------------------------------------------------------------------------------

    root.bind('<Control-Key-x>', cut_text)
    root.bind('<Control-Key-c>', copy_text)
    root.bind('<Control-Key-v>', paste_text)

    root.bind('<Control-Key-t>', tiwme)

    root.bind('<Control-Key-s>', save_file)


    root.bind('<Control-Key-r>', reading_mode)

    root.bind('<Control-Key-b>', bold_it)
    root.bind('<Control-Key-i>', italics_it)
    root.bind('<Control-Key-u>', underline_it)

    root.bind('<Button-3>', popup)
    root.bind('<Control-Button-3>', popup2)
#-------------------------------------------------------------------------------

    root.mainloop()

intro()