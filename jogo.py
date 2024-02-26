import desenho as d
from random import choice
import banco

def jogar():
    lista_palavras = []
    arquivo = open('palavras.txt', 'r')
    for linha in arquivo:
        palavras = linha.strip()
        lista_palavras.append(palavras)

    palavra_sorteada = choice(lista_palavras)

    digitadas = []
    acertos = []
    erros = 0

    nome = input('Quem está jogando ? ')

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

        if adivinha == palavra_sorteada:
            print('Você acertou!\n')
            break

        tentativa = input('Digíte uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('Você já usou essa letra!')
            continue

        else:
            digitadas += tentativa
            if tentativa in palavra_sorteada:
                acertos += tentativa
            else:
                erros += 1
                print('Você errou!')

        score = d.desenhar_forca(erros)

        if erros == 6:
            print('Enforcado!')
            print(f'A palavra correta era {palavra_sorteada}')
            break

    banco.inserir_dado(nome, score) 