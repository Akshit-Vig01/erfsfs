import tkinter
import tkinter.messagebox as msg    #alias
import tkinter.ttk as ttk
from connection import Connect

class Main:
    def __init__(self):
        self.mainlbcolour="#385F71"
        self.root = tkinter.Tk()
        self.root.title('Add Admin')
        self.root.geometry('700x700')
        self.root.configure(bg="#FCB5B5")
        self.mainlabel = tkinter.Label(self.root, text="Add Admin", font=('arial',28),bg=self.mainlbcolour,foreground="White",relief=tkinter.SOLID)
        self.mainlabel.pack(pady=20,ipadx=20,ipady=20)

        self.formFrame = tkinter.Frame(self.root,bg="#BED8D4")
        self.formFrame.pack()
        self.font =('arial',14)

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Name ", font=self.font,bg="#BED8D4")
        self.txt1 = tkinter.Entry(self.formFrame, font=self.font,relief=tkinter.SOLID)
        self.lb1.grid(row=0, column=0, pady=10, padx=10)
        self.txt1.grid(row=0, column=1, pady=10, padx=10)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Email ", font=self.font)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.font)
        self.lb2.grid(row=1, column=0, pady=10, padx=10)
        self.txt2.grid(row=1, column=1, pady=10, padx=10)

        self.lb3 = tkinter.Label(self.formFrame, text="Enter Mobile ", font=self.font)
        self.txt3 = tkinter.Entry(self.formFrame, font=self.font)
        self.lb3.grid(row=2, column=0, pady=10, padx=10)
        self.txt3.grid(row=2, column=1, pady=10, padx=10)

        self.lb4 = tkinter.Label(self.formFrame, text="Enter Password ", font=self.font)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.font,show='*')
        self.lb4.grid(row=3, column=0, pady=10, padx=10)
        self.txt4.grid(row=3, column=1, pady=10, padx=10)

        self.lb5 = tkinter.Label(self.formFrame, text="Select Role ", font=self.font)
        self.txt5 = ttk.Combobox(self.formFrame,values=['Super Admin',"Admin"], state='readonly', font=self.font)
        self.lb5.grid(row=4, column=0, pady=10, padx=10)
        self.txt5.grid(row=4, column=1, pady=10, padx=10)

        self.btn = tkinter.Button(self.root, text='Submit', width=20,font=('arial',14), command=self.insertadmin,background="brown",foreground="blue",activebackground="yellow",activeforeground="red",highlightthickness=5,relief=tkinter.SUNKEN)
        self.btn.pack(pady=10)
        self.root.mainloop()

    def insertadmin(self):
         name=self.txt1.get()
         email = self.txt2.get()
         mobile = self.txt3.get()
         password = self.txt4.get()
         role = self.txt5.get()
         if name == '' or email == '' or mobile == '' or password == '' or role == '':
             msg.showwarning("Warning","Please Enter All Values", parent=self.root)
         else:
             conn = Connect()
             cr = conn.cursor()
             q = f"insert into admin values(null,'{name}','{email}','{mobile}','{password}','{role}')"
             cr.execute(q)
             conn.commit()
             msg.showinfo("Success","Admin has been Added ", parent=self.root)








if __name__ == '__main__':
    obj = Main()