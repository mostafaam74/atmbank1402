from tkinter import*
from tkinter import messagebox
import sqlite3
import user
import random
def connector(baghi,idcard): #agar shod akhar kar ketabkhane shavad
    con=sqlite3.connect('data_card.db')
    cur=con.cursor()
    cur.execute('update user set mojodi={} where sh_kart={}'.format(baghi,idcard))
    con.commit()
    con.close()
#_________________________________________________________________________________________________:
def connector2(password1,idcard2): #agar shod akhar kar ketabkhane shavad
    con=sqlite3.connect('data_card.db')
    cur=con.cursor()
    cur.execute('update user set pass1={} where sh_kart={}'.format(password1,idcard2))
    con.commit()
    con.close()
#_________________________________________________________________________________________________:
def connector3(password2,idcard3): #agar shod akhar kar ketabkhane shavad
    con=sqlite3.connect('data_card.db')
    cur=con.cursor()
    cur.execute('update user set pass2={} where sh_kart={}'.format(password2,idcard3))
    con.commit()
    con.close()
#_________________________________________________________________________________________________:

def mande_hesab(): #namayeshe mande hesab
    pass_list=[]
    pass_list=password_entry.get()
    if password_entry.get()==pass6840:
        user1=[]
        user1=user.karbaran.user6840()
        x=user1[4] 
    elif password_entry.get()==pass1278:
        user2=[]
        user2=user.karbaran.user1278()
        x=user2[4] 
    elif password_entry.get()==pass1354:
        user3=[]
        user3=user.karbaran.user1354()
        x=user3[4]    
    top3=Toplevel()
    top3.geometry('1530x785+0+0')
    top3.config(bg='#aaa398')
    show_mandeh_hesab=Label(top3,text='مانده حساب به ریال :{}'.format(x),font=('Nazanin',40,'bold')).pack()
         
#_________________________________________________________________________________________________:           
def daryaft_vajh(): #daryaft pool az atm
    global top4
    top4=Toplevel()
    top4.geometry('1530x785+0+0')
    top4.config(bg='#aa55cc')
    label4=Label(top4,text='لطفا مبلغ را وارد کنید',font=('Nazanin',40,'bold'))
    label4.place(x=580,y=350)
    global cash_entry
    cash_entry=Entry(top4,font=50)
    cash_entry.place(x=655,y=480)
    cash_But=Button(top4,text='تایید',font=('Nazanin',25,'bold'),command=bardasht_pool).place(x=725,y=510)
def bardasht_pool(): #tahvile poll khaste shodeh va namayeshe mande
    pass_list=[]
    pass_list=password_entry.get()
    if password_entry.get()==pass6840:
        meghdar_vorodi= int(cash_entry.get())
        user1=[]
        user1=user.karbaran.user6840()
        mojodi=user1[4] 
        if mojodi>=meghdar_vorodi:
            mande_jadid=mojodi-meghdar_vorodi
            sh_kart='6037997391690337'
            connector(mande_jadid,sh_kart)
            mande_new=Label(top4,text='پول خود را بردارید...مانده قابل برداشت به ریال :{}'.format(mande_jadid),font=('Nazanin',40,'bold')).pack(side=BOTTOM)        
        else:
            not_cash=Label(top4,text='موجودی حساب شما کافی نمیباشد!!!',font=('Nazanin',40,'bold')).place(x=725,y=710)
                          
    elif password_entry.get()==pass1278:
        meghdar_vorodi= int(cash_entry.get())
        user2=[]
        user2=user.karbaran.user1278()
        mojodi=user2[4] 
        if mojodi>=meghdar_vorodi:
            mande_jadid=mojodi-meghdar_vorodi
            sh_kart='6219861925027848'
            connector(mande_jadid,sh_kart)
            mande_new=Label(top4,text='پول خود را بردارید...مانده قابل برداشت به ریال :{}'.format(mande_jadid),font=('Nazanin',40,'bold')).pack(side=BOTTOM)        
        else:
            not_cash=Label(top4,text='موجودی حساب شما کافی نمیباشد!!!',font=('Nazanin',40,'bold')).place(x=725,y=710)
                          
    elif password_entry.get()==pass1354:
        meghdar_vorodi= int(cash_entry.get())
        user3=[]
        user3=user.karbaran.user1354()
        mojodi=user3[4] 
        if mojodi>=meghdar_vorodi:
            mande_jadid=mojodi-meghdar_vorodi
            sh_kart='6037697689563531'
            connector(mande_jadid,sh_kart)
            mande_new=Label(top4,text='پول خود را بردارید...مانده قابل برداشت به ریال :{}'.format(mande_jadid),font=('Nazanin',40,'bold')).pack(side=BOTTOM)        
        else:
            not_cash=Label(top4,text='موجودی حساب شما کافی نمیباشد!!!',font=('Nazanin',40,'bold')).place(x=725,y=710)
