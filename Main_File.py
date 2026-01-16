from tkinter import Tk,Label,Frame,Button,Entry,messagebox,simpledialog,filedialog
from datetime import datetime
import time
import sqlite3
import Emailhandler
import DatabaseCreater
import pass_genrator
import re
import os
from PIL import Image,ImageTk

DatabaseCreater.create()

def update_time():
    curdate=time.strftime("  📅 %d-%b-%Y\n  ⏰ %r")
    date.configure(text=curdate)
    date.after(1000,update_time)

# ---------------- MAIN SCREEN ----------------------------------------------------------------------------

def main_frame():
     def newuser_click():
          frm.destroy()
          newuser_screen()

     frm=Frame(root,highlightbackground='black',highlightthickness=3)
     frm.configure(bg='teal')
     frm.place(relx=0,rely=.21,relwidth=1,relheight=.7)
     welcome_name=Label(frm,text='Welcome to',
         font=('arial',20,'bold'),
        bg='teal')
     welcome_name.pack()


     img = Image.open(r"Images\main screen logo 1.png").resize((250,140))
     imgtk = ImageTk.PhotoImage(img)

     lbl_img = Label(root, image=imgtk)
     lbl_img.image = imgtk
     lbl_img.place(relx=.0, rely=.0027)


     img2= Image.open(r"Images\main screen logo 1.png").resize((250,140))
     imgtk2 = ImageTk.PhotoImage(img2)

     lbl_img2= Label(root, image=imgtk2)
     lbl_img2.image = imgtk2
     lbl_img2.place(relx=.802, rely=.0027)


     img5= Image.open(r"Images\bank main screen logoo1.jpeg").resize((550,400))
     imgtk5 = ImageTk.PhotoImage(img5)

     lbl_img5= Label(root, image=imgtk5)
     lbl_img5.image = imgtk5
     lbl_img5.place(relx=.286, rely=.29)


     newuser_btn=Button(frm,text="New user\n Create Account",
                        font=("arial",20),
                        fg="black",
                        bg="gray",
                        bd=5,
                        width=13,
                        activeforeground='white',
                        activebackground='purple',
                        command=newuser_screen)
     
                        
     newuser_btn.place(relx=.06,rely=.23)
     existuser_btn=Button(frm,text="Existing User\n Login",
                        font=("arial",20),
                        fg="black",
                        bg="gray",
                        bd=5,
                        width=13,
                        activeforeground='white',
                        activebackground='purple',
                        command=existuser_screen)
     existuser_btn.place(relx=.766,rely=.23)

# ---------------- NEW USER -------------------------------------------------------------------------------

