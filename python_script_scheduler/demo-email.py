import os #To get env variable 
import smtplib# astandard to send and recieve emails 
# to send a proper email message 
from email.message import EmailMessage


#Get the email and password of the sender from env
EMAIL_ADDRESS=os.environ.get('EMAIL_ADDRESS')
SMTP_APP_PASSWORD=os.getenv('SMTP_APP_PASSWORD')

print(EMAIL_ADDRESS, SMTP_APP_PASSWORD)

# recepients of the email
recepients=['dineshthiran97@gmail.com','lokeshsbusiness@gmail.com'] 
#build the message object 
msg=EmailMessage()
msg['Subject']='your joke of the Day !'
msg['From']=EMAIL_ADDRESS
msg['To']=recepients
msg.set_content("Enjoy the day and keep moving forward 😁")


# print(help(EmailMessage.add_attachment))
#add attachment takes context manager 
with open('YOUR_FEED.txt','r') as f:
    file_data=f.read()
    file_name=f.name
msg.add_attachment(file_data,subtype='file_type',filename=file_name)


#establish connection to the gmail server 


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(user=EMAIL_ADDRESS,password=SMTP_APP_PASSWORD)
    smtp.send_message(msg)


print('Email sent Successfully ...' ,recepients)