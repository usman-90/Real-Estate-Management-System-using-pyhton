from tkinter import*
import time
from tkinter import ttk
import webbrowser
import pypyodbc
from tkinter import messagebox

# CREATING A ROOT WINDOW
w=Tk()

# DEFINIG  ITS INITIAL GEOMETRY
w.geometry('1000x800')

# DIFINIG ITS TITLE
w.title('Real Estate Managment System')

# CREATING TOP FRAME FOR TITLE
tf=Frame(w,bg='gray30',height=70)
tf.pack(side=TOP,fill=X)

# CREATING SIDE FRAME FOR SIDE BUTTONS
ts=Frame(w,bg='gray40')
ts.place(x=0,y=70,width=100,height=1000)

# IMPORTING IMAGES FOR LATER USE

bk_img=PhotoImage(file=r'E:\1st sem\Project\mapp.PNG')
in_img=PhotoImage(file=r'E:\1st sem\Project\ty.PNG')
img6=PhotoImage(file=r'E:\1st sem\Project\pp.PNG')
del_img=PhotoImage(file=r'E:\1st sem\Project\delin.PNG')
img4=PhotoImage(file=r'E:\1st sem\Project\image.PNG')
img5=PhotoImage(file=r'E:\1st sem\Project\ss.PNG')

# ASSIGNING TEXT-VARIABLES FOR ENTRIES

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
var10=StringVar()
var11=StringVar()
var12=StringVar()
var13=StringVar()
var14=StringVar()
typee=StringVar()
pr1=StringVar()
pur=StringVar()
city=StringVar()
var_del=StringVar()

# FUNCTION TO CLOSE THE WINDOW

def quitt():
    w.quit()


# FUNCTION TO RETRIEVE DATA

