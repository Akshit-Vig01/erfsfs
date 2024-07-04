from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import connection
class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('View Admin')

        self.mainLabel = Label(self.root, text="View Admin", font=('',30,'bold'))
        self.mainLabel.pack(pady=20)

        self.formFrame = Frame(self.root)
        self.formFrame.pack(pady=10)

        self.lb = Label(self.formFrame, text="Search by Name,Email,Mobile",font=('arial',14))
        self.txt = Entry(self.formFrame,font=('arial',14))
        self.bt1 = Button(self.formFrame ,text="Search",font=('arial',14) , command=self.searchAdmin)
        self.bt2 = Button(self.formFrame,text="Refresh",font=('arial',14), command=self.getvalues)
        self.lb.grid(row=0,column=0,padx=10)
        self.txt.grid(row=0, column=1, padx=10)
        self.bt1.grid(row=0, column=2, padx=10)
        self.bt2.grid(row=0, column=3, padx=10)

        self.adminTable = ttk.Treeview(self.root, columns=('id','name','email','mobile','role'))
        self.adminTable.pack(pady=20 ,padx=20, expand=True, fill='both')
        self.adminTable.heading('id',text="ID")
        self.adminTable.heading('name', text="Name")
        self.adminTable.heading('email',text= "Email")
        self.adminTable.heading('mobile', text="Mobile")
        self.adminTable.heading('role', text="Role")
        self.adminTable['show'] = 'headings'
        self.getvalues()
        style = ttk.Style()
        style.configure('Treeview',font=('arial',14), rowheight=40,background="#BED8D4",fieldbackground="#BED8D4",foreground="green")
        style.configure('Treeview.Heading', font=('arial',14),background="red",foreground="brown")
        self.adminTable.bind("<Double-1>", self.openUpdateWindow)

        self.delButton =Button(self.root, text="Delete", width=15,font=('',14),command=self.deleteAdmin)
        self.delButton.pack(pady=20)

        self.root.mainloop()


    def openUpdateWindow(self, event):
        data = self.adminTable.item(self.adminTable.selection()[0])['values']
        self.root1 = Toplevel()
        self.root1.title('Update Admin')
        self.root1.geometry('800x800')
        self.mainLabel1 = Label(self.root1,text="Update Admin",font=('',24,'bold'))
        self.mainLabel1.pack(pady=20)

        self.updateForm = Frame(self.root1)
        self.updateForm.pack(pady=10)
        font = ('',14)
        self.lb1 = Label(self.updateForm,text="Admin ID",font=font)
        self.txt1 = Entry(self.updateForm,font=font,width=30)
        self.lb1.grid(row=0 , column=0, pady=20, padx=10)
        self.txt1.grid(row=0, column=1,pady=20,padx=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.updateForm, text="Admin Name", font=font)
        self.txt2 = Entry(self.updateForm, font=font, width=30)
        self.lb2.grid(row=1, column=0, pady=20, padx=10)
        self.txt2.grid(row=1, column=1, pady=20, padx=10)
        self.txt2.insert(0, data[1])


        self.lb3 = Label(self.updateForm, text="Admin Email", font=font)
        self.txt3 = Entry(self.updateForm, font=font, width=30)
        self.lb3.grid(row=2, column=0, pady=20, padx=10)
        self.txt3.grid(row=2, column=1, pady=20, padx=10)
        self.txt3.insert(0, data[2])


        self.lb4 = Label(self.updateForm, text="Admin Mobile", font=font)
        self.txt4 = Entry(self.updateForm, font=font, width=30, )
        self.lb4.grid(row=3, column=0, pady=20, padx=10)
        self.txt4.grid(row=3, column=1, pady=20, padx=10)
        self.txt4.insert(0, data[3])

        self.lb5 = Label(self.updateForm, text="Admin Role", font=font)
        self.txt5 =ttk.Combobox(self.updateForm, font=font, width=28 ,  values=['Super Admin','Admin'],state='readonly')
        self.lb5.grid(row=4, column=0, pady=10, padx=10)
        self.txt5.grid(row=4, column=1, pady=10, padx=10)
        self.txt5.set(data[4])

        self.updateBtn = Button(self.root1, text="Update",width=15,font=font, command=self.updateAdmin)
        self.updateBtn.pack(pady=20)



    def updateAdmin(self):
        id = self.txt1.get()
        name = self.txt2.get()
        email = self.txt3.get()
        mobile = self.txt4.get()
        role = self.txt5.get()

        q = f"update admin set name='{name}',email = '{email}',mobile='{mobile}',role='{role}' where id ='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        self.getvalues()
        self.root1.destroy()
        msg.showinfo("Success","Admin has been Updated....",parent=self.root)










    def deleteAdmin(self):
        rowid = self.adminTable.selection()
        if len(rowid) == 0:
            msg.showwarning("Warning","Please Select a Row", parent=self.root)
        elif len(rowid)>1:
            msg.showwarning("Warning", "Please Select a Single Row at a time", parent=self.root)
        else:
            items = self.adminTable.item(rowid[0])
            data = items['values']
            q = f"delete from admin where id = '{data[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            self.getvalues()
            msg.showinfo("Success","Admin has been Removed...", parent=self.root)


    def searchAdmin(self):
        search = self.txt.get()
        q = f"select * from admin where name like '%{search}%' or email like '%{search}' or mobile like '%{search}'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for row in self.adminTable.get_children():
            self.adminTable.delete(row)
        count = 0
        for i in data:
            self.adminTable.insert('', index=count, values=i)
            count += 1

    def getvalues(self):
        self.conn = connection.Connect()
        self.cr = self.conn.cursor()
        q = "select id,name,email,mobile,role from admin"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for row in self.adminTable.get_children():
            self.adminTable.delete(row)
        count = 0
        for i in data:
            self.adminTable.insert('', index=count, values=i)
            count += 1


if __name__ == '__main__':
    obj = Main()