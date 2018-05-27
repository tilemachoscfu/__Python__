# Atbash cipher
from pycipher import Atbash 
encipher = Atbash().encipher('defend the walls')
decipher = Atbash().decipher(encipher)
print(encipher,decipher)

# Rot13
from pycipher import Rot13
encipher = Rot13().encipher('defend the walls')
decipher = Rot13().decipher(encipher)
print(encipher,decipher)

# Caesar cipher 
from pycipher import Caesar
encipher = Caesar(key = 3).encipher('defend the walls')
decipher = Caesar(key = 3).decipher(encipher)
print(encipher,decipher)

# Affine cipher 
from pycipher import Affine
encipher = Affine(a=5, b=9).encipher('defend the walls')
decipher = Affine(a=5, b=9).decipher(encipher)
print(encipher,decipher)

# Polybius Square
from pycipher import PolybiusSquare
p = PolybiusSquare('phqgiumeaylnofdxkrcvstzwb', 5, 'ABCDE')
encipher = p.encipher('defend the walls')
decipher = p.decipher(encipher)
print(encipher,decipher)

# Substitution cipher
from pycipher import SimpleSubstitution
ss = SimpleSubstitution('phqgiumeaylnofdxjkrcvstzwb')
encipher = ss.encipher('defend the walls')
decipher = ss.decipher(encipher)
print(encipher,decipher)

# Columnar Transposition
from pycipher import ColTrans
encipher = ColTrans("KEY").encipher('defend the walls')
decipher = ColTrans("KEY").decipher(encipher)
print(encipher,decipher)