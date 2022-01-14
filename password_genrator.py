import random
from time import sleep
from keyboard import press, write
def gen():
    small = "abcdefghijklmnopqrstuvwxyz"
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "1234567890"

    total = small + big + number

    length = 10

    password = "".join(random.sample(total,length))
    password = str(password)
    #print(password)
    return password

def NPG():
    name1  = "fury","hello",'new',"future","advance","project","huge","normal","vegitable","map","stay","boss","fat"
    name2 = "middle","sound","brush","fill","chill","wake","chill","mat","max","close","cake","love","prision"
    symb = "_","$","#","@","&"
    first = random.choice(name1)
    second = random.choice(name2)
    symbol = random.choice(symb)
    new_password  = (f"{first}{symbol}{second}")
    return new_password
