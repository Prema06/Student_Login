import tkinter
import mysql.connector

con=mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = 'Bharathy@2'
)
cur = con.cursor(buffered=True)

try:
    cur.execute("use studentregistration")
except:
    cur.execute("create database studentregistration")
    cur.execute("use studentregistration")

try:
    cur.execute("describe persons")
except:
    cur.execute("create table persons( id int primary key auto_increment,e_id varchar(20), name varchar(20), age int, email varchar(20), mobile varchar(10)")
def Registration():
    cur.execute(f"insert into persons( e_id, name, age, email, mobile) values('{e1.get()}','{e2.get()}', '{e3.get()}', '{e4.get()}','{e5.get()}')")
    con.commit()

def Registration():
    pass

win=tkinter.Tk()
win.geometry('500x500')
win.title('Student Management System')
l1=tkinter.Label(win,text='Person Details')
l2=tkinter.Label(win,text='e_id')
l3=tkinter.Label(win,text='Name')
l4=tkinter.Label(win,text='Age')
l5=tkinter.Label(win,text='Email')
l6=tkinter.Label(win,text='Mobile')
l1.grid(row=1, column=1)
l2.grid(row=2, column=1)
l3.grid(row=3, column=1)
l4.grid(row=4, column=1)
l5.grid(row=5, column=1)
l6.grid(row=6, column=1)
e1=tkinter.Entry(win)
e2=tkinter.Entry(win)
e3=tkinter.Entry(win)
e4=tkinter.Entry(win)
e5=tkinter.Entry(win)
e1.grid(row=2,column=2)
e2.grid(row=3,column=2)
e3.grid(row=4,column=2)
e4.grid(row=5,column=2)
e5.grid(row=6,column=2)
b=tkinter.Button(win, text='Submit Here', command=Registration)
b.grid(row=7,column=1)

win.mainloop()