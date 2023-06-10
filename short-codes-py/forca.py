def linha():
    print("=" * 40)


def espaço():
    print()


def printlist():
    for b in range(0, len(palavra)):
        print(plista[b], end="")
        
        
def posletra(x):
     for a in range(0, len(palavra)):
            if x == palavra[a]:
                plista[a] = x

    
def vidas(x):
    print(f"Você ainda tem {x} chances:")
    print(lista)


linha()
print("JOGO DA FORCA".center(40))
linha()

espaço()
start = str(input('Digite START para começar: ')).lower()
if start == 'start':
    espaço()
    
    palavra = input("Digite uma palavra: ").lower()
    
    espaço()
    linha()
    espaço()
    
    lista = []
    plista = []
    game = False
    for a in range(0, len(palavra)):
        plista.append("_")
    chute = list(palavra)
    
    while not game:
        vidas(6 - len(lista))
        espaço()
        printlist()
        espaço()
        espaço()
        linha()
        letra = input("\nDigite uma letra: ").lower()
        if letra not in palavra and letra not in lista:
           lista.append(letra)
        if letra in palavra:
           posletra(letra)
        if plista == chute:
           espaço()
           print(palavra)
           espaço()
           print("PARABÉNS, Você ganhou!!!")
           game = True
        if len(lista) == 6:
            espaço()
            print(f"A palavra era {palavra}")
            espaço()
            print("Que pena... Você perdeu!")
            game = True
elif start == 'quit':
    pass
else:
    while start not in ('start', 'quit'):
        print("Dado inválido, tente novamente:")
        start = str(input('Digite START para começar: ')).lower()
