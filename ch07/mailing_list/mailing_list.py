import mailing_list.send_email
from collections import defaultdict


class MailingList:
    """Manage groups of email addresses for sending emails."""

    def __init__(self):
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups):
        """
        Collect all the email addresses in one or more groups by converting the
        list of groups to a set.
        :param groups:
        :return:
        """
        groups = set(groups)
        emails = set()
        for e, g in self.email_map.items():
            if g & groups:
                emails.add(e)
        return emails
