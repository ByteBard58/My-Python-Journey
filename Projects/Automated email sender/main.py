import smtplib
from email.message import EmailMessage
import mimetypes
import os
from dotenv import load_dotenv

load_dotenv()
gmail_addr= os.getenv("gmail")
gmail_passw = os.getenv("password")

def send_email(subject, body, recipent, attachment, attachment_name):
  mail = EmailMessage()
  mail["From"] = gmail_addr
  mail["To"] = recipent
  mail["Subject"] = subject
  mail.set_content(body)
  file_path = attachment
  mime_type,_= mimetypes.guess_type(file_path)
  mainn,subb = mime_type.split("/")
  with open(file_path, "rb") as file:
    mail.add_attachment(file.read(),maintype=mainn,subtype=subb,filename=attachment_name)

  
  with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(gmail_addr, gmail_passw)
    server.send_message(mail)

send_email("SUBEJECT_HERE","BODY_HERE","RECIPANT_HERE","ATTACHMENT_PATH_HERE","ATTACHMENT_NAME_HERE")