def newuser_screen():
     def back():
          frm.destroy()
          main_frame()

     def reset_click():
          e_name.delete(0,"end")
          e_mail.delete(0,"end")
          e_mobile.delete(0,"end")
          e_aadhar.delete(0,"end")
          e_name.focus()

     def createacn_db():
          name=e_name.get()
          email=e_mail.get()
          mobile=e_mobile.get()
          aadhar=e_aadhar.get()



          if len(name)==0 or len(mobile)==0 or len(aadhar)==0 or len(email)==0:
               messagebox.showerror("Error","Incomplete Details")
               return
          
          match_mob=re.fullmatch("[6-9][0-9]{9}",mobile)
          if match_mob==None:
               messagebox.showerror("Error","Invalid Mobile No.")
               return
          
          match_adhr=re.fullmatch("[0-9]{12}",aadhar)
          if match_adhr==None:
               messagebox.showerror("Error","Invalid Aadhar Number")
               return
          
          match_email=re.fullmatch(r"[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]+",email)
          if match_email==None:
               messagebox.showerror("Error","Invalid Email ID")
               return


          bal=0
          opendate= datetime.now()
          passw=pass_genrator.genrate_pass()
          query="""insert into accounts values(?,?,?,?,?,?,?,?)"""
          conobj=sqlite3.connect(database="mybank.sqlite")
          curobj=conobj.cursor()
          curobj.execute(query,(None,name,passw,mobile,email,aadhar,bal,opendate))
          conobj.commit()
          conobj.close()

          conobj=sqlite3.connect(database="mybank.sqlite")
          curobj=conobj.cursor()
          query="""select max(account) from accounts"""
          curobj.execute(query)
          tup=curobj.fetchone()
          conobj.close()
          Emailhandler.send_credentials(name,passw,tup[0],email)

          messagebox.showinfo("Account Creation","Your ACCOUNT Is Opened \nAnd We Have Mailed \nYour Account Details To Your Given Mail ID")


     frm=Frame(root,highlightbackground='black',highlightthickness=3)
     frm.configure(bg='teal')
     frm.place(relx=0,rely=.21,relwidth=1,relheight=.7)

     img3= Image.open(r"Images\bank logo.png").resize((420,410))
     imgtk3 = ImageTk.PhotoImage(img3)

     lbl_img3= Label(frm, image=imgtk3)
     lbl_img3.image = imgtk3
     lbl_img3.place(relx=.66, rely=.07)


     back_btn=Button(frm,text="Back",font=("arial",20),
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,
                     command=back)
     back_btn.place(relx=0,rely=0)


     note=Label(frm,text='Account Opening Form',
         font=('arial',20,'bold'),
        bg='teal')

     note.pack()

     lbl_name=Label(frm,text="👤Name",width=8,font=("arial",20),
                         bg='gray',
                         bd=5)                        
     lbl_name.place(relx=.08,rely=.3)


     e_name=Entry(frm,font=("arial",20),bd=5)
     e_name.place(relx=.23,rely=.3)


     lbl_mail=Label(frm,text="✉E-mail",width=8,font=("arial",20),
                         bg='gray',
                         bd=5)            
     lbl_mail.place(relx=.08,rely=.42)


     e_mail=Entry(frm,font=("arial",20,),bd=5)
     e_mail.place(relx=.23,rely=.42)
     
     lbl_mobile=Label(frm,text="Mobile no.",width=8,font=("arial",20),
                         bg='gray',
                         bd=5)                        
     lbl_mobile.place(relx=.08,rely=.54)


     e_mobile=Entry(frm,font=("arial",20),bd=5)
     e_mobile.place(relx=.23,rely=.54)


     lbl_aadhar=Label(frm,text="Aadhar No.",width=8,font=("arial",20),
                         bg='gray',
                         bd=5)            
     lbl_aadhar.place(relx=.08,rely=.66)


     e_aadhar=Entry(frm,font=("arial",20),bd=5)
     e_aadhar.place(relx=.23,rely=.66)


     submit_btn=Button(frm,text="Submit",font=("arial",20,"bold"),
                     width=9,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,
                     command=createacn_db)         
     submit_btn.place(relx=.52,rely=.43)
     

     reset_btn=Button(frm,text="Reset",font=("arial",15),
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,command=reset_click)         
     reset_btn.place(relx=.2,rely=.80)

# ---------------- EXISTING USER --------------------------------------------------------------------------

