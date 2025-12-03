import string
import random

def gerar_password(qnt):    
    chars = string.ascii_letters + string.digits + string.punctuation
    password = []
    for i in range(qnt):
        ch = random.choice(chars)
        password.append(ch) 

    return ''.join(password)

password = gerar_password(8)
