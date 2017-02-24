from tengwar.orthography import diacritics, glyphs
from parsing import *

from tengwar.misc.helpers import base12, many1, mapping

__all__ = ['transliterate']
__author__ = 'Darren M. Struthers <dstruthers@gmail.com>'
__version__ = 'dev'

# Tengwar Transliterator
# ----------------------
#
# This file defines an algorithm for transliterating English text into the
# Tengwar script, using what is known as the Common Mode. [X]
#
# The algorithm is built on a combinatorial parsing framework, which allows
# transliteration rules to be defined as individual functions, which are later
# combined together to form a complete transliteration function.

# To begin, we will create some very basic parsers which are needed throughout
# the code. `boundary` identifies portions of the input text, such as spaces and
# punctuation characters, which do not need to undergo transliteration. `vowel`
# simply identifies vowel characters. We define it here, rather than in the
# Vowels section below, because vowel identification is needed for special
# considerations given to the transliteration of the letter <R> (the "R Rule"
# [X]). For the purposes of the algorithm, the semi-vowel <Y> is always treated
# as a consonant.

boundary = many1(word_boundary) | eof
vowel = one_of('aeiou')

# Consonants
# ----------
#
# The word "tengwar" is Quenya for "letters" (the singular form is "tengwa"). In
# most Tengwar modes, including the Common Mode, consonant sounds are rendered
# using tengwar, while vowel sounds are indicated with diacritics ("tehtar").

# Many sounds that are rendered by two letters in English, such as <CH>, <TH>,
# etc., can be rendered with a single tengwa. They are defined here. <QU> is
# treated differently, but we include it here alongside the other digraphs for
# convenience.

digraph = ( mapping('ch', glyphs.calma)
          | mapping('gh', glyphs.unque)
          | mapping('ng', glyphs.ngwalme)
          | mapping('ph', glyphs.aspirated_parma)
          | mapping('qu', glyphs.quesse + glyphs.vala)
          | mapping('sh', glyphs.harma)
          | mapping('th', glyphs.thule)
          | mapping('wh', glyphs.hwesta_sindarinwa)
)

# The `mapping` function accepts a `Parser` (or other type such as a `str` which
# can be coerced to a `Parser` instance) as its first argument, and the
# corresponding transliteration output as its second argument. The overloaded
# `|` operator from the `parsing` library joins `Parser` operands into a set
# of alternatives which are attempted in order until one `Parser` succeeds in
# processing some input. Therefore we can use the pattern seen above and 
# elsewhere of combining transliteration mappings into a list for the algorithm
# to attempt, in order.

# Here are mappings for single consonants. Some consonants, such as <S> and <R>,
# which have more than one possible tengwa equivalent, will require more
# attention to get right, but they are included in this simple list of consonant
# mappings with a good default tengwa, serving as a fallback if the algorithm
# cannot choose a more suitable alternative based on context. This is explained
# in more detail below.

consonant = ( mapping('b', glyphs.umbar)
            | mapping('c', glyphs.quesse)
            | mapping('d', glyphs.ando)
            | mapping('f', glyphs.formen)
            | mapping('g', glyphs.ungwe)
            | mapping('h', glyphs.hyarmen)
            | mapping('j', glyphs.anga)
            | mapping('k', glyphs.quesse)
            | mapping('l', glyphs.lambe)
            | mapping('m', glyphs.malta)
            | mapping('n', glyphs.numen)
            | mapping('p', glyphs.parma)
            | mapping('q', glyphs.quesse)
            | mapping('r', glyphs.ore)
            | mapping('s', glyphs.silme)
            | mapping('t', glyphs.tinco)
            | mapping('v', glyphs.ampa)
            | mapping('w', glyphs.vala)
            | mapping('x', glyphs.quesse + diacritics.left_hook)
            | mapping('y', glyphs.anna)
            | mapping('z', glyphs.esse)
)

# The Common Mode employs an underbar tehta to indicate that a consonant is to
# be doubled, so we define a parser to identify double consonants in the input
# text, and provide the corresponding tengwa with the underbar attached.

@parser
def double_consonant(input):
    c = input.match(consonant)
    input.match(c.matched)
    return c + diacritics.underbar

