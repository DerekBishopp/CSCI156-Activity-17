__author__ = 'Derek'

class Social:
    class InvalidSocial(ValueError):
         pass

    def __init__(self):
        self.social = self.ss

    def validatess(self):
        try:
            x, y, z = self.ss.split('-')
            if self == '078-05-1120':
                raise self.InvalidSocial
            if x == '000':
                raise self.InvalidSocial
            if y == '00':
                raise self.InvalidSocial
            if z == '0000':
                raise self.InvalidSocial
            if len(x) == 3 and len(y) == 2 and len(z) == 4:
                pass
            else:
                raise self.InvalidSocial
            x = int(x)
            if x == 666:
                raise self.InvalidSocial
            else:
                pass
            if x <= 899:
                pass
            else:
                raise self.InvalidSocial

        except ValueError:
            raise self.InvalidSocial

    def getsocial(self):
        self.ss = input('#SS: ')
        try:
            self.validatess()
        except self.InvalidSocial:
            print('Invalid SS \n')
            self.getsocial()