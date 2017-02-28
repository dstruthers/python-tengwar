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
    OfThe : '\ue01d\ue051',
    AspiratedParma : '\ue019', # used for 'ph'
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
    Overbar : '\ue0050',
    Underbar : '\ue051'
})

def encode_tengwa(tengwa):
    if isinstance(tengwa, Unknown):
        return tengwa.value
    else:
        return (unicode_mappings[tengwa.__class__]
                + ''.join([unicode_mappings[t.__class__] for t in tengwa.tehtar]))

def decode_tengwa(char):
    if char in unicode_mappings.inv:
        return unicode_mappings.inv[char]()
    else:
        return Unknown(char)
    
def encode(tengwar):
    #return ''.join(map(encode_tengwa, tengwar.tengwar))
    return ''.join([encode_tengwa(t) for t in tengwar])

def decode(chars):
    return reduce(lambda x, y: x + y, map(decode_tengwa, chars))
    #return reduce(lambda x, y: x + y, [decode_tengwa(c) for c in chars])
