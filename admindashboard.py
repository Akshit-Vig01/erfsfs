from  tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import addadmin
import addcategory
import adminpasswordchange
import bookingdetail
import bookingroom
import viewadmin
import viewbooking
import viewcategory



class Main:
    def __init__(self,adminid,adminname,adminemail,adminrole):
        self.root = Tk()
        self.root.title('Admin Dashboard')
        self.root.state('zoomed')

        self.mainlabel = Label(self.root, text=f"Welcome {adminname}", font=('arial', 28))
        self.mainlabel.pack(pady=20)

        self.rootMenu =Menu(self.root)#initialize a main menu
        self.root.configure(menu=self.rootMenu)

        if adminrole== "Super Admin":
            self.adminMenu=Menu(self.rootMenu,tearoff=0)
            self.adminMenu.add_command(label='Add Admin',command=lambda :addadmin.Main())
            self.adminMenu.add_command(label='View Admin',command=lambda:viewadmin.Main())
            self.rootMenu.add_cascade(label="Admin",menu=self.adminMenu)



        self.catMenu = Menu(self.rootMenu, tearoff=0)
        self.catMenu.add_command(label='Add Category', command=lambda: addcategory.Main())
        self.catMenu.add_command(label='View category', command=lambda: viewcategory.Main())
        self.rootMenu.add_cascade(label="Category", menu=self.catMenu)

        self.catMenu = Menu(self.rootMenu, tearoff=0)
        self.catMenu.add_command(label='password change', command=lambda:adminpasswordchange.Main(adminemail))
        self.catMenu.add_command(label='logout',command=lambda:self.root.destroy() )
        self.rootMenu.add_cascade(label="profile", menu=self.catMenu)

        self.catMenu = Menu(self.rootMenu, tearoff=0)
        self.catMenu.add_command(label='Add Bookings', command=lambda: bookingroom.Main())
        self.catMenu.add_command(label='View Bookings', command=lambda:viewbooking.Main())
        self.catMenu.add_command(label='Booking Details', command=lambda:bookingdetail.Main())
        self.rootMenu.add_cascade(label="Booking", menu=self.catMenu)



        self.root.mainloop()





# obj =Main()