from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import connection

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('View Category')

        self.mainLabel = Label(self.root, text="View Category",font=('',14,'bold'))
        self.mainLabel.pack(pady=20)

        self.formFrame = Frame(self.root)
        self.formFrame.pack(pady=10)

        self.lb = Label(self.formFrame,  text="Search by Name , Description", font=('arial',14))
        self.txt = Entry(self.formFrame,font=('arial',14))
        self.bt1 = Button(self.formFrame,text="Search",font=('arial',14), command=self.searchcategory)
        self.bt2 = Button(self.formFrame,text="Refresh",font=('arial',14),command=self.getvalues)
        self.lb.grid(row=0, column=0,padx=10)
        self.txt.grid(row=0, column=1, padx=10)
        self.bt1.grid(row=0, column=2, padx=10)
        self.bt2.grid(row=0, column=3, padx=10)

        self.admin1Table = ttk.Treeview(self.root, columns=('name', 'description'))
        self.admin1Table.pack(pady=20, padx=20, expand=True, fill='both')
        self.admin1Table.heading('name', text="Name")
        self.admin1Table.heading('description', text="Description")
        self.admin1Table['show'] = 'headings'
        self.getvalues()
        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14))


        self.delButton = Button(self.root, text="Delete", width=15, font=('', 14), command=self.deleteAdmin1)
        self.delButton.pack(pady=20)






        self.root.mainloop()



    def deleteAdmin1(self):
        rowid = self.admin1Table.selection()
        if len(rowid) == 0:
            msg.showwarning("Warning","Please Select a Row",parent=self.root)
        elif len(rowid)>1:
            msg.showwarning("Warning","Please Select a Single Row at a time", parent=self.root)
        else:
            items = self.admin1Table.item(rowid[0])
            data = items['values']
            print(data)
            q = f"delete from category where name = '{data[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            self.getvalues()
            msg.showinfo("Success","category has been Removed....",parent=self.root)






    def searchcategory(self):
        search = self.txt.get()
        q = f"select * from category where name like'%{search}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for row in self.admin1Table.get_children():
            self.admin1Table.delete(row)
            count = 0
        for i in data:
            self.admin1Table.insert('',index=count,values=i)
            count+=1

    def getvalues(self):
        self.conn = connection.Connect()
        self.cr = self.conn.cursor()
        q = "select name,description from category"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for row in self.admin1Table.get_children():
            self.admin1Table.delete(row)
        count = 0
        for i in data:
            self.admin1Table.insert('',index=count, values=i)
            count+=1



if __name__ == '__main__':
    obj = Main()
