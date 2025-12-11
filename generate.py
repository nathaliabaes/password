import string
import random

def gerar_password(qnt, use_upper=True, use_lower=True, use_number=True, use_special=True):

    chars = ""

    if use_upper:
        chars += string.ascii_uppercase
    
    if use_lower:
        chars += string.ascii_lowercase
    
    if use_number:
        chars += string.digits
    
    if use_special:
        chars += string.punctuation

    if not chars:
        return "" 

    return ''.join(random.choice(chars) for _ in range(qnt))
