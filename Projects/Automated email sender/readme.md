# 📧 Gmail Auto Attachment Sender

A simple Python script to send emails with file attachments using your Gmail account.

## 🧠 What It Does

- Sends an email with subject and body
- Attaches any file type
- Uses Gmail's SMTP server
- Uses .env file for credentials (didn't upload it here for my own privacy)

## 🚀 Features

- ✅ Email sending via Gmail  
- ✅ File attachments  
- ✅ Environment variable support  
- ✅ Minimal setup

## ⚙️ Tech Stack

- Python 3.6 or higher  
- smtplib, email.message, mimetypes, os (standard libs)  
- python-dotenv

## 📝 Notes

- Works only with Gmail
- Gmail must have 2-Step Verification enabled
- Only plain text emails supported

## How to write the .env file?
- Create a file and name it .env in the same folder
- Write the follpwing code;
  gmail = YOUR_GMAIL_ADDRESS
  password = APP_PASSWORD

**Keep in mind:** Due to security reasons, you can only use the app password of your google account with SMTP. To get app password, make sure you have 2 step verifiation turned on in your google account, then go to the link:
https://myaccount.google.com/apppasswords
