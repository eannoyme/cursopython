#programa de criptografia

import random
import hashlib

c = random.randint(1,99999)
senha=input(" digite sua senha: ")
s = senha + str(c)
criptografado = hashlib.sha512( str( s ).encode("utf-8") ).hexdigest()

print(" sua senha criptografada é : ")
print(criptografado)