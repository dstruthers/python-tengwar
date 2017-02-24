import parsing
from tengwar.orthography.diacritics import Tehta

class Tengwa():
    def __init__(self, name, tehtar=[]):
        self.name = name
        self.tehtar = set(tehtar)

    def __repr__(self):
        if len(self.tehtar) > 0:
            return '<{} with {}>'.format(self.name, ', '.join([repr(t).lower() for t in self.tehtar]))
        else:
            return '<{}>'.format(self.name)

    def __str__(self):
        return repr(self)

    def __add__(self, other):
        if isinstance(other, Tengwa):
            return Tengwar([self, other])
        elif isinstance(other, Tehta):
            return self.__class__(self.name, self.tehtar | set([other]))
        elif isinstance(other, Tengwar):
            return Tengwar([self] + other.tengwar)
        elif isinstance(other, parsing.Partial):
            print('result=', other.result.result)
            print('input=', other.remainder)
            raise TypeError
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Tengwa):
            return self.name == other.name and self.tehtar == other.tehtar

class AspiratedTengwa(Tengwa):
    def __repr__(self):
        return '<{} with long stem>'.format(self.name)

class Numeral(Tengwa):
    def __init__(self, digit):
        self.name = 'Numeral ' + digit
        self.tehtar = []

class Unknown(Tengwa):
    def __init__(self, value):
        self.value = str(value)

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return self.value

class Tengwar(object):
    """List of Tengwa instances"""
    def __init__(self, tengwar):
        self.tengwar = tengwar

    def __eq__(self, other):
        if isinstance(other, Tengwar):
            return self.tengwar == other.tengwar

    def __repr__(self):
        return ''.join([str(tengwa) for tengwa in self.tengwar])

    def __add__(self, other):
        if isinstance(other, Tengwar):
            return Tengwar(self.tengwar + other.tengwar)
        elif isinstance(other, Tengwa):
            return Tengwar(self.tengwar + [other])
        elif isinstance(other, Tehta):
            self.tengwar[-1] += other
            return self
        else:
            raise TypeError

    def __radd__(self, other):
        if isinstance(other, Tengwa):
            return Tengwar([other] + self.tengwar)
        else:
            raise TypeError

tinco = Tengwa('Tinco') # '\ue000'
parma = Tengwa('Parma') # '\ue001'
calma = Tengwa('Calma') # '\ue002'
quesse = Tengwa('Quesse') # '\ue003'

ando = Tengwa('Ando') # '\ue004'
umbar = Tengwa('Umbar') # '\ue005'
anga = Tengwa('Anga') # '\ue006'
ungwe = Tengwa('Ungwe') #'\ue007'

thule = Tengwa('Thule') # '\ue008'
formen = Tengwa('Formen') # '\ue009'
harma = Tengwa('Harma') # '\ue00a'
hwesta = Tengwa('Hwesta') # '\ue00b'

anto = Tengwa('Anto') # '\ue00c'
ampa = Tengwa('Ampa') # '\ue00d'
anca = Tengwa('Anca') #'\ue00e'
unque = Tengwa('Unque') # '\ue00f'

numen = Tengwa('Numen') # '\ue010'
malta = Tengwa('Malta') #'\ue011'
ngoldo = Tengwa('Ngoldo') # \ue012'
ngwalme = Tengwa('Ngwalme') # '\ue013'

ore = Tengwa('Ore') # '\ue014'
vala = Tengwa('Vala') # '\ue015'
anna = Tengwa('Anna') # '\ue016'
vilya = Tengwa('Vilya') # '\ue017'

romen = Tengwa('Romen') # '\ue020'
arda = Tengwa('Arda') # '\ue021'
lambe = Tengwa('Lambe') # '\ue022'
alda = Tengwa('Alda') # '\ue023'

silme = Tengwa('Silme') # '\ue024'
silme_nuquerna = Tengwa('Silme nuquerna') # '\ue025'
esse = Tengwa('Esse') # '\ue026'
esse_nuquerna = Tengwa('Esse nuquerna') # '\ue027'

hyarmen = Tengwa('Hyarmen') # '\ue028'
hwesta_sindarinwa = Tengwa('Hwesta sindarinwa') # '\ue029'
yanta = Tengwa('Yanta') # '\ue02a'
ure = Tengwa('Ure') # '\ue02b'

short_carrier = Tengwa('Short carrier') # '\ue02e'
long_carrier = Tengwa('Long carrier') # '\ue02d'

the = Tengwa('The') # '\ue01c'

of = Tengwa('Of') # '\ue01d'
of_the = Tengwa('Of the') # '\ue01d\ue051'

aspirated_parma = AspiratedTengwa('Parma') # \ue019' # used for 'ph'

numeral_0 = Numeral('0') # '\ue070'
numeral_1 = Numeral('1') # '\ue071'
numeral_2 = Numeral('2') # '\ue072'
numeral_3 = Numeral('3') # '\ue073'
numeral_4 = Numeral('4') # '\ue074'
numeral_5 = Numeral('5') # '\ue075'
numeral_6 = Numeral('6') # '\ue076'
numeral_7 = Numeral('7') # '\ue077'
numeral_8 = Numeral('8') # '\ue078'
numeral_9 = Numeral('9') # '\ue079'
numeral_a = Numeral('A') # '\ue07a'
numeral_b = Numeral('B') # '\ue07b'
