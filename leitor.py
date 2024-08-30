import os

def scan_card(card_arquivo):
    resul = []
    try:
        with open(card_arquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                linha_bi = ''.join('1' if c == 'X' else '0' if c == 'O' else c for c in linha)
                grupo = linha_bi.split()
                resul.append(grupo)

    except Exception as e:
        print(f"Erro ao abrir ou ler o arquivo: {e}")

    return resul

nome_arquivo = 'card'

resul = scan_card(nome_arquivo)
print(resul)
