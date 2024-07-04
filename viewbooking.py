from tkinter import *
import os.path
import tkinter.ttk as ttk
import connection
import tkinter.messagebox as msg
from tkcalendar import DateEntry
import datetime
import webbrowser

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("View Bookings")
        self.root.state('zoomed')
        self.mainLabel = Label(self.root, text='View Bookings', font=('arial', 28, 'bold'))
        self.mainLabel.pack(pady=10)
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.formFrame = Frame(self.root, height=int(height * (2 / 3)))
        self.formFrame.pack(pady=10, side='top', fill='both', expand=True)
        self.viewFrame = Frame(self.root, height=int(height * (1 / 2)))
        self.viewFrame.pack(pady=10, side='bottom', fill='both', expand=True)

        self.mainLabel = Label(self.viewFrame, text='View Booking Details', font=('arial', 28, 'bold'))
        self.mainLabel.pack(pady=10)

        font = ('arial', 14)
        self.lb1 = Label(self.formFrame, text="Search by ", font=font)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.btn1 = Button(self.formFrame, text='Search', font=font, command=self.searchBooking)
        self.btn1.grid(row=0, column=3, padx=10, pady=10)
        self.btn2 = Button(self.formFrame, text='Refresh', font=font, command=self.getValues)
        self.btn2.grid(row=0, column=4, padx=10, pady=10)
        self.updatebtn = Button(self.formFrame, text='Update Booking', font=font, command=self.editThisBooking)
        self.updatebtn.grid(row=0, column=5, padx=10, pady=10)
        self.btn4 = Button(self.formFrame, text='Print Reciept', font=font, command=self.print)
        self.btn4.grid(row=0, column=6, padx=10, pady=10)



        self.lbb1 = Label(self.formFrame, text='Search')
        self.cbSearch = ttk.Combobox(self.formFrame, font=font, width=10, state='readonly', values=['Customer Name', 'Check-In Date', 'Check-Out Date', 'Time', 'Persons'])
        # self.cbSearch.bind('<<ComboboxSelected>>', self.selectSearchType)
        self.cbSearch.grid(row=0, column=1, padx=10, pady=10)
        self.searchNamebox = Entry(self.formFrame, width=40)
        self.searchNamebox.grid(row=0, column=2, padx=10, pady=10)
        self.bookingTable = ttk.Treeview(self.root, columns=("id", "checkin_date", "checkin_time", "checkout_date", "checkout_time", "customer_name", "customer_email", "customer_mobile", "aadhaar_number", "persons", "amount"))
        self.bookingTable.pack(pady=10, expand=True, fill='both')

        self.bookingTable.heading('id', text='ID')
        self.bookingTable.heading('checkin_date', text='CHECK-IN DATE')
        self.bookingTable.heading('checkin_time', text='CHECK-IN TIME')
        self.bookingTable.heading('checkout_date', text='CHECK-OUT DATE')
        self.bookingTable.heading('checkout_time', text='CHECK-OUT TIME')
        self.bookingTable.heading('customer_name', text='CUSTOMER NAME')
        self.bookingTable.heading('customer_email', text='EMAIL')
        self.bookingTable.heading('customer_mobile', text='MOBILE')
        self.bookingTable.heading('aadhaar_number', text='AADHAAR')
        self.bookingTable.heading('persons', text='PERSONS')
        self.bookingTable.heading('amount', text='AMOUNT')

        self.bookingTable.column("id", width=30)
        self.bookingTable.column("checkin_date", width=110)
        self.bookingTable.column("checkin_time", width=150)
        self.bookingTable.column("checkout_time", width=150)
        self.bookingTable.column("checkout_date", width=130)
        self.bookingTable.column("customer_mobile", width=130)
        self.bookingTable.column("customer_name", width=140)
        self.bookingTable.column("aadhaar_number", width=130)
        self.bookingTable.column("persons", width=130)
        self.bookingTable.column("amount", width=90)

        self.bookingTable['show'] = 'headings'
        self.bookingTable.bind('<Double-1>', self.showDataInViewTv)
        self.getValues()

        self.style = ttk.Style()
        self.style.configure("Treeview", font=('arial', 10), rowheight=30)
        self.style.configure("Treeview.Heading", font=('arial', 13))

        self.viewTv = ttk.Treeview(self.viewFrame, columns=['id', 'bookingid', 'roomid', 'roomNumber'])
        self.viewTv.pack(pady=10)
        self.viewTv.heading("id", text='ID')
        self.viewTv.heading("bookingid", text='BOOKING ID')
        self.viewTv.heading("roomid", text='ROOM ID')
        self.viewTv.heading("roomNumber", text='ROOM NUMBER')
        self.viewTv['show'] = 'headings'
        self.root.mainloop()

    def print(self):

        self.conn =connection.Connect()
        self.cr = self.conn.cursor()
        data = self.bookingTable.selection()
        data = self.bookingTable.item(data)
        data = data['values']
        q = f"select rooms.name, rooms.category, rooms.price from booking_detail inner join rooms on booking_detail.room_id = rooms.id where booking_id='{data[0]}'"
        print(q)
        self.cr.execute(q)
        result = self.cr.fetchall()

        table = ''
        for i in result:
            table += '<tr>'
            table += f"<td>{i[0]}</td>"
            table += f"<td>{i[1]}</td>"
            table += f"<td>{i[2]}</td>"
            table += '</tr>'

        htmlcode = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Bill</title>
            <link rel="stylesheet" href="bootstrap.min.css">
        </head>
        <body onload="window.print()">

        <h3 class="text-center my-3">Booking Reciept</h3>
        <h4 class="text-end px-5"> Date - {datetime.date.today()}</h4>

        <div class="row">
            <div class="offset-1 col-5 text-start py-3">
                Customer Name - {data[5]}
            </div>
            <div class="col-5 text-end py-3">
                Customer Email - {data[6]}
            </div>
            <div class="offset-1 col-5 text-start py-3">
                Customer Mobile - {data[7]}
            </div>
            <div class="col-5 text-end py-3">
                Customer Aadhaar - {data[8]}
            </div>
            <div class="offset-1 col-5 text-start py-3">
                Check In Date - {data[1]}
            </div>
            <div class="col-5 text-end py-3">
                Check Out Date - {data[3]}
            </div>
            <div class="offset-1 col-5 text-start py-3">
                Check In Time - {data[2]}
            </div>
            <div class="col-5 text-end py-3">
                Check Out Time - {data[4]}
            </div>
        </div>

        <div class="py-5 px-5">
            <table width="100%" class="table table-bordered">
                <thead>
                <tr>
                    <th>Room No.</th>
                    <th>Category</th>
                    <th>Price</th>
                </tr>
                </thead>
                <tbody>
                {table}
                </tbody>
                <tfoot>
                <tr>
                    <th colspan="2" class="text-end">Total Balance</td>
                    <th>&#x20b9; {data[10]} </td>
                </tr>
                </tfoot>
            </table>
        </div>

        <p class="py-3 text-center h6">Your Booking ID - {data[0]} with Total of &#x20b9; {data[10]}  for {data[11]} days</p>

        </body>
        </html>"""

        with open('reciept/bill.html', 'w') as file:
            file.write(htmlcode)
            file.close()

        path = os.path.abspath('reciept/bill.html')
        print(path)
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C://Program Files//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(path)




    def editThisBooking(self):
        self.editBk = Toplevel()
        self.editBk.title("Update Booking")
        self.editBk.geometry('700x700')

        self.mainLabel = Label(self.editBk,text="Edit Booking", font=('',28,'bold'))
        self.mainLabel.pack(pady=10,padx=10)

        self.formFrameEditBk = Frame(self.editBk)
        self.formFrameEditBk.pack(padx=10, pady=10)

        self.font = ('arial',14)

        self.lb1  = Label(self.formFrameEditBk, text="Check-Out Date", font=self.font)
        self.lb2 = Label(self.formFrameEditBk, text="Check-Out Time", font=self.font)

        self.txt1 = DateEntry(self.formFrameEditBk, date_pattern='yyyy-mm-dd', width=35, font=self.font)
        self.txt2 = Entry(self.formFrameEditBk, font=self.font)

        self.lb1.grid(row=0, column=0, pady=10, padx=10)
        self.lb2.grid(row=1, column=0,padx=10,pady=10)
        self.txt1.grid(row=0, column=1, pady=10, padx=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.updatebtn = Button(self.formFrameEditBk, text='UPDATE', font=self.font, command=self.updateTheseFields)
        self.updatebtn.grid(row=2, column=1, pady=20, padx=20)

        self.editBk.mainloop()

    def updateTheseFields(self):
        checkoutDate = self.txt1.get()
        checkoutTime = self.txt2.get()

        date = datetime.datetime.strptime(f"{checkoutDate}", '%Y-%m-%d')

        rowid = self.bookingTable.selection()[0]
        item = self.bookingTable.item(rowid)
        data = item['values']
        bookingiD = data[0]

        msg.showinfo("", bookingiD)

        query = f"update booking set check_out_date='{date}', check_out_time='{checkoutTime}' where id = '{bookingiD}'"
        print(query)
        self.cr.execute(query)
        self.conn.commit()
        msg.showinfo("",f"Booking Information Updated For {bookingiD}")
        self.getValues()


    def showDataInViewTv(self, e):

        rowid = self.bookingTable.selection()[0]
        item = self.bookingTable.item(rowid)
        data = item['values']
        bookingID = data[0]

        q = f"select * from booking_detail where booking_id = '{bookingID}'"
        self.cr.execute(q)
        bookingDetailData = self.cr.fetchall()

        if len(bookingDetailData) == 0:
            msg.showinfo("",'This room is Vacant')
        else:
            for row in self.viewTv.get_children():
                self.viewTv.delete(row)

            count=0
            for i in bookingDetailData:
                self.viewTv.insert("", index=0, values=i)

    def selectSearchType(self, e):
        self.searchNamebox.grid_forget()
        font = ('arial', 14)
        searchType = self.cbSearch.get()
        if searchType == 'Customer Name':
            self.searchNamebox = Entry(self.formFrame, width=40)
            self.searchNamebox.grid(row=0, column=2, padx=10, pady=10)
        elif searchType == 'Check-In Date':
            self.searchNamebox = Entry(self.formFrame, width=40)
            self.searchNamebox.grid(row=0, column=2, padx=10, pady=10)
        elif searchType == 'Check-Out Date':
            self.searchNamebox = Entry(self.formFrame, width=40)
            self.searchNamebox.grid(row=0, column=2, padx=10, pady=10)
        elif searchType == 'Time':
            self.searchNamebox = Entry(self.formFrame, width=40)
            self.searchNamebox.grid(row=0, column=2, padx=10, pady=10)
        elif searchType == 'Persons':
            self.searchNamebox = Entry(self.formFrame, width=40)
            self.searchNamebox.grid(row=0, column=2, padx=10, pady=10)

    def deleteBooking(self):
        rowid = self.bookingTable.selection()  # getting id that sql stores
        item = self.bookingTable.item(rowid)  # using that id to fetch row data
        id = item['values'][0]
        q = f"delete from booking where id='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo("Success", f"Entry for booking '{item['values'][1]}' deleted successfully!")
        self.getValues()

    def searchBooking(self):
        print("ha")
        searchType = self.cbSearch.get()
        search = self.searchNamebox.get()

        if len(search) == 0:
            msg.showwarning("warning", 'Type Something to search')
        else:
            if searchType == 'Customer Name':
                q = f" select * from booking where customer_name like'%{search}%'"

            elif searchType == 'Check-In Date':
                q = f" select * from booking where checkin_date like'%{search}%' "

            elif searchType == 'Check-Out Date':
                q = f" select * from booking where checkout_date='{search}'"

            elif searchType == 'Time':
                q = f" select * from booking where checkin_time='{search}' or checkout_time='{search}'"

            elif searchType == 'Persons':
                q = f"select * from booking where persons='{search}'"

            print(q)
            self.cr.execute(q)
            data = self.cr.fetchall()

            if len(data) == 0:
                msg.showerror("Warning", f'No Data Found for the Search: "{search}"')

            else:

                for row in self.bookingTable.get_children():
                    self.bookingTable.delete(row)

                count = 0
                for i in data:
                    self.bookingTable.insert("", index=count, value=i)
                    count += 1

                print(data)

    def getValues(self):
        self.conn = connection.Connect()
        self.cr = self.conn.cursor()
        q = f"select * from booking"
        self.cr.execute(q)
        data = self.cr.fetchall()
        print(data)

        for row in self.bookingTable.get_children():
            self.bookingTable.delete(row)

        count = 0
        for i in data:
            self.bookingTable.insert("", index=count, value=i)
            count += 1


if __name__ == '__main__':
    obj = Main()
