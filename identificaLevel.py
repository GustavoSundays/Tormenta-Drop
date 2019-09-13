import rolagemRiqueza
import rolagemItem

def identificaLevel(level):
    riqueza = 0
    item = 0
    if level == '':
        level = 0
    level = int(level)
    titulo = f'Roll para o level %d: \n\n\n'%level
    if level == 1:
        riqueza = rolagemRiqueza.rolagemRiqueza1()
        item = rolagemItem.rolagemItem1()
    elif level == 2:
        riqueza = rolagemRiqueza.rolagemRiqueza2()
        item = rolagemItem.rolagemItem2()
    elif level == 3:
        riqueza = rolagemRiqueza.rolagemRiqueza3()
        item = rolagemItem.rolagemItem3()
    elif level == 4:
        riqueza = rolagemRiqueza.rolagemRiqueza4()
        item = rolagemItem.rolagemItem4()
    elif level == 5:
        riqueza = rolagemRiqueza.rolagemRiqueza5()
        item = rolagemItem.rolagemItem5()
    elif level == 6:
        riqueza = rolagemRiqueza.rolagemRiqueza6()
        item = rolagemItem.rolagemItem6()
    elif level == 7:
        riqueza = rolagemRiqueza.rolagemRiqueza7()
        item = rolagemItem.rolagemItem7()
    elif level == 8:
        riqueza = rolagemRiqueza.rolagemRiqueza8()
        item = rolagemItem.rolagemItem8()
    elif level == 9:
        riqueza = rolagemRiqueza.rolagemRiqueza9()
        item = rolagemItem.rolagemItem9()
    elif level == 10:
        riqueza = rolagemRiqueza.rolagemRiqueza10()
        item = rolagemItem.rolagemItem10()
    elif level == 11:
        riqueza = rolagemRiqueza.rolagemRiqueza11()
        item = rolagemItem.rolagemItem11()
    elif level == 12:
        riqueza = rolagemRiqueza.rolagemRiqueza12()
        item = rolagemItem.rolagemItem12()
    elif level == 13:
        riqueza = rolagemRiqueza.rolagemRiqueza13()
        item = rolagemItem.rolagemItem13()
    elif level == 14:
        riqueza = rolagemRiqueza.rolagemRiqueza14()
        item = rolagemItem.rolagemItem14()
    elif level == 15:
        riqueza = rolagemRiqueza.rolagemRiqueza15()
        item = rolagemItem.rolagemItem15()
    elif level == 16:
        riqueza = rolagemRiqueza.rolagemRiqueza16()
        item = rolagemItem.rolagemItem16()
    elif level == 17:
        riqueza = rolagemRiqueza.rolagemRiqueza17()
        item = rolagemItem.rolagemItem17()
    elif level == 18:
        riqueza = rolagemRiqueza.rolagemRiqueza18()
        item = rolagemItem.rolagemItem18()
    elif level == 19:
        riqueza = rolagemRiqueza.rolagemRiqueza19()
        item = rolagemItem.rolagemItem19()
    elif level == 20:
        riqueza = rolagemRiqueza.rolagemRiqueza20()
        item = rolagemItem.rolagemItem20()
    elif level <= 0 or level > 20:
        return 'Digite um nível correto (entre 1 e 20)'
    return titulo + riqueza + item
