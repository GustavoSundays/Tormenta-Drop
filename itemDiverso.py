from random import randint

def itemDiverso():
    roll = randint(1, 100)
    if roll <= 5:
        return('Ácido')
    elif roll <= 10:
        return('Água benta')
    elif roll == 11:
       return('Algemas')
    elif roll <= 21:
        return('Balsamo restaurador')
    elif roll <= 26:
        return('Corda')
    elif roll <= 28:
        return('Espelho de metal')
    elif roll <= 33:
        return('Fogo alquímico')
    elif roll == 34:
        return('Granada')
    elif roll <= 36:
        return('Instrumento musical')
    elif roll <= 38:
        return('Kit de artesão')
    elif roll <= 40:
        return('Kit de disfarces')
    elif roll <= 42:
        return('Kit de ladrão')
    elif roll <= 44:
        return('Kit de medicamentos')
    elif roll <= 49:
        return('Lampião')
    elif roll <= 54:
        return('Mochila')
    elif roll <= 59:
        return('Odre')
    elif roll <= 61:
        return('Pé de cabra')
    elif roll <= 66:
        return('Pederneira')
    elif roll <= 68:
        return('Pena')
    elif roll <= 73:
        return('Pergaminho')
    elif roll <= 78:
        return('Ração de viagem')
    elif roll <= 83:
        return('Saco de dormir')
    elif roll <= 85:
        return('Tinta')
    elif roll <= 95:
        return('Tocha')
    elif roll <= 100:
        return('Vara de madeira')