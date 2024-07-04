from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import connection
class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('View Bookings')

        self.mainLabel = Label(self.root, text="Bookings Details", font=('',30,'bold'))
        self.mainLabel.pack(pady=20)

        self.formFrame = Frame(self.root)
        self.formFrame.pack(pady=10)


        self.adminTable = ttk.Treeview(self.root, columns=('id','booking_id','room_id','room_number'))
        self.adminTable.pack(pady=20 ,padx=20, expand=True, fill='both')
        self.adminTable.heading('id',text="ID")
        self.adminTable.heading('booking_id', text="Booking_ID")
        self.adminTable.heading('room_id',text= "Room_ID")
        self.adminTable.heading('room_number',text='Room_Number')

        self.adminTable['show'] = 'headings'
        self.getvalues()

        style = ttk.Style()
        style.configure('Treeview',font=('arial',14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial',14))
        # self.adminTable.bind("<Double-1>", self.openUpdateWindow)

        # self.delButton =Button(self.root, text="Delete", width=15,font=('',14),command=self.deleteuser)
        # self.delButton.pack(pady=20)

        self.root.mainloop()
    def getvalues(self):
        self.conn = connection.Connect()
        self.cr = self.conn.cursor()
        q = "select id ,booking_id,room_id,room_number from booking_detail"
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