class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        try:
            name = name.split('@')
            if len(name[0]) >= self.min_length:
                return True
            return False
        except:
            return False

    def __is_mail_valid(self, mail):
        try:
            mail = mail.split('@')

            res = mail[1].split('.')
            if res[0] in self.mails:
                return True
            else:
                return False
        except:
            return False

    def __is_domain_valid(self, domain):
        domain = domain.split('.')
        if domain[1] in self.domains:
            return True
        return False

    def validate(self, email):
        if EmailValidator.__is_name_valid(self, email) and EmailValidator.__is_mail_valid(self, email) \
                and EmailValidator.__is_domain_valid(self, email):
            return True
        return False

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77ergmail.com"))
print(email_validator.validate("georgiosgmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev.min_length, 5)
        self.assertEqual(ev.mails, ["me"])
        self.assertEqual(ev.domains, ["you", "he"])

    def test_private_validate_name(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__is_name_valid("abc"), False)
        self.assertEqual(ev._EmailValidator__is_name_valid("abcdef"), True)

    def test_private_validate_mail(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__is_mail_valid("me"), True)
        self.assertEqual(ev._EmailValidator__is_mail_valid("you"), False)

    def test_private_validate_domain(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__is_domain_valid("he"), True)
        self.assertEqual(ev._EmailValidator__is_domain_valid("she"), False)

    def test_validate(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev.validate("itsme@me.you"), True)
        self.assertEqual(ev.validate("me@me.you"), False)
        self.assertEqual(ev.validate("itsme@me.she"), False)
        self.assertEqual(ev.validate("itsme@you.he"), False)


if __name__ == "__main__":
    unittest.main()