#_________________________________________________________________________________________________: 
 
def amaliyate_ramz():
    top5=Toplevel()
    top5.geometry('1530x785+0+0')
    top5.config(bg='#aa55cc')
    change_pass1=Button(top5,text='تغییر رمز اول',font=('Nazanin',30,'bold'),command=changepass1).place(x=0,y=100)
    change_pass2=Button(top5,text='تغییر رمز دوم',font=('Nazanin',30,'bold'),command= changepass2).place(x=1350,y=110)

def changepass1():
    global top6
    top6=Toplevel()
    top6.geometry('1530x785+0+0')
    top6.config(bg='#aa55cc')
    global new_pass1entry
    new_pass1entry=Entry(top6,font=50)
    new_pass1entry.place(x=655,y=480)
    confirm_change=Button(top6,text='تایید',font=('Nazanin',25,'bold'),command=confirm_change1).place(x=725,y=510)
    label=Label (top6,text='رمز اول جدید را وارد کنید',font=('Nazanin',40,'bold')).pack(side=TOP)
def confirm_change1():
    pass_list=[]
    pass_list=password_entry.get()
    if password_entry.get()==pass6840:
        z=int(new_pass1entry.get())
        sh_kart='6037997391690337'
        connector2(z,sh_kart)
        label=Label (top6,text='رمز اول شما با موفقیت تغییر کرد ',font=('Nazanin',40,'bold')).pack(side=BOTTOM)
    if password_entry.get()==pass1278:
        z=int(new_pass1entry.get())
        sh_kart='6219861925027848'
        connector2(z,sh_kart)
        label=Label (top6,text='رمز اول شما با موفقیت تغییر کرد ',font=('Nazanin',40,'bold')).pack(side=BOTTOM)
    if password_entry.get()==pass1354:
        z=int(new_pass1entry.get())
        sh_kart='6037697689563531'
        connector2(z,sh_kart)
        label=Label (top6,text='رمز اول شما با موفقیت تغییر کرد ',font=('Nazanin',40,'bold')).pack(side=BOTTOM)
          
        
        
def changepass2():
    global top7
    top7=Toplevel()
    top7.geometry('1530x785+0+0')
    top7.config(bg='#aa55cc')
    global new_pass2entry
    new_pass2entry=Entry(top7,font=50)
    new_pass2entry.place(x=655,y=480)
    confirm_change=Button(top7,text='تایید',font=('Nazanin',25,'bold'),command=confirm_change2).place(x=725,y=510)
    label=Label (top7,text='رمز دوم جدید را وارد کنید',font=('Nazanin',40,'bold')).pack(side=TOP)

def confirm_change2():
    pass_list=[]
    pass_list=password_entry.get()
    if password_entry.get()==pass6840:
        z=int(new_pass2entry.get())
        sh_kart='6037997391690337'
        connector3(z,sh_kart)
        label=Label (top7,text='رمز دوم شما با موفقیت تغییر کرد ',font=('Nazanin',40,'bold')).pack(side=BOTTOM)
    if password_entry.get()==pass1278:
        z=int(new_pass2entry.get())
        sh_kart='6219861925027848'
        connector3(z,sh_kart)
        label=Label (top7,text='رمز دوم شما با موفقیت تغییر کرد ',font=('Nazanin',40,'bold')).pack(side=BOTTOM)
    if password_entry.get()==pass1354:
        z=int(new_pass2entry.get())
        sh_kart='6037697689563531'
        connector3(z,sh_kart)
        label=Label (top7,text='رمز دوم شما با موفقیت تغییر کرد ',font=('Nazanin',40,'bold')).pack(side=BOTTOM)
#___________________________________________________________________________________________________________________:
def shaarzh():
    top8=Toplevel()
    top8.geometry('1530x785+0+0')
    top8.config(bg='#aa55cc')
    H_avval=Button(top8,text='همراه اول',font=('Nazanin',30,'bold'),command=gheymatsharzh).place(x=1350,y=110)
    I_cell=Button(top8,text='ایرانسل',font=('Nazanin',30,'bold'),command=gheymatsharzh).place(x=1365,y=410)
    R_tell=Button(top8,text='رایتل',font=('Nazanin',30,'bold'),command=gheymatsharzh).place(x=1365,y=260)
