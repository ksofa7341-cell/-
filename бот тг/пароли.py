import random

def pp(voproc):


    ps="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
     
    passford=""
    for i in range(voproc):
        s=random.choice(ps)
        passford+=s
    return passford

pp(5)