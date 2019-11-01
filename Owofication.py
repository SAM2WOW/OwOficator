#Tkinter version owofied software
#by Sam Feng

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from time import strftime 

class MyWindow:
    def __init__(self, win):

        #Titled Border
        labelframe = LabelFrame(text="Text Editor", bg="#023859", fg="white")
        labelframe.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

        self.input1 = ScrolledText(labelframe, font=("Helvetica", 13), bd=2, bg="#04668C", fg="white")
        self.input1.grid(row=0, column=0, columnspan=3)
        self.input1.grid_columnconfigure(0, weight=20)

        #Buttons Actions Border
        Actionframe = LabelFrame(text="Actions", bg="#023859", fg="white")
        Actionframe.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        #Buttons Icon
        self.btnicon = PhotoImage(file = r"C:\Users\fengy\source\repos\OWOficator\OwOficator\Graphics\owoface_sm.png").subsample(2, 2)
        self.btn1icon = PhotoImage(file = r"C:\Users\fengy\source\repos\OWOficator\OwOficator\Graphics\Clean_sm.png").subsample(2, 2)
        self.btn2icon = PhotoImage(file = r"C:\Users\fengy\source\repos\OWOficator\OwOficator\Graphics\Copy_sm.png").subsample(2, 2)

        #Buttons
        self.btn = Button(Actionframe, text="OwOfied", image = self.btnicon, compound = LEFT, font=("Verdana", 15, "bold"), bd=2, bg="#04668C", fg="white")
        self.btn.bind('<Button-1>', self.owofied)
        self.btn.grid(row=2, column=1, padx=10, pady=5)

        self.btn1 = Button(Actionframe, text="Clean All", image = self.btn1icon, compound = LEFT, font=("Verdana", 15), bd=2, bg="#04668C", fg="white")
        self.btn1.bind('<Button-1>', self.clean)
        self.btn1.grid(row=2, column=0, padx=10, pady=5)

        self.btn2 = Button(Actionframe, text="Copy All", image = self.btn2icon, compound = LEFT, font=("Verdana", 15), bd=2, bg="#04668C", fg="white")
        self.btn2.bind('<Button-1>', self.copy)
        self.btn2.grid(row=2, column=2, padx=10, pady=5)


        #Border for settings
        settingframe = LabelFrame(text="Settings", bg="#023859", fg="white")
        settingframe.grid(row=1, column=3, padx=10, pady=10)

        #Settings Checkboxs
        self.boxval0 = IntVar()
        self.boxval1 = IntVar()
        self.boxs = Checkbutton(settingframe, text="OwO & UwU in line", font=("Verdana", 12), variable=self.boxval0, bg="#023859", fg="#73C6D9")
        self.boxs.grid(row=1, column=3)
        self.boxs1 = Checkbutton(settingframe, text="OwO at the end", font=("Verdana", 12), variable=self.boxval1, bg="#023859", fg="#73C6D9")
        self.boxs1.grid(row=2, column=3)

        #Monster
        #owomonster = PhotoImage(file = r"C:\Users\fengy\source\repos\OWOficator\OwOficator\Graphics\owographic.gif") 
        #self.monster = Label(window, image = owomonster)
        #self.monster.grid(row=1, column=3)

        # Creating Menubar 
        menubar = Menu(window)
            
        # Adding File Menu and commands 
        files = Menu(menubar, tearoff = 0, bg="#73C6D9") 
        menubar.add_cascade(label ='File', menu = files) 
        files.add_command(label ='New File', command = self.notavaliable) 
        files.add_command(label ='Open...', command = self.notavaliable) 
        files.add_command(label ='Save', command = self.notavaliable) 
        files.add_separator() 
        files.add_command(label ='Demo Texts', command = self.demotexts) 
        files.add_separator() 
        files.add_command(label ='Exit', command = window.destroy) 
                
        # Adding Help Menu 
        help_ = Menu(menubar, tearoff = 0, bg="#73C6D9") 
        menubar.add_cascade(label ='Help', menu = help_) 
        help_.add_command(label ='Help', command = self.showhelp) 
        help_.add_command(label ='About', command = self.showabout) 
        help_.add_separator() 
        help_.add_command(label ='Dev Logs', command = self.showdevlog) 

        #config
        window.config(menu = menubar) 
    

    #MainFuctions
    #Replace and open Files
    ###
    def owofied(self, event):

        global sentence
        sentence = str(self.input1.get("1.0",END))

        #Replaces
        #Common OwO
        dictionary = {"i":"wi", "ea":"ew", "ou":"ow", "ha":"a", "u":"uw", "ee":"eew", "mp":"wp", "m":"mya", "an":"nya", "on":"nyon"} 
        for key in dictionary.keys():
            sentence = sentence.replace(key, dictionary[key])
        #Special OwO
        dic_owo = {"I":"I ~OwO~", ".":". ~UwU~", " a ":" a ~UwU~ "}
        if self.boxval0.get() == True:
            for key in dic_owo.keys():
                sentence = sentence.replace(key, dic_owo[key])
        #Add OwO at End
        if self.boxval1.get() == True:
            sentence = str(sentence + "OWO")

        #Output
        self.input1.delete('1.0', END)
        self.input1.insert(END, sentence)
    
    def clean(self, event):
        self.input1.delete('1.0', END)

    def copy(self, event):
        window.clipboard_clear()
        window.clipboard_append(str(self.input1.get("1.0",END)))
        window.update()
    


    #Menu Functions
    #Infos
    ###
    def openfile(self, event):
        awdawd

    def demotexts(self):
        self.input1.delete('1.0', END)
        self.input1.insert(END, "I’m designing a document and don’t want to get bogged down in what the text actually says.\nI’m creating a template with various paragraph styles and need to see what they will look like.\nI’m creating a macro and need some text for testing purposes.\nI’m trying to learn more about some feature of OwOficator and don’t want to practice on a real document.")

    def showhelp(self):
        messagebox.showinfo("*Notice your help*","OwOficator can help you turn your text into OwO format. Simply open a text file or type in the text editor area and click the OwOfied button. UwU")
    
    def showabout(self):
        messagebox.showinfo("About","~OwOficator~  By SamF")

    def showdevlog(self):
        messagebox.showinfo("*Notice the devs*","Version v1.0 - 10/30/2019\nVersion v2.0beta - 10/31/2019\nIn Development...")

    def notavaliable(self):
        messagebox.showwarning("*Notice the error!*","This feature is not avaliable yet!")


#Windows
window=Tk()
mywin=MyWindow(window)
window.title('OwOficator v2.0 beta                 *Notice*')
window.iconbitmap(r"C:\Users\fengy\source\repos\OWOficator\OwOficator\Graphics\owo.ico")
window.configure(bg="#023859")
window.geometry("770x610")
window.resizable(False, False)

#Mainloops
mainloop()