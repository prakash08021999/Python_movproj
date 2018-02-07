from tkinter import *
import datetime
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
import time
conn = mysql.connector.connect(user='root', password='',  host='127.0.0.1', database='movie')
cursor = conn.cursor()
top=Tk()
f2=Frame(top)
f3=Frame(top,height=700,width=800)
f4=Frame(top)
gf=Frame(top)
f0=Frame(top ,width=600 ,height=500)
f1=Frame(top)

#-----------------------------function 1 and 0---------------------------------------------------------------------------------------s
def go_to_zero():
    f1.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    gf.pack_forget()
    f4.pack_forget()
    f0.pack(fill='both', expand='yes')
def go_to_first():
 
    f0.pack_forget()
    f1.pack(fill='both', expand='yes')
    top.geometry('600x550')


def Exit():
    top.destroy()

def first():
    f0.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    gf.pack_forget()
    f4.pack_forget()
    f1.pack(fill='both', expand='yes')
#------------------------------Login page------------------------------------------------------------------------------------------
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_1 = Label(self, text="Username",font="Times 15 bold")
        self.label_2 = Label(self, text="Password",font="Times 15 bold")

        self.entry_1 = Entry(self, width=30,bd="3px")
        self.entry_2 = Entry(self, show="*",width=30,bd="3px")
        canvas=Canvas(self,height=20,width=20)
        canvas.grid(row=14, column=0)
        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.logbtn1 = Button(self, text="Login",bd="3px",width=10,font="Times 11 bold",command = self._login_btn_clickked)
        self.logbtn1.grid(row=15, column=0)
        self.logbtn = Button(self, text="REGISTER",width=10,bd="3px",command = go_to_first,font="Times 11 bold")
        self.logbtn.grid(row=15, column=1)
        top.geometry('600x550')
        self.grid()
    def _login_btn_clickked(self):
        global username
        username = self.entry_1.get()
        password = self.entry_2.get()
        cursor.execute("select * from user")
        results = cursor.fetchall()
        a=False
        for row in results:
            y = row[2]
            z=row[3]
            if(y==username and z==password):
                f0.pack_forget()
                tkinter.messagebox.showinfo(" task_maneger  ","WELCOME")
                f3.pack(fill='both', expand='yes')
                
                a=True
        if a is False:
             tkinter.messagebox.showinfo(" task_maneger  ","Wrong username or password")


    def check1(self):
        username = self.entry_1.get()
        password = self.entry_2.get()
        if(username=='prakash'and password=='123'):
            Create()
        else:
            print("prakash")
    def admin(self):
        self.logbtn.grid_forget()
        self.logbtn4 = Button(self, text="ADMIN",bd="3px",width=10,font="Times 11 bold" ,command = self.check1)
        self.logbtn4.grid(row=15, column=0)

        
    def user(self):
        self.logbtn4.grid_forget()
        self.logbtn1 = Button(self, text="Login",bd="3px",width=10,font="Times 11 bold",command = self._login_btn_clickked)
        self.logbtn1.grid(row=15, column=0)
        self.logbtn = Button(self, text="REGISTER",width=10,bd="3px",command = go_to_first,font="Times 11 bold")
        self.logbtn.grid(row=15, column=1)
    def logout(self):
        f1.pack_forget()
        f2.pack_forget()
        f3.pack_forget()
        gf.pack_forget()
        f4.pack_forget()
        f0.pack(fill='both', expand='yes')


from tkinter import *
import tkinter.messagebox as tm
from tkinter import *
import tkinter
import mysql.connector
from tkinter import ttk
def feed():
    top=Tk()
    mess=Frame(top)
    three=StringVar()
    Text(mess,bd="3px",width=40,height=10).grid()
    mess.pack()        

label=Label(f0,width=700,height=300)
label.grid(row=0, column=0)
image_object = PhotoImage(file='log2.gif')
label.config(image=image_object)
d=LoginFrame(f0)
#Top menubar
menubar = Menu(top)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Start" ,command =first)
editmenu.add_separator()
editmenu.add_command(label="Exit",command=Exit)
menubar.add_cascade(label="START", menu=editmenu)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Admin", command=d.admin)
filemenu.add_command(label="User",command=d.user)
menubar.add_cascade(label="SINGIN", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="Licence")
helpmenu.add_separator()
helpmenu.add_command(label="About...")
menubar.add_cascade(label="HELP", menu=helpmenu)
menubar.add_cascade(label="FEEDBACK",command=feed)
h2 = Menu(menubar, tearoff=0)
h2.add_command(label="Logout",command=d.logout)
menubar.add_cascade(label="SINGOUT",menu=h2)
top.config(menu=menubar)
#end of menu
f0.pack(fill='both', expand='yes')
#----------------------------registration code ------------------------------------------------------------------------------------
def insert(): 
    use_nm=five.get()
    passw=six.get()
    phone=three.get()
    cus_id=seven.get()
    cursor.execute("select * from user")
    results = cursor.fetchall()
    try:
        for row in results:
            y = row[2]
            x= row[0]
            if(y==use_nm or x==cus_id):
                raise NameError
    except NameError:
            tkinter.messagebox.showinfo(" task_maneger  ","username alredy exist")
            return

    import re
    if(len(use_nm)!=0 and len(passw)!=0 and len(phone)!=0):
        if(re.match("^[0-9]{0,10}$",phone) and len(phone)==10):
            cursor.execute("""INSERT INTO user VALUES (%s,%s,%s,%s)""",(cus_id,phone,use_nm,passw))
            row = cursor.fetchone()
            conn.commit()
            tkinter.messagebox.showinfo(" task_maneger  ","inserted successfully")
        else:
            tkinter.messagebox.showinfo(" alert  ","Enter Coreect NUMBER:")
            return
    else:
        tkinter.messagebox.showinfo(" alert  ","FILL ALL DATA ")
        return

    cursor.execute("select * from user")
    results = cursor.fetchall()
    for row in results:
        y = row[2]
        if(y==use_nm):
            y=row[0]
            seven.set(row[0])
            break
