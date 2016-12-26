import smtplib
import imaplib

"""
This code demonstrates the facade pattern.

The facade pattern is designed to provide a simple interface to a complex system
of components. It abstracts a simpler interface out of a complex one. The facade
pattern is often used to encapsulate a typical usage of a system.

This code implements a simple facade for an e-mail application. It provides a
simple interface to enable sending a single e-mail and listing of e-mails in
the inbox on an IMAP connection.

There is no API demonstration code because it requires an actual email server.
"""


class EmailFacade:
    """
    This class implements the facade design pattern by providing a simple
    interface for an email client application. It assumes the SMTP and IMAP
    are identical servers.
    """

    def __init__(self, host, username, password):
        """
        Initialise the object with the hostname of the e-mail server, account
        username and password.
        :param host: hostname of the e-mail server; assumes SMTP and IMAP server
        are identical.
        :param username: e-mail account username.
        :param password: e-mail account password.
        """
        self.host = host
        self.username = username
        self.password = password

    def send_mail(self, to_email, subject, message):
        """
        Send an email message to the specified email address. This method
        implements the simplified facade interface used by client code. It hides
        the complexity behind a simplified facade interface.
        :param to_email: destination e-mail address.
        :param subject: email message subject.
        :param message: email message.
        :return: None
        """
        if '@' not in self.username:
            from_email = '{0}@{1}'.format(self.username, self.host)
        else:
            from_email = self.username
        message = ('From: {0}\r\n'
                   'To: {1}\r\n'
                   'Subject: {2}\r\n\r\n{3}').format(
            from_email, to_email, subject, message
        )
        smtp = smtplib.SMTP(self.host)
        smtp.login(self.username, self.password)
        smtp.sendmail(from_email, [to_email], message)

    def get_inbox(self):
        """
        Get the messages in the inbox.
        :return: list of email messages (as strings) in the inbox.
        """
        mailbox = imaplib.IMAP4(self.host)
        mailbox.login(bytes(self.username, 'utf8'),
                      bytes(self.password, 'utf8'))
        mailbox.select()
        x, data = mailbox.search(None, 'ALL')
        messages = []
        for num in data[0].split():
            x, message = mailbox.fetch(num, '(RFC822)')
            messages.append(message[0][1])
        return messages