def existuser_screen():
     def back():
          frm.destroy()
          main_frame()

     def reset_click():
          e_acn.delete(0,"end")
          e_pass.delete(0,"end") 
          e_acn.focus()    

     def submit():
          acn=e_acn.get()
          pwd=e_pass.get()

          if len(acn)==0 or len(pwd)==0:
               messagebox.showerror("Error","Incomplete Details")
               return
          
          match_acn=re.fullmatch("[0-9]+",acn) 
          if match_acn==None:
               messagebox.showerror("Error","Invalid Account No.")
               return
          
          match_pwd=re.fullmatch("[A-Za-z]+",pwd)
          if match_pwd==None:
               messagebox.showerror("Error","Invalid Password")
               return

          conobj=sqlite3.connect(database="mybank.sqlite")
          curobj=conobj.cursor()
          query="select * from accounts where account=? and password=?"
          curobj.execute(query,(acn,pwd))
          tup=curobj.fetchone()
          conobj.close()
          if tup==None:
               messagebox.showerror("Login","Invalid Details")
          else:
               acn=tup[0]
               frm.destroy()
               user_welcome(acn)

     frm=Frame(root,highlightbackground='black',highlightthickness=3)
     frm.configure(bg='teal')
     frm.place(relx=0,rely=.21,relwidth=1,relheight=.7)

     img6= Image.open(r"Images\existing user screen logo.jpeg").resize((350,400))
     imgtk6= ImageTk.PhotoImage(img6)

     lbl_img6= Label(frm, image=imgtk6)
     lbl_img6.image = imgtk6
     lbl_img6.place(relx=.7, rely=.07)     


     note=Label(frm,text='Fill These Details For Login ',
         font=('arial',20,'bold'),
        bg='teal')

     note.pack()

     lbl_acn=Label(frm,text="👤ACCOUNT NO.",width=14,font=("arial",20),
                         bg='gray',
                         bd=5)                        
     lbl_acn.place(relx=.045,rely=.3)


     e_acn=Entry(frm,font=("arial",20,"bold"),bd=5)
     e_acn.place(relx=.25,rely=.3)


     lbl_pass=Label(frm,text="PASSWORD",width=14,font=("arial",20),
                         bg='gray',
                         bd=5)            
     lbl_pass.place(relx=.046,rely=.45)
     

     e_pass=Entry(frm,font=("arial",20,"bold"),show="*",bd=5)
     e_pass.place(relx=.25,rely=.45) 


     back_btn=Button(frm,text="Back",font=("arial",20),
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,
                     command=back)
     back_btn.place(relx=0,rely=0)


     forgot_btn=Button(frm,text="Forgot Password",font=("arial",15),
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,
                     command=forgot_screen)         
     forgot_btn.place(relx=.24,rely=.60)


     submit_btn=Button(frm,text="Submit",font=("arial",20,"bold"),
                     width=9,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,
                     command=submit)         
     submit_btn.place(relx=.55,rely=.34)
     

     reset_btn=Button(frm,text="Reset",font=("arial",15),
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,command=reset_click)         
     reset_btn.place(relx=.12,rely=.60)

# ---------------- FORGOT SCREEN -------------------------------------------------------------------------------------------

def forgot_screen():
     def back():
          frm.destroy()
          existuser_screen()

     def reset_click():
          e_acn.delete(0,"end")
          e_aadhar.delete(0,"end")
          e_acn.focus()          

     def send_otp():
               gen_otp=pass_genrator.send_otp()
               acn=e_acn.get()
               adhr=e_aadhar.get()

               conobj=sqlite3.connect(database="mybank.sqlite")
               curobj=conobj.cursor()
               query="select name,email,password from accounts where account=? and aadhar=?"
               curobj.execute(query,(acn,adhr))
               tup=curobj.fetchone()
               conobj.close()
               if tup==None:
                    messagebox.showerror("Forgot Password","Record Not Found")
               else:
                    Emailhandler.send_otp(tup[1],tup[0],gen_otp)
                    user_otp=simpledialog.askinteger("Password Recovery","Enter OTP")
                    if gen_otp==user_otp:
                         messagebox.showinfo("Pasword Recovery",f"Your Password={tup[2]}")
                    else:
                         for i in range(3):
                              messagebox.showerror("Password Recovery","Invalid OTP \n Try Again")
                              otp_btn.configure(text="Resend Otp")             


     frm=Frame(root,highlightbackground='black',highlightthickness=3)
     frm.configure(bg='teal')
     frm.place(relx=0,rely=.21,relwidth=1,relheight=.7)

     welcome_name=Label(frm,text='Fill Details',
                        font=('arial',20,'bold'),
                        bg='teal')
     welcome_name.pack()     

     lbl_acn=Label(frm,text="👤ACCOUNT NO.",font=("arial",20),
                   width=14,
                   bg='gray',
                   bd=5)  
                 
                
     lbl_acn.place(relx=.045,rely=.3)


     e_acn=Entry(frm,font=("arial",20,"bold"),bd=5)
     e_acn.place(relx=.25,rely=.3)          


     lbl_aadhar=Label(frm,text="Aadhar No.",font=("arial",20),
                         width=14,
                         bg='gray',
                         bd=5)            
     lbl_aadhar.place(relx=.046,rely=.45)


     e_aadhar=Entry(frm,font=("arial",20,"bold"),bd=5)
     e_aadhar.place(relx=.25,rely=.45)


     back_btn=Button(frm,text="Back",font=("arial",20),
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,
                     command=back)
     back_btn.place(relx=0,rely=0)


     reset_btn=Button(frm,text="Reset",font=("arial",15),
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,command=reset_click)         
     reset_btn.place(relx=.12,rely=.60)


     otp_btn=Button(frm,text="Send Otp",font=("arial",15),
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,command=send_otp)         
     otp_btn.place(relx=.24,rely=.60)


     submit_btn=Button(frm,text="Submit",font=("arial",20,"bold"),
                     width=9,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5)         
     submit_btn.place(relx=.55,rely=.34)

