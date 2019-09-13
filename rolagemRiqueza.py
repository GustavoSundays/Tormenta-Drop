from random import randint
from gema import gema
from obraDeArte import obraDeArte

def rolagemRiqueza1():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 30:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 75:
        riqueza = randint(1, 6) * 100
        return f'{riqueza} TP  (roll = {roll}) \n \n'
    elif roll <= 95:
        for i in range(2):
            riqueza += randint(1,4)
        riqueza *= 10
        return f'{riqueza} TO  (roll = {roll}) \n \n'
    elif roll <= 100:
        for i in range(2):
            riqueza += randint(1,12)
        return f'{riqueza} TL  (roll = {roll}) \n \n'

def rolagemRiqueza2():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 25:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 75:
        riqueza = randint(1, 8) * 100
        return f'{riqueza} TP  (roll = {roll}) \n \n'
    elif roll <= 95:
        for i in range(3):
            riqueza += randint(1, 6)
        riqueza *= 10
        return f'{riqueza} TO  (roll = {roll}) \n \n'
    elif roll <= 100:
        for i in range(4):
            riqueza += randint(1, 12)
        return f'{riqueza} TL  (roll = {roll}) \n \n'

def rolagemRiqueza3():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 20:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 70:
        riqueza = randint(1, 10) * 10
        return f'{riqueza} TP  (roll = {roll}) \n \n'
    elif roll <= 95:
        for i in range(3):
            riqueza += randint(1, 8)
        riqueza *= 10
        return f'{riqueza} TO  (roll = {roll}) \n \n'
    elif roll <= 100:
        for i in range(4):
            riqueza += randint(1, 12)
        return f'{riqueza} TL  (roll = {roll}) \n \n'

def rolagemRiqueza4():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 15:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 65:
        for i in range(3):
            riqueza += randint(1, 8)
        riqueza *= 100
        return f'{riqueza} TP  (roll = {roll}) \n \n'
    elif roll <= 95:
        riqueza = randint(1, 6) * 100
        return f'{riqueza} TO  (roll = {roll}) \n \n'
    elif roll <= 100:
        riqueza = randint(1, 10) * 10
        return f'{riqueza} TL  (roll = {roll}) \n \n'

def rolagemRiqueza5():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 10:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 60:
        for i in range(3):
            riqueza += randint(1, 10)
        riqueza *= 10
        return f'{riqueza} TO  (roll = {roll}) \n \n'
    elif roll <= 90:
        for i in range(2):
            riqueza += randint(1, 4)
        riqueza *= 10
        return f'{riqueza} TL  (roll = {roll}) \n \n'
    elif roll <= 100:
        riqueza = 1
        return f'{riqueza} Gema  (roll = {roll}) \n \n' + gema(riqueza)

def rolagemRiqueza6():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 10:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 60:
        riqueza = randint(1, 4) * 100
        return f'{riqueza} TO  (roll = {roll}) \n \n'
    elif roll <= 90:
        riqueza = randint(1, 8) * 10
        return f'{riqueza} TL  (roll = {roll}) \n \n'
    elif roll <= 100:
        riqueza = 1
        return f'{riqueza} Gema  (roll = {roll}) \n \n' + gema(riqueza)

def rolagemRiqueza7():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 10:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 60:
        riqueza = randint(1, 6) * 100
        return f'{riqueza} TO  (roll = {roll}) \n \n'
    elif roll <= 90:
        for i in range(2):
            riqueza += randint(1, 6)
        riqueza *= 10
        return f'{riqueza} TL  (roll = {roll}) \n \n'
    elif roll <= 100:
        riqueza = randint(1, 3)
        return f'{riqueza} Gema  (roll = {roll}) \n \n' + gema(riqueza)

def rolagemRiqueza8():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 10:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 60:
        riqueza = randint(1, 6) * 100
        return f'{riqueza} TO  (roll = {roll}) \n \n'
    elif roll <= 90:
        for i in range(3):
            riqueza += randint(1, 4)
        riqueza *= 10
        return f'{riqueza} TL  (roll = {roll}) \n \n'
    elif roll <= 100:
        riqueza = randint(1, 3)
        return f'{riqueza} Gema  (roll = {roll}) \n \n' + gema(riqueza)

def rolagemRiqueza9():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 10:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 60:
        for i in range(2):
            riqueza += randint(1, 4)
        riqueza *= 100
        return f'{riqueza} TO  (roll = {roll}) \n \n'
    elif roll <= 90:
        for i in range(2):
            riqueza += randint(1, 8)
        riqueza *= 10
        return f'{riqueza} TL  (roll = {roll}) \n \n'
    elif roll <= 100:
        riqueza = randint(1, 4)
        return f'{riqueza} Gema  (roll = {roll}) \n \n' + gema(riqueza)

