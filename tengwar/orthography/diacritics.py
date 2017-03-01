class Tehta(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return self.name

class TripleDot(Tehta): name = 'Triple dot'
class AcuteAccent(Tehta): name = 'Acute accent'
class Overdot(Tehta): name = 'Overdot'
class Underdot(Tehta): name = 'Underdot'
class RightCurl(Tehta): name = 'Right curl'
class LeftCurl(Tehta): name = 'Left curl'
class RightHook(Tehta): name = 'Right hook'
class LeftHook(Tehta): name = 'Left hook'
class Overbar(Tehta): name = 'Overbar'
class Underbar(Tehta): name = 'Underbar'

triple_dot = TripleDot()
acute_accent = AcuteAccent()
overdot = Overdot()
underdot = Underdot()
right_curl = RightCurl()
left_curl = LeftCurl()

right_hook = RightHook()
left_hook = LeftHook()
overbar = Overbar()
underbar = Underbar()
