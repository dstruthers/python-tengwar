tinco = '\ue000'
parma = '\ue001'
calma = '\ue002'
quesse = '\ue003'

ando = '\ue004'
umbar = '\ue005'
anga = '\ue006'
ungwe = '\ue007'

thule = '\ue008'
formen = '\ue009'
harma = '\ue00a'
hwesta = '\ue00b'

anto = '\ue00c'
ampa = '\ue00d'
anca = '\ue00e'
unque = '\ue00f'

numen = '\ue010'
malta = '\ue011'
ngoldo = '\ue012'
ngwalme = '\ue013'

ore = '\ue014'
vala = '\ue015'
anna = '\ue016'
vilya = '\ue017'

romen = '\ue020'
arda = '\ue021'
lambe = '\ue022'
alda = '\ue023'

silme = '\ue024'
silme_nuquerna = '\ue025'
esse = '\ue026'
esse_nuquerna = '\ue027'

hyarmen = '\ue028'
hwesta_sindarinwa = '\ue029'
yanta = '\ue02a'
ure = '\ue02b'

short_carrier = '\ue02e'
long_carrier = '\ue02d'

the = '\ue01c'

of = '\ue01d'
of_the = '\ue01d\ue051'

aspirated_parma = '\ue019' # used for 'ph'

numeral_0 = '\ue070'
numeral_1 = '\ue071'
numeral_2 = '\ue072'
numeral_3 = '\ue073'
numeral_4 = '\ue074'
numeral_5 = '\ue075'
numeral_6 = '\ue076'
numeral_7 = '\ue077'
numeral_8 = '\ue078'
numeral_9 = '\ue079'
numeral_a = '\ue07a'
numeral_b = '\ue07b'

def invert(glyph):
    """Convert glyph to inverted variant, if available."""
    if glyph == silme:
        return silme_nuquerna
    elif glyph == esse:
        return esse_nuquerna
    else:
        return glyph
