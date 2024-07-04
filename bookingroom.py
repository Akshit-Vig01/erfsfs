import tkinter
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from tkcalendar import DateEntry
import datetime
import connection


class Main:
    def __init__(self):
        self.root = Tk()
        self.conn = connection.Connect()
        self.cr = self.conn.cursor()
        self.root.state('zoomed')
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()


        self.mainLabel = Label(self.root, text="Booking", font=('', 28, 'bold'))
        self.mainLabel.pack(pady=20)

        self.mainFrame = Frame(self.root)
        self.mainFrame.pack(fill='both', expand=True)

        self.RoomListFrame = Frame(self.mainFrame, width=int(width * (2 / 3)))
        self.RoomListFrame.pack(side='left', fill='both', expand=True)

        self.BookingFrame = Frame(self.mainFrame, width=int(width * (1 / 3)))
        self.BookingFrame.pack(side='right', fill='both', expand=True)

        # Fix the width of RoomListFrame to not resize with the window
        self.mainFrame.columnconfigure(0, weight=1)

        self.choiceFrame = Frame(self.RoomListFrame)
        self.choiceFrame.pack(pady=10)
        self.lb1 = Label(self.choiceFrame, text="Choose Floor", font=('', 12))
        self.lb1.grid(row=0, column=0, pady=10, padx=10)

        self.choice = ttk.Combobox(self.choiceFrame, values=tuple(range(1, 6)), state='readonly',
                                   font=('', 12))
        self.choice.grid(row=0, column=1, pady=10, padx=10)
        self.choice.bind("<<ComboboxSelected>>", self.getRooms)

        self.ACFrame = LabelFrame(self.RoomListFrame, text="AC Rooms", font=('', 14), width=200)
        self.ACFrame.pack()
        self.NonACFrame = LabelFrame(self.RoomListFrame, text="Non AC Rooms", font=('', 14))
        self.NonACFrame.pack()

        self.ACFrame = LabelFrame(self.RoomListFrame, text="AC Rooms", font=('', 14), width=200)
        self.ACFrame.pack()
        self.NonACFrame = LabelFrame(self.RoomListFrame, text="Non AC Rooms", font=('', 14))
        self.NonACFrame.pack()
        self.lb = Label(self.BookingFrame, text="Booking Details", font=('', 20, 'bold'))
        self.lb.pack(pady=10)
        self.roomTv = ttk.Treeview(self.BookingFrame, columns=['id', 'num', 'price'])
        self.roomTv.pack(pady=10)
        self.roomTv.heading('id', text='ID')
        self.roomTv.heading('num', text='Room Number')
        self.roomTv.heading('price', text='Price')
        self.roomTv['show'] = 'headings'
        self.selectedRoomList = []

        self.btn = Button(self.BookingFrame, text="Submit",command=self.openupdatewindow, font=('', 14), width=10)
        self.btn.pack(pady=10)
        self.mainFrame.columnconfigure(0, weight=1)
        self.root.mainloop()

    def openupdatewindow(self):
        if len(self.roomTv.get_children()) == 0:
            msg.showinfo('', 'No Rooms Selected')
        else:
            self.root1 = Toplevel()
            self.root1.title('Booking Form')
            # self.root1.geometry('600x600')
            self.root1.state('zoomed')
            self.mainLabel = Label(self.root1, text="Booking Form", font=('arial', 26, 'bold'))
            self.mainLabel.pack(pady=20)

            self.formFrame = tkinter.Frame(self.root1)
            self.formFrame.pack()
            self.font = ('arial', 14,'bold')

            self.lb2 = tkinter.Label(self.formFrame, text="Customer Name", font=self.font)
            self.txt2 = tkinter.Entry(self.formFrame, font=self.font)
            self.lb2.grid(row=0, column=0, pady=10, padx=10)
            self.txt2.grid(row=0, column=1, pady=10, padx=10)

            self.lb3 = tkinter.Label(self.formFrame, text="Customer Mobile no.", font=self.font)
            self.txt3 = tkinter.Entry(self.formFrame, font=self.font)
            self.lb3.grid(row=1, column=0, pady=10, padx=10)
            self.txt3.grid(row=1, column=1, pady=10, padx=10)

            self.lb4 = tkinter.Label(self.formFrame, text="Customer Email", font=self.font)
            self.txt4 = tkinter.Entry(self.formFrame, font=self.font)
            self.lb4.grid(row=2, column=0, pady=10, padx=10)
            self.txt4.grid(row=2, column=1, pady=10, padx=10)

            self.lb5 = tkinter.Label(self.formFrame, text="Customer Aadhaar No.", font=self.font)
            self.txt5 = tkinter.Entry(self.formFrame, font=self.font)
            self.lb5.grid(row=3, column=0, pady=10, padx=10)
            self.txt5.grid(row=3, column=1, pady=10, padx=10)

            self.lb6 = tkinter.Label(self.formFrame, text="Check-In Date", font=self.font)
            self.txt6 = DateEntry(self.formFrame, font=self.font, date_pattern="yyyy-mm-dd", width=20)
            self.lb6.grid(row=4, column=0, pady=10, padx=10)
            self.txt6.grid(row=4, column=1, pady=10, padx=10)

            self.lb6_1 = tkinter.Label(self.formFrame, text="Select Days", font=self.font)
            self.txt6_1 = ttk.Combobox(self.formFrame, values=tuple(range(1, 11)), state='readonly', font=self.font)
            self.lb6_1.grid(row=4, column=2, pady=10, padx=10)
            self.txt6_1.grid(row=4, column=3, pady=10, padx=10)
            self.txt6_1.bind('<<ComboboxSelected>>', self.calculateDateAmount)

            self.lb7 = tkinter.Label(self.formFrame, text="Check-In-Time", font=self.font)
            self.txt7 = tkinter.Entry(self.formFrame, font=self.font)
            self.lb7.grid(row=5, column=0, pady=10, padx=10)
            self.txt7.grid(row=5, column=1, pady=10, padx=10)
            # self.btn1=Button(self.formFrame,text="get",command=self.gettime )
            # self.btn1.grid(row=5, column=3)

            self.lb8 = tkinter.Label(self.formFrame, text="Persons", font=self.font)
            self.txt8 = ttk.Combobox(self.formFrame, values=['1', "2", "3", "4","5","6","7","8","9","10"], state='readonly', font=self.font)
            self.lb8.grid(row=9, column=0, pady=10, padx=10)
            self.txt8.grid(row=9, column=1, pady=10, padx=10)

            self.lb9 = tkinter.Label(self.formFrame, text="Total Amount", font=self.font)
            self.txt9 = tkinter.Entry(self.formFrame, font=self.font)
            self.lb9.grid(row=10, column=0, pady=10, padx=10)
            self.txt9.grid(row=10, column=1, pady=10, padx=10)

            self.lb10 = tkinter.Label(self.formFrame, text="Check-Out Date", font=self.font)
            self.txt10 = Entry(self.formFrame, font=self.font,state='readonly')
            self.lb10.grid(row=6, column=0, pady=10, padx=10)
            self.txt10.grid(row=6, column=1, pady=10, padx=10)

            self.lb11 = tkinter.Label(self.formFrame, text="Check-Out Time", font=self.font)
            self.txt11 = tkinter.Entry(self.formFrame, font=self.font)
            self.lb11.grid(row=7, column=0, pady=10, padx=10)
            self.txt11.grid(row=7, column=1, pady=10, padx=10)

            self.getTimeButton = Button(self.formFrame, text='Get Current Time', font=('', 10,'bold'),
                                        command=self.gettime)
            self.getTimeButton.grid(row=5, column=2, padx=10, pady=20)

            self.btn = Button(self.formFrame, text="Submit", font=('', 14,'bold'), width=10, command=self.confirmBooking)
            self.btn.grid(row=11, column=1, pady=10)
            self.root1.mainloop()

    def calculateDateAmount(self, e):
        days = int(self.txt6_1.get())
        date_str = self.txt6.get()
        date = datetime.datetime.strptime(f"{date_str}", '%Y-%m-%d')
        if date.date() < datetime.date.today():
            self.txt6_1.set('')
            msg.showwarning("", 'Please Select a Valid Date')

        else:
            print(date)
            outdate = date + datetime.timedelta(days=days)
            self.txt10.configure(state='normal')
            self.txt10.delete(0, 'end')
            self.txt10.insert(0, str(outdate).split(' ')[0])
            self.txt10.configure(state='readonly')
            self.gettime()
            self.getAmount()

    def getAmount(self):
        days = self.txt6_1.get()
        if days != '':
            total = 0.0 #Initialize total as a floating-point number
            for row in self.roomTv.get_children():
                room = self.roomTv.item(row)['values']
                total += float(room[-1])
            total *= int(days)
            self.txt9.delete(0, 'end')
            self.txt9.insert(0, "{:.2f}".format(total))
            # self.txt9.insert(0, f"{round(total)}")

    def confirmBooking(self):
        name = self.txt2.get()
        mobile = self.txt3.get()
        email = self.txt4.get()
        in_date = self.txt6.get()
        in_time = self.txt7.get()
        aadhaar = self.txt5.get()
        persons = self.txt8.get()
        amount = self.txt9.get()
        out_date = self.txt10.get()
        out_time = self.txt11.get()
        days = self.txt6_1.get()
        if name == '' or email == '' or mobile == '' or in_time == '' or in_date == '' or out_time == '' or out_date == '' or aadhaar == '' or persons =='' :
            msg.showwarning("Warning", "Please Enter All Values")

        else:
            q = f"insert into booking values(null, '{in_date}', '{in_time}','{out_date}','{out_time}','{name}','{email}','{mobile}','{aadhaar}','{persons}','{amount}','{days}')"
            self.cr.execute(q)
            self.conn.commit()
            booking_id = self.cr.lastrowid

        for row in self.roomTv.get_children():
            room = self.roomTv.item(row)['values']
            q = f"insert into booking_detail values(null, '{booking_id}','{room[0]}','{room[1]}')"
            self.cr.execute(q)
            self.conn.commit()
            self.roomTv.delete(row)
            self.selectedRoomList.clear()
        msg.showinfo("", f"Booking has been confirmed with Booking ID - {booking_id}")


    def getRooms(self, e):
        for i in self.ACFrame.winfo_children():
            i.destroy()
        floor = self.choice.get()
        q = f"select * from rooms where floor='{floor}'"
        self.cr.execute(q)
        result = self.cr.fetchall()
        ACList = []
        NonACList = []
        for i in result:
            if i[4] == 'AC':
                ACList.append(i)
            else:
                NonACList.append(list(i))
        self.showACRooms(ACList)
        self.showNonACRooms(NonACList)

    def showACRooms(self, rooms):
        for i in self.NonACFrame.winfo_children():  # return list of all widget
            i.destroy()
        row = 0
        col = 0
        for i in rooms:
            if col == 4:
                row += 1
                col = 0
            self.btn = Button(self.ACFrame, text=i[1], font=('', 12), width=5, height=5,
                              command=lambda room=i: self.roomSelected(room)) # passes a tuple that contains all information for the room
                              #command=lambda room=id=i[0], num=i[1]: self.roomSelected(id, num)) # passes id, num that represents the selected room
            self.btn.grid(row=row, column=col, padx=20, pady=20)
            col += 1

    def roomSelected(self, room):
        print(room)
        detail = f"""Room No - {room[1]}
        Category - {room[6]}
        Floor - {room[2]}
        Price - {room[7]}
        Occupancy - {room[5]}
        Status - {room[8]}"""
        self.option = msg.askokcancel(f"Room - {room[1]}", detail)
        if self.option == True:
            if room[1] not in self.selectedRoomList:
                self.roomTv.insert('', index=0, values=[room[0], room[1], room[7]])
                self.selectedRoomList.append(room[1])
            else:
                msg.showwarning("","Already Selected")

    def showNonACRooms(self, rooms):
        row = 0
        col = 0
        for i in rooms:
            if col == 4:
                row += 1
                col = 0
            self.btn = Button(self.NonACFrame, text=i[1], font=('', 12), width=5, height=5,
                              command=lambda room=i: self.roomSelected(room))
            self.btn.grid(row=row, column=col, padx=20, pady=20)
            col += 1
    def gettime(self):
        time= datetime.datetime.now().time()
        self.txt7.delete(0,'end')
        self.txt7.insert(0, str(time).split('.')[0])
        self.txt11.delete(0, 'end')
        self.txt11.insert(0, str(time).split('.')[0])



# obj = Main()
