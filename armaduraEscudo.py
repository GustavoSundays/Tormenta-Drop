from random import randint

def armaduraEscudo():
    roll = randint(1, 100)
    if roll == 1:
        return('Armadura acolchoada')
    elif roll <= 16:
        return('Armadura completa')
    elif roll <= 18:
        return('Brunea')
    elif roll <= 28:
        return('Camisa de cota de malha')
    elif roll <= 33:
        return('Corselete de couro')
    elif roll <= 43:
        return('Cota de malha')
    elif roll <= 45:
        return('Cota de talas')
    elif roll <= 55:
        return('Couraça')
    elif roll <= 65:
        return('Couro batida')
    elif roll <= 75:
        return('Escudo leve')
    elif roll <= 85:
        return('Escudo pesado')
    elif roll <= 90:
        return('Gibão de peles')
    elif roll <= 95:
        return('Loriga segmentada')
    elif roll <= 100:
        return('Meia armadura')