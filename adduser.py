import tkinter
import tkinter.messagebox as msg #alias
import tkinter.ttk as ttk
from connection import Connect

class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Add User')
        self.root.geometry('700x700')

        self.mainlabel = tkinter.Label(self.root,text="Add User",font=('arial',28))
        self.mainlabel.pack(pady=20)

        self.formFrame = tkinter.Frame(self.root)
        self.formFrame.pack()
        self.font = ('arial',14)

        self.lb1 = tkinter.Label(self.formFrame,text="Enter Name ",font=self.font)
        self.txt1 = tkinter.Entry(self.formFrame,font=self.font)
        self.lb1.grid(row=0, column=0, pady=10,padx=10)
        self.txt1.grid(row=0, column=1,pady=10 ,padx=10)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Email ", font=self.font)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.font)
        self.lb2.grid(row=1, column=0, pady=10, padx=10)
        self.txt2.grid(row=1, column=1, pady=10, padx=10)

        self.lb3 = tkinter.Label(self.formFrame, text="Enter Mobile ", font=self.font)
        self.txt3 = tkinter.Entry(self.formFrame, font=self.font)
        self.lb3.grid(row=2, column=0, pady=10, padx=10)
        self.txt3.grid(row=2, column=1, pady=10, padx=10)

        self.lb4 = tkinter.Label(self.formFrame, text="Enter Password", font=self.font)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.font,show='*')
        self.lb4.grid(row=3, column=0, pady=10, padx=10)
        self.txt4.grid(row=3, column=1, pady=10, padx=10)

        self.lb5 = tkinter.Label(self.formFrame, text=" Select Gender", font=self.font)
        self.txt5 = ttk.Combobox(self.formFrame,values=['Male','Female',"Transgender"],state='readonly' ,font=self.font)
        self.lb5.grid(row=4, column=0, pady=10, padx=10)
        self.txt5.grid(row=4, column=1, pady=10, padx=10)

        self.lb6 = tkinter.Label(self.formFrame, text="Enter Address ", font=self.font)
        self.txt6 = tkinter.Entry(self.formFrame, font=self.font)
        self.lb6.grid(row=5, column=0, pady=10, padx=10)
        self.txt6.grid(row=5, column=1, pady=10, padx=10)


        self.btn = tkinter.Button(self.root,text="Submit",width=20,font=('arial',14),command=self.insertuser)
        self.btn.pack(pady=10)

        self.root.mainloop()


    def insertuser(self):
        name=self.txt1.get()
        email=self.txt2.get()
        mobile=self.txt3.get()
        password=self.txt4.get()
        gender=self.txt5.get()
        address=self.txt6.get()
        if name == ''or email == ''or mobile==''or password == ''or gender ==''or address == '':
            msg.showwarning("Warning","Please Enter All Values",parent=self.root)
        else:
            conn = Connect()
            cr = conn.cursor()
            q = f"insert into user values (null,'{name}','{email}','{mobile}','{password}','{gender}','{address}')"
            cr.execute(q)
            conn.commit()
            msg.showinfo("Success","User has been Added ",parent=self.root)




if __name__ == '__main__':
    obj = Main()