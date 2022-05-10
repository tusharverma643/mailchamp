from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django.conf import settings
from base.models import Content,ContentType
import datetime
from django.db.models import Q

#function to find the mails that have to be sent at the current time ie(whose sending time <= Current time)
# Function sends those mails and then deletes those mail entries from the database.
def sendmail():
    cont_mails_obj=Content.objects.filter(Q(sending_datetime__lte=datetime.datetime.now()))     #contentMail that have to be send now.
    contentmails=cont_mails_obj.values_list() #conv contentMails into querry-list
    content_types=[i[1] for i in contentmails] #extracting the Topic of those mails
    subjects=[i[2] for i in contentmails] #extracting subjects similarly
    messages=[i[3] for i in contentmails] #extracting messages similarly

    #Using list of lists , where list[i] provides all the information about a particular content Mail
    
    recipient_lists=[] #list of list :- stores list of recipients of a particular mail.
    for contType in content_types: #iterating throught each type of content and extracting the recipients of that particular mail.
        mailobj=list(ContentType.objects.get(content_type=contType).emails.all().values_list())
        recipient_list = [i[0] for i in mailobj]
        recipient_lists.append(recipient_list)
    
    cont_mails_obj.delete() #delete all the mails from Database whose info has already been extracted.

    #function to send the mail using Google SMTP service.
    for i in range(len(subjects)):
        subject = subjects[i]
        message = messages[i]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = recipient_lists[i]
        send_mail( subject, message, email_from, recipient_list )

#recurring background service after every 60 seconds.
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(sendmail,'interval', seconds=60)
    scheduler.start()
    

