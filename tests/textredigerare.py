from distutils import text_file
from tkinter import *
from tkinter import filedialog
from tkinter import font

def redigerare():
    root = Tk()
    root.title("Journal")
    #root.iconbitmap

    my_frame = Frame(root)
    my_frame.pack(pady = 5)

    #skapa ny fil
    def ny_fil():
        my_text.delete("1.0", END)
        root.title("ny fil")
        status_bar.config(text="ny fil        ")

    def öppna_fil():
        #delete previous
        my_text.delete("1.0", END)
        
        #grab filename
        text_file = filedialog.askopenfilename(initialdir="/Users/erikduvander/Documents/JournalSystem/source/Journaler",title="öppna fil", filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))
        
        #update status bar
        name = text_file
        status_bar.config(text=f'{name}        ')
        name.replace("/Users/erikduvander/Documents/JournalSystem/source/Journaler/", "")
        root.title(f"{name}        ")

        #open file
        text_file = open(text_file, "r")
        stuff = text_file.read()
        #add file to textbox
        my_text.insert(END, stuff)
        #close
        text_file.close()

    def spara_som():
        text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="/Users/erikduvander/Documents/JournalSystem/source/Journaler", title="spara fil", filetypes=(("Text File", "*.txt"), ("All files", "*.*")) )
        if text_file:
            
            #update status bar
            name = text_file
            status_bar.config(text=f'Sparad: {name}        ')
            name = name.replace("/Users/erikduvander/Documents/JournalSystem/source/Journaler","")
            root.title(f"{name}        ")

            #save the file
            text_file = open(text_file, "w")
            text_file.write(my_text.get("1.0", END))
            text_file.close()
            
    #scrollbar textbar
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    #create text box
    my_text = Text(my_frame, width=97, height=25, font=("Helvetice", 16), selectbackground="white", selectforeground="blue", undo=True, yscrollcommand=text_scroll.set)
    my_text.pack()

    #configure scrollbar
    text_scroll.config(command = my_text.yview)

    #create menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    #add file menu 
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="fil", menu=file_menu)
    file_menu.add_command(label="ny", command=ny_fil)
    file_menu.add_command(label="öppna", command=öppna_fil)
    file_menu.add_command(label="spara")
    file_menu.add_command(label="spara som", command=spara_som)
    file_menu.add_separator()
    file_menu.add_command(label="stäng")

    #status bar
    status_bar = Label(root, text="redo        ", anchor=E)
    status_bar.pack(fill=X, side=BOTTOM, ipady=5)


    root.mainloop()

redigerare()


