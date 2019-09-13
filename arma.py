from random import randint

def arma():
    roll = randint(1, 100)
    if roll <= 3:
        return('Adaga')
    elif roll <= 5:
        return('Alabarda')
    elif roll <= 7:
        return('Alfange')
    elif roll <= 9:
        return('Arco composto')
    elif roll <= 12:
        return('Arco curto')
    elif roll <= 15:
        return('Arco longo')
    elif roll <= 17:
        return('Azagaia')
    elif roll <= 20:
        return('Besta leve')
    elif roll <= 23:
        return('Besta pesada')
    elif roll <= 26:
        return('Bordão')
    elif roll <= 28:
        return('Chicote')
    elif roll <= 31:
        return('Cimitarra')
    elif roll <= 33:
        return('Clava')
    elif roll == 34:
        return('Corrente com cravos')
    elif roll <= 36:
        return('Espada bastarda')
    elif roll <= 39:
        return('Espada curta')
    elif roll == 40:
        return('Espada de duas lâminas')
    elif roll <= 43:
        return('Espada grande')
    elif roll <= 46:
        return('Espada longa')
    elif roll == 47:
        return('Espada táurica')
    elif roll <= 50:
        return('Florete')
    elif roll <= 52:
        return('Foice')
    elif roll <= 55:
        return('Funda')
    elif roll == 56:
        return('Katana')
    elif roll <= 59:
        return('Lança')
    elif roll == 60:
        return('Lança montada')
    elif roll <= 63:
        return('Maça')
    elif roll <= 66:
        return('Machadinha')
    elif roll == 67:
        return('Machado anão')
    elif roll <= 70:
        return('Machado de batalha')
    elif roll <= 73:
        return('Machado grande')
    elif roll <= 75:
        return('Mangual')
    elif roll == 76:
        return('Manopla')
    elif roll == 77:
        return('Marreta estilhaçadora')
    elif roll <= 79:
        return('Martelo')
    elif roll <= 81:
        return('Martelo de guerra')
    elif roll == 82:
        return('Mosquete')
    elif roll <= 87:
        roll = randint(1, 100)
        if roll <= 20:
            return('Munição: Balas(x50)')
        elif roll <= 60:
            return('Munição: Flechas(x50)')
        elif roll <= 70:
            return('Munição: Pólvora(x50)')
        elif roll <= 100:
            return('Munição: Virotes(x50)')
    elif roll == 88:
        return('Nunchaku')
    elif roll == 89:
        return('Picareta')
    elif roll == 90:
        return('Pique')
    elif roll == 91:
        return('Pistola')
    elif roll == 92:
        return('Rede')
    elif roll == 93:
        return('Sabre serrilhado')
    elif roll == 94:
        return('Sai')
    elif roll == 95:
        return('Shuriken')
    elif roll <= 97:
        return('Tacape')
    elif roll == 98:
        return('Tai-tai')
    elif roll == 99:
        return('Tridente')
    elif roll == 100:
        return('Wakisashi')