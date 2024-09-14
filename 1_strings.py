from gtts import gTTS
import os
a = '123PYTHON'.capitalize()
print(a)
print(a.title())

a = 'aB12cb'
print(a.isalnum())

a = '1234'.isalnum()
print(a)

a = 'ABC'.swapcase()
print(a)

a = 'ab@123Bc'.isalnum()
print(a)

a = 'PYTHON'.casefold()
print(a)

a = '1234'.isnumeric()
print(a)

a = '1234'.isdigit()
print(a)

a = 'ababababababab'
print(a.count('a'))
print(a.count('b'))
print(a.count('ab'))
print(a.count('abb'))
print(a.count('abab'))

a = 'abc bca def'
print(a.count(' '))
print(a[0])

a = 'python'
print(a.index('py'))

a = 'Boys are beautiful'
print(a)
print(a.replace('beautiful','Amazing'))
print(a.replace('Boys','Girls'))

a = 'python'
print(','.join(a))
print(len(','.join(a)))

a = 'ABC'.isalpha()
print(a)

a = 'ABC24'.isalpha()
print(a)

a,b,c = 'hi '
print(a,b,c)

a = 'hi'
b = 'hi'
print(id(a),id(b))

a = 'good morning'
b = 'good morning'
print(id(a),id(b))

a,b,c = 'good morning','good morning','good morning'
print(id(a),id(b),id(c))

language = 'en'
a = '''One cup Chai Please!
        Thik hai ye le
        Ayye Bhenchod garam hai garam hai!!'''
        
myobj = gTTS(text=a, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")