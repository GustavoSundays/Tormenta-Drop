from random import randint

def obraDeArte(qtd):
    obra = ""
    for i in range(qtd):
        roll = randint(1, 100)
        valor = 0
        if roll <= 10:
            valor = randint(1, 10) * 10
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Vaso de prata; estatueta de osso ou marfi m entalhado; pequeno bracelete de ouro fi namente trabalhado \n \n'
            obra += total + exemplo
        elif roll <= 25:
            for i in range(3):
                valor = randint(1, 6)
            valor *= 10
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Vestimentas de pano de ouro; máscara negra de seda com uma boa quantidade de citrinos; cálice de prata com gemas de lápis-lazúli. \n \n'
            obra += total + exemplo
        elif roll <= 40:
            valor = randint(1, 6) * 100
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Tapeçaria grande e bem-feita de lã; caneco de bronze com ornamentos de jade. \n \n'
            obra += total + exemplo
        elif roll <= 50:
            valor = randint(1, 10) * 100
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Pente de prata com adularias; espada longa ornada com prata e gema negra no cabo. \n \n'
            obra += total + exemplo
        elif roll <= 60:
            for i in range(2):
                valor = randint(1, 6)
            valor *= 100
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Harpa feita de madeira exótica com ornamentos de zircões e marfi m; ídolo de ouro puro maciço (5kg). \n \n'
            obra += total + exemplo
        elif roll <= 70:
            for i in range(3):
                valor = randint(1, 6)
            valor *= 100
            total  = f'Valor: {valor} TO \n \n'
            exemplo = f'Exemplos: Escova de cabelos em forma de dragão dourado e com um olho de gema vermelha; rolha de garrafa de ouro e topázio; adaga cerimonial de electrum com um rubi estrela na ponta do cabo. \n \n'
            obra += total + exemplo
        elif roll <= 80:
            for i in range(4):
                valor = randint(1, 6)
            valor *= 100
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Tapa-olho com um olho falso de safi ra e adularia; pingente de opala vermelha em uma correntinha de ouro; antiga pintura obra-prima. \n \n'
            obra += total + exemplo
        elif roll <= 85:
            for i in range(5):
                valor = randint(1, 6)
            valor *= 100
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Manto bordado em veludo e seda com inúmeras adularias; pingente de safi ra em uma correntinha de ouro \n \n'
            obra += total + exemplo
        elif roll <= 90:
            valor = randint(1, 4) * 1000
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Luva bordada e adornada com gemas; tornozeleira com gemas; caixinha de música de ouro. \n \n'
            obra += total + exemplo
        elif roll <= 95:
            valor = randint(1, 6) * 1000
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Argola dourada com quatro água-marinhas; correntinha com pequenas pérolas rosas (colar) \n \n'
            obra += total + exemplo
        elif roll <= 99:
            for i in range(2):
                valor = randint(1, 4)
            valor *= 1000
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Coroa de ouro adornada com gemas; anel de electrum adornado com gemas. \n \n'
            obra += total + exemplo
        elif roll == 100:
            for i in range(2):
                valor = randint(1, 6)
            valor *= 1000
            total = f'Valor: {valor} TO \n'
            exemplo = f'Exemplos: Anel de ouro e rubi; conjunto de taças douradas e adornadas com esmeraldas. \n \n'
            obra += total + exemplo
    return obra