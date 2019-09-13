from random import randint

def gema(qtd):
    gema = ""
    for i in range(qtd):
        roll = randint(1, 100)
        valor = 0
        if roll <= 25:
            for i in range(4):
                valor += randint(1, 4)
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Ágata listrada, ciclope ou do musgo; quartzo azul, hematita; lápis-lazúli; malaquita; obsidiana; rodocrosita; (turquesa) olho de tigre; pérola (irregular); água-marinha \n \n'
            gema += total + exemplo
        elif roll <= 50:
            for i in range(2):
                valor += randint(1, 4)
            valor *= 10
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Heliotropo (ou pedra sangue); cornalina; calcedônia; crisoprase; (topázio) citrino; iolita; jaspe; adulária; ônix; perídoto; cristal de rocha (quartzo hialino); sárdio; sardônico; quartzo rosa, fumado ou estrela; zircão. \n \n'
            gema += total + exemplo
        elif roll <= 70:
            for i in range(4):
                valor += randint(1, 4)
            valor *= 10
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Âmbar; ametista; crisoberilo; coral; piropo ou grossularite (grossulária); jade; lignito; pérola branca, dourada, rosa ou prateada; espinela vermelha; espinela marrom ou verde escuro; turmalina. \n \n'
            gema += total + exemplo
        elif roll <= 90:
            for i in range(2):
                valor += randint(1, 4)
            valor *= 100
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Alexandrita; água-marinha; espinela violeta; pérola negra; espinela azul escuro; topázio amarelo. \n \n'
            gema += total + exemplo
        elif roll <= 99:
            for i in range(4):
                valor += randint(1, 4)
            valor *= 100
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Esmeralda; opala branca, negra ou vermelha; safira azul; negra; rubi estrela. \n \n'
            gema += total + exemplo
        elif roll == 100:
            for i in range(2):
                valor += randint(1, 4)
            valor *= 1000
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Esmeralda verde-claro; diamante branco-azulado, canário, rosa, marrom ou azul; zircão vermelho ou transparente. \n \n'
            gema += total + exemplo
    return gema