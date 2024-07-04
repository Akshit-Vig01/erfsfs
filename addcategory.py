import tkinter
import tkinter.messagebox as msg     #alias
import tkinter.ttk as ttk
from connection import Connect

class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Add Category')
        self.root.geometry('500x500')

        self.mainlabel = tkinter.Label(self.root,text="Add Category",font=('arial',14))
        self.mainlabel.pack(pady=20)

        self.formFrame = tkinter.Frame(self.root)
        self.formFrame.pack()
        self.font=('arial',14)

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Name ", font=self.font)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.font)
        self.lb1.grid(row=0, column=0, pady=10, padx=10)
        self.txt1.grid(row=0, column=1, pady=10, padx=10)


        self.lb2 = tkinter.Label(self.formFrame,text="Enter Description", font=self.font)
        self.txt2 = tkinter.Entry(self.formFrame,font=self.font)
        self.lb2.grid(row=1, column=0,pady=10, padx=10)
        self.txt2.grid(row=1,column=1,pady=10,padx=10)

        self.btn = tkinter.Button(self.root , text="Submit", width=20 ,font=('arial',14),command=self.insertAdmin1)
        self.btn.pack(pady=10)








        self.root.mainloop()


    def insertAdmin1(self):
        name=self.txt1.get()
        description=self.txt2.get()
        if name =='' or description =='':
            msg.showwarning("Warning","Please Enter All Values",parent=self.root)
        else:
            conn = Connect()
            cr = conn.cursor()
            q = f"insert into category values ('{name}','{description}')"
            cr.execute(q)
            conn.commit()
            msg.showinfo("Success","Category has been Added",parent=self.root)











if __name__ == '__main__':
    obj = Main()