def find():
    
    # FRAME TO SHOW DATA IN TREEVIEW
    t_show=Frame(w)
    t_show.place(x=100,y=70,width=2000,height=1000)
    
    # BACKGROUND IMAGE
    bac_l=Label(t_show,image=bk_img)
    bac_l.place(x=0,y=0,height=635,width=1300)
    
    # DEFINING TREEVIEW AND ITS COLUMNS
    ustable=ttk.Treeview(bac_l,columns=('Property ID','Location ID','URL link','Property Type','Price','Address Location','City','Province','Latitude','Longitude','Baths','Area','Purpose','Bedrooms','Date Added','Agency','Agent'))
    
    # DEFINING ITS COLUMN'S HEADINGS
    ustable.heading(0,text='Property ID')
    ustable.heading(1,text='Location ID')
    ustable.heading(2,text='URL Link')
    ustable.heading(3,text='Property Type')
    ustable.heading(4,text='Price')
    ustable.heading(5,text='Address Location')
    ustable.heading(6,text='City')
    ustable.heading(7,text='Province')
    ustable.heading(8,text='Latitude')
    ustable.heading(9,text='Longitude')
    ustable.heading(10,text='Baths')
    ustable.heading(11,text='Area')
    ustable.heading(12,text='Purpose')
    ustable.heading(13,text='Bedrooms')
    ustable.heading(14,text='Date Added')
    ustable.heading(15,text='Agency')
    ustable.heading(16,text='Agent')
    ustable.place(x=50,y=30)
    

    # ADDING AN VERTICAL SCROLL-BAR TO OUR TREEVIEW 
    sb1 = Scrollbar(bac_l, orient=VERTICAL,command=ustable.yview)
    sb1.pack(side=LEFT,fill=Y)
    ustable.config(yscrollcommand=sb1.set)
   
    # ADDING AN HORIZONTAL SCROLL-BAR TO OUR TREEVIEW
    sb = Scrollbar(bac_l, orient=HORIZONTAL, command=ustable.xview)
    ustable.configure(xscroll=sb.set)
    sb.pack(side=BOTTOM,fill=X)
    
    # CONNECTING THE DATABASE 
    con=pypyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                     r'DBQ=E:\1st sem\Project\House Database.accdb;')
    
    # CREATING A CURSOR
    cur1=con.cursor()
    
    # EXECUTING OUR QUERY 
    cur1.execute(f"select * from info_table where City='{city.get()}' and Purpose='{pur.get()}' and Property_Type='{typee.get()} and Price<={pr1.get()}'")
    
    # FETCHING AND INSERTING DATA INTO OUR TREEVIEW
    data=cur1.fetchall()
    for i in data:
        ustable.insert('',END,values=i)
        
    # CLOSING THE CONNECCTION
    con.close()

    # DEFINFINING THE WIDTH OF EVERY COLUMN OF OUR TREEVIEW
    ustable.column("#0",width=0,stretch=NO,minwidth=0)
    ustable.column('Property ID',anchor=CENTER,width=80,minwidth=130)
    ustable.column('Location ID',anchor=CENTER,width=80,minwidth=130)
    ustable.column('URL link',anchor=CENTER,width=200,minwidth=250)
    ustable.column('Property Type',anchor=CENTER,width=110,minwidth=160)
    ustable.column('Price',anchor=CENTER,width=80,minwidth=130)
    ustable.column('Address Location',anchor=CENTER,width=140,minwidth=190)
    ustable.column('City',anchor=CENTER,width=130,minwidth=180)
    ustable.column('Province',anchor=CENTER,width=120,minwidth=170)
    ustable.column('Latitude',anchor=CENTER,width=130,minwidth=180)
    ustable.column('Longitude',anchor=CENTER,width=130,minwidth=180)
    ustable.column('Baths',anchor=CENTER,width=60,minwidth=110)
    ustable.column('Area',anchor=CENTER,width=80,minwidth=130)
    ustable.column('Purpose',anchor=CENTER,width=100,minwidth=150)
    ustable.column('Bedrooms',anchor=CENTER,width=60,minwidth=110)
    ustable.column('Date Added',anchor=CENTER,width=120,minwidth=170)
    ustable.column('Agency',anchor=CENTER,width=160,minwidth=210)
    ustable.column('Agent',anchor=CENTER,width=160,minwidth=210)
    ustable.config(height=27)

    
    # FUNCTION TO OPEN THE URL LINK IN TREE-VIEW
    def URL_link(event):
           id= ustable.selection()
           input_item = ustable.item(id)['values'][2]

   
           import webbrowser
           webbrowser.open_new(f'{input_item}')

    # BINDING THE ABOVE FUNCTION WITH DOUBLE CLICK
    ustable.bind("<Double-1>",URL_link)
   
    


# FUNCTION TO ADD NEW RECORD IN DATABASE
def adddd():
    
    #CONNECTING TO DATABASE
    con=pypyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                     r'E:\1st sem\Project\House Database.accdb;')
    
    #CREATING A CURSOR
    cur1=con.cursor()
    
    # USING TRY AND EXCEPT BLOCK FOR EXCEPTION HANDLING
    try:
        
        a=var1.get()
        b=(var2.get()).title()
        c=var3.get()
        d=(var4.get()).title()
        e=(var5.get()).title()
        f=var6.get()
        g=var7.get()
        h=var8.get()
        i=var9.get()
        j=var10.get()
        k=(var11.get()).title()
        l=var12.get()
        m=var13.get()
        n=var14.get()
        
   
        # CHECKING IF THE ENTRIES ARE EMPTY OR NOT
        if (a and b and c and d and f and j and k and l and m) == "":
            messagebox.showerror("Error","Above Fields cannot be empty")
        else:       
           
           # EXECUTING THE QUERY TO INSERT DATA IN DATABASE
           cur1.execute(f"INSERT INTO info_table([Location Id],[Property_Type],[Price],[City],[Province],[Agent],[Latitude],[Longitude],[Baths],[Area],[Purpose],[Bedrooms],[Date Added],[Agency]) values('{a}','{b}','{c}','{d}','{e}','{f}','{g}','{h}','{i}','{j}','{k}','{l}','{m}','{n}')")
           con.commit()
           
           # CONFIRMATION MESSAGE
           messagebox.showinfo("Added","Successfully Added! ")
    
    # EXCEPT BLOCK TO HANDLE IF INVALID DATA IS ENTERED
    except pypyodbc.DataError as error:
        messagebox.showerror(error,'Please Enter Valid Data')
    
    finally:
        # CLOSING OUR CONNECTION
        con.close()         



