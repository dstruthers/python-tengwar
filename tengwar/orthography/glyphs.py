from tengwar.orthography.diacritics import Tehta

class Tengwa():
    def __init__(self, tehtar=[]):
        self.tehtar = set(tehtar)
        self._iterated = False

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
            return self.__class__(self.tehtar | set([other]))
        elif isinstance(other, Tengwar):
            return Tengwar([self] + other.tengwar)
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Tengwa):
            return self.name == other.name and self.tehtar == other.tehtar

    def __iter__(self):
        self._iterated = False
        return self

    def __next__(self):
        if self._iterated:
            raise StopIteration
        else:
            self._iterated = True
            return self
        

class Tinco(Tengwa): name = 'Tinco'
class Parma(Tengwa): name = 'Parma'
class Calma(Tengwa): name = 'Calma'
class Quesse(Tengwa): name = 'Quesse'

class Ando(Tengwa): name = 'Ando'
class Umbar(Tengwa): name = 'Umbar'
class Anga(Tengwa): name = 'Anga'
class Ungwe(Tengwa): name = 'Ungwe'

class Thule(Tengwa): name = 'Thule'
class Formen(Tengwa): name = 'Formen'
class Harma(Tengwa): name = 'Harma'
class Hwesta(Tengwa): name = 'Hwesta'

class Anto(Tengwa): name = 'Anto'
class Ampa(Tengwa): name = 'Ampa'
class Anca(Tengwa): name = 'Anca'
class Unque(Tengwa): name = 'Unque'

class Numen(Tengwa): name = 'Numen'
class Malta(Tengwa): name = 'Malta'
class Ngoldo(Tengwa): name = 'Ngoldo'
class Ngwalme(Tengwa): name = 'Ngwalme'

class Ore(Tengwa): name = 'Ore'
class Vala(Tengwa): name = 'Vala'
class Anna(Tengwa): name = 'Anna'
class Vilya(Tengwa): name = 'Vilya'

class Romen(Tengwa): name = 'Romen'
class Arda(Tengwa): name = 'Arda'
class Lambe(Tengwa): name = 'Lambe'
class Alda(Tengwa): name = 'Alda'

class Silme(Tengwa): name = 'Silme'
class SilmeNuquerna(Tengwa): name = 'Silme nuquerna'
class Esse(Tengwa): name = 'Esse'
class EsseNuquerna(Tengwa): name = 'Esse nuquerna'

class Hyarmen(Tengwa): name = 'Hyarmen'
class HwestaSindarinwa(Tengwa): name = 'Hwesta sindarinwa'
class Yanta(Tengwa): name = 'Yanta'
class Ure(Tengwa): name = 'Ure'

class ShortCarrier(Tengwa): name = 'Short carrier'
class LongCarrier(Tengwa): name = 'Long carrier'
class The(Tengwa): name = 'The'
class Of(Tengwa): name = 'Of'
class OfThe(Tengwa): name = 'Of The'
class AspiratedParma(Tengwa): name = 'Parma with long stem'

class Numeral0(Tengwa): name = 'Numeral 0'
class Numeral1(Tengwa): name = 'Numeral 1'
class Numeral2(Tengwa): name = 'Numeral 2'
class Numeral3(Tengwa): name = 'Numeral 3'
class Numeral4(Tengwa): name = 'Numeral 4'
class Numeral5(Tengwa): name = 'Numeral 5'
class Numeral6(Tengwa): name = 'Numeral 6'
class Numeral7(Tengwa): name = 'Numeral 7'
class Numeral8(Tengwa): name = 'Numeral 8'
class Numeral9(Tengwa): name = 'Numeral 9'
class NumeralA(Tengwa): name = 'Numeral A'
class NumeralB(Tengwa): name = 'Numeral B'

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
        self._iter_index = 0

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

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index < len(self.tengwar):
            self._iter_index += 1
            return self.tengwar[self._iter_index - 1]
        else:
            raise StopIteration

    def __radd__(self, other):
        if isinstance(other, Tengwa):
            return Tengwar([other] + self.tengwar)
        else:
            raise TypeError

tinco = Tinco()
parma = Parma()
calma = Calma()
quesse = Quesse()

ando = Ando()
umbar = Umbar()
anga = Anga()
ungwe = Ungwe()

thule = Thule()
formen = Formen()
harma = Harma()
hwesta = Hwesta()

anto = Anto()
ampa = Ampa()
anca = Anca()
unque = Unque()

numen = Numen()
malta = Malta()
ngoldo = Ngoldo()
ngwalme = Ngwalme()

ore = Ore()
vala = Vala()
anna = Anna()
vilya = Vilya()

romen = Romen()
arda = Arda()
lambe = Lambe()
alda = Alda()

silme = Silme()
silme_nuquerna = SilmeNuquerna()
esse = Esse()
esse_nuquerna = EsseNuquerna()

hyarmen = Hyarmen()
hwesta_sindarinwa = HwestaSindarinwa()
yanta = Yanta()
ure = Ure()

short_carrier = ShortCarrier()
long_carrier = LongCarrier()

the = The()

of = Of()
of_the = OfThe()

aspirated_parma = AspiratedParma()

numeral_0 = Numeral0()
numeral_1 = Numeral1()
numeral_2 = Numeral2()
numeral_3 = Numeral3()
numeral_4 = Numeral4()
numeral_5 = Numeral5()
numeral_6 = Numeral6()
numeral_7 = Numeral7()
numeral_8 = Numeral8()
numeral_9 = Numeral9()
numeral_a = NumeralA()
numeral_b = NumeralB()