# When a double consonant and a digraph occur at the same time (<CCH>, <SSH>,
# etc.), we want the digraph pattern to take precedence, so we will define a
# special parser for this situation and cause it to consume the first character
# of input, saving the subsequent digraph for the next round of parsing. This
# parser is easy to create by taking advantage of the `peek` combinator, which
# forces a match for its provided `Parser` instance, but does not actually use
# the parser to consume input. Therefore, we can `peek` multiple times, testing
# multiple patterns.

@parser
def consonant_before_its_digraph(input):
    c = input.match(consonant)
    input.match(peek(c.matched))
    input.match(peek(digraph))
    return c

digraph_patterns = consonant_before_its_digraph | digraph

# When the <M> or <N> sound occurs before a consonant, the tengwa for these
# sounds is omitted and an overbar added to the following tengwa.

@parser
def m_n_patterns(input):
    mn = input.match(one_of(['m', 'n']))
    c = input.match(digraph | double_consonant | consonant)
    return c + diacritics.overbar

# Most Tengwar modes, including the Common Mode, obey what is known as the "R
# Rule", which dictates that the tengwa <ore> is to be used to render the <R>
# sound before consonants, and <romen> to be used before vowels. We take
# advantage of the `peek` combinator from the `parsing` library in order to
# confirm a match of the `vowel` parser without processing any input.
    
@parser
def r_before_vowel(input):
    input.match('r' + peek(vowel))
    return glyphs.romen

# We also treat the case of a <RR> followed by a vowel separately, to guarantee
# that the algorithm correctly outputs a single <Romen> tengwa with an underbar
# to indicate the doubling. Otherwise, the algorithm would likely output an
# <Ore> followed by a <Romen> in this situation, which is incorrect.

@parser
def double_r_before_vowel(input):
    input.match('r')
    input.match(r_before_vowel)
    return glyphs.romen + diacritics.underbar

# The exception to the R Rule is when the vowel followed by <R> is at the end of
# the word and should be represented with the underdot tehta. We will define a
# parser for this situation and prioritize it above the other R Rule parsers.

@parser
def r_before_final_e(input):
    input.match('re' + peek(boundary))
    return glyphs.ore + diacritics.underdot

r_patterns = r_before_final_e | r_before_vowel | double_r_before_vowel

# When <S> occurs at the end of a word and is immediately following a consonant
# sound, a hook tehta is attached to that preceding consonant tengwa.

@parser
def final_s_after_consonant(input):
    c = input.match(digraph | m_n_patterns | double_consonant | consonant)
    input.match('s')
    peek(boundary)(input)
    return c + diacritics.right_hook

# However, in the case of a word ending in <SS>, we do not use this hook
# convention, so we force the output of a <Silme> with an underbar in this
# situation.

@parser
def final_double_s(input):
    input.match('ss' + peek(boundary))
    return glyphs.silme + diacritics.underbar

s_patterns = final_double_s | final_s_after_consonant

# Now we can combine each of the patterns above into a single parser which is
# capable of transliterating consonants, with attention given to context in
# order to guarantee that the best possible tengwa is always produced.

consonant_patterns = ( digraph_patterns
                     | m_n_patterns
                     | r_patterns
                     | s_patterns
                     | double_consonant
                     | consonant
)

# Vowels
# ------
#
# Vowels are represented by tehtar placed above the tengwa the vowel precedes.
# Therefore, this Tengwar mode is read from left to right, and from up to down
# when tehtar are present.

def vowel_tehta(vowel):
    """Return tehta (diacritic) corresponding to the specified vowel."""
    return { 'a': diacritics.triple_dot
           , 'e': diacritics.acute_accent
           , 'i': diacritics.overdot
           , 'o': diacritics.right_curl
           , 'u': diacritics.left_curl
         }[vowel[0].lower()]

@parser
def vowel_before_consonants(input):
    v = input.match(vowel)
    c = input.match(consonant_patterns)
    return c + vowel_tehta(v)

# In the case of a doubled vowel, we place the corresponding tehta above the
# "long carrier" glyph.

@parser
def double_vowel(input):
    v = input.match(vowel)
    input.match(v)
    return glyphs.long_carrier + vowel_tehta(v)

# The tengwar for <S> and <Z> (<Silme> and <Esse>, respectively) each have two
# variants, to be used at the composer's discretion. We will opt for the
# inverted variants (<Silme nuquerna> and <Esse nuquerna>) when we need to place
# tehtar above these tengwar.

