print('')
print ('Escolha entre "Contagem Regressiva", "Contagem de Pares", "Soma Ímpares", "Progressão Aritmética", "Maior Que Menor Que" e "Tabuada V2.0"')
print('')
print ('Contagem Regressiva: 1')
print ('Contagem de Pares: 2')
print ('Soma Ímpares: 3')
print ('Progressão Aritmética: 4')
print ('Maior Que Menor Que: 5')
print('Tabuada V2.0: 6')
print('')

nome = int(input('Escolha entre 1, 2, 3, 4, 5 e 6: '))

match nome:
    case 1:
        import contagemRegressiva

    case 2:
        import contagemDePares

    case 3:
        import somaÍmpares

    case 4:
        import ProgressaoAritmetica

    case 5:
        import MaiorQueMenorQue

    case 6:
        import tabuadav2

    case _:
        ValueError
        print('ERRO: Digite apenas NÚMEROS entre 1, 2, 3, 4, 5 e 6! ')