def rolagemRiqueza10():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 10:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 60:
        for i in range(2):
            riqueza += randint(1, 6)
        riqueza *= 100
        return f'{riqueza} TO  (roll = {roll}) \n \n'
    elif roll <= 90:
        riqueza = randint(1, 4)
        return f'{riqueza} Gema  (roll = {roll}) \n \n' + gema(riqueza)
    elif roll <= 100:
        riqueza = 1
        return f'{riqueza} Obras de arte  (roll = {roll}) \n \n' + obraDeArte(riqueza)

def rolagemRiqueza11():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 15:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 85:
        for i in range(2):
            riqueza += randint(1, 10)
        riqueza *= 10
        return f'{riqueza} TL (roll = {roll}) \n \n'
    elif roll <= 100:
        for i in range(2):
            riqueza += randint(1, 4)
        return f'{riqueza} Gema  (roll = {roll}) \n \n' + gema(riqueza)

def rolagemRiqueza12():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 15:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 85:
        riqueza = randint(1, 3) * 1000
        return f'{riqueza} TO (roll = {roll}) \n \n'
    elif roll <= 100:
        riqueza = randint(1, 3)
        return f'{riqueza} Obras de arte  (roll = {roll}) \n \n' + obraDeArte(riqueza)

def rolagemRiqueza13():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 15:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 85:
        for i in range(3):
            riqueza += randint(1, 10)
        riqueza *= 100
        return f'{riqueza} TO (roll = {roll}) \n \n'
    elif roll <= 100:
        for i in range(2):
            riqueza += randint(1, 6)
        return f'{riqueza} Gema  (roll = {roll}) \n \n' + gema(riqueza)

def rolagemRiqueza14():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 10:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 80:
        for i in range(4):
            riqueza += randint(1, 8)
        riqueza *= 10
        return f'{riqueza} TL (roll = {roll}) \n \n'
    elif roll <= 100:
        riqueza = randint(1, 4)
        return f'{riqueza} Obras de arte  (roll = {roll}) \n \n' + obraDeArte(riqueza)

def rolagemRiqueza15():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 10:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 80:
        for i in range(4):
            riqueza += randint(1, 10)
        riqueza *= 100
        return f'{riqueza} TO (roll = {roll}) \n \n'
    elif roll <= 100:
        riqueza = randint(1, 6)
        return f'{riqueza} Obras de arte  (roll = {roll}) \n \n' + obraDeArte(riqueza)

def rolagemRiqueza16():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 10:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 80:
        for i in range(4):
            riqueza += randint(1, 12)
        riqueza *= 10
        return f'{riqueza} TL (roll = {roll}) \n \n'
    elif roll <= 100:
        for i in range(2):
            riqueza += randint(1, 4)
        return f'{riqueza} Obras de arte  (roll = {roll}) \n \n' + obraDeArte(riqueza)

def rolagemRiqueza17():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 10:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 80:
        riqueza = randint(1, 6) * 1000
        return f'{riqueza} TO (roll = {roll}) \n \n'
    elif roll <= 100:
        for i in range(2):
            riqueza += randint(1, 6)
        return f'{riqueza} Obras de arte  (roll = {roll}) \n \n' + obraDeArte(riqueza)

def rolagemRiqueza18():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 5:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 75:
        riqueza += randint(1, 8) * 1000
        return f'{riqueza} TO (roll = {roll}) \n \n'
    elif roll <= 100:
        for i in range(2):
            riqueza += randint(1, 6)
        riqueza *= 100
        return f'{riqueza} TL (roll = {roll}) \n \n'

def rolagemRiqueza19():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 5:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 75:
        for i in range(2):
            riqueza += randint(1, 4)
        riqueza *= 1000
        return f'{riqueza} TO (roll = {roll}) \n \n'
    elif roll <= 100:
        for i in range(2):
            riqueza += randint(1, 10)
        riqueza *= 100
        return f'{riqueza} TL (roll = {roll}) \n \n'

def rolagemRiqueza20():
    riqueza = 0
    roll = randint(1, 100)
    if roll <= 5:
        return f'{riqueza} (roll = {roll}) \n \n'
    elif roll <= 75:
        riqueza = randint(1, 12) * 1000
        return f'{riqueza} TO (roll = {roll}) \n \n'
    elif roll <= 100:
        for i in range(3):
            riqueza += randint(1, 6)
        riqueza *= 100
        return f'{riqueza} TL (roll = {roll}) \n \n'

