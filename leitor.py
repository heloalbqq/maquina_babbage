import os

def scan_card(card_arquivo):
    resul = []

    with open(card_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            linha_bi = ''.join('1' if c == 'X' else '0' if c == 'O' else c for c in linha)
            grupo = linha_bi.split()
            resul.append(grupo)

    
    return resul


