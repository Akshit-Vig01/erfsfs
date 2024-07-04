import tkinter
import tkinter.messagebox as msg  # alias
import tkinter.ttk as ttk
from connection import Connect


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('User Change Password')
        self.root.geometry('700x700')

        self.mainlabel = tkinter.Label(self.root, text="Change Password", font=('arial', 28))
        self.mainlabel.pack(pady=20)

        self.formFrame = tkinter.Frame(self.root)
        self.formFrame.pack()
        self.font = ('arial', 14)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Email ", font=self.font)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.font)
        self.lb2.grid(row=0, column=0, pady=10, padx=10)
        self.txt2.grid(row=0, column=1, pady=10, padx=10)

        self.lb3 = tkinter.Label(self.formFrame, text="Enter Old Password ", font=self.font)
        self.txt3 = tkinter.Entry(self.formFrame, font=self.font, show='*')
        self.lb3.grid(row=1, column=0, pady=10, padx=10)
        self.txt3.grid(row=1, column=1, pady=10, padx=10)

        self.lb4 = tkinter.Label(self.formFrame, text="Enter New Password ", font=self.font)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.font, show='*')
        self.lb4.grid(row=2, column=0, pady=10, padx=10)
        self.txt4.grid(row=2, column=1, pady=10, padx=10)

        self.btn = tkinter.Button(self.root, text='Change Password', width=20, font=('arial', 14),
                                  command=self.checkAdmin)
        self.btn.pack(pady=10)
        self.root.mainloop()

    def checkAdmin(self):
        email = self.txt2.get()
        password = self.txt3.get()
        newpassword = self.txt4.get()
        conn = Connect()
        cr = conn.cursor()
        q = f"select * from user where email='{email}' and  password='{password}'"
        print(q)
        cr.execute(q)
        result = cr.fetchall()
        print(result)
        if len(result) == 0:
            msg.showwarning("", "Invalid Email/Password", parent=self.root)
        else:
            q = f"update user set password='{newpassword}' where email ='{email}'"
            cr.execute(q)
            conn.commit()
            # self.getvalues()
            # self.root.destroy()
            msg.showinfo("Success", "User  Password has been Updated....", parent=self.root)


if __name__ == '__main__':
    obj = Main()