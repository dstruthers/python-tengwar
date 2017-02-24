from parsing import *

def base12(n):
    digits = '0123456789ab'
    result = ''
    while n >= 12:
        result = digits[n % 12] + result
        n //= 12
        
    result = digits[n] + result
    return result

def mapping(pattern, output):
    @parser
    def mapping_implementation(input):
        input.match(Parser.coerce(pattern))
        return output
    return mapping_implementation

def many1(parser):
    return many(parser, at_least=1)