#***************************************************************************************************************
def gheymatsharzh():
    top9=Toplevel()
    top9.geometry('1530x785+0+0')
    top9.config(bg='#aa55cc')
    panjtomani=Button(top9,text='پنج هزار تومانی',font=('Nazanin',30,'bold'),command=sh_5toman).place(x=1350,y=110)
    dahtomani=Button(top9,text='ده هزار تومانی',font=('Nazanin',30,'bold'),command=sh_10toman).place(x=1365,y=410)
    bistomani=Button(top9,text='بیست هزار تومانی',font=('Nazanin',30,'bold'),command=sh_20toman).place(x=1365,y=260)
#************************************************************************************************************************
  
def sh_5toman():
    top10=Toplevel()
    top10.geometry('1530x785+0+0')
    top10.config(bg='#aa55cc')

    if password_entry.get()==pass6840:
        meghdar_vorodi=50000
        user1=[]
        user1=user.karbaran.user6840()
        mojodi=user1[4] 
        if mojodi>=meghdar_vorodi:
            mande_jadid=mojodi-meghdar_vorodi
            sh_kart='6037997391690337'
            connector(mande_jadid,sh_kart)
            mostaghim_sh=Button(top10,text='شارژ مستقیم',font=('Nazanin',30,'bold'),command=mostaghim).place(x=1350,y=110)
            ramz_sh=Button(top10,text='رمز شارژ',font=('Nazanin',30,'bold'),command=ramzget).place(x=1365,y=410)
        else:
            not_cash=Label(top4,text='موجودی حساب شما کافی نمیباشد!!!',font=('Nazanin',40,'bold')).place(x=725,y=710)
    elif password_entry.get()==pass1278:
        meghdar_vorodi=50000
        user2=[]
        user2=user.karbaran.user1278()
        mojodi=user2[4] 
        if mojodi>=meghdar_vorodi:
            mande_jadid=mojodi-meghdar_vorodi
            sh_kart='6219861925027848'
            connector(mande_jadid,sh_kart)
            mostaghim_sh=Button(top10,text='شارژ مستقیم',font=('Nazanin',30,'bold'),command=mostaghim).place(x=1350,y=110)
            ramz_sh=Button(top10,text='رمز شارژ',font=('Nazanin',30,'bold'),command=ramzget).place(x=1365,y=410)
                   
        else:
            not_cash=Label(top4,text='موجودی حساب شما کافی نمیباشد!!!',font=('Nazanin',40,'bold')).place(x=725,y=710)
    elif password_entry.get()==pass1354:
        meghdar_vorodi=50000
        user3=[]
        user3=user.karbaran.user1354()
        mojodi=user3[4] 
        if mojodi>=meghdar_vorodi:
            mande_jadid=mojodi-meghdar_vorodi
            sh_kart='6037697689563531'
            connector(mande_jadid,sh_kart)
            mostaghim_sh=Button(top10,text='شارژ مستقیم',font=('Nazanin',30,'bold'),command=mostaghim).place(x=1350,y=110)
            ramz_sh=Button(top10,text='رمز شارژ',font=('Nazanin',30,'bold'),command=ramzget).place(x=1365,y=410)
                   
        else:
            not_cash=Label(top4,text='موجودی حساب شما کافی نمیباشد!!!',font=('Nazanin',40,'bold')).place(x=725,y=710)
