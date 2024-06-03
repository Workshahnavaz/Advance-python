# import qrcode 

# x = qrcode.make("https://packaging.python.org/en/latest/tutorials/installing-packages/")

# x.save("1.png")



# import segno

# x = segno.make_qr("https://www.python.org/")

# x.save("2.png")

# import pywhatkit

# x = pywhatkit.open_web()

# import pywhatkit

# x = pywhatkit.search("https://www.geeksforgeeks.org/introduction-to-pywhatkit-module/?ref=gcse")

# import pywhatkit

# x = pywhatkit.info()


def info(topic,lines=3):
    '''Gives information on a topic from wikipedia.'''
    spe = wikipedia.summary(topic, sentences = lines)
    print(spe)

output = wikipedia.summary(search, sentences=15)
>>> from contextlib import redirect_stdout
>>> from io import StringIO
>>> 
 buffer = StringIO()
with redirect_stdout(buffer):
...     pywhatkit.info(search, lines=15)
... 
buffer.getvalue()
Output will appear here>