# ---------------- USER WELCOME SCREEN AFTER LOGIN -----------------------------------------------------------------------------------------------

def user_welcome(acn=None):
     def logout():
          frm.destroy()
          main_frame()
       

     def checkdetail_screen():
          ifrm=Frame(frm,highlightbackground='black',highlightthickness=3)
          ifrm.configure(bg='gray')
          ifrm.place(relx=.05,rely=.13,relwidth=.725,relheight=.82)

          lbl_checknote=Label(ifrm,text="Account Holder Details",bg="gray",font=("arial",20))
          lbl_checknote.pack()

          conobj=sqlite3.connect(database="mybank.sqlite")
          curobj=conobj.cursor()
          query="select account,balance,aadhar,email,mobile,opendate from accounts where account=?"
          curobj.execute(query,(acn,))
          tup=curobj.fetchone()
          conobj.close()

          if tup is None:
               messagebox.showerror("Error", "No record found")
          else:     
               details=f"""
Account No.= {tup[0]}\n
Account Balance= {tup[1]}\n
Account Holder Aadhar No.= {tup[2]}\n
Account Holder Email Id= {tup[3]}\n
Account holder Mobile no.= {tup[4]}\n
Account Open Date= {tup[5]}
"""
          lbl_details=Label(ifrm,text=details,bg="gray",font=("arial",18),
    justify="left",
    anchor="w")
          lbl_details.place(relx=.1,rely=.08)

          
     def update_screen():
          def update_db():
               name=e_name.get()
               email=e_mail.get()
               mob=e_mobile.get()
               passw=e_password.get()

               conobj=sqlite3.connect(database="mybank.sqlite")
               curobj=conobj.cursor()
               query="update accounts set name=?,mobile=?,email=?,password=? where account=?"
               curobj.execute(query,(name,mob,email,passw,acn))
               conobj.commit()
               conobj.close()
               messagebox.showinfo("Update Screen","Updated Sucessfully")
               checkdetail_screen()


          conobj=sqlite3.connect(database="mybank.sqlite")
          curobj=conobj.cursor()
          query="select name,email,mobile,password from accounts where account=?"
          curobj.execute(query,(acn,))
          tup=curobj.fetchone()
          conobj.close()



          ifrm=Frame(frm,highlightbackground='black',highlightthickness=3)
          ifrm.configure(bg='gray')
          ifrm.place(relx=.05,rely=.13,relwidth=.725,relheight=.82)

          lbl_updatenote=Label(ifrm,text="Update Your Details",bg="gray",font=("arial",20))
          lbl_updatenote.pack()
     

          lbl_name=Label(ifrm,text="👤Name",width=8,font=("arial",20),
                         bg='gray',justify="left",anchor="w",
                         bd=5)                        
          lbl_name.place(relx=.02,rely=.2)


          e_name=Entry(ifrm,font=("arial",20),bd=5)
          e_name.place(relx=.17,rely=.2)


          lbl_mail=Label(ifrm,text="✉E-mail",width=8,font=("arial",20),
                         bg='gray',justify="left",anchor="w",
                         bd=5)            
          lbl_mail.place(relx=.02,rely=.33)


          e_mail=Entry(ifrm,font=("arial",20,),bd=5)
          e_mail.place(relx=.17,rely=.33)
     
          lbl_mobile=Label(ifrm,text="Mobile no.",width=8,font=("arial",20),
                         bg='gray',justify="left",anchor="w",
                         bd=5)                        
          lbl_mobile.place(relx=.02,rely=.46)


          e_mobile=Entry(ifrm,font=("arial",20),bd=5)
          e_mobile.place(relx=.17,rely=.46)


          lbl_password=Label(ifrm,text="Password",width=8,font=("arial",20),
                         bg='gray',justify="left",anchor="w",
                         bd=5)            
          lbl_password.place(relx=.02,rely=.59)


          e_password=Entry(ifrm,font=("arial",20),bd=5)
          e_password.place(relx=.17,rely=.59)

          e_name.insert(0,tup[0])
          e_mail.insert(0,tup[1])
          e_mobile.insert(0,tup[2])
          e_password.insert(0,tup[3])

          update_btn=Button(ifrm,text="Update",font=("arial",20,"bold"),
                     width=9,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,command=update_db)         
          update_btn.place(relx=.62,rely=.4)
     
     def deposite_screen():
          def deposit_db():
               amt=float(e_amount.get())

               conobj=sqlite3.connect(database="mybank.sqlite")
               curobj=conobj.cursor()
               query="update accounts set balance=balance+? where account=?"
               curobj.execute(query,(amt,acn))
               conobj.commit()
               conobj.close()
               messagebox.showinfo("Deposit Screen","Amount Deposit Sucessfully")
               e_amount.delete(0,"end")
               e_amount.focus()
               checkdetail_screen()

          ifrm=Frame(frm,highlightbackground='black',highlightthickness=3)
          ifrm.configure(bg='gray')
          ifrm.place(relx=.05,rely=.13,relwidth=.725,relheight=.82)

          lbl_depositenote=Label(ifrm,text="Deposite Here",bg="gray",font=("arial",20))
          lbl_depositenote.pack()

          lbl_amount=Label(ifrm,text=" Amount",width=8,font=("arial",21,"bold"),
                         bg='gray',justify="left",anchor="w",
                         bd=5)            
          lbl_amount.place(relx=.32,rely=.4)


          e_amount=Entry(ifrm,font=("arial",20),bd=5)
          e_amount.place(relx=.47,rely=.4)
          e_amount.focus()

          submit_btn=Button(ifrm,text="Submit",font=("arial",20,"bold"),
                     width=9,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,command=deposit_db)         
          submit_btn.place(relx=.45,rely=.65)
     
     def withdraw_screen():
          def withdraw_db():
               amt=float(e_amount.get())

               conobj=sqlite3.connect(database="mybank.sqlite")
               curobj=conobj.cursor()
               query="select email,name,balance from accounts where account=?"
               curobj.execute(query,(acn,))
               tup=curobj.fetchone()
               conobj.close()

               if amt<=tup[2]:
                    gen_otp=pass_genrator.send_otp()
                    Emailhandler.send_withdraw_otp(tup[0],tup[1],gen_otp,amt)
                    messagebox.showinfo("Withdraw","Otp Sent To Your Registered Email ID")
                    user_otp=simpledialog.askinteger("Withdraw Balance","OTP")
                    if gen_otp==user_otp:

                         conobj=sqlite3.connect(database="mybank.sqlite")
                         curobj=conobj.cursor()
                         query="update accounts set balance=balance-? where account=?"
                         curobj.execute(query,(amt,acn))
                         conobj.commit()
                         conobj.close()
                         messagebox.showinfo("Withdraw Screen",f"Amount: {amt} Withdraw Sucessfully")
                         e_amount.delete(0,"end")
                         e_amount.focus()
                         checkdetail_screen()
                    else:
                         messagebox.showerror("Error","Invalid Otp")
                         submit_btn.configure(text="Resend")
               else:
                    messagebox.showwarning("Withdraw Screen",f"Insufficient Balance?\n Abaliable Balance:{tup[2]}")     


          ifrm=Frame(frm,highlightbackground='black',highlightthickness=3)
          ifrm.configure(bg='gray')
          ifrm.place(relx=.05,rely=.13,relwidth=.725,relheight=.82)

          lbl_withdrawnote=Label(ifrm,text="Withdraw Here",bg="gray",font=("arial",20))
          lbl_withdrawnote.pack()

          lbl_amount=Label(ifrm,text=" Amount",width=8,font=("arial",21,"bold"),
                         bg='gray',justify="left",anchor="w",
                         bd=5)            
          lbl_amount.place(relx=.32,rely=.4)


          e_amount=Entry(ifrm,font=("arial",20),bd=5)
          e_amount.place(relx=.47,rely=.4)
          e_amount.focus()

          submit_btn=Button(ifrm,text="Submit",font=("arial",20,"bold"),
                     width=9,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,command=withdraw_db)         
          submit_btn.place(relx=.45,rely=.65)
     
     def transfer_screen():
          def transfer_db():
               to_acn=e_to_acn.get()
               amt=float(e_amount.get())


               conobj=sqlite3.connect(database="mybank.sqlite")
               curobj=conobj.cursor()
               query="select * from accounts where account=?"
               curobj.execute(query,(to_acn,))
               tup=curobj.fetchone()
               conobj.close()

               if tup==None:
                    messagebox.showerror("Transfer","Given Account Number Is Invalid \n Please Check Account Number And  \n Try Again")
                    return


               conobj=sqlite3.connect(database="mybank.sqlite")
               curobj=conobj.cursor()
               query="select email,name,balance from accounts where account=?"
               curobj.execute(query,(acn,))
               tup=curobj.fetchone()
               conobj.close()

               if amt<=tup[2]:
                    gen_otp=pass_genrator.send_otp()
                    Emailhandler.send_transferamt_otp(tup[0],tup[1],gen_otp,amt,to_acn)
                    messagebox.showinfo("Transfer","Otp Sent To Your Registered Email ID")
                    user_otp=simpledialog.askinteger("Transfer","OTP")
                    if gen_otp==user_otp:

                         conobj=sqlite3.connect(database="mybank.sqlite")
                         curobj=conobj.cursor()
                         query1="update accounts set balance=balance-? where account=?"
                         query2="update accounts set balance=balance+? where account=?"
                         curobj.execute(query1,(amt,acn))
                         curobj.execute(query2,(amt,to_acn))
                         conobj.commit()
                         conobj.close()
                         messagebox.showinfo("Transfer Screen",f"Amount: {amt} Transfer Sucessfully")
                         e_amount.delete(0,"end")
                         e_amount.focus()
                         checkdetail_screen()
                    else:
                         messagebox.showerror("Error","Invalid Otp")
                         submit_btn.configure(text="Resend")
               else:
                    messagebox.showwarning("Transfer Screen",f"Insufficient Balance?\n Abaliable Balance:{tup[2]}")     



          ifrm=Frame(frm,highlightbackground='black',highlightthickness=3)
          ifrm.configure(bg='gray')
          ifrm.place(relx=.05,rely=.13,relwidth=.725,relheight=.82)


          lbl_transfernote=Label(ifrm,text="Transfer Here",bg="gray",font=("arial",20))
          lbl_transfernote.pack()
   
          lbl_to_acn=Label(ifrm,text="To Account",width=9,font=("arial",21,"bold"),
                         bg='gray',
                         bd=5)            
          lbl_to_acn.place(relx=.275,rely=.3)


          e_to_acn=Entry(ifrm,font=("arial",20),bd=5)
          e_to_acn.place(relx=.47,rely=.3)
          e_to_acn.focus()

          lbl_amount=Label(ifrm,text=" Amount",width=9,font=("arial",21,"bold"),
                         bg='gray',justify="left",anchor="w",
                         bd=5)            
          lbl_amount.place(relx=.32,rely=.43)


          e_amount=Entry(ifrm,font=("arial",20),bd=5)
          e_amount.place(relx=.47,rely=.43)

          submit_btn=Button(ifrm,text="Submit",font=("arial",20,"bold"),
                     width=9,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,command=transfer_db)         
          submit_btn.place(relx=.45,rely=.6)
     
 


     frm=Frame(root,highlightbackground='black',highlightthickness=3)
     frm.configure(bg='teal')
     frm.place(relx=0,rely=.21,relwidth=1,relheight=.7)

     def update_pic():
          name=filedialog.askopenfilename()
          os.replace(name,f"Images/{acn}.jpg")
          img7= Image.open(f"Images/{acn}.jpg").resize((200,140))
          imgtk7 = ImageTk.PhotoImage(img7)

          lbl_img7= Label(frm, image=imgtk7)
          lbl_img7.image = imgtk7
          lbl_img7.place(relx=.804, rely=.002)       
     if os.path.exists(f"Images/{acn}.jpg"):
          img4= Image.open(f"Images/{acn}.jpg").resize((200,140))
     else:     
          img4= Image.open(r"Images\default user logo.jpg").resize((200,140))
     imgtk4 = ImageTk.PhotoImage(img4)

     lbl_img4= Label(frm, image=imgtk4)
     lbl_img4.image = imgtk4
     lbl_img4.place(relx=.804, rely=.002)

     conobj=sqlite3.connect(database="mybank.sqlite")
     curobj=conobj.cursor()
     query="select name from accounts where account=?"
     curobj.execute(query,(acn,))
     tup=curobj.fetchone()
     conobj.close()


     welcome_name=Label(frm,text=f'Welcome,{tup[0]}',
                        font=('arial',20,"bold"),
                        bg='teal')
     welcome_name.place(relx=.3,rely=0)


     logout_btn=Button(frm,text="Log Out",font=("arial",17),
                     width=9,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,
                     command=logout)         
     logout_btn.place(relx=0,rely=0)   

   

     changepicture_btn=Button(frm,text="Update Photo",font=("arial",17),
                     width=14,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,command=update_pic)         
     changepicture_btn.place(relx=.806,rely=.32)     


     details_btn=Button(frm,text="Check Details",font=("arial",17),
                     width=14,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,
                     command=checkdetail_screen)         
     details_btn.place(relx=.806,rely=.435)   


     update_btn=Button(frm,text="Update Details",font=("arial",17),
                     width=14,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,
                     command=update_screen)         
     update_btn.place(relx=.806,rely=.55)  


     deposit_btn=Button(frm,text="Deposit Amount",font=("arial",17),
                     width=14,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,
                     command=deposite_screen)
     deposit_btn.place(relx=.806,rely=.665)


     Withdraw_btn=Button(frm,text="Withdraw Amount",font=("arial",17),
                     width=14,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,
                     command=withdraw_screen)         
     Withdraw_btn.place(relx=.806,rely=.78)


     transfer_btn=Button(frm,text="Transfer Amount",font=("arial",17),
                     width=14,
                     activeforeground='white',
                     activebackground='purple',
                     bg='gray',
                     bd=5,
                     command=transfer_screen)         
     transfer_btn.place(relx=.806,rely=.895)


# ---------------- ROOT -------------------------------------------------------------------------------------------

root=Tk()
root.state('zoomed')
root.resizable(width=False,height=False)
root.configure(bg='gray')

title=Label(root,
            text="Banking Simulation",
            font=('arial',50,'bold','underline'),
            bg='gray',
            )
title.pack()
curdate=time.strftime(" 📅 %d-%b-%Y\n  ⏰ %r")
date=Label(root,text=curdate,
           font=('arial',15),
           fg='blue',
           bg='gray')

date.pack(pady=15)
update_time()
footer=Label(root,
            text="For  Support:\n📞9999999999    ✉ support@furfurijantabank.com",
            font=('arial',20,'bold'),
            bg='gray')
    
footer.pack(side='bottom')
main_frame()
root.mainloop()