#*****************************************************************************************************************************
def sh_10toman():
    top11=Toplevel()
    top11.geometry('1530x785+0+0')
    top11.config(bg='#aa55cc')
    
    if password_entry.get()==pass6840:
        meghdar_vorodi=100000
        user1=[]
        user1=user.karbaran.user6840()
        mojodi=user1[4] 
        if mojodi>=meghdar_vorodi:
            mande_jadid=mojodi-meghdar_vorodi
            sh_kart='6037997391690337'
            connector(mande_jadid,sh_kart)
            mostaghim_sh=Button(top11,text='شارژ مستقیم',font=('Nazanin',30,'bold'),command=mostaghim).place(x=1350,y=110)
            ramz_sh=Button(top11,text='رمز شارژ',font=('Nazanin',30,'bold'),command=ramzget).place(x=1365,y=410)
        else:
            not_cash=Label(top4,text='موجودی حساب شما کافی نمیباشد!!!',font=('Nazanin',40,'bold')).place(x=725,y=710)

    elif password_entry.get()==pass1278:
        meghdar_vorodi=100000
        user2=[]
        user2=user.karbaran.user1278()
        mojodi=user2[4] 
        if mojodi>=meghdar_vorodi:
            mande_jadid=mojodi-meghdar_vorodi
            sh_kart='6219861925027848'
            connector(mande_jadid,sh_kart)
            mostaghim_sh=Button(top11,text='شارژ مستقیم',font=('Nazanin',30,'bold'),command=mostaghim).place(x=1350,y=110)
            ramz_sh=Button(top11,text='رمز شارژ',font=('Nazanin',30,'bold'),command=ramzget).place(x=1365,y=410)
                   
        else:
            not_cash=Label(top4,text='موجودی حساب شما کافی نمیباشد!!!',font=('Nazanin',40,'bold')).place(x=725,y=710)
    elif password_entry.get()==pass1354:
        meghdar_vorodi=100000
        user3=[]
        user3=user.karbaran.user1354()
        mojodi=user3[4] 
        if mojodi>=meghdar_vorodi:
            mande_jadid=mojodi-meghdar_vorodi
            sh_kart='6037697689563531'
            connector(mande_jadid,sh_kart)
            mostaghim_sh=Button(top11,text='شارژ مستقیم',font=('Nazanin',30,'bold'),command=mostaghim).place(x=1350,y=110)
            ramz_sh=Button(top11,text='رمز شارژ',font=('Nazanin',30,'bold'),command=ramzget).place(x=1365,y=410)
                    
        else:
            not_cash=Label(top4,text='موجودی حساب شما کافی نمیباشد!!!',font=('Nazanin',40,'bold')).place(x=725,y=710)
#**********************************************************************************************************************************
def sh_20toman():
    top12=Toplevel()
    top12.geometry('1530x785+0+0')
    top12.config(bg='#aa55cc')
    
    if password_entry.get()==pass6840:
        meghdar_vorodi=200000
        user1=[]
        user1=user.karbaran.user6840()
        mojodi=user1[4] 
        if mojodi>=meghdar_vorodi:
            mande_jadid=mojodi-meghdar_vorodi
            sh_kart='6037997391690337'
            connector(mande_jadid,sh_kart)
            mostaghim_sh=Button(top12,text='شارژ مستقیم',font=('Nazanin',30,'bold'),command=mostaghim).place(x=1350,y=110)
            ramz_sh=Button(top12,text='رمز شارژ',font=('Nazanin',30,'bold'),command=ramzget).place(x=1365,y=410)
        else:
            not_cash=Label(top4,text='موجودی حساب شما کافی نمیباشد!!!',font=('Nazanin',40,'bold')).place(x=725,y=710)
    elif password_entry.get()==pass1278:
        meghdar_vorodi=200000
        user2=[]
        user2=user.karbaran.user1278()
        mojodi=user2[4] 
        if mojodi>=meghdar_vorodi:
            mande_jadid=mojodi-meghdar_vorodi
            sh_kart='6219861925027848'
            connector(mande_jadid,sh_kart)
            mostaghim_sh=Button(top12,text='شارژ مستقیم',font=('Nazanin',30,'bold'),command=mostaghim).place(x=1350,y=110)
            ramz_sh=Button(top12,text='رمز شارژ',font=('Nazanin',30,'bold'),command=ramzget).place(x=1365,y=410)
                   
        else:
            not_cash=Label(top4,text='موجودی حساب شما کافی نمیباشد!!!',font=('Nazanin',40,'bold')).place(x=725,y=710)
    elif password_entry.get()==pass1354:
        meghdar_vorodi=200000
        user3=[]
        user3=user.karbaran.user1354()
        mojodi=user3[4] 
        if mojodi>=meghdar_vorodi:
            mande_jadid=mojodi-meghdar_vorodi
            sh_kart='6037697689563531'
            connector(mande_jadid,sh_kart)
            mostaghim_sh=Button(top12,text='شارژ مستقیم',font=('Nazanin',30,'bold'),command=mostaghim).place(x=1350,y=110)
            ramz_sh=Button(top12,text='رمز شارژ',font=('Nazanin',30,'bold'),command=ramzget).place(x=1365,y=410)
                   
        else:
            not_cash=Label(top4,text='موجودی حساب شما کافی نمیباشد!!!',font=('Nazanin',40,'bold')).place(x=725,y=710)
                          

