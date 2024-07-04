from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import connection

class Main:
    def __init__(self):
        self.conn = connection.Connect()
        self.cr = self.conn.cursor()
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('View Rooms')

        self.roomlabel = Label(self.root,text="View Rooms",font=('arial',30,'bold'))
        self.roomlabel.pack(pady=20)


        self.searchFrame = Frame(self.root)
        self.searchFrame.pack(pady=10)

        self.searchLabel = Label(self.searchFrame,text="Search",font=('arial',14))
        self.searchLabel.grid(row=0,column=0,pady=10,padx=10)
        self.searchBox = ttk.Combobox(self.searchFrame,font=('arial',14),width=20,state='readonly',values=['Name','Floor','Type','Category'])
        self.searchBox.bind('<<ComboboxSelected>>',self.selectSearchType)
        self.searchBox.grid(row=0,column=1,pady=10,padx=10)
        self.searchBtn = Button(self.searchFrame,font=('arial',14),text="Search",width=10,command=self.searchRoom)
        self.searchNameBox = Entry(self.searchFrame, width=10, font=('arial', 14))
        self.searchNameBox.grid(row=0, column=2, padx=10, pady=10)
        self.searchBtn.grid(row=0,column=3,pady=10,padx=10)
        self.refreshBtn = Button(self.searchFrame,font=('arial',14),text="Refresh",width=10,command=self.getvalues)
        self.refreshBtn.grid(row=0,column=4,pady=10,padx=10)

        self.roomtable = ttk.Treeview(self.root,columns=('id','name','floor',"description",'type','occupancy','category',"price","status"))
        self.roomtable.pack(pady=20,padx=20,expand=True,fill='both')

        self.roomtable.heading('id',text="ID")
        self.roomtable.heading('name', text="Name")
        self.roomtable.heading('floor', text="Floor")
        self.roomtable.heading("description",text="Description")
        self.roomtable.heading('type', text="Type")
        self.roomtable.heading('occupancy', text="Occupancy")
        self.roomtable.heading('category', text="Category")
        self.roomtable.heading('price',text="Price")
        self.roomtable.heading('status',text="Status")

        self.roomtable['show'] = 'headings'
        self.roomtable.bind("<Double-1>", self.openUpdateWindow)
        self.getvalues()

        self.style = ttk.Style()
        self.style.configure('Treeview',font=('arial',14),rowheight=40)
        self.style.configure("Treeview.Heading", font=('arial', 14))

        self.delButton=Button(self.root,text="Delete",width=15,font=('arial',14),command=self.delrooms)
        self.delButton.pack(pady=20)

        self.root.mainloop()

    def selectSearchType(self,e):
        self.searchNameBox.grid_forget()
        searchType = self.searchBox.get()
        if searchType =='Name':
            self.searchNameBox = Entry(self.searchFrame,width=10,font=('arial',14))
            self.searchNameBox.grid(row = 0,column=2,padx=10,pady=10)
        elif searchType == 'Floor':
            self.searchNameBox = ttk.Combobox(self.searchFrame,width=10,font=('arial',14),state='readonly',values=tuple(range(1,101)))
            self.searchNameBox.grid(row=0,column=2,padx=10,pady=10)
        elif searchType == 'Type':
            self.searchNameBox = ttk.Combobox(self.searchFrame,width=10,font=('arial',14),state='readonly',values=['AC','Non AC'])
            self.searchNameBox.grid(row=0,column=2,pady=10,padx=10)
        elif searchType == 'Category':
            self.searchNameBox = ttk.Combobox(self.searchFrame,width=10,font=('arial',14),state='readonly',values=connection.getCatName())
            self.searchNameBox.grid(row=0,column=2,pady=10,padx=10)


    def searchRoom(self):
        searchType = self.searchBox.get()
        searchName = self.searchNameBox.get()
        if searchType =='Name':
            q = f"select * from rooms where name like '{searchName}'"
        elif searchType =='Floor':
            q = f"select * from rooms where floor = '{searchName}'"
        elif searchType =='Type':
            q = f"select * from rooms where type = '{searchName}'"
        elif searchType =='Category':
            q = f"select * from rooms where category ='{searchName}'"
        else:
            q = f"select * from rooms"

        conn  = connection.Connect()
        cr = conn.cursor()
        cr.execute(q)
        result = cr.fetchall()
        count = 0
        for row in self.roomtable.get_children():
            self.roomtable.delete(row)
        for i in result:
            self.roomtable.insert("",index=count,values=i)
            count +=1



    def openUpdateWindow(self, event):
        data = self.roomtable.item(self.roomtable.selection()[0])['values']
        self.root1 = Toplevel()
        self.root1.title('Update Room')
        self.root1.geometry('800x800')

        self.roomlabel1 = Label(self.root1,text="Update Room",font=('arial',24,'bold'))
        self.roomlabel1.pack(pady=20)

        self.updateForm = Frame(self.root1)
        self.updateForm.pack(pady=10)
        self.font = ('arial',14)

        self.lb1 = Label(self.updateForm,text="ID",font=self.font)
        self.txt1=Entry(self.updateForm,font=self.font,width=30)
        self.lb1.grid(row= 0,column=0,pady=20,padx=10)
        self.txt1.grid(row=0,column=1,pady=20,padx=10)
        self.txt1.insert(0,data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.updateForm, text="Enter Name", font=self.font)
        self.txt2 = Entry(self.updateForm, font=self.font, width=30)
        self.lb2.grid(row=1, column=0, pady=20, padx=10)
        self.txt2.grid(row=1, column=1, pady=20, padx=10)
        self.txt2.insert(0, data[1])

        self.lb3 = Label(self.updateForm, text="Select Floor", font=self.font)
        self.txt3 = ttk.Combobox(self.updateForm, font=self.font, width=30,values=['1','2','3','4','5'],state='readonly')
        self.lb3.grid(row=2, column=0, pady=20, padx=10)
        self.txt3.grid(row=2, column=1, pady=20, padx=10)
        self.txt3.insert(0, data[2])

        self.lb4 = Label(self.updateForm, text="Enter Description", font=self.font)
        self.txt4 = Entry(self.updateForm, font=self.font, width=30)
        self.lb4.grid(row=3, column=0, pady=20, padx=10)
        self.txt4.grid(row=3, column=1, pady=20, padx=10)
        self.txt4.insert(0, data[3])

        self.lb5 = Label(self.updateForm, text="Select Type ", font=self.font)
        self.txt5 = ttk.Combobox(self.updateForm, font=self.font, width=28,values=['AC','Non AC'],state='readonly')
        self.lb5.grid(row=4, column=0, pady=20, padx=10)
        self.txt5.grid(row=4, column=1, pady=20, padx=10)
        self.txt5.insert(0, data[4])

        self.lb6 = Label(self.updateForm, text="Enter Occupancy", font=self.font)
        self.txt6 = Entry(self.updateForm, font=self.font, width=30)
        self.lb6.grid(row=5, column=0, pady=20, padx=10)
        self.txt6.grid(row=5, column=1, pady=20, padx=10)
        self.txt6.insert(0, data[5])

        self.lb7 = Label(self.updateForm, text="Enter Category", font=self.font)
        self.txt7 =ttk.Combobox(self.updateForm, font=self.font , width=30,state='readonly',values=connection.getCatName())
        self.lb7.grid(row=6, column=0, pady=20, padx=10)
        self.txt7.grid(row=6, column=1, pady=20, padx=10)
        self.txt7.insert(0, data[6])

        self.lb8 = Label(self.updateForm, text="Enter Price", font=self.font)
        self.txt8 = Entry(self.updateForm, font=self.font, width=30)
        self.lb8.grid(row=7, column=0, pady=20, padx=10)
        self.txt8.grid(row=7, column=1, pady=20, padx=10)
        self.txt8.insert(0, data[7])

        self.lb9 = Label(self.updateForm, text="Enter Status", font=self.font)
        self.txt9 = ttk.Combobox(self.updateForm, font=self.font, width=30, state='readonly', values=['0',["1"]])
        self.lb9.grid(row=8, column=0, pady=20, padx=10)
        self.txt9.grid(row=8, column=1, pady=20, padx=10)
        self.txt9.insert(0, data[8])

        self.updateBtn = Button(self.root1,text="Update",width=15,font=self.font,command=self.updaterooms)
        self.updateBtn.pack(pady=20)

    def updaterooms(self):
        id = self.txt1.get()
        name = self.txt2.get()
        floor = self.txt3.get()
        description = self.txt4.get()
        type = self.txt5.get()
        occupancy = self.txt6.get()
        category = self.txt7.get()
        price = self.txt8.get()
        status = self.txt9.get()

        q = f"update rooms set name='{name}',floor='{floor}',description='{description}',type='{type}',occupancy='{occupancy}',category='{category}',price='{price}',status='{status}' where id='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        self.getvalues()
        self.root1.destroy()
        msg.showinfo("Success","Room has been Updated....",parent=self.root)







    def delrooms(self):
        rowid = self.roomtable.selection()
        if len(rowid) ==0:
            msg.showwarning("Warning","Please Select a Row ",parent = self.root)
        elif len(rowid)>1:
            msg.showwarning("Warning","Please Select a Single Row at a time",parent=self.root)
        else:
            items = self.roomtable.item(rowid[0])
            data = items['values']
            q = f"delete from rooms where id='{data[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            self.getvalues()
            msg.showinfo("Success","Room has been Removed....",parent=self.root)

    def getvalues(self):
        self.conn = connection.Connect()
        self.cr = self.conn.cursor()
        q = "select id,name,floor,description,type,occupancy,category,price,status from rooms"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for row in self.roomtable.get_children():
            self.roomtable.delete(row)
        count = 0
        for i in data :
            self.roomtable.insert('',index=count,values=i)
            count += 1



if __name__ == '__main__':
    obj = Main()
