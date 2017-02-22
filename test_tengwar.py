from tengwar import transliterate
from glyphs import *
from diacritics import *

def test_digraphs():
    assert(transliterate('chi') == calma + short_carrier + overdot)
    assert(transliterate('ugh') == unque + left_curl)
    assert(transliterate('bang') == umbar + ngwalme + triple_dot)
    assert(transliterate('phat') == aspirated_parma + tinco + triple_dot)
    assert(transliterate('quid') == quesse + vala + ando + overdot)
    assert(transliterate('ash') == harma + triple_dot)
    assert(transliterate('eth') == thule + acute_accent)
    assert(transliterate('why') == hwesta_sindarinwa + anna)
    assert(transliterate('ssh') == silme + harma)
    
def test_consonants():
    assert(transliterate('cab') == quesse + umbar + triple_dot)
    assert(transliterate('def') == ando + formen + acute_accent)
    assert(transliterate('hug') == hyarmen + ungwe + left_curl)
    assert(transliterate('jam') == anga + malta + triple_dot)
    assert(transliterate('kit') == quesse + tinco + overdot)
    assert(transliterate('lol') == lambe + lambe + right_curl)
    assert(transliterate('nor') == numen + ore + right_curl)
    assert(transliterate('pip') == parma + parma + overdot)
    assert(transliterate('qi') == quesse + short_carrier + overdot)
    assert(transliterate('sic') == silme + quesse + overdot)
    assert(transliterate('vis') == ampa + silme_nuquerna + overdot)
    # TODO: investigate whether -x should end in right hook
    assert(transliterate('wax') == vala + quesse + left_hook + triple_dot)
    assert(transliterate('yam') == anna + malta + triple_dot)
    assert(transliterate('zen') == esse + numen + acute_accent)
    
def test_double_consonant():
    assert(transliterate('ebb') == umbar + underbar + acute_accent)

def test_m():
    assert(transliterate('mom') == malta + malta + right_curl)
    assert(transliterate('amp') == parma + overbar + triple_dot)

def test_n():
    assert(transliterate('and') == ando + overbar + triple_dot)
    assert(transliterate('net') == numen + tinco + acute_accent)
    assert(transliterate('ent') == tinco + overbar + acute_accent)
    
def test_r():
    assert(transliterate('are') == ore + underdot + triple_dot)
    assert(transliterate('art') == ore + triple_dot + tinco)
    assert(transliterate('red') == romen + ando + acute_accent)
    assert(transliterate('err') == ore + underbar + acute_accent)
    assert(transliterate('erred') == romen + underbar + acute_accent + ando
           + acute_accent)
    assert(transliterate('mirror') == malta + romen + underbar + overdot + ore
           + right_curl)

def test_s():
    assert(transliterate('so') == silme + short_carrier + right_curl)
    assert(transliterate('is') == silme_nuquerna + overdot)
    assert(transliterate('its') == tinco + right_hook + overdot)
    assert(transliterate('miss') == malta + silme_nuquerna + underbar + overdot)

def test_vowel_before_consonant():
    assert(transliterate('et') == tinco + acute_accent)

def test_double_vowel():
    assert(transliterate('boo') == umbar + long_carrier + right_curl)

def test_vowel_before_s():
    assert(transliterate('as') == silme_nuquerna + triple_dot)

def test_vowel_before_double_s():
    assert(transliterate('ass') == silme_nuquerna + underbar + triple_dot)

def test_vowel_before_z():
    assert(transliterate('jazz') == anga + esse_nuquerna + underbar + triple_dot)
    assert(transliterate('paz') == parma + esse_nuquerna + triple_dot)

def test_final_vowel():
    assert(transliterate('so') == silme + short_carrier + right_curl)

def test_final_e_after_consonant():
    assert(transliterate('ate') == tinco + underdot + triple_dot)
    assert(transliterate('axe') == quesse + left_hook + underdot + triple_dot)
    
def test_diphthongs():
    assert(transliterate('aim') == yanta + triple_dot + malta)
    assert(transliterate('out') == ure + right_curl + tinco)

def test_tricky_words():
    assert(transliterate('aether') == short_carrier + triple_dot + thule
           + acute_accent + ore + acute_accent)
    assert(transliterate('assess') == silme_nuquerna + underbar + triple_dot
           + silme_nuquerna + underbar + acute_accent)
    assert(transliterate('government') == ungwe + ampa + right_curl + ore
           + acute_accent + malta + overbar + tinco + overbar + acute_accent)
    assert(transliterate('mnemonic') == numen + overbar + malta + acute_accent
           + numen + right_curl + quesse + overdot)
    assert(transliterate('pizzazz') == parma + esse_nuquerna + underbar
           + overdot + esse_nuquerna + underbar + triple_dot)
    assert(transliterate('schadenfreude') == silme + calma + ando + triple_dot
           + formen + overbar + acute_accent + romen + ure + acute_accent
           + ando + underdot)
    assert(transliterate('yttrium') == anna + tinco + underbar + romen + ure
           + overdot + malta)

def test_numbers():
    assert(transliterate('9') == numeral_9)
    assert(transliterate('10') == numeral_a)
    assert(transliterate('11') == numeral_b)
    assert(transliterate('12') == numeral_1 + numeral_0)
    assert(transliterate('100') == numeral_8 + numeral_4)
    assert(transliterate('1000') == numeral_6 + numeral_b + numeral_4)