#Registration

background_image=PhotoImage(file="singam.gif")
background_label = Label(f1, image=background_image)
background_label.place(x=0, y=0)
  
label = Label(f1,text='PERSONAL DETAIL',relief=RAISED,width=90,height=2,fg='Green',font=1,bg='black',bd=12);label.place(x=40,y=0)

label = Label(f1,text='ID',relief=RAISED,width=12,height=1,fg='blue',font=1,bg='black',bd =5);label.place(x=0,y=80)
seven=StringVar()#
E2 = Entry(f1,bd =5,textvariable=seven);E2.place(x=140,y=80)

l4=Label(f1,text="USER NAME",fg="blue",font=2,relief=RAISED,bd =5,bg='black',width=12);l4.place(x=0,y=140)
five=StringVar()#
e4=Entry(f1,textvariable=five,bd=4,fg="blue");e4.place(x=140,y=142)

l4=Label(f1,text="PASSWORD",fg="blue",bd =5,font=2,relief=RAISED,bg='black',width=12);l4.place(x=0,y=200)
six=StringVar()#
e4=Entry(f1,textvariable=six,bd=4);e4.place(x=140,y=200)

l4=Label(f1,text="Phone no:",fg="blue",font=2,relief=RAISED,bg='black',width=12,bd=5);l4.place(x=0,y=260)
three=StringVar()#
e4=Entry(f1,textvariable=three,bd=4);e4.place(x=140,y=260)

blackbutton = Button(f1, text="REGISTER", fg="Green",font=3,command=insert,bg="black",bd=5);blackbutton.place(x=230,y=320)
blackbutton = Button(f1, text="Back", fg="Green",font=3,command=go_to_zero,bg="black",bd=5);blackbutton.place(x=180,y=320)
#########################################################################################################################
#--------------------------theater--------------------------------------------------------------------

class THEATER(tkinter.Frame):
    def __init__(self, parent):
        top.geometry('700x700')
        tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.initialize_user_interface()
    def BACK(self):
        gf.pack_forget()
        f3.pack(fill='both', expand='yes')
        
    def create(self):
        global Move_id
        global usr
        self.tree.delete(*self.tree.get_children())
        cursor.execute("select ID from user where user_nm='%s'"%username)
        result=str(cursor.fetchone())
        usr=int(result[1])
        cursor.execute("select movie_id from user_mov where usr_ID=%d"%(int(result[1])))
        Move_id=str(cursor.fetchone())
        cursor.execute("select * from theater where movie_id=%d"%(int( Move_id[1])))
        results = cursor.fetchall()
        pra=list()
        for row in results:
            x = row[0]
            y=row[1]
            z=row[2]
            a=row[3]
            b=row[4]
            c=row[5]
            d=row[6]
            pra.append(d)
            valuelist = [z,b,c]
            
            self.tree.insert('', 'end',values=(valuelist), tags='cold',text=x)
        return pra
    def initialize_user_interface(self):
        self.label_2 = Label(self.parent, text="SELECT THEATER",font="Times 55 bold").place(x=20,y=20)
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")
        # Set the treeview
        self.tree = ttk.Treeview( self.parent, columns=('ID', 'MOVIES','DATE'))
        self.tree.column("#0",minwidth=0,width=50, stretch=NO)
        vsb = ttk.Scrollbar(self.parent, orient="vertical", command=self.tree.yview)
        vsb.place(x=650, y=280, height=200+20)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='THEATER')
        self.tree.heading('#2', text='DATE')
        self.tree.heading('#3', text='EX_DATE')
        self.tree.column('#0', stretch=tkinter.YES)
        self.tree.column('#1' ,stretch=tkinter.YES)
        self.tree.column('#2', stretch=tkinter.YES)
        self.tree.column('#3' ,stretch=tkinter.YES)
        self.tree.place(x=0,y=280)
        options=self.create()
        self.label_1 = Label(self.parent, text="TIME",font="Times 15 bold",relief=RAISED).place(x=80,y=520)
        selected = StringVar(value="SELECT TIME")
        op = OptionMenu(self.parent, selected, *(options))
        op.place(x=150,y=520)
        op.configure(width=20, height=1)
        cursor.execute("select movie_nm from movie where movie_id=%d"%(int( Move_id[1])))
        results = cursor.fetchone()
        self.label_2 = Label(self.parent, text="MOVIE : ",font="Times 15 bold",bd=8,relief=RAISED).place(x=0,y=238)
        lab = Label(self.parent, text=results,font="Times 15 bold",relief=RAISED,bd=8).place(x=100,y=238)
        self.logbtn1 = Button(self.parent, text="BACK",bd="3px",width=10,font="Times 11 bold",command = self.BACK)
        self.logbtn1.place(x=200,y=600)
        self.tree.bind("<Double-Button-1>", self.selectItem)
    def selectItem(self,*args):
        for item in self.tree.selection():
            item_text = self.tree.item(item,"values")
            x=item_text[0]
            print(usr)
            cursor.execute("update user_mov set thea_nm='%s' where usr_id=%d"%(x,int(usr)))
            result=cursor.fetchone()
            conn.commit()
            tkinter.messagebox.showinfo(" task_maneger  ","Theater selected..")
            gf.pack_forget()
            f4.pack(fill='both', expand='yes')
            
