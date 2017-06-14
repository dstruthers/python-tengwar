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
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Tengwa):
            return type(self) == type(other) and self.tehtar == other.tehtar

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
class Quesse(Tengwa): name = 'Quessë'

class Ando(Tengwa): name = 'Ando'
class Umbar(Tengwa): name = 'Umbar'
class Anga(Tengwa): name = 'Anga'
class Ungwe(Tengwa): name = 'Ungwë'

class Thule(Tengwa): name = 'Thúlë'
class Formen(Tengwa): name = 'Formen'
class Harma(Tengwa): name = 'Harma'
class Hwesta(Tengwa): name = 'Hwesta'

class Anto(Tengwa): name = 'Anto'
class Ampa(Tengwa): name = 'Ampa'
class Anca(Tengwa): name = 'Anca'
class Unque(Tengwa): name = 'Unquë'

class Numen(Tengwa): name = 'Numen'
class Malta(Tengwa): name = 'Malta'
class Ngoldo(Tengwa): name = 'Ngoldo'
class Ngwalme(Tengwa): name = 'Ngwalmë'

class Ore(Tengwa): name = 'Órë'
class Vala(Tengwa): name = 'Vala'
class Anna(Tengwa): name = 'Anna'
class Vilya(Tengwa): name = 'Vilya'

class Romen(Tengwa): name = 'Rómen'
class Arda(Tengwa): name = 'Arda'
class Lambe(Tengwa): name = 'Lambë'
class Alda(Tengwa): name = 'Alda'

class Silme(Tengwa): name = 'Silmë'
class SilmeNuquerna(Tengwa): name = 'Silmë nuquerna'
class Esse(Tengwa): name = 'Essë'
class EsseNuquerna(Tengwa): name = 'Essë nuquerna'

class Hyarmen(Tengwa): name = 'Hyarmen'
class HwestaSindarinwa(Tengwa): name = 'Hwesta sindarinwa'
class Yanta(Tengwa): name = 'Yanta'
class Ure(Tengwa): name = 'Úrë'

class ShortCarrier(Tengwa): name = 'Short carrier'
class LongCarrier(Tengwa): name = 'Long carrier'
class The(Tengwa): name = 'The'
class Of(Tengwa): name = 'Of'
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

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.value == other.value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return self.value

class Tengwar(object):
    """List of Tengwa instances"""
    def __init__(self, tengwar=[]):
        self.tengwar = tengwar
        self._iter_index = 0

    def __eq__(self, other):
        if isinstance(other, Tengwar):
            return self.tengwar == other.tengwar
        elif isinstance(other, Tengwa):
            return self.tengwar == [other]

    def __repr__(self):
        return ''.join([str(tengwa) for tengwa in self.tengwar])

    def __add__(self, other):
        if isinstance(other, Tengwar):
            return Tengwar(self.tengwar + other.tengwar)
        elif isinstance(other, Tengwa):
            return Tengwar(self.tengwar + [other])
        elif isinstance(other, Tehta):
            if len(self.tengwar):
                self.tengwar[-1] += other
            else:
                self.tengwar = [ShortCarrier(), other]
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
