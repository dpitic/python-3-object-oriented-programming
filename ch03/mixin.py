from contact import Contact

class MailSender:
    """Demonstration of a mixin. MailSender enables subclasses to send email."""
    def send_mail(self, message):
        # Warning: this class depends on the implementation of Contact
        print("Sending mail to " + self.email)
        # Email logic goes here

class EmailableContact(Contact, MailSender):
    """Multiple inheritance. Produces a Contact that can send emails."""
    pass

# Demonstration code
def main():
    e = EmailableContact("John Smith", "jsmith@example.net")
    print(Contact.all_contacts)
    e.send_mail("Hello, test e-mail here")

if __name__ == '__main__':
    main()
