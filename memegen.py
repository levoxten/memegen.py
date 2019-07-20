import random

# Meme Gen - WOLQC 2019 (c)

memes = ["'Levoxten is a meme' - Levoxten, 2019", 'Oh god please why', 'Just say YES!', 'PETA is a joke', 'End this', 'Doge', 'Dogecoin Cryptocurrency', "'Optic's discord profile picture is a meme' - OpticLight (optislight on github), 2019"]

while 1:
    randomvar = input('Type stuff (or not) then press the "enter" key > ')

    print(f'{random.choice(memes)}')
