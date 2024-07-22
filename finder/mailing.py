# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def send_email(subject, body, to_email):
   
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'E-mailinizi giriniz'
    from_password = 'Şifrenizi giriniz'  #veya uygulama şifresi

    body.encode('utf-8')
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = Header(subject,'utf-8')

    msg.attach(MIMEText(body, 'plain','utf-8'))

    try:
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.close()

        print("E-posta başarıyla gönderildi!")
    except Exception as e:
        print(f"E-posta gönderilirken hata oluştu: {str(e)}")
