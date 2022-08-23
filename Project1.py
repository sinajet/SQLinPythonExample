from tkinter import *
from tkinter.scrolledtext import ScrolledText
import mysql.connector
#============================================================Creat and connect to database
mydb=mysql.connector.connect(host='localhost',user='root',password='')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists library")
mycursor.close()
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='library')
mycursor=mydb.cursor()   
mycursor.execute("create table if not exists books(ISBN BIGINT(13) PRIMARY KEY,Title VARCHAR(30),Author VARCHAR(30),Year INT(4))")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Classes
def tClear():
    textTitle.set('')
    textAuthor.set('')
    textYear.set('')
    textISBN.set('')
    stShow.delete('1.0', END)
class db():
    def __init__(self):
        self.Title=textTitle.get()
        self.Author=textAuthor.get()
        self.Year=textYear.get()
        self.ISBN=textISBN.get()
    def dbAdd(self):
        if self.ISBN!='':
            sql="insert into books (ISBN,Title,Author,Year) Values (%s,%s,%s,%s)"
            val=(self.ISBN,self.Title,self.Author,self.Year)
            mycursor.execute(sql,val)
            mydb.commit()
            tClear()
            stShow.insert(INSERT,mycursor.rowcount)
            stShow.insert(INSERT," record inserted")
        else:
            tClear()
            stShow.insert(INSERT,"ISBN is EMPTY")
    
    def dbViewall():
        tClear()
        mycursor.execute("select * from books")
        myx=mycursor.fetchall()
        stShow.insert(INSERT," ISBN |     Title      |      Author      | Year\n============================================================\n")
        for j in myx:
            stShow.insert(INSERT,j)
            stShow.insert(INSERT,"\n____________________________________________________________\n")

    def dbDelete(self):
        if self.ISBN!='':
            sql="""delete from books where ISBN = %s"""
            mycursor.execute(sql,(self.ISBN,))
            mydb.commit()
            tClear()
            stShow.insert(INSERT,"\nRecord DELETED!!!!!!\n")
        else:
            tClear()
            stShow.insert(INSERT,"ISBN is EMPTY, You can delelet a record only with ISBN")
    
    def dbUpdate(self):
        if self.ISBN!='':
            sql="update books set Title = %s , Author = %s , Year = %s  where ISBN = %s"
            val=(self.Title,self.Author,self.Year,self.ISBN)
            mycursor.execute(sql,val)
            mydb.commit()
            tClear()
            stShow.insert(INSERT,"record Updated")
        else:
            tClear()
            stShow.insert(INSERT,"ISBN is EMPTY,You can Update a Record Only with ISBN")

    def dbSearch(self):
        if self.ISBN!='' and self.Title=='' and self.Author=='' and self.Year=='':
            tClear()
            sql=f"select * from books where ISBN = '{self.ISBN}'"
            mycursor.execute(sql)
            myx=mycursor.fetchall()
            stShow.insert(INSERT," ISBN |     Title      |      Author      | Year\n============================================================\n")
            for j in myx:
                stShow.insert(INSERT,j)
                stShow.insert(INSERT,"\n____________________________________________________________\n")
        elif self.Title!='' and self.ISBN=='' and self.Author=='' and self.Year=='':
            tClear()
            sql=f"select * from books where Title = '{self.Title}'"
            mycursor.execute(sql)
            myx=mycursor.fetchall()
            stShow.insert(INSERT," ISBN |     Title      |      Author      | Year\n============================================================\n")
            for j in myx:
                stShow.insert(INSERT,j)
                stShow.insert(INSERT,"\n____________________________________________________________\n")
        elif self.Year!='' and self.Title=='' and self.ISBN=='' and self.Author=='':
            tClear()
            sql=f"select * from books where Year = '{self.Year}'"
            mycursor.execute(sql)
            myx=mycursor.fetchall()
            stShow.insert(INSERT," ISBN |     Title      |      Author      | Year\n============================================================\n")
            for j in myx:
                stShow.insert(INSERT,j)
                stShow.insert(INSERT,"\n____________________________________________________________\n")
        elif self.Author!='' and self.Year=='' and self.Title=='' and self.ISBN=='':
            tClear()
            sql=f"select * from books where Author = '{self.Author}'"
            mycursor.execute(sql)
            myx=mycursor.fetchall()
            stShow.insert(INSERT," ISBN |     Title      |      Author      | Year\n============================================================\n")
            for j in myx:
                stShow.insert(INSERT,j)
                stShow.insert(INSERT,"\n____________________________________________________________\n")
        elif self.Author!='' and self.Year!='' and self.Title=='' and self.ISBN=='':
            tClear()
            sql=f"select * from books where Author = '{self.Author}' and Year = '{self.Year}' "
            mycursor.execute(sql)
            myx=mycursor.fetchall()
            stShow.insert(INSERT," ISBN |     Title      |      Author      | Year\n============================================================\n")
            for j in myx:
                stShow.insert(INSERT,j)
                stShow.insert(INSERT,"\n____________________________________________________________\n")
        else:
            tClear()
            stShow.insert(INSERT,"Fields are EMPTY Or The values were entered incorrectly\nYou can Search by Enter 1 Value in Fields or only Search by Author and Year!!!")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ControlDefs
def Cadd():
    o=db()
    o.dbAdd()
def Cdelete():
    o=db()
    o.dbDelete()
def Csearch():
    o=db()
    o.dbSearch()
def Cupdate():
    o=db()
    o.dbUpdate()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == "__main__":    
    lib=Tk()
    Sw=int(lib.winfo_screenwidth()/2)
    Sw=Sw-300
    Sh=int(lib.winfo_screenheight()/2)
    Sh=Sh-300
    w=f"+{Sw}+{Sh}"
    lib.geometry(w)
    lib.resizable(False,False)
    lib.title("library")
#UI============================================================UI
textTitle=StringVar()
textAuthor=StringVar()
textYear=StringVar()
textISBN=StringVar()
#============================================================Lable
lblTitle=Label(lib,text="Title:").grid(row=0,column=0)
lblAuthor=Label(lib,text="Author:").grid(row=1,column=0)
lblYear=Label(lib,text="Year:").grid(row=2,column=0)
lblIsbn=Label(lib,text="ISBN:").grid(row=3,column=0)
#============================================================Entries
txtTitle=Entry(lib,width=30,textvariable=textTitle).place(x=40,y=1)
txtAuthor=Entry(lib,width=29,textvariable=textAuthor).place(x=45,y=22)
txtYear=Entry(lib,width=30,textvariable=textYear).place(x=40,y=43)
txtIsbn=Entry(lib,width=30,textvariable=textISBN).place(x=40,y=64)
stShow=ScrolledText(lib,width=60)
stShow.grid(row=4,column=1)
#============================================================Buttons
btnViewall=Button(lib,text=" View All ",command=lambda:db.dbViewall()).place(x=240,y=1)
btnSearch=Button(lib,text=" Search ",command=lambda:Csearch()).place(x=300,y=1)
btnAdd=Button(lib,text="Add",command=lambda:Cadd()).place(x=355,y=1)
btnUpdate=Button(lib,text=" Update ",command=lambda:Cupdate()).place(x=240,y=30)
btnDelete=Button(lib,text="Delete",command=lambda:Cdelete()).place(x=300,y=30)
btnClear=Button(lib,text="Clear",command=lambda:tClear()).place(x=350,y=30)
#============================================================
lib.mainloop()