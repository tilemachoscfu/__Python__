Common classical ciphers implemented in Python.
<br>
>>> from pycipher import ADFGVX
>>> adfgvx = ADFGVX(key='PH0QG64MEA1YL2NOFDXKR3CVS5ZW7BJ9UTI8', keyword='GERMAN')
>>> adfgvx.encipher("Hello world!")
'FVFDAGXAFFFFGFAGADFG'
>>> adfgvx.decipher(_)
'HELLOWORLD'
