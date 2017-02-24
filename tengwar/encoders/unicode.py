from tengwar.orthography.diacritics import *
from tengwar.orthography.glyphs import *

unicode_mappings = {
    tinco.name : '\ue000',
    parma.name : '\ue001',
    calma.name : '\ue002',
    quesse.name : '\ue003',
    ando.name : '\ue004',
    umbar.name : '\ue005',
    anga.name : '\ue006',
    ungwe.name : '\ue007',
    thule.name : '\ue008',
    formen.name : '\ue009',
    harma.name : '\ue00a',
    hwesta.name : '\ue00b',
    anto.name : '\ue00c',
    ampa.name : '\ue00d',
    anca.name : '\ue00e',
    unque.name : '\ue00f',
    numen.name : '\ue010',
    malta.name : '\ue011',
    ngoldo.name : '\ue012',
    ngwalme.name : '\ue013',
    ore.name : '\ue014',
    vala.name : '\ue015',
    anna.name : '\ue016',
    vilya.name : '\ue017',
    romen.name : '\ue020',
    arda.name : '\ue021',
    lambe.name : '\ue022',
    alda.name : '\ue023',
    silme.name : '\ue024',
    silme_nuquerna.name : '\ue025',
    esse.name : '\ue026',
    esse_nuquerna.name : '\ue027',
    hyarmen.name : '\ue028',
    hwesta_sindarinwa.name : '\ue029',
    yanta.name : '\ue02a',
    ure.name : '\ue02b',
    short_carrier.name : '\ue02e',
    long_carrier.name : '\ue02d',
    the.name : '\ue01c',
    of.name : '\ue01d',
    of_the.name : '\ue01d\ue051',
    aspirated_parma.name : '\ue019', # used for 'ph'
    numeral_0.name : '\ue070',
    numeral_1.name : '\ue071',
    numeral_2.name : '\ue072',
    numeral_3.name : '\ue073',
    numeral_4.name : '\ue074',
    numeral_5.name : '\ue075',
    numeral_6.name : '\ue076',
    numeral_7.name : '\ue077',
    numeral_8.name : '\ue078',
    numeral_9.name : '\ue079',
    numeral_a.name : '\ue07a',
    numeral_b.name : '\ue07b',

    # Tehtar
    triple_dot.name : '\ue040',
    acute_accent.name : '\ue046',
    overdot.name : '\ue044',
    underdot.name : '\ue045',
    right_curl.name : '\ue04a',
    left_curl.name : '\ue04c',
    right_hook.name : '\ue058',
    left_hook.name : '\ue059',
    overbar.name : '\ue0050',
    underbar.name : '\ue051'
}

def encode_tengwa(tengwa):
    if isinstance(tengwa, Unknown):
        return tengwa.value
    else:
        return (unicode_mappings[tengwa.name]
                + ''.join([unicode_mappings[t.name] for t in tengwa.tehtar]))

def encode(tengwar):
    return ''.join(map(encode_tengwa, tengwar.tengwar))
