from tkinter import*
import tkinter.messagebox as messagebox
import mysql.connector as mysql

def insert():
    name=e1.get()
    phone=e2.get()
    email=e3.get()
    if name=='' or phone=='' or email=='':
        messagebox.showinfo("Insert Status","Please fill all the fields")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='pythonn')
        cursor=conn.cursor()
        cursor.execute("insert into hello values('%s','%s','%s')"%(name,phone,email))
        conn.commit()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        messagebox.showinfo("Insert Status","Inserted Successfully")
        cursor.close()
        conn.close()

def show():
    name=e1.get()
    if name=='':
         messagebox.showinfo("Deatails","Please enter your details")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='pythonn')
        cursor=conn.cursor()
        cursor.execute("select * from hello where name='%s'"%name)
        rows=cursor.fetchall()
        for row in rows:
            e2.insert(0,row[1])
            e3.insert(0,row[2])
        cursor.close()
        conn.commit()

def delete():
    name=e1.get()
    if name=='':
         messagebox.showinfo("Deatails","Deatails deleted")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='pythonn')
        cursor=conn.cursor()
        cursor.execute("delete from hello where name='%s'"%name)
        conn.commit()
        e1.delete(0,END)
        messagebox.showinfo("Delet Status","Deleted Successfully")
        cursor.close()
def update():
    name=e1.get()
    phone=e2.get()
    email=e3.get()
    if  name=='' or phone=='' or email=='':
        messagebox.showinfo("update","updated")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='pythonn')
        cursor=conn.cursor()
        cursor.execute("update hello set email='%s',phone='%s' where name='%s'"%(email,phone,name))
        conn.commit()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        messagebox.showinfo("update Status","updated Successfully")
        cursor.close()
        conn.close()
def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        messagebox.showinfo("Clear Status","Cleared Successfully")
loop=Tk()

loop.title("Application")
loop.geometry("300x300")

lbl=Label(loop,text="name")
lbl.place(x=0,y=10)

lbl=Label(loop,text="phone")
lbl.place(x=0,y=40)

lbl=Label(loop,text="email")
lbl.place(x=0,y=70)
e1=Entry(loop)
e1.place(x=40,y=10)



e2=Entry(loop)
e2.place(x=40,y=40)

e3=Entry(loop)
e3.place(x=40,y=70)

a=Button(loop,text="Insert",command=insert)
a.place(x=10,y=100)

b=Button(loop,text="Show",command=show)
b.place(x=60,y=100)

c=Button(loop,text="Delete",command=delete)
c.place(x=110,y=100)

d=Button(loop,text="Update",command=update)
d.place(x=160,y=100)

e=Button(loop,text="Clear",command=clear)
e.place(x=220,y=100)
loop.mainloop()