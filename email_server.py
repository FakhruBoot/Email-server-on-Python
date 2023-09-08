import smtplib
import getpass
def get_mail():
    service = ['gmail' , 'yahoo' , 'hotmail' , 'outlook']
    while True:
        mail_id = input("email id :")
        if '@' in mail_id and '.com' in mail_id:
            sym_pos = mail_id.find("@")
            scm_pos = mail_id.find(".com")
            sp = mail_id[sym_pos+1:scm_pos]
            if sp in service:
                return mail_id , sp
            else:
                print('we do not provide service for this mail' + sp)
                print('we provide service for gmail only')
                continue
        
        else:
            print('invalid email id')
            continue
def domain(ser):
    if ser == 'gmail' :
        return 'smtp.gmail.com'
    elif ser == 'yahoo' :
        return 'smtp.yahoo.com'
    elif ser == 'outlook' or ser == 'hotmail':
        return 'smtp.outlook.com'
 
while True:
    user_mail , sp = get_mail ()
    password = getpass.getpass("password:")
    try:
        domain_name = domain(sp)
        connect = smtplib.SMTP(domain_name, 587)
        connect.ehlo()
        connect.starttls()
        connect.login(user_mail,password)
        to_email = input ('recever id:')
        to_sub = input ('subject:')
        to_mes = input ("message:")
        connect.sendmail(user_mail,to_email,'Subject:' + str(to_sub) + '\n\n' + str(to_mes))
        connect.quit()
        
    except Exception as e:
        print('error found : '+str(e))
        continue
    else:
        print("email send sucesfully")
        break