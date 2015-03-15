from tkinter import *
import sys
out=[]
root = Tk()
frame = Frame(root)
txt=open('myfile.txt','a+')

def save():
    form = Toplevel(root)
    Label(form, text='Name: ').grid(column=0, row=0, sticky=E)
    Label(form, text='Department: ').grid(column=0, row=1, sticky=E)
    Label(form, text='Room No: ').grid(column=0,row=2,sticky=E)
    Label(form, text='Year: ').grid(column=0,row=3,sticky=E)
    Label(form, text='Nick: ').grid(column=0,row=4,sticky=E)
    Label(form, text='Phone Number: ').grid(column=0,row=5,sticky=E)
    Label(form, text='Address: ').grid(column=0,row=6,sticky=E)
    Label(form, text='Email ID: ').grid(column=0,row=7,sticky=E)
    Label(form, text='Facebook Link: ').grid(column=0,row=8,sticky=E)

    name = StringVar()
    dept = StringVar()
    room= StringVar()
    year=StringVar()
    nick=StringVar()
    phn=StringVar()
    add=StringVar()
    email=StringVar()
    fb=StringVar()
    a=Entry(form, textvariable=name, width=15)
    a.grid(column=1, row=0, sticky=W)
    depl=['CSE','IT','ME','EE','ECE']
    dept.set("Select Department")
    dep=OptionMenu(form,dept,*depl)
    dep.grid(column=1, row=1, sticky=W)
    rooml=['101','102','103','104','105','106','201','202','203','204','205','207','208','209','210','211','212','214','301','302','303','304','305','306','307','308','309','310','311','312']
    room.set("Select Room")
    roo=OptionMenu(form,room,*rooml)
    roo.grid(column=1, row=2, sticky=W)
    yrl=['2nd','3rd','4th','M.Tech 1st','M.Tech 2nd']
    year.set("Select Year")
    yr=OptionMenu(form,year,*yrl)
    yr.grid(column=1, row=3, sticky=W)
    
    Entry(form, textvariable=nick, width=15).grid(column=1, row=4, sticky=W)
    Entry(form, textvariable=phn, width=15).grid(column=1, row=5, sticky=W)
    Entry(form, textvariable=add, width=15).grid(column=1, row=6, sticky=W)
    Entry(form, textvariable=email, width=15).grid(column=1, row=7, sticky=W)
    Entry(form, textvariable=fb, width=15).grid(column=1, row=8, sticky=W)

    def onCancel():
        form.destroy()

    def onOk():
        txt.write('Name : ' + str(name.get()) + ' , ' + 'Deprtment : ' + str(dept.get()) + ' , ' + 'Room No : ' + str(room.get()) + ' , ' + 'Year: ' + str(year.get())+ ' , ' + 'Nick: ' + str(nick.get()) + ' , ' + 'Contact No: ' + str(phn.get()) + ' , ' + 'Address: ' + str(add.get()) + ' , ' + 'Email ID: ' + str(email.get()) + ' , ' + 'Facebook Link: ' + str(fb.get()))
        txt.write('\n')
    def onadd():
        onOk()
        onCancel()
        save()
    def onclose():
        onOk()
        onCancel()
        txt.close()


    Button(form, text='OK', command=onclose).grid(column=0, row=9, sticky=E)
    Button(form, text='ADD', command=onadd).grid(column=1, row=9, sticky=S)
    Button(form, text='Cancel', command=onCancel).grid(column=2, row=9, sticky=W)
def show():
    with open('myfile.txt','r') as f:
        print (f.read())
def close():
    print('your saved data is: ')
    show()
    root.destroy()
def delfile():
    fobj=open('myfile.txt','w')
    fobj.close()
    show()

v = Label(root,text='RBC DataBase').grid(column=0,row=0,sticky=S)
w = Button(root, text='UPDATE',command=save).grid(column=0,row=1,sticky=S)
x = Button(root, text='SHOW',command=show).grid(column=0,row=2,sticky=S)
m = Button(root, text='EXIT',command=close).grid(column=0,row=3,sticky=S)
u = Button(root, text='DELETE',command=delfile).grid(column=0,row=4,sticky=S)

root.title('form')
root.mainloop()
