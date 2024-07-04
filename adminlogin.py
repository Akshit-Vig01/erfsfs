import tkinter
import tkinter.messagebox as msg    #alias
import tkinter.ttk as ttk
from connection import Connect
import admindashboard


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Admin Login')
        self.root.geometry('700x700')

        self.mainlabel = tkinter.Label(self.root, text="Admin Login", font=('arial',28))
        self.mainlabel.pack(pady=20)

        self.formFrame = tkinter.Frame(self.root)
        self.formFrame.pack()
        self.font =('arial',14)


        self.lb2 = tkinter.Label(self.formFrame, text="Enter Email ", font=self.font)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.font)
        self.lb2.grid(row=0, column=0, pady=10, padx=10)
        self.txt2.grid(row=0, column=1, pady=10, padx=10)


        self.lb4 = tkinter.Label(self.formFrame, text="Enter Password ", font=self.font)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.font,show='*')
        self.lb4.grid(row=1, column=0, pady=10, padx=10)
        self.txt4.grid(row=1, column=1, pady=10, padx=10)


        self.btn = tkinter.Button(self.root, text='Login', width=20,font=('arial',14), command=self.checkAdmin)
        self.btn.pack(pady=10)
        self.root.mainloop()

    def checkAdmin(self):
        email = self.txt2.get()
        password = self.txt4.get()
        conn = Connect()
        cr = conn.cursor()
        q = f"select * from admin where email='{email}' and password='{password}'"
        cr.execute(q)
        result = cr.fetchall()
        if len(result) ==0:
            msg.showwarning("","Invalid Email/Password",parent=self.root)
        else:
            msg.showinfo("","Login Successful",parent=self.root)
            self.root.destroy()
            id=result[0][0]
            name=result[0][1]
            role=result[0][-1]
            email=result[0][2]
            admindashboard.Main(adminid=id,adminname=name,adminemail=email,adminrole=role)



if __name__ == '__main__':
    obj = Main()