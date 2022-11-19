from tkinter import *
import webbrowser as wb


root = Tk()


class Methods():

    def func_ggl(self):
        self.web_ggl = self.en_ggl.get()
        self.en_ggl.delete(0,END)
        wb.open(f'https://www.google.com/search?q={self.web_ggl}')

    def func_yah(self):
        self.web_yah = self.en_yah.get()
        self.en_yah.delete(0,END)
        wb.open(f'https://br.search.yahoo.com/search?p={self.web_yah}')

    def func_mic(self):
        self.web_mic = self.en_mic.get()
        self.en_mic.delete(0,END)
        wb.open(f'https://www.bing.com/search?q={self.web_mic}')

    def func_eco(self):
        self.web_eco = self.en_eco.get()
        self.en_eco.delete(0,END)
        wb.open(f'https://www.ecosia.org/search?method=index&q={self.web_eco}')
        

    





class Application(Methods):
    
    def __init__(self):
        self.root = root
        self.tela()
        self.google()
        self.yahoo()
        self.microsoft()
        self.ecosia()
        root.mainloop()



    def tela(self):
        self.root.title('Search Engine')
        self.root.configure(background='gray22')
        self.root.geometry('600x350')
        self.root.resizable(False, False)
        self.intro = Label(self.root, text = 'Write Where and What want from Web and just click the button behind.',bg='gray22', fg = 'white')
        self.intro.place(relx=0.06, rely=0.1)

    

    def google(self):
        self.ggl = PhotoImage(file='C:\\Users\\Vinicius\\Desktop\\ESFERA CRIATIVA\\google.png')

        """self.lb_google = Label(self.root, text="GOOGLE", bg = 'azure', fg = 'steel blue', font=('Verdana', 8, 'bold'))
        self.lb_google.place(relx= 0.02, rely=0.2)"""
        self.en_ggl = Entry(self.root, bd=2, bg='gainsboro', font=('Verdana', 8))
        self.en_ggl.place(relx= 0.022,rely=0.22, relwidth=0.7, relheight=0.1)
        self.bt_ggl = Button(self.root, image=self.ggl, command=self.func_ggl)
        self.bt_ggl.place(relx=0.74, rely=0.21, relwidth=0.2, relheight=0.12)
    
        

    def yahoo(self):
        self.yah = PhotoImage(file='C:\\Users\\Vinicius\\Desktop\\ESFERA CRIATIVA\\yahoo.png')

        """self.lb_google = Label(self.root, text="YAHOO", bg = 'azure', fg = 'steel blue', font=('Verdana', 8, 'bold'))
        self.lb_google.place(relx= 0.02, rely=0.4)"""
        self.en_yah = Entry(self.root, bd=2, bg='gainsboro', font=('Verdana', 8))
        self.en_yah.place(relx= 0.022,rely=0.42, relwidth=0.7, relheight=0.1)
        self.bt_yah = Button(self.root, image=self.yah, command=self.func_yah)
        self.bt_yah.place(relx=0.74, rely=0.41, relwidth=0.2, relheight=0.12)    

    def microsoft(self):
        self.mic = PhotoImage(file='C:\\Users\\Vinicius\\Desktop\\ESFERA CRIATIVA\\microsoft.png')

        """self.lb_google = Label(self.root, text="MICROSOFT", bg = 'azure', fg = 'steel blue', font=('Verdana', 8, 'bold'))
        self.lb_google.place(relx= 0.02, rely=0.6)"""
        self.en_mic = Entry(self.root, bd=2, bg='gainsboro', font=('Verdana', 8))
        self.en_mic.place(relx= 0.022,rely=0.62, relwidth=0.7, relheight=0.1)
        self.bt_mic = Button(self.root, image=self.mic, command=self.func_mic)
        self.bt_mic.place(relx=0.74, rely=0.61, relwidth=0.2, relheight=0.12)

    def ecosia(self):
        self.eco = PhotoImage(file='C:\\Users\\Vinicius\\Desktop\\ESFERA CRIATIVA\\ecosia.png')

        """self.lb_google = Label(self.root, text="ECOSIA", bg = 'azure', fg = 'steel blue', font=('Verdana', 8, 'bold'))
        self.lb_google.place(relx= 0.02, rely=0.8)"""
        self.en_eco = Entry(self.root, bd=2, bg='gainsboro', font=('Verdana', 8))
        self.en_eco.place(relx= 0.022,rely=0.82, relwidth=0.7, relheight=0.1)
        self.bt_eco = Button(self.root, image=self.eco, command=self.func_eco)
        self.bt_eco.place(relx=0.74, rely=0.81, relwidth=0.2, relheight=0.12)


Application()
