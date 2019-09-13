from random import randint

def materialEspecial():
    roll = randint(1, 100)
    if roll <= 10:
        return('Aço-rubi')
    elif roll <= 25:
        return('Adamante')
    elif roll <= 45:
        return('Gelo eterno')
    elif roll <= 70:
        return('Madeira tollon')
    elif roll <= 80:
        return('Matéria vermelha')
    elif roll <= 100:
        return('Mitral')