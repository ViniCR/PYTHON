from tkinter import *
from tkinter import ttk

def insert():
    gt_nome = en_nome.get()
    gt_num  = en_num.get()
    en_nome.delete(0,END)
    en_num.delete(0,END)
    tree.insert("", "end", values=(gt_nome,gt_num), tags=('All',))
    tree.tag_configure('All', background='gray11',foreground='pale green')

root = Tk()
root.geometry('400x400')
root.configure(bg='gray28')
root.resizable(False,False)

tree = ttk.Treeview(root,columns=('nome','numero'), show='headings')
tree.heading("nome", text="NOME")
tree.heading("numero", text="NUMERO")

tree.column("nome",width=200)
tree.column("numero",width=200)
tree.place(relx=0,rely=0)

lb_nome = Label(text='NOME', bg='gray28', fg='white')
lb_nome.place(relx=0.1,rely=0.6)

en_nome = Entry()
en_nome.place(relx=0.1,rely=0.65, relwidth=0.6)

lb_num  = Label(text='NUMERO', bg='gray28', fg='white')
lb_num.place(relx=0.1,rely=0.75)

en_num  = Entry()
en_num.place(relx=0.1,rely=0.8, relwidth=0.6)

bt = Button (text='ADD', command = insert, bg='gray21', fg='white')
bt.place(relx=0.1,rely=0.88)




root.mainloop()