# FUNCTION TO DELETE DATA IN DATABASE
def delete():
    
    # CONNECTING TO DATA BASE AND CREATING A CURSOR
    con=pypyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                     r'E:\1st sem\Project\House Database.accdb;')
    cur1=con.cursor()
    
    # EXECUTING OUR QUERY TO DELETE DATA ACCORDING TO PROPERTY ID ENTERED BY USER
    cur1.execute(f"DELETE FROM info_table where [Property ID]={var_del.get()}")
    con.commit()
    
    # CONFIRMATION MESSAGE
    messagebox.showinfo('DELETED',"Record DELETED Successfully!")    
    con.close()    

    

# A FUNCTION FOR DASHBOARD UI
def dashboard():
    
    # CREATING A MAIN FRAME OF OUR DASHBOARD
    
    tm=Frame(w)
    tm.place(x=100,y=70,width=2000,height=1000)

    # ADDING BACKGROUND IMAGE
    
    back_l=Label(tm,image=bk_img)
    back_l.place(x=0,y=0,height=650,width=1300)

    # ADDING LABELS
    
    l1=Label(tm,image=img4,text='TOTAL CITIES: 5',compound=CENTER,bg='slate gray',fg='gray80',font='classic-roman 26 italic')
    l1.place(x=150,y=100,height=160,width=400)

    l2=Label(tm,image=img4,text='HOUSES ON SALE: 1786',compound=CENTER,bg='slate gray',fg='gray80',font='classic-roman 24 italic')
    l2.place(x=150,y=300,height=160,width=400)

    l3=Label(tm,image=img5,text='POPULAR CITIES \n \n Karachi \t \t (39,816) \n Lahore \t \t (33,450) \n Islamabd \t (18,261) \n Rawalpindi \t (11,689) \nPeshawar \t (3,446)',compound=CENTER,bg='slate gray',fg='gray80',font='classic-roman 18 italic')
    l3.place(x=800,y=100,height=350,width=335)


# FUNCTION FOR SEARCH FRAME 

def search():
    
    # CREATING FRAMES AND LABELS 
    
    tm=Frame(w)
    tm.place(x=100,y=70,width=2000,height=1000)
    
    back_l=Label(tm,image=bk_img)
    back_l.place(x=0,y=0,height=650,width=1300)

    t_in=Frame(tm,bg='slate gray')
    t_in.place(x=400,y=80,width=400,height=500)

    l_in=Label(t_in,image=in_img,text="\tSEARCH \n\n \nSelect City \t\t\n\nPurpose \t\n\nPrice Range \t\n\nProperty Type",compound=CENTER,justify=LEFT,fg='gray80',font='classic-roman 18 italic')
    l_in.place(x=-3,y=-3)

    # CREATING COMBO- BOXES
    
    cities=['Karachi','Lahore','Islamabad','Rawalpindi','Faisalabad',]
    c_combo=ttk.Combobox(t_in,textvariable=city,value=cities,width=10,height=12,font='aerial 16')
    c_combo.current()
    c_combo.place(x=230,y=195)

    purpose=['For Sale','For Rent']
    p_combo=ttk.Combobox(t_in,textvariable=pur,value=purpose,width=10,height=12,font='aerial 16')
    p_combo.current()
    p_combo.place(x=230,y=250)
    
    pr_range=['   For Rent','10000','20000','40000','60000','70000','100000','17000000','   For Buy','100000','500000','1500000','3000000','5000000','7500000','10000000','20000000','80000000','2000000000']
    pr_combo=ttk.Combobox(t_in,textvariable=pr1,value=pr_range,width=10,height=12,font='aerial 16')
    pr_combo.current()
    pr_combo.place(x=230,y=305)
    
    pr_type=['House','Flat','Upper Portion','Lower Portion','Penthouse','Farmhouse','Room']
    ty_combo=ttk.Combobox(t_in,textvariable=typee,value=pr_type,width=10,height=12,font='aerial 16')
    ty_combo.current()
    ty_combo.place(x=230,y=360)

    # BUTTON TO EXCUTE SEARCH COMMAND
    
    fd_btn=Button(t_in,width=10,height=1,relief=FLAT,activebackground='gray30',activeforeground='gray20',cursor='hand2',command=find,text='FIND',font='helvetica 16',fg='gray80',bg='gray30')
    fd_btn.place(x=150,y=420)

