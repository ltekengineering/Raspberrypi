class Email:
    import smtplib,configparser
    import email.utils
    from email.mime.text import MIMEText

    def __init__(self,serverType):
        self.ini = self.configparser.ConfigParser()
        self.ini.read("/home/pi/Raspberrypi/resources/config.ini")
        self.serverType = serverType

    def sendEmail(self, From, To, Subject, Message):
        #setup server connection        
        if self.serverType == "gmail":
            server = self.smtplib.SMTP( self.ini.get("gmail","server"), int(self.ini.get("gmail","port")) )
            server.ehlo()
            server.starttls()
            server.login(self.ini.get("gmail","username"),self.ini.get("gmail","password") )        
        else:
            server = self.smtplib.SMTP("localhost")

        #create the message

        msg = self.MIMEText(Message,"plain")    
        msg['Subject'] = Subject
        msg["From"] = From
        msg["To"] = To

        server.sendmail(From, [To],msg.as_string())
        server.quit()
