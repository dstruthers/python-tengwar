from tengwar.modes import common
from tengwar.encoders import unicode

class Transliterator(object):
    def __init__(self, mode, encoder):
        self.mode = mode
        self.encoder = encoder

    def transliterate(self, src):
        return self.encoder.encode(self.mode.transliterate(src))

_default_transliterator = Transliterator(common, unicode)

def transliterate(src):
    return _default_transliterator.transliterate(src)
