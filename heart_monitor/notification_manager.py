import notifications_sender
from common_types import Contact
import smtplib
import twilio
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class NotificationManager(object):
    '''
    :developer: Josh
    This class uses urgency to dictate which messaging mediums get used
        LOW_URGENCY = 0
    	MEDIUM_URGENCY = 1
    	HIGH_URGENCY = 2
    '''
    
    def whichMethod(urg):
    	if(urg == URGENCY.LOW_URGENCY):
    		notifications_sender.Telegram()
    	else if(urg == URGENCY.MEDIUM_URGENCY):
    		notifications_sender.Telegram()
    		notifications_sender.Email()
    	else if(urg == URGENCY.HIGH_URGENCY):
    		notifications_sender.Telegram()
    		notifications_sender.email()
    		notifications_sender.SMSSender()
    pass
    	
