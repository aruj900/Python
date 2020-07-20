print(bin(10))

n = 0b10
print(n)

def from_base10(n,b):
    if b < 2:
        raise ValueError('Base b must be >=2')
    if n < 0:
        raise ValueError("Number n must be >=0")
    if n == 0:
        return [0]
    
    digits = []
    while n > 0:
        m = n % b
        n = n // b
        n,m = divmod(n,b)
        digits.insert(0,m)
    return digits

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("Digit_map is not long enough to encode the digits")
    encoding = ''
    for d in digits:
        encoding += digit_map[d]
    return encoding

print(encode([15,15],'0123456789ABCDEF'))

def rebase_from10(number,base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    sign = -1 if number < 0 else 1
    number *= sign
    
    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding

e = rebase_from10(3451,16)
print(e)
print(int(e, base=16))