def mostaghim():
    global top13
    top13=Toplevel()
    top13.geometry('1530x785+0+0')
    top13.config(bg='#bb44aa')
    sh_sim_entry=Entry(top13,font=50)
    sh_sim_entry.place(x=655,y=480)
    cash_But=Button(top13,text='تایید',font=('Nazanin',25,'bold'),command=sim_sharzh_shod).place(x=725,y=510)
    Label(top13,text='لطفا شماره تلفن مورد نظر را وارد کنید',font=('Nazanin',40,'bold')).place(x=725,y=710)

def sim_sharzh_shod():
    Label(top13,text='سیم کارت شما با موفقیت شارژ شد',font=('Nazanin',40,'bold')).place(x=725,y=710)

def ramzget():
    global top13
    top13=Toplevel()
    top13.geometry('1530x785+0+0')
    x=random.randint(1222222222222222,9999999999999999)
    str (x)
    Label(top13,text='رمز شارژ:{}'.format(x),font=('Nazanin',40,'bold')).pack(side=BOTTOM)  
#_______________________________________________________________________________________________________________     

    













#_________________________________________________________________________________________________________________________:
def sorathesab():
    pass

def variz_vajh():
    pass
def enteghaal():
    pass
def pardakhte_ghabz():
    pass
def password(): #karbar ramz aval khod ra vared mikonad
    top1=Toplevel()
    top1.geometry('1530x785+0+0')
    top1.config(bg='#aa55cc')
    label1=Label(top1,text='رمز خود را وارد کنید',font=('Nazanin',40,'bold'))
    label1.place(x=580,y=350)
    global password_entry
    password_entry=Entry(top1,font=50,show='*')
    password_entry.place(x=655,y=480)
    login_but=Button(top1,text='ورود',font=('Nazanin',25,'bold'),command=login).place(x=725,y=510)

#________________________________________________________________________________________________:

def login():

    user1=[]
    user1=user.karbaran.user6840()
    global pass6840
    pass6840=user1[2]

    user2=[]
    user2=user.karbaran.user1278()
    global pass1278
    pass1278=user2[2]
    
    user3=[]
    user3=user.karbaran.user1354()
    global pass1354
    pass1354=user3[2]
    
    if   password_entry.get()==pass6840:
        page_2()
    elif password_entry.get()==pass1278:
        page_2()
    elif password_entry.get()==pass1354:
        page_2()
    else:
        messagebox.showerror('!!!رمز وارد شده صحیح نیست')
    

#________________________________________________________________________________________________:
        
def page_2(): # dar in method page toplevel dovom va khadamt bank ra namayesh midahim
    top2=Toplevel()
    top2.geometry('1530x785+0+0')
    top2.config(bg='#ccffcc')
    labelp2=Label(top2,text='نوع خدمات را انتخاب کنید',font=('Nazanin',40,'bold'))
    labelp2.pack(side=TOP)
    mande=Button(top2,text='اعلام مانده حساب',font=('Nazanin',30,'bold'),command=mande_hesab).place(x=0,y=100)
    daryaft=Button(top2,text='دریافت وجه',font=('Nazanin',30,'bold'),command= daryaft_vajh).place(x=1350,y=110)
    ramz=Button(top2,text='عملیات رمز',font=('Nazanin',30,'bold'),command=amaliyate_ramz).place(x=0,y=250)
    sorat_hesab=Button(top2,text='صورت حساب',font=('Nazanin',30,'bold')).place(x=0,y=400)
    sharzh=Button(top2,text='شارژ سیم کارت',font=('Nazanin',30,'bold'),command=shaarzh).place(x=0,y=550)
    variz=Button(top2,text='واریز وجه',font=('Nazanin',30,'bold')).place(x=1365,y=260)
    enteghal=Button(top2,text='انتقال وجه',font=('Nazanin',30,'bold')).place(x=1365,y=410)
    ghabz=Button(top2,text='پرداخت قبوض',font=('Nazanin',30,'bold')).place(x=1310,y=560)

    
#_________________________________________________________________________________________________:



        




master=Tk()
master.title('ATM')
master.geometry('1530x785+0+0')# in geometry faghat baraye namayesh gar in laptop mibashad
master.config(bg='#ffcc99')
label=Label(master,text='به خود پرداز بانک ملی خوش امدید',font=('Nazanin',40,'bold'))
label.pack()
label2=Label(master,text='لطفا کارت خود را وارد کنید',font=('Titr',35,'bold'))
label2.place(x=550,y=350)
x=PhotoImage(file='meli.png')
label3=Label(master,image=x)
label3.place(x=655,y=75)
button=Button(master,width=50,height=1,fg='white',bg='blue',bd=8,command=password)
button.pack(side='bottom')
button.place(x=580,y=410)



master.mainloop()