#-------------------------- selection+++++++++++++++++++++
import tkinter.messagebox
from tkinter import *
import tkinter as Tk
import datetime
def seat():
    no=[]
    
    po=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t1,ro,v1,w,xi,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww,xx,yy,zz,aaa,bbb,ccc,ddd,eee,fff,ggg,hhh,iii,jjj,kkk,lll,mmm,nnn,ooo,ppp,qqq,rrr,sss,ttt,uuu,vvv,www,xxx,yyy,zzz,abc,pqr)
    for kl in range(0,len(po)):
        if(kl!=22):
            mi=po[kl].get()
            if(mi==1):
                no.append(kl)
    cursor.execute("select prie_ce from movprice where movie_id=%d"%(int(mov_id)))
    result=cursor.fetchone()
    i1=int(result[0])
    rp0.set(no)
    rp.set("8:50")
    rp1.set(len(no))
    rp5.set(i1)
    rp2.set(0.5)
    rp3.set(((len(no)*i1)+0.5))

    tkinter.messagebox.showinfo(" task_maneger  ","data is inserted")
def cancel():
    tkinter.messagebox.showinfo(" task_maneger  ","ticket is cancel")
    f4.pack_forget()
    conn.rollback()
    f0.pack(fill='both', expand='yes')
def first():
    tkinter.messagebox.showinfo(" task_maneger  ","Data get inserted")
    f4.pack_forget()
    conn.commit()
    f0.pack(fill='both', expand='yes')
 
#frame4###################################################################################################
'''THIS IS FORE SCREEN SELECTION'''

