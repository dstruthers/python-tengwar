class Tehta(object):
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

# triple_dot = Tehta('Triple dot') # '\ue040'
# acute_accent = Tehta('Acute accent') # '\ue046'
# overdot = Tehta('Overdot') # '\ue044'
# underdot = Tehta('Underdot') # '\ue045'
# right_curl = Tehta('Right curl') # '\ue04a'
# left_curl = Tehta('Left curl') # '\ue04c'

# right_hook = Tehta('Right hook') # '\ue058'
# left_hook = Tehta('Left hook') # '\ue059'
# overbar = Tehta('Overbar') # '\ue0050'
# underbar = Tehta('Underbar') # '\ue051'
