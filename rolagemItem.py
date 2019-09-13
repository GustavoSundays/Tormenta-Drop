from random import randint
from itemDiverso import itemDiverso
from arma import arma
from armaduraEscudo import armaduraEscudo
from materialEspecial import materialEspecial

def rolagemItem1():
    roll = randint(1, 100)
    if roll <= 50:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 75:
        item = itemDiverso()
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 95:
        item = arma()
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = armaduraEscudo()
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem2():
    roll = randint(1, 100)
    if roll <= 45:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 70:
        item = itemDiverso()
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 90:
        item = arma()
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = armaduraEscudo()
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem3():
    roll = randint(1, 100)
    if roll <= 40:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 65:
        item = itemDiverso()
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 90:
        item = arma()
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = armaduraEscudo()
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem4():
    roll = randint(1, 100)
    if roll <= 30:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 70:
        item = arma()
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 95:
        item = armaduraEscudo()
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = arma()
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem5():
    roll = randint(1, 100)
    if roll <= 25:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 60:
        item = armaduraEscudo()
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 90:
        item = arma()
        return(f'Item: {item} +1  (roll = {roll}) \n')
    elif roll <= 100:
        item = armaduraEscudo()
        return(f'Item: {item} +1 (roll = {roll}) \n')

def rolagemItem6():
    roll = randint(1, 100)
    if roll <= 25:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 65:
        item = arma()
        return(f'Item: {item} +1 (roll = {roll}) \n')
    elif roll <= 95:
        item = armaduraEscudo()
        return(f'Item: {item} +1 (roll = {roll}) \n')
    elif roll <= 100:
        item = arma()
        material = materialEspecial()
        return(f'Item: {item} de {material} (roll = {roll}) \n')

def rolagemItem7():
    roll = randint(1, 100)
    if roll <= 25:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 65:
        item = armaduraEscudo()
        return(f'Item: {item} +1 (roll = {roll}) \n')
    elif roll <= 95:
        item = arma()
        material = materialEspecial()
        return(f'Item: {item} de {material} (roll = {roll}) \n')
    elif roll <= 100:
        item = armaduraEscudo()
        material = materialEspecial()
        return(f'Item: {item} de {material} (roll = {roll}) \n')

def rolagemItem8():
    roll = randint(1, 100)
    if roll <= 25:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 70:
        item = arma()
        material = materialEspecial()
        return(f'Item: {item} de {material} (roll = {roll}) \n')
    elif roll <= 90:
        item = armaduraEscudo()
        material = materialEspecial()
        return(f'Item: {item} de {material} (roll = {roll}) \n')
    elif roll <= 100:
        item = 'Item mágico menor'
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem9():
    roll = randint(1, 100)
    if roll <= 25:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 65:
        item = arma()
        material = materialEspecial()
        return(f'Item: {item} de {material} (roll = {roll}) \n')
    elif roll <= 85:
        item = armaduraEscudo()
        material = materialEspecial()
        return(f'Item: {item} de {material} (roll = {roll}) \n')
    elif roll <= 100:
        item = 'Item mágico menor'
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem10():
    roll = randint(1, 100)
    if roll <= 25:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 55:
        item = arma()
        material = materialEspecial()
        return(f'Item: {item} de {material} (roll = {roll}) \n')
    elif roll <= 80:
        item = armaduraEscudo()
        material = materialEspecial()
        return(f'Item: {item} de {material} (roll = {roll}) \n')
    elif roll <= 100:
        item = 'Item mágico menor'
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem11():
    roll = randint(1, 100)
    if roll <= 50:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 90:
        item = 'Item mágico menor'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = 'Item mágico médio'
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem12():
    roll = randint(1, 100)
    if roll <= 50:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 85:
        item = 'Item mágico menor'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = 'Item mágico médio'
        return f'Item: {item} (roll = {roll}) \n'


def rolagemItem13():
    roll = randint(1, 100)
    if roll <= 50:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 80:
        item = 'Item mágico menor'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = 'Item mágico médio'
        return f'Item: {item} (roll = {roll}) \n'


def rolagemItem14():
    roll = randint(1, 100)
    if roll <= 50:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 95:
        item = 'Item mágico médio'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = 'Item mágico maior'
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem15():
    roll = randint(1, 100)
    if roll <= 45:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 95:
        item = 'Item mágico médio'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = 'Item mágico maior'
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem16():
    roll = randint(1, 100)
    if roll <= 45:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 90:
        item = 'Item mágico médio'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = 'Item mágico maior'
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem17():
    roll = randint(1, 100)
    if roll <= 45:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 85:
        item = 'Item mágico médio'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = 'Item mágico maior'
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem18():
    roll = randint(1, 100)
    if roll <= 45:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 80:
        item = 'Item mágico médio'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = 'Item mágico maior'
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem19():
    roll = randint(1, 100)
    if roll <= 45:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 75:
        item = 'Item mágico médio'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = 'Item mágico maior'
        return f'Item: {item} (roll = {roll}) \n'

def rolagemItem20():
    roll = randint(1, 100)
    if roll <= 40:
        item = 'nada'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 70:
        item = 'Item mágico médio'
        return f'Item: {item} (roll = {roll}) \n'
    elif roll <= 100:
        item = 'Item mágico maior'
        return f'Item: {item} (roll = {roll}) \n'