# FUNCTION FOR DELETE FRAME

def dele():
    
    # CREATING MAIN FRAME AND LABELS
    
    t_del=Frame(w)
    t_del.place(x=100,y=70,width=2000,height=1000)
 
    back_l=Label(t_del,image=bk_img)
    back_l.place(x=0,y=0,height=650,width=1300)    

    t_in=Frame(t_del,bg='slate gray')
    t_in.place(x=370,y=200,width=500,height=220)
    

    l_in=Label(t_in,image=del_img,text="\t      DELETE\n\nProperty ID\t\t\t",compound=CENTER,justify=LEFT,fg='gray80',font='classic-roman 18 italic')
    l_in.place(x=-3,y=-3)
    
    # CREATING ENTRY AND BUTTON TO EXECUTE DELETE COMMAND
    
    ed=Entry(t_del,bg='gray50',bd=0,textvariable=var_del,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    ed.place(x=580,y=329,width=250)

    del_btn=Button(t_del,width=10,height=1,relief=GROOVE,command=delete,activebackground='gray30',activeforeground='gray20',cursor='hand2',text='DELETE',font='helvetica 16',fg='gray80',bg='gray30')
    del_btn.place(x=550,y=379,height=30)

############ ADD FRAME ############

def add():
    
    t_add=Frame(w)
    t_add.place(x=100,y=70,width=2000,height=1000)

    back_l=Label(t_add,image=bk_img)
    back_l.place(x=0,y=0,height=650,width=1300)

    lb=Label(t_add,image=img6,text='\t\t\t      ADD PROPERTY \n\nLocation ID \t\t\t\tLongitude \t\t\t\n\nProperty Type \t\t\t\tBaths \t\t\t\n\nPrice \t\t\t\t\tArea \t\t\t\n\nCity \t\t\t\t\tPurpose \t\t\t\n\nProvince \t\t\t\t\tBedrooms \t\t\t\n\nAgent \t\t\t\t\tDate \t\t\t\n\nLatitude \t\t\t\t\tAgency',bg='slate gray',fg='gray80',compound=CENTER,justify=LEFT,font='classic-roman 18 italic')
    lb.place(x=63,y=50,height=530,width=1150)
    
    ################## ENTRIES OF ADD FRMAE #################
    
    e1=Entry(t_add,bg='gray50',bd=0,textvariable=var1,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e1.place(x=400,y=165,width=220)
    
    e2=Entry(t_add,bg='gray50',bd=0,textvariable=var2,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e2.place(x=400,y=220,width=220)
    
    e3=Entry(t_add,bg='gray50',bd=0,textvariable=var3,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e3.place(x=400,y=273,width=220)
    
    e4=Entry(t_add,bg='gray50',bd=0,textvariable=var4,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e4.place(x=400,y=328,width=220)
    
    e5=Entry(t_add,bg='gray50',bd=0,textvariable=var5,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e5.place(x=400,y=380,width=220)
    
    e6=Entry(t_add,bg='gray50',bd=0,textvariable=var6,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e6.place(x=400,y=438,width=220)
    
    e7=Entry(t_add,bg='gray50',bd=0,textvariable=var7,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e7.place(x=400,y=492,width=220)
    
    e8=Entry(t_add,bg='gray50',bd=0,textvariable=var8,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e8.place(x=900,y=165,width=220)
    
    e9=Entry(t_add,bg='gray50',bd=0,textvariable=var9,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e9.place(x=900,y=220,width=220)
    
    e10=Entry(t_add,bg='gray50',bd=0,textvariable=var10,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e10.place(x=900,y=273,width=220)
    
    e11=Entry(t_add,bg='gray50',bd=0,textvariable=var11,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e11.place(x=900,y=328,width=220)
    
    e12=Entry(t_add,bg='gray50',bd=0,textvariable=var12,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e12.place(x=900,y=380,width=220)
    
    e13=Entry(t_add,bg='gray50',bd=0,textvariable=var13,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e13.place(x=900,y=438,width=220)
    
    e14=Entry(t_add,bg='gray50',bd=0,textvariable=var14,font='classic-roman 16 italic',fg='black',justify=LEFT,relief=SUNKEN)
    e14.place(x=900,y=492,width=220)

    # BUTTON TO ADD DATA
    
    f_btn=Button(t_add,width=10,height=1,relief=FLAT,activebackground='gray30',activeforeground='gray20',cursor='hand2',text='ADD',command=adddd,font='helvetica 16',fg='gray80',bg='gray30')
    f_btn.place(x=550,y=535)

################# SIDE BUTTONS #####################

img=PhotoImage(file=r'E:\1st sem\Project\dashboard.PNG')
btn_d=Button(ts,image=img,bg='gray40',activebackground='gray40',command=dashboard,width=70,height=70,cursor='hand2',relief=FLAT)
btn_d.place(x=10,y=30)

img1=PhotoImage(file=r'E:\1st sem\Project\search.PNG')
btn_s=Button(ts,image=img1,bg='gray40',command=search,width=70,height=70,activebackground='gray40',cursor='hand2',relief=FLAT)
btn_s.place(x=10,y=135)

img2=PhotoImage(file=r'E:\1st sem\Project\plus.PNG')
btn_p=Button(ts,image=img2,bg='gray40',activebackground='gray40',command=add,cursor='hand2',width=70,height=70,relief=FLAT)
btn_p.place(x=10,y=240)

img3=PhotoImage(file=r'E:\1st sem\Project\export.PNG')
btn_e=Button(ts,image=img3,width=70,activebackground='gray40',command=quitt,height=70,bg='gray40',cursor='hand2',relief=FLAT)
btn_e.place(x=10,y=540)

img_d=PhotoImage(file=r'E:\1st sem\Project\delete.PNG')
btn_del=Button(ts,image=img_d,command=dele,width=70,activebackground='gray40',height=70,bg='gray40',cursor='hand2',relief=FLAT)
btn_del.place(x=10,y=345)

################## TITLE #####################

l_title=Label(tf,text='REAL ESTATE MANAGMENT SYSTEM',bg='gray30',font='classic-roman 30 italic bold',fg='gray90')
l_title.place(x=320,y=20)

#################  DATE TIME FUNCTION ##################

def timee():
    a=time.strftime('%d/%b/%y', time.localtime())
    y=time.strftime('%I:%M:%S', time.localtime())
    lt.configure(text=y,fg='gray80')
    ld.configure(text=a,fg='gray80') 
    lt.after(1000,timee)

ld=Label(tf,font='aerial 12',bg='gray30')
ld.place(x=5,y=10,width=100,height=20)

lt=Label(tf,font='aerail 12',bg='gray30')
lt.place(x=5,y=35,width=100,height=20)
timee()

# CALLING DASHBOARD FRAME FUNCTION
dashboard()





w.mainloop()