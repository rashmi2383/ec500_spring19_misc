from common_types import Contact, Message


class NotificationSender(object):
    '''
    :developer Naelle
    Base class that defines shared attributes, methods

    :param message: object_instance of Message class containing message content and urgency
    :param recipient: string value of recipients number/email from Contact class
    returns: void function (sends message)
    :raises keyError: raises an exception
    '''
    def send_notification(Message, recipient):
    pass


# We can define the individual notification senders in more detail later if needed
class SMSSender(NotificationSender):
	'''
    :param message: object_instance of Contact class
    returns: string with sms destination number
    :raises keyError: raises an exception
    '''
    def find_number(Contact):
    	return Contact.get_sms()


class EmailSender(NotificationSender):
	'''
    :param message: object_instance of Contact class
    returns: string with email destination
    :raises keyError: raises an exception
    '''
    def find_email(Contact):
    	return Contact.get_email()
    


class TelegramSender(NotificationSender):
	''' 
    :param message: object_instance of Contact class;
    returns: string with telegraph destination number
    :raises keyError: raises an exception
    '''
    def find_number(Contact):
    	return Contact.get_telegraph()
    


