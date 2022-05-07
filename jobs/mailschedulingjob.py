from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django.conf import settings

def sendmail():
    print("triggered")
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['tverma_be19@thapar.edu',]
    send_mail( subject, message, email_from, recipient_list )

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(sendmail,'interval', seconds=60)
    scheduler.start()
    

