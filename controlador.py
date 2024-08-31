from leitor import scan_card
nome_arquivo = 'card'

resul = scan_card(nome_arquivo)
cont = 0
instrucao = []
posicao = []
valor = []
for c in resul:
    instrucao.append(c[0])
    posicao.append(c[1])
    valor.append(c[2:])

    cont += 3


print(instrucao)
print(posicao)
print(valor)
