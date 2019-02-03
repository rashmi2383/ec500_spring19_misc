from common_types import Contact


class NotificationSender(object):
    '''
    :developer Naelle
    Base class that defines shared attributes, methods
    '''
    pass


# We can define the individual notification senders in more detail later if needed
class SMSSender(NotificationSender):
    pass


class EmailSender(NotificationSender):
    pass


class TelegramSender(NotificationSender):
    pass


