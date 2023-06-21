#criptiografa qr code

import qrcode

e=input("digite seu indereço: ")
img = qrcode.make(e)
img.save("some_file.png")