background_image=PhotoImage(file="10.gif")
background_label = Label(f4, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
L4 = Label(f4,width=80,relief=RAISED )
L4.place(x=30,y=5)
L4 = Label(f4,width=80,relief=RAISED )
L4.place(x=30,y=40)
L4 = Label(f4,text='SELECT SEAT',width=80,relief=RAISED )
L4.place(x=30,y=90)
L4 = Label(f4,text='BOX',width=18,relief=RAISED )
L4.place(x=140,y=150)
##################################################################################################
#variable declare
a=IntVar();b=IntVar();c=IntVar();d=IntVar();e=IntVar();f=IntVar();g=IntVar();h=IntVar();i=IntVar();j=IntVar();k=IntVar();l=IntVar();m=IntVar();n=IntVar();p=IntVar();q=IntVar();r=IntVar();s=IntVar();o=IntVar();t1=IntVar();ro=IntVar();v1=IntVar();w=IntVar();xi=IntVar();y=IntVar();z=IntVar();aa=IntVar();bb=IntVar();cc=IntVar();dd=IntVar();ee=IntVar();ff=IntVar();gg=IntVar();hh=IntVar();ii=IntVar();jj=IntVar();kk=IntVar();ll=IntVar();mm=IntVar();nn=IntVar();oo=IntVar();pp=IntVar();qq=IntVar();rr=IntVar();ss=IntVar();tt=IntVar();uu=IntVar();vv=IntVar();ww=IntVar();xx=IntVar();yy=IntVar();zz=IntVar();
aaa=IntVar();bbb=IntVar();ccc=IntVar();ddd=IntVar();eee=IntVar();fff=IntVar();ggg=IntVar();hhh=IntVar();iii=IntVar();ooo=IntVar();jjj=IntVar();kkk=IntVar();lll=IntVar();mmm=IntVar();nnn=IntVar();ppp=IntVar();qqq=IntVar();rrr=IntVar();sss=IntVar();ttt=IntVar();uuu=IntVar();vvv=IntVar();www=IntVar();xxx=IntVar();yyy=IntVar();zzz=IntVar();abc=IntVar();pqr=IntVar()
##################################################################################################
C1 = Checkbutton(f4, variable = a,onvalue = 1);C1.place(x=30,y=185)
C2 = Checkbutton(f4, variable = b, onvalue = 1);C2.place(x=70,y=185)
C3 = Checkbutton(f4, variable = c,onvalue = 1);C3.place(x=100,y=185)
C4 = Checkbutton(f4, variable = d, onvalue = 1);C4.place(x=130,y=185)
C5 = Checkbutton(f4, variable = e,onvalue = 1);C5.place(x=170,y=185)
C6 = Checkbutton(f4, variable = f, onvalue = 1);C6.place(x=240,y=185)
C7 = Checkbutton(f4, variable = g,onvalue = 1);C7.place(x=270,y=185)
C8 = Checkbutton(f4, variable = h, onvalue = 1);C8.place(x=300,y=185)
C9 = Checkbutton(f4, variable = i,onvalue = 1);C9.place(x=330,y=185)
C10 = Checkbutton(f4, variable = j, onvalue =1);C10.place(x=370,y=185)
#####################
C11 = Checkbutton(f4, variable = k,onvalue = 1);C11.place(x=30,y=210)
C12 = Checkbutton(f4, variable = l, onvalue = 1);C12.place(x=70,y=210)
C13 = Checkbutton(f4, variable = m,onvalue = 1);C13.place(x=100,y=210)
C14 = Checkbutton(f4, variable = n, onvalue = 1);C14.place(x=130,y=210)
C15 = Checkbutton(f4, variable = o,onvalue = 1);C15.place(x=170,y=210)
C16 = Checkbutton(f4, variable = p, onvalue = 1);C16.place(x=240,y=210)
C17 = Checkbutton(f4, variable = q,onvalue = 1);C17.place(x=270,y=210)
C18 = Checkbutton(f4, variable = r, onvalue = 1);C18.place(x=300,y=210)
C19 = Checkbutton(f4, variable = s,onvalue = 1);C19.place(x=330,y=210)
C20 = Checkbutton(f4, variable = t1, onvalue = 1);C20.place(x=370,y=210)

#2########################
L4 = Label(f4,text='FIRST CLASS',width=18,relief=RAISED )
L4.place(x=140,y=238)
d1= Checkbutton(f4, variable = ro,onvalue = 1);d1.place(x=30,y=260)
d1.configure(state='disabled')
C2 = Checkbutton(f4, variable = v1, onvalue = 1);C2.place(x=70,y=260)
C3 = Checkbutton(f4, variable = w,onvalue = 1);C3.place(x=100,y=260)
C4 = Checkbutton(f4, variable = xi, onvalue = 1);C4.place(x=130,y=260)
C5 = Checkbutton(f4, variable = y,onvalue = 1);C5.place(x=170,y=260)
C6 = Checkbutton(f4, variable = z, onvalue = 1);C6.place(x=240,y=260)
C7 = Checkbutton(f4, variable = aa,onvalue = 1);C7.place(x=270,y=260)
C8 = Checkbutton(f4, variable = bb, onvalue = 1);C8.place(x=300,y=260)
C9 = Checkbutton(f4, variable =cc,onvalue = 1);C9.place(x=330,y=260)
C10 = Checkbutton(f4, variable = dd, onvalue =1);C10.place(x=370,y=260)
#####################
C11 = Checkbutton(f4, variable = ee,onvalue = 1);C11.place(x=30,y=290)
C12 = Checkbutton(f4, variable = ff, onvalue = 1);C12.place(x=70,y=290)
C13 = Checkbutton(f4, variable = gg,onvalue = 1);C13.place(x=100,y=290)
C14 = Checkbutton(f4, variable =hh, onvalue = 1);C14.place(x=130,y=290)
C15 = Checkbutton(f4, variable = ii,onvalue = 1);C15.place(x=170,y=290)
C16 = Checkbutton(f4, variable = jj, onvalue = 1);C16.place(x=240,y=290)
C17 = Checkbutton(f4, variable = kk,onvalue = 1);C17.place(x=270,y=290)
C18 = Checkbutton(f4, variable = ll, onvalue = 1);C18.place(x=300,y=290)
C19 = Checkbutton(f4, variable =mm,onvalue = 1);C19.place(x=330,y=290)
C20 = Checkbutton(f4, variable = nn, onvalue = 1);C20.place(x=370,y=290)
##FIRST CLASS######

C1 = Checkbutton(f4, variable = oo,onvalue = 1);C1.place(x=30,y=320)
C2 = Checkbutton(f4, variable = pp, onvalue = 1);C2.place(x=70,y=320)
C3 = Checkbutton(f4, variable = qq,onvalue = 1);C3.place(x=100,y=320)
C4 = Checkbutton(f4, variable = rr, onvalue = 1);C4.place(x=130,y=320)
C5 = Checkbutton(f4, variable = ss,onvalue = 1);C5.place(x=170,y=320)
C6 = Checkbutton(f4, variable =tt, onvalue = 1);C6.place(x=240,y=320)
C7 = Checkbutton(f4, variable = uu,onvalue = 1);C7.place(x=270,y=320)
C8 = Checkbutton(f4, variable = vv, onvalue = 1);C8.place(x=300,y=320)
C9 = Checkbutton(f4, variable = ww,onvalue = 1);C9.place(x=330,y=320)
C10 = Checkbutton(f4, variable = xx, onvalue =1);C10.place(x=370,y=320)
#####################
C11 = Checkbutton(f4, variable =yy,onvalue = 1);C11.place(x=30,y=350)
C12 = Checkbutton(f4, variable =zz, onvalue = 1);C12.place(x=70,y=350)
C13 = Checkbutton(f4, variable =aaa,onvalue = 1);C13.place(x=100,y=350)
C14 = Checkbutton(f4, variable = bbb, onvalue = 1);C14.place(x=130,y=350)
C15 = Checkbutton(f4, variable = ccc,onvalue = 1);C15.place(x=170,y=350)
C16 = Checkbutton(f4, variable =ddd, onvalue = 1);C16.place(x=240,y=350)
C17 = Checkbutton(f4, variable = eee,onvalue = 1);C17.place(x=270,y=350)
C18 = Checkbutton(f4, variable = fff, onvalue = 1);C18.place(x=300,y=350)
C19 = Checkbutton(f4, variable = ggg,onvalue = 1);C19.place(x=330,y=350)
C20 = Checkbutton(f4, variable =hhh, onvalue = 1);C20.place(x=370,y=350)
#################
L4 = Label(f4,text='SECOND CLASS',width=18,relief=RAISED )
L4.place(x=140,y=380)
C1 = Checkbutton(f4, variable =iii,onvalue = 1);C1.place(x=30,y=410)
C2 = Checkbutton(f4, variable = jjj, onvalue = 1);C2.place(x=70,y=410)
C3 = Checkbutton(f4, variable = kkk,onvalue = 1);C3.place(x=100,y=410)
C4 = Checkbutton(f4, variable =lll, onvalue = 1);C4.place(x=130,y=410)
C5 = Checkbutton(f4, variable = mmm,onvalue = 1);C5.place(x=170,y=410)
C6 = Checkbutton(f4, variable =nnn, onvalue = 1);C6.place(x=240,y=410)
C7 = Checkbutton(f4, variable =ooo,onvalue = 1);C7.place(x=270,y=410)
C8 = Checkbutton(f4, variable = ppp, onvalue = 1);C8.place(x=300,y=410)
C9 = Checkbutton(f4, variable =qqq,onvalue = 1);C9.place(x=330,y=410)
C10 = Checkbutton(f4, variable = rrr, onvalue =1);C10.place(x=370,y=410)
#####################
C11 = Checkbutton(f4, variable = sss,onvalue = 1);C11.place(x=30,y=440)
C12 = Checkbutton(f4, variable = ttt, onvalue = 1);C12.place(x=70,y=440)
C13 = Checkbutton(f4, variable = uuu,onvalue = 1);C13.place(x=100,y=440)
C14 = Checkbutton(f4, variable =vvv, onvalue = 1);C14.place(x=130,y=440)
C15 = Checkbutton(f4, variable = www,onvalue = 1);C15.place(x=170,y=440)
C16 = Checkbutton(f4, variable = xxx, onvalue = 1);C16.place(x=240,y=440)
C17 = Checkbutton(f4, variable =yyy,onvalue = 1);C17.place(x=270,y=440)
C18 = Checkbutton(f4, variable = zzz, onvalue = 1);C18.place(x=300,y=440)
C19 = Checkbutton(f4, variable = abc,onvalue = 1);C19.place(x=330,y=440)
C20 = Checkbutton(f4, variable = pqr, onvalue = 1);C20.place(x=370,y=440)

####################################################################

from tkinter import *
import tkinter.messagebox as tm
from tkinter import *
import tkinter
import mysql.connector
from tkinter import ttk
def Create():
    
    root=Tk()
    root.geometry("700x500")
    f2=Frame(root)
    f3=Frame(root)
    
    def menu1():

        class Admin(Frame):
         
            def __init__(self, parent):
                self.parent=parent
                self.initialize_user_interface()
            def create(self):
                global i
                i=1
                self.tree.delete(*self.tree.get_children())
                cursor.execute("select * from movie")
                results = cursor.fetchall()
                for row in results:
                    x = row[0]
                    y=row[1]
                    z=row[2]
                    valuelist = [y,z,x]
                    i=i+1
                    self.tree.insert('', 'end',values=(valuelist), tags='cold',text=x)

                

            def initialize_user_interface(self):
                global selected
                global selected2
                global selected3
                self.parent.grid_rowconfigure(0,weight=1)
                self.parent.grid_columnconfigure(0,weight=1)
                self.parent.config(background="lavender")
                self.dose_label =Label(self.parent ,text = "Movie Name")
                self.dose_entry = Entry(self.parent)
                self.dose_label.place(x=50,y=10)
                self.dose_entry.place(x=250,y=10)
                self.dose_label2 =Label(self.parent ,text = "Date",width=20)
                self.dose_label2.place(x=50,y=40)
                options = ["2018","2019","2020","2021","2022","2023","2024","2025","2026"]
                selected = StringVar(value="Year")
                op=OptionMenu(self.parent, selected, *(options))
                op.place(x=250,y=40)
                options2 = ["1","2","3","4","5","6","7","8","9","10","11","12"]
                selected2 = StringVar(value="Month")
                op2 = OptionMenu(self.parent, selected2, *(options2))
                op2.place(x=320,y=40)
                op2.config(width=5)
                options3 = ['1','2','3','4','5','6','7''8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
                selected3 = StringVar(value="Date")
                op3 = OptionMenu(self.parent, selected3, *(options3))
                op3.place(x=400,y=40)
                self.submit_button = Button(self.parent, text = "Insert", bd=4,command = self.insert_data)
                self.submit_button.place(x=250,y=100)
                self.b=Button(self.parent, fg='blue',text="Update",bd=4,command=up1).place(x=300,y=100)
               

            # Set the treeview
                self.tree = ttk.Treeview( self.parent, columns=('Movie', 'date'))
                self.tree.heading('#0', text='ID')
                self.tree.heading('#1', text='movie')
                self.tree.heading('#2', text='Date')
                self.tree.column('#1', stretch=YES)
                self.tree.column('#2', stretch=YES)
                self.tree.column('#0', stretch=YES)
                self.tree.place(x=10,y=130)
                self.treeview = self.tree
                self.create()
            # Initialize the counter
                self.i = 0
            def insert_data(self):
                self.treeview.insert('', 'end', text=""+str(i), values=(self.dose_entry.get(),str(selected.get()+"-"+selected2.get()+"-"+selected3.get())))
                a=str(selected.get()+"-"+selected2.get()+"-"+selected3.get())
                b=self.dose_entry.get()
                cursor.execute("""INSERT INTO movie VALUES (%d,'%s','%s')"""%(i,b,a))
                row= cursor.fetchone()
                conn.commit()
            def retur(self):
                a=str(selected.get()+"-"+selected2.get()+"-"+selected3.get())
                b=self.dose_entry.get()
                l=list(a,b)
                return(l)



      


        def main():
            f2.pack(fill=BOTH, expand=1)
            d=Admin(f2)
            root.mainloop()

        if __name__=="__main__":
            main()
    def menu4():
        c.delete("all")
        c.create_rectangle(200,25,700,150,fill="Red")
        label1.config(text="It is a rectangle ")

    def  det():
        top=Tk()
        dose_label =Label(top ,text = "Movie Name")
        dose_entry = Entry(top)
        dose_label.place(x=0,y=10)
        dose_entry.place(x=90,y=10)
        modified_label = Label(top, text = "ID ")
        modified_entry =Entry(top)
        modified_label.place(x=0,y=60)
        modified_entry.place(x=90,y=60)
        b3=Button(top, fg='blue',text="Delete",bd=4).place(x=30,y=90)
         

        
    def  up1(*args):
        def  up12():    
            cursor.execute("update movie set movie_nm='%s' , movie_date='%s' where movie_id=%d"%(b,a,int(modified_entry.get())))
            row= cursor.fetchone()
        dose_label =Label(root,text = "Movie Name")
        dose_entry = Entry(root)
        dose_label.place(x=50,y=10)
        dose_entry.place(x=250,y=10)
        dose_label2 =Label(root ,text = "Date",width=20)
        dose_label2.place(x=50,y=40)
        options = ["2018","2019","2020","2021","2022","2023","2024","2025","2026"]
        selected = StringVar(value="Year")
        op=OptionMenu(root, selected, *(options))
        op.place(x=250,y=40)
        options2 = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        selected2 = StringVar(value="Month")
        op2 = OptionMenu(root, selected2, *(options2))
        op2.place(x=320,y=40)
        op2.config(width=5)
        options3 = ['1','2','3','4','5','6','7''8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
        selected3 = StringVar(value="Date")
        op3 = OptionMenu(root, selected3, *(options3))
        op3.place(x=400,y=40)
        b2=Button(root ,fg='blue',text="   DATE  ",bd=4,command=up12).place(x=300,y=100)
        modified_label = Label(root, text = "ID ")
        modified_entry =Entry(root)
        modified_label.place(x=50,y=80)
        modified_entry.place(x=250,y=80)
        a=str(selected.get()+"-"+selected2.get()+"-"+selected3.get())
        b=dose_entry.get()
        
         
    def  user():

        class user_det(Frame):

            def create(self):
                a=[]

                self.tree.delete(*self.tree.get_children())
                cursor.execute("select ID from user")
                results = cursor.fetchall()
                cursor.execute("select usr_ID from user_mov")
                row = cursor.fetchall()
                k=0
                for i in results:
                    if i in row:
                        a.append(1)
                    else:
                        a.append(0)
                for i in range(len(a)):
                    w=i+1
                    cursor.execute("select user_nm from user where ID=%d"%w)
                    rp = cursor.fetchone()
                    if a[i]==1:
                        z=i+1
                        cursor.execute("select movie_id,thea_nm from user_mov where usr_ID=%d"%z)
                        results = cursor.fetchone()
                        r=results[0]
                        cursor.execute("select movie_dt from movie where movie_id=%d"%r)
                        rk = cursor.fetchone()
                        p=results[1]
                        cursor.execute("select movie_nm from movie where movie_id=%d"%(int(r)))
                        x= cursor.fetchone()
                        self.tree.insert('', 'end', text="", values=(rp,x,rk,p))
                    else:
                        
                        self.tree.insert('', 'end', text="", values=(rp,'NOT BOOK','NOT BOOK','NOT BOOK'))
                        
          
         
            def __init__(self, parent):
                self.parent=parent
                self.initialize_user_interface()

            def initialize_user_interface(self):
                
                self.parent.grid_rowconfigure(0,weight=1)
                self.parent.grid_columnconfigure(0,weight=1)
                self.parent.config(background="lavender")
                win2 = Toplevel()
                new_element_header=['1st','2nd','3rd','4th']
                treeScroll = ttk.Scrollbar(win2)
                treeScroll.pack(side=RIGHT, fill=Y)
                self.tree = ttk.Treeview(win2,columns=new_element_header, show="headings", yscrollcommand = treeScroll)
                self.tree.heading('#0', text='Item')
                self.tree.heading('#1', text='User name')
                self.tree.heading('#2', text='Movie')
                self.tree.heading('#3', text='Date')
                self.tree.heading('#4', text='Theater')
                self.create()


                self.tree.pack(side=LEFT, fill=BOTH)
               

       
            # Initialize the counter
                self.i = 0
            def insert_data(self):
                
                self.treeview.insert('', 'end', text="Item_"+str(self.i), values=(self.dose_entry.get()+" mg", self.modified_entry.get()))
                self.i = self.i + 1


      


        def main():
            root.geometry("500x500")
            
           
            f3.pack(fill=BOTH, expand=1)
            d= user_det(f3)
            root.mainloop()

        if __name__=="__main__":
            main()
        

        
    def log():
        root.destroy()


    menubar=Menu(root)
    menubar=Menu(root)
    filename1=Menu(menubar)
    filename2=Menu(menubar)
    filename1.add_command(label="INSERT",command=menu1)
    filename1.add_command(label="Delete",command=det)
    filename2.add_command(label="SHOW USER",command=user)

    menubar.add_cascade(label="MOVIE",menu=filename1)
    menubar.add_cascade(label="USER",menu=filename2)
    menubar.add_cascade(label="LOGOUT",command=log)
    root.config(menu=menubar)
    root.mainloop()
    root.mainloop()
##########################four 2#############################################3
rp0=IntVar()
L1 = Label(f4, text="SEAT SELECTED",bd =3,relief=RAISED)
L1.place(x=450,y=175)
E1 = Entry(f4, bd =5,textvariable=rp0)
E1.place(x=590,y=175)
L2= Label(f4, text="TIME",bd =3,relief=RAISED,width=9)
L2.place(x=450,y=220)
rp=StringVar()
E2 = Entry(f4,textvariable=rp,bd =5,)
E2.place(x=590,y=220)
rp1=IntVar()
L2= Label(f4, text="TOTAL TICKETS",bd =3,relief=RAISED)
L2.place(x=450,y=260)
E2 = Entry(f4, bd =5,textvariable=rp1)
E2.place(x=590,y=260)
rp5=IntVar()
L2= Label(f4, text="AMOUNT",bd =3,relief=RAISED)
L2.place(x=450,y=290)
E2 = Entry(f4, bd =5,textvariable=rp5)
E2.place(x=590,y=290)

L2= Label(f4, text="Tax",bd =3,relief=RAISED)
L2.place(x=450,y=320)
rp2=IntVar()
E2 = Entry(f4, bd =5,textvariable=rp2)
E2.place(x=590,y=320)
rp3=IntVar()
L2= Label(f4, text="TOTAL AMOUNT",bd =3,relief=RAISED)
L2.place(x=450,y=360)
E2 = Entry(f4, bd =5,textvariable=rp3)
E2.place(x=590,y=360)
w = Canvas(f4, width=400, height=4)
w.place(x=5,y=140)
w.create_rectangle(0, 0, 600, 4, outline="#fb0", fill="black")
w = Canvas(f4, width=400, height=4)
w.place(x=5,y=170)
w.create_rectangle(0, 0, 600, 4, outline="#fb0", fill="black")
w = Canvas(f4, width=4, height=400)
w.place(x=4,y=140)
w.create_rectangle(5, 600, 0, 0, outline="#fb0", fill="black")
w = Canvas(f4, width=4, height=400)
w.place(x=400,y=140)
w.create_rectangle(5, 600, 0, 0, outline="#fb0", fill="black")
w = Canvas(f4, width=400, height=4)
w.place(x=5,y=255)
w.create_rectangle(0, 0, 600, 4, outline="#fb0", fill="black")
w = Canvas(f4, width=399, height=4)
w.place(x=5,y=399)
w.create_rectangle(0, 0, 600, 4, outline="#fb0", fill="black")
B = Button(f4,text='RESEAT',width=20,command=first)
B.place(x=530,y=400)
w = Canvas(f4, width=400, height=4)
w.place(x=5,y=540)
w.create_rectangle(0, 0, 600, 4, outline="#fb0", fill="black")
L2= Label(f4, text="SCREEN",bd =3,relief=RAISED,width=55)
L2.place(x=8,y=515)
B = Button(f4,text='CANCEL BOOKING',width=20, command=cancel)
B.place(x=40,y=560)
B = Button(f4,text='PROCEED BOOKING',width=20,command=seat)
B.place(x=180,y=560)

#----------------------------------------------------------------

class Frame1(tkinter.Frame):
    def __init__(self, parent):
        top.geometry('700x700')
        tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.initialize_user_interface()
    def create(self):
        self.tree.delete(*self.tree.get_children())
        cursor.execute("select * from movie")
        results = cursor.fetchall()
        for row in results:
            x = row[0]
            y=row[1]
            z=row[2]
            valuelist = [y,z,x]
            self.tree.insert('', 'end',values=(valuelist), tags='cold',text=x)
        return
    def initialize_user_interface(self):      
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")
        # Set the treeview
        self.tree = ttk.Treeview( self.parent, columns=('ID', 'MOVIES'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='MOVIES')
        self.tree.heading('#2', text='Date')
        self.tree.column('#1', stretch=tkinter.YES)
        self.tree.column('#2' ,stretch=tkinter.YES)
        self.tree.column('#0', stretch=tkinter.YES)
        self.tree.place(x=60,y=370)
        self.tree.bind("<Double-Button-1>", self.selectItem)
        self.entry=Entry(self.parent)
        self.entry.place(x=180,y=330)
        blackbutton = Button(self.parent, text="SEARCH", fg="black",command=self.search)
        blackbutton.place(x=350,y=330)
        blackbutton = Button(self.parent, text="ALL", fg="black",command=self.create)
        blackbutton.place(x=450,y=330)
        self.create()   
        self.car = StringVar()
        label = Label(self.parent,width=700,height=300)
        label.place(x=60,y=10)
        delay = 0.5
        image_files = [
        'singam.gif'
        ,'ra.gif'
        ,'ka.gif'
        ,'kab.gif'
        ]
        try:
            while 1:
                for image in image_files:
                    image_object = PhotoImage(file=image)
                    label.config(image=image_object)
                    self.parent.update()
                    time.sleep(delay)
        except:
            pass;
            

    def selectItem(self,*args):
        global x
        global rst
        global mov_id
        for item in self.tree.selection():
            item_text = self.tree.item(item,"values")
            x=item_text[0]
            rst=item_text[1]
            cursor.execute("select movie_id from movie where movie_nm='%s'"%x)#move id
            result=str(cursor.fetchone())
            mov_id=int(result[1])
            cursor.execute("select ID from user where user_nm='%s'"%username)
            result=str(cursor.fetchone())
            usr=int(result[1])
            
            cursor.execute("select * from user_mov")
            row = cursor.fetchall()
            a=False
            for k in row:
                if(k[0]==usr):
                   a=True
            if(a):
                cursor.execute("update user_mov set movie_id=%d where usr_ID=%d"%(mov_id,usr))
                conn.commit()
            else:
                cursor.execute("""INSERT INTO user_mov VALUES (%d,%d,'%s')"""%(usr,mov_id,'null'))
                result = cursor.fetchone()
                conn.commit()
            #cursor.execute("update user_mov set ")
            tkinter.messagebox.showinfo(" task_maneger  ","Movie Detail Inserted")
            f3.pack_forget()
            THEATER(gf)
            gf.pack(fill='both', expand='yes')
            
        
    def search(self):
        self.tree.delete(*self.tree.get_children())
        mk1 = self.entry.get()
        cursor.execute("select * from movie")
        results = cursor.fetchall()
        for row in results:
            x = row[0]
            y=row[1]
            z=row[2]
            if( str.lower(y)== str.lower(mk1)):   
                valuelist =[y,z]
                self.tree.insert('', 'end', text=x, values=(valuelist))
        

def main():
    Frame1(f3)
  
if __name__=="__main__":
    main()



