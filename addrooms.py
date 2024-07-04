import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect

class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Check In')
        self.root.geometry('800x800')

        self.mainLabel = tkinter.Label(self.root, text="Check In", font=('arial', 28, "bold"))
        self.mainLabel.pack(pady=20)

        self.formFrame = tkinter.Frame(self.root)
        self.formFrame.pack()
        self.font =('arial',14)

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Name", font=self.font)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.font)
        self.lb1.grid(row=0, column=0, pady=10, padx=10)
        self.txt1.grid(row=0, column=1, pady=10, padx=10)

        self.lb2 = tkinter.Label(self.formFrame, text="Select Floor", font=self.font)
        self.txt2 = ttk.Combobox(self.formFrame, font=self.font,values=['1','2','3','4','5'],state='readonly')
        self.lb2.grid(row=1, column=0, pady=10, padx=10)
        self.txt2.grid(row=1, column=1, pady=10, padx=10)

        self.lb3 = tkinter.Label(self.formFrame, text="Enter Description", font=self.font)
        self.txt3 = tkinter.Entry(self.formFrame, font=self.font)
        self.lb3.grid(row=2, column=0, pady=10, padx=10)
        self.txt3.grid(row=2, column=1, pady=10, padx=10)

        self.lb4 = tkinter.Label(self.formFrame, text="Select Type", font=self.font)
        self.txt4 = ttk.Combobox(self.formFrame, values=['AC', "Non AC"], state='readonly', font=self.font)
        self.lb4.grid(row=3, column=0, pady=10, padx=10)
        self.txt4.grid(row=3, column=1, pady=10, padx=20)



        self.lb5 = tkinter.Label(self.formFrame, text="Enter Occupancy", font=self.font)
        self.txt5 = tkinter.Entry(self.formFrame, font=self.font)
        self.lb5.grid(row=4, column=0, pady=10, padx=10)
        self.txt5.grid(row=4, column=1, pady=10, padx=10)

        self.lb6 = tkinter.Label(self.formFrame, text="Select Category", font=self.font)
        self.txt6 = ttk.Combobox(self.formFrame, font=self.font, state='readonly', values=self.getCatName())
        self.lb6.grid(row=5, column
        =0, pady=10, padx=10)
        self.txt6.grid(row=5, column=1, pady=10, padx=10)

        self.lb7 = tkinter.Label(self.formFrame, text=" Room Price" , font=self.font)
        self.txt7 = tkinter.Entry(self.formFrame,font=self.font)
        self.lb7.grid(row=6,column=0,pady=10,padx=10)
        self.txt7.grid(row=6,column=1,pady=10,padx=10)

        self.lb8 = tkinter.Label(self.formFrame, text="Room Status", font=self.font)
        self.txt8 = ttk.Combobox(self.formFrame, font=self.font,values=['0',"1"])
        self.lb8.grid(row=7, column=0, pady=10, padx=10)
        self.txt8.grid(row=7, column=1, pady=10, padx=10)






        self.btn = tkinter.Button(self.root, text='Submit', width=20, font=('arial',14), command=self.insert)
        self.btn.pack(pady=10)
        self.root.mainloop()


    def getCatName(self):
        conn = Connect()
        cr = conn.cursor()
        q = f'select name from category'
        cr.execute(q)
        result = cr.fetchall()
        lst = []
        for i in result:
            lst.append(i[0])
        return lst


    def insert(self):
        name = self.txt1.get()
        floor = self.txt2.get()
        desc= self.txt3.get()
        type = self.txt4.get()
        occupancy = self.txt5.get()
        category = self.txt6.get()
        price = self.txt7.get()
        status = self.txt8.get()
        if name == '' or floor == '' or desc == '' or type == '' or occupancy == '' or category =='' or price =='' or status =='':
            msg.showwarning("Warning", "Please Enter All Values")
        else:
            conn = Connect()
            cr = conn.cursor()
            q = f"insert into rooms values(null,'{name}','{floor}','{desc}', '{type}','{occupancy}','{category}','{price}','{status}')"
            cr.execute(q)
            conn.commit()
            msg.showinfo("Success","Rooms Added Successfully....")
            self.txt1.delete(0,"end")
            self.txt2.set("")
            self.txt3.delete(0,"end")
            self.txt4.set("")
            self.txt5.delete(0,"end")
            self.txt6.set("")
            self.txt7.delete(0,"end")
            self.txt8.set("")



if __name__ == '__main__':
    Main()