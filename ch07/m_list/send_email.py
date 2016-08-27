import smtplib
from email.mime.text import MIMEText


def send_email(subject, message, from_addr, *to_addrs, host="localhost",
               port=1025, headers=None):
    """
    Send and email message with a subject.

    This function is used to send an email message to the specified email
    address(es) using the specified SMTP server and port, along with the
    specified headers (stored in dictionary).

    The function can be tested using the built-in Python SMTP server module by
    running the following command:

    python3 -m smtpd -n -c DebuggingServer localhost:1025

    :param subject: email subject
    :param message: email message
    :param from_addr: email address from which the email was sent from
    :param to_addrs: destination email addresses
    :param host: SMTP server hostname
    :param port: SMTP server port
    :param headers: dictionary of email headers (dictionaries allow any string
    to be used as a key).
    :return: None
    """
    headers = {} if headers is None else headers
    email = MIMEText(message)
    email['Subject'] = subject
    email['From'] = from_addr
    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email['To']
        email['To'] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()


# Demonstration of API
def main():
    # Send email message to several addresses using default SMTP host & port
    send_email("A model subject", "The message contents", "from@example.com",
               "to1@example.com", "to2@example.com")


# Import guard
if __name__ == '__main__':
    main()
