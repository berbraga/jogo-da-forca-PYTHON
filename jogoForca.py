"""
O objetivo desse programa é o de simplesmente entender o funcionamento de
lista em PYTHON, sendo um programa facil, de baixa complexidade este mesmo
servirar como um exercicio de conteudos.
"""

secreto= 'perfume'
digitada= []
chances= 3

while True:
    if chances<= 0:
        print( 'Voce perdeu feioo!!!' )
        break
    
    letra= input( 'Digite uma letra: ' )
    if len(letra) > 1:
        print( 'Digite apenas uma letra!!!' )
        continue
    
    digitada.append(letra)
    if letra in secreto:
        print( f'UHHULLL, a letra {letra}existe na palavra secreta!' )
    else:
        print( f'aff, a letra {letra}NÃO EXISTE NA PALAVRA SECRETA' )
        digitada.pop()
    
    secreto_temporario= ''
    for letra_secreta in secreto:
        if letra_secreta in digitada:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    if secreto_temporario == secreto:
        print( f'Que legal, Voce ganhou!!! A palavra era {secreto_temporario}' )
        break
    else:
        print( f'A palavra secreta esta assim:{secreto_temporario}' )
        
    if letra not in secreto:
        chances -= 1
        
    print( f'Voce ainda tem {chances} chances.' )
    print()
        