import datetime
import os
from notification import notify
from password_genrator import NPG
from Myemail import Myemail

extracted_month = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\passcode changer.txt",'rt')
month = extracted_month.read()
last_Month = str(month)
correntMonth = datetime.datetime.now().strftime("%m")
correntMonth = str(correntMonth)
def nps():
          newP = NPG()
          new_pass = f"\nboss your new password of the month is:\n{newP}"
          new_pass = str(new_pass)
          delete_month = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\passcode changer.txt",'r+')
          delete_month.truncate(0)
          delete_month.close()
          month_input = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\passcode changer.txt","a")
          month_input.write(correntMonth)
          month_input.close()
          delete_pass = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\password.txt",'r+')
          delete_pass.truncate(0)
          delete_pass.close()
          pass_input = open("C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\password.txt","a")
          pass_input.write(newP)
          pass_input.close()
          Myemail('vishnuarunkmgupta@gmail.com',new_pass)
          notify("New password changed and send","new password of fury for this month is send to your email")

def npem():
     #correntMonth = datetime.datetime.now().strftime("%m")
     
     if (last_Month == correntMonth):
          pass
     else:
          nps()

                              