Common classical ciphers implemented in Python.
<br>
>>> from pycipher import ADFGVX<br>
>>> adfgvx = ADFGVX(key='PH0QG64MEA1YL2NOFDXKR3CVS5ZW7BJ9UTI8', keyword='GERMAN')<br>
>>> adfgvx.encipher("Hello world!")<br>
'FVFDAGXAFFFFGFAGADFG'<br>
>>> adfgvx.decipher(_)<br>
'HELLOWORLD'<br>
