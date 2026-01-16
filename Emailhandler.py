import gmail

def send_credentials(name,password,account,email):

    to=f"{email}"
    to_attach=[r"D:\CLASSROOM\PROJECT\Images\Bank attatchment.png"]
    to_sub="Your Credentials For opersting Account"
    to_msg=f"""Dear {name},

Welcome to **FURFURI JANTA BANK**! We are delighted to have you with us.

Here are your account credentials:  

- Account Number: {account}  
- Temporary Password:{password}  

For your security, please **change your password on your first login**.  

If you have any questions or need assistance, our customer support team is always here to help.  

Thank you for choosing **FURFURI JANTA BANK**.  

Best regards,  
**FURFURI JANTA BANK Team**  
Sector 1355, Ramanpur  
Phone: 9999999999  
Email: support@furfurijantabank.com

"""
    con=gmail.GMail("aryan665565@gmail.com","cvmv djir rpmy uwhy")
    msg=gmail.Message(to=email,subject=to_sub,text=to_msg,attachments=to_attach)
    con.send(msg)   




def send_otp(email,name,otp):
    con=gmail.GMail("aryan665565@gmail.com","cvmv djir rpmy uwhy")
   

    to=f"{email}"
    to_attach=[r"D:\CLASSROOM\PROJECT\Images\Bank attatchment.png"]
    to_sub="OTP For Password Recovery"
    to_msg=f"""Dear {name},
    

Welcome to **FURFURI JANTA BANK**! We are delighted to have you with us.

Here Is Your OTP For Password Recovery
OTP={otp}

If you have any questions or need assistance, our customer support team is always here to help.  

Thank you for choosing **FURFURI JANTA BANK**.  

Best regards,  
**FURFURI JANTA BANK Team**  
Sector 1355, Ramanpur  
Phone: 9999999999  
Email: support@furfurijantabank.com

"""
    msg=gmail.Message(to=email,subject=to_sub,text=to_msg,attachments=to_attach)
    con.send(msg)  
    



def send_withdraw_otp(email,name,otp,amt):
    con=gmail.GMail("aryan665565@gmail.com","cvmv djir rpmy uwhy")

    to=f"{email}"
    to_attach=[r"D:\CLASSROOM\PROJECT\Images\Bank attatchment.png"]
    to_sub = "OTP for Withdrawal Transaction – FURFURI JANTA BANK"
    to_msg = f"""
    Dear {name},

Thank you for choosing FURFURI JANTA BANK.

To proceed with your withdrawal transaction {amt}, please use the One-Time Password (OTP) provided below:

Withdrawal Transaction Amount Is: ₹{amt}
OTP: {otp}

This OTP is strictly confidential and is valid for a limited time only.  
Please do not share this OTP with anyone for security reasons.

If you did not initiate this request, please contact our customer support team immediately.

We appreciate your trust in FURFURI JANTA BANK.

Warm regards,  
FURFURI JANTA BANK  
Sector 1355, Ramanpur  
Phone: 9999999999  
Email: support@furfurijantabank.com
"""

    msg=gmail.Message(to=email,subject=to_sub,text=to_msg,attachments=to_attach)
    con.send(msg)

def send_transferamt_otp(email,name,otp,amt,to_acn):
    con=gmail.GMail("aryan665565@gmail.com","cvmv djir rpmy uwhy")

    to=f"{email}"
    to_attach=[r"D:\CLASSROOM\PROJECT\Images\Bank attatchment.png"]
    to_sub = "OTP for Fund Transfer – FURFURI JANTA BANK"
    to_msg =  f"""Dear {name},

Thank you for choosing FURFURI JANTA BANK.

We have received a request to transfer funds from your account to acccount {to_acn}.  
To proceed with this transaction, please use the One-Time Password (OTP) provided below:

Transfer Amount: ₹{amt}
OTP: {otp}

This OTP is valid for a limited time only and is strictly confidential.  
For your security, please do not share this OTP with anyone.

If you did not initiate this fund transfer, please contact our customer support team immediately.

We appreciate your continued trust in FURFURI JANTA BANK.

Warm regards,  
FURFURI JANTA BANK  
Sector 1355, Ramanpur  
📞 9999999999  
✉ support@furfurijantabank.com
"""
    msg=gmail.Message(to=email,subject=to_sub,text=to_msg,attachments=to_attach)
    con.send(msg)   