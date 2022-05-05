import sys
import os
import smtplib 
from email.message import EmailMessage

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
import tkinter.messagebox as messagebox


class RGui(QMainWindow):
    def __init__(self):
        super(RGui, self).__init__()
        
        uic.loadUi(os.getcwd() + "\\ui\\ReportBug.ui", self)
        self.bt1.clicked.connect(self.mailF)
        self.setWindowIcon(QtGui.QIcon(os.getcwd().replace('\\tools\\errors', '') + "\\resources\\BRicon.ico"))
        
        self.shadow1 = QGraphicsDropShadowEffect()
        self.shadow2 = QGraphicsDropShadowEffect()
        self.shadow3 = QGraphicsDropShadowEffect()
        self.shadow1.setBlurRadius(15)
        self.shadow2.setBlurRadius(15)
        self.shadow3.setBlurRadius(15)
        
        self.emailT.setGraphicsEffect(self.shadow1)
        self.problemT.setGraphicsEffect(self.shadow2)
        self.bt1.setGraphicsEffect(self.shadow2)
        
        
    def mailF(self):
        message = EmailMessage()
        mail = self.emailT.text()
        problem = self.problemT.toPlainText()
        
        self.emailT.clear()
        if mail.__contains__("@gmail.com") == False:
            messagebox.showerror(title="Correo no valido", message="Correo no valido. \n Introduce un correo valido.")
        else:
            self.problemT.clear()
            
            email_subject = mail 
            sender_email_address = "SoporteDeEva@gmail.com"
            receiver_email_address = "j.armando140208g@gmail.com"
            email_password = "Armando131408"
            
            message['Subject'] = email_subject 
            message['From'] = sender_email_address 
            message['To'] = receiver_email_address

            message.set_content(problem)
            
            email_smtp = "smtp.gmail.com"  
            server = smtplib.SMTP(email_smtp, 587)
            server.ehlo()
            server.starttls()
            
            server.login(sender_email_address, email_password) 
            server.send_message(message)  
            server.quit()
            sys.exit()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = RGui()
    GUI.show()
    sys.exit(app.exec_())