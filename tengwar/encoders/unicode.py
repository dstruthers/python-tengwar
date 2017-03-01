from bidict import bidict
from functools import reduce

from tengwar.orthography.diacritics import *
from tengwar.orthography.glyphs import *

unicode_mappings = bidict({
    Tinco : '\ue000',
    Parma : '\ue001',
    Calma : '\ue002',
    Quesse : '\ue003',
    Ando : '\ue004',
    Umbar : '\ue005',
    Anga : '\ue006',
    Ungwe : '\ue007',
    Thule : '\ue008',
    Formen : '\ue009',
    Harma : '\ue00a',
    Hwesta : '\ue00b',
    Anto : '\ue00c',
    Ampa : '\ue00d',
    Anca : '\ue00e',
    Unque : '\ue00f',
    Numen : '\ue010',
    Malta : '\ue011',
    Ngoldo : '\ue012',
    Ngwalme : '\ue013',
    Ore : '\ue014',
    Vala : '\ue015',
    Anna : '\ue016',
    Vilya : '\ue017',
    Romen : '\ue020',
    Arda : '\ue021',
    Lambe : '\ue022',
    Alda : '\ue023',
    Silme : '\ue024',
    SilmeNuquerna : '\ue025',
    Esse : '\ue026',
    EsseNuquerna : '\ue027',
    Hyarmen : '\ue028',
    HwestaSindarinwa : '\ue029',
    Yanta : '\ue02a',
    Ure : '\ue02b',
    ShortCarrier : '\ue02e',
    LongCarrier : '\ue02d',
    The : '\ue01c',
    Of : '\ue01d',
#    OfThe : '\ue01d\ue051',
    AspiratedParma : '\ue019',
    Numeral0 : '\ue070',
    Numeral1 : '\ue071',
    Numeral2 : '\ue072',
    Numeral3 : '\ue073',
    Numeral4 : '\ue074',
    Numeral5 : '\ue075',
    Numeral6 : '\ue076',
    Numeral7 : '\ue077',
    Numeral8 : '\ue078',
    Numeral9 : '\ue079',
    NumeralA : '\ue07a',
    NumeralB : '\ue07b',

    # Tehtar
    TripleDot : '\ue040',
    AcuteAccent : '\ue046',
    Overdot : '\ue044',
    Underdot : '\ue045',
    RightCurl : '\ue04a',
    LeftCurl : '\ue04c',
    RightHook : '\ue058',
    LeftHook : '\ue059',
    Overbar : '\ue050',
    Underbar : '\ue051'
})

def encode(tengwar):
    output = ''
    for tengwa in tengwar:
        if isinstance(tengwa, Unknown):
            output += tengwa.value
        else:
            output += unicode_mappings[tengwa.__class__]
            for tehta in tengwa.tehtar:
                output += unicode_mappings[tehta.__class__]
    return output

def decode(chars):
    output = Tengwar()
    for char in chars:
        if char in unicode_mappings.inv:
            output += unicode_mappings.inv[char]()
        else:
            output += Unknown(char)
    return output
