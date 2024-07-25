#Exemplo de for com IF


import random

pontuacao = 0
qtdVitorias = 0
qtdEmpates = 0 
qtdDderrotas = 0

frase = 'Jogo número:'

for jogo in range(38):
    resultado = random.randrange(0, 3)
    
    if resultado == 2:
        pontuacao += 3
        qtdVitorias += 1
        print (f'{frase} {jogo}, Vitória')
        

    elif resultado == 1:
        pontuacao += 1
        qtdEmpates += 1
        print (f'{frase} {jogo}, Empate')

    else:
        qtdDderrotas += 1
        print (f'{frase} {jogo}, Derrota')

print(f'''
Pontuação: {pontuacao}
Vitorias: {qtdVitorias}
Empates: {qtdEmpates}
Derrotas: {qtdDderrotas} 
''')