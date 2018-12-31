
class Employee(object):

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}{}@domain.com'.format(self.first, self.last).lower()

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.raise_amount * self.pay)

