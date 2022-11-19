import random

def escolher_palavra():
    arquivo = open("objetos-sem-acentos.txt")
    linhas= arquivo.readlines()


    palavra = ''
    while len(palavra) < 5:
        sorteio = random.randint(0, len(linhas)) + 1
        palavra = linhas[sorteio]


    arquivo.close()
    return palavra.strip()


vazio = """
 ┎---┐
 │
 │
 │
 ┴
"""
cabeca = """
 ┎---┐
 │   ⭘
 │   
 │
 ┴
"""
corpo = """
----┐
 ┎---┐
 │   ⭘
 │   |
 │
 ┴
"""
braco_esquerdo = '''
 ┎---┐
 │   ⭘
 │  /|
 │
 ┴
'''
braco_direito = '''
 ┎---┐
 │   ⭘
 │  /|╲
 │  
 ┴
'''
perna_esquerda = '''
 ┎---┐
 │   ⭘
 │  /|╲
 │  / 
 ┴
'''
perna_direita = '''
 ┎---┐
 │   ⭘
 │  /|╲
 │  / ╲
 ┴
'''

palavra = escolher_palavra()
chances = [vazio, cabeca, corpo, braco_esquerdo, braco_direito, perna_esquerda, perna_direita]
quantidade = len(palavra)
acertos = 0
erros = 0
letra_acertada = ''
letra_errada = ''

while acertos != quantidade and erros != 7:
    print(chances[erros])
    mensagem = ''
    for letra in palavra:
        if letra in letra_acertada:
            mensagem += letra + ' '
        else:
            mensagem += '_ '
    print(mensagem)
    print(f'A palavra contém {quantidade} letras')
    print(f'voce ja errou as seguintes letras: {letra_errada}')
    print(f'acertos = {acertos}')
    print(f'erros = {erros}')

    letra = input('Digite uma letra: ')
    letra = letra[0]

    if not letra.isalpha():
        print(f"{letra} não é letra")
    else:
        if letra in palavra:
            if letra not in letra_acertada:
                letra_acertada += letra
                print(f'Tem letra letra: {letra}')
                acertos += palavra.count(letra)
                print('--' * 25)
        else:
            if letra not in letra_errada:
                letra_errada += letra
                print(f'Não tem letra {letra}')
                erros += 1
                print('--' * 25)


if acertos == quantidade:
    print('Parabéns voce conseguiu!!')
    print('=-=-=-=-=-FIM-=-=-=-=-=')
else:
    print(f'A palavra era {palavra}')
    print('=-=-=-=-=-FIM-=-=-=-=-=')
