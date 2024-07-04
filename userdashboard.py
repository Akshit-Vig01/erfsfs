from  tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import adduser
import viewuser

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title('User Dashboard')
        self.root.state('zoomed')

        self.rootMenu =Menu(self.root)
        self.root.configure(menu=self.rootMenu)
        self.catMenu=Menu(self.rootMenu,tearoff=0)
        self.catMenu.add_command(label='Add User',command=lambda :adduser.Main())
        self.catMenu.add_command(label='View User',command=lambda:viewuser.Main())
        self.rootMenu.add_cascade(label="User",menu=self.catMenu)

        self.root.mainloop()


obj = Main()