from tkinter import *
from tkinter import filedialog
import webbrowser, os

win = Tk()
a = 0
globe = []


class Methods():

    def add_info(self):
        self.name = self.name_en.get()
        self.code = self.code_en.get()
        self.email = self.email_en.get()
        self.address = self.address_en.get()
        self.name_en.delete(0, END)
        self.code_en.delete(0, END)
        self.email_en.delete(0, END)
        self.address_en.delete(0, END)

        a =+ 1
        self.file = open("data.txt", "a")
        self.file.write(
            F'''
            #__00{self.code}__ 

            NAME: {self.name}
            EMAIL: {self.email}
            ADDRESS: {self.address}
            '''
        )
        self.file.close()

    def clean_info(self):
        self.name_en.delete(0, END)
        self.code_en.delete(0, END)
        self.email_en.delete(0, END)
        self.address_en.delete(0, END)

    def search_web(self):
        webbrowser.open('https://id.heroku.com/login')
    
    def open_data(self):
        self.oppening = webbrowser.open(os.path.realpath('data.txt'))





class Application(Methods):
    def __init__(self):
        self.win = win
        self.attr()
        self.frame_1()
        self.button()
        self.widget()

        self.win.mainloop()

    def attr(self):
        self.win.title('Main Plate')
        self.win.geometry('400x200')
        self.win.resizable(False,False)
        self.win.configure(bg='MediumPurple4')

    def frame_1(self):
        self.win_f1 = Frame(self.win, bg= 'gray36', highlightbackground='gray70', highlightthickness=2)
        self.win_f1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

    def button(self):
        self.button_1 = Button(self.win_f1, text ='Add Info', command=self.add_info, bg ='gray30' , fg= 'gray99' , bd = 0.5, )
        self.button_1.place(relx = 0.05, rely = 0.15)

        self.button_2 = Button(self.win_f1, text ='Clean Info', command=self.clean_info, bg ='gray30' , fg= 'gray99' , bd = 0.5)
        self.button_2.place(relx = 0.26, rely = 0.15)

        self.button_3 = Button(self.win_f1, text ='Web Search', command=self.search_web, bg ='gray30' , fg= 'gray99' , bd = 0.5)
        self.button_3.place(relx = 0.5, rely = 0.15)


        self.button_4 = Button(self.win_f1, text ='Open Data', command=self.open_data, bg ='gray30' , fg= 'gray99' , bd = 0.5)
        self.button_4.place(relx = 0.75, rely = 0.15)

    def widget(self):
        
        # NAME
        self.name_lb = Label(self.win, text='NAME:' ,bg="MediumPurple4", fg='White')
        self.name_lb.place(relx=0.042, rely=0.3 )
        self.name_en = Entry(self.win, )
        self.name_en.place(relx=0.05, rely=0.4 )
        # CODE
        self.address_lb = Label(self.win, text='ADDRESS:' ,bg="MediumPurple4", fg='White')
        self.address_lb.place(relx=0.042, rely=0.5 )
        self.address_en = Entry(self.win, )
        self.address_en.place(relx=0.05, rely=0.6 )        
        # EMAIL
        self.email_lb = Label(self.win, text='EMAIL:' ,bg="MediumPurple4", fg='White')
        self.email_lb.place(relx=0.042, rely=0.7 )
        self.email_en = Entry(self.win, )
        self.email_en.place(relx=0.05, rely=0.8 )
        # ADDRESS
        self.code_lb = Label(self.win, text='CODE:' ,bg="MediumPurple4", fg='White')
        self.code_lb.place(relx=0.84, rely=0.7 )
        self.code_en = Entry(self.win, )
        self.code_en.place(relx=0.85, rely=0.8 , relwidth=0.1)







    
        



Application()

    
    


