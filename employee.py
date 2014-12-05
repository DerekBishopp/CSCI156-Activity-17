__author__ = 'Derek'

from ss import *

class Employee:
    def __init__(self, last=None, first=None, start=None, pay_rate=None, social=None):
        if (first is None):
            self.last = input("Input Employee Last Name: ").title
            self.first = input("Input Employee First Name: ").title
            self.start = input("Input Employee Start Date(MM/DD/YYYY : ")
            self.pay_rate = input("Input Employee Pay Rate: ")
            self.social = Social()
        else:
            self.last = last
            self.first = first
            self.start = start
            self.pay_rate = pay_rate
            self.social = social

    def __str__(self):
        return (self.first + self.last + " began work on " + self.start + " \nmaking " + self.pay_rate + ". " +
                self.first + self.last + "'s social security number is " + self.social)