@parser
def vowel_before_s(input):
    v = input.match(vowel)
    c = input.match('s')
    input.match(peek(boundary | not_('h')))
    return glyphs.silme_nuquerna + vowel_tehta(v)

@parser
def vowel_before_double_s(input):
    v = input.match(vowel)
    input.match('ss')
    return glyphs.silme_nuquerna + diacritics.underbar + vowel_tehta(v)

@parser
def vowel_before_z(input):
    v = input.match(vowel)
    input.match('z')
    return glyphs.esse_nuquerna + vowel_tehta(v)

@parser
def vowel_before_double_z(input):
    v = input.match(vowel)
    input.match('zz')
    return glyphs.esse_nuquerna + diacritics.underbar + vowel_tehta(v)

vowel_before_s_or_z = ( vowel_before_double_s
                      | vowel_before_s
                      | vowel_before_double_z
                      | vowel_before_z
)

# When a vowel occurs at the end of a word, there is no subsequent tengwa over
# which to place the vowel tehta, so we add a "short carrier" glyph for it.

@parser
def final_vowel(input):
    v = input.match(vowel)
    input.match(peek(boundary))
    return glyphs.short_carrier + vowel_tehta(v)

# When a word ends in a final <E> preceded by a consonant, an underdot is added
# to that consonant's tengwa.

@parser
def final_e_after_consonant(input):
    c = input.match(consonant_patterns)
    input.match('e' + peek(boundary))
    return c + diacritics.underdot

@parser
def vowel_before_consonant_final_e(input):
    v = input.match(vowel)
    c = input.match(final_e_after_consonant)
    return c + vowel_tehta(v)

# The Tengwar provides special glyphs for rendering diphthongs. In the Common
# Mode, <Yanta> is used for i-glide diphthongs, and <Ure> is used for u-glide
# diphthongs.

@parser
def i_glide_diphthong(input):
    v = input.match(vowel)
    input.match('i')
    return glyphs.yanta + vowel_tehta(v)

@parser
def u_glide_diphthong(input):
    v = input.match(vowel)
    input.match('u')
    return glyphs.ure + vowel_tehta(v)

diphthong = i_glide_diphthong | u_glide_diphthong

@parser
def single_vowel(input):
    v = input.match(vowel)
    return glyphs.short_carrier + vowel_tehta(v)

# Having defined each case that needs to be considered to render vowels, we can
# now combine them all together into one parser.

vowel_patterns = ( diphthong
                 | double_vowel
                 | vowel_before_s_or_z
                 | vowel_before_consonant_final_e
                 | vowel_before_consonants
                 | final_e_after_consonant
                 | final_vowel
                 | single_vowel
)

# Numbers
# -------
#
# Tengwar traditionally uses a duodecimal system, and therefore has twelve
# numeral glyphs.

numeral = ( mapping('0', glyphs.numeral_0)
          | mapping('1', glyphs.numeral_1)
          | mapping('2', glyphs.numeral_2)
          | mapping('3', glyphs.numeral_3)
          | mapping('4', glyphs.numeral_4)
          | mapping('5', glyphs.numeral_5)
          | mapping('6', glyphs.numeral_6)
          | mapping('7', glyphs.numeral_7)
          | mapping('8', glyphs.numeral_8)
          | mapping('9', glyphs.numeral_9)
          | mapping('a', glyphs.numeral_a)
          | mapping('b', glyphs.numeral_b)
)

# The parser above maps duodecimal digits, but we should expect the input to be
# in base 10. So We define a parser that reads in base 10 digits, converts them
# to base 12, and then passes that result to the numeral transliterator above.

number = many1(digit) >> int >> base12 >> many(numeral)

# Special Forms
# -------------
#
# Tengwar has special glyphs for the common words, <OF>, <THE>, and <OF THE>.

special_form = ( mapping('of', glyphs.of)
               | mapping('of the', glyphs.of_the)
               | mapping('the', glyphs.the)
) + peek(boundary)

# Let any unrecognizable input pass through

passthrough = char >> glyphs.Unknown

# Plug it all together
word = many1(vowel_patterns | consonant_patterns)
term = special_form | word | number
        
transliterate = str.lower >> many(term | passthrough)
