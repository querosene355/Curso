# Exemplo de cabeçalho 

'''
Nome: Primeira aula curso udemy
Autor: Gabriel
Data: 23/07
Versão: 1.0
'''

# Exemplo de interpolação 
'''
nome = "Gabriel"
idade = 20

frase = f"Olá, meu nome é {nome} e eu tenho {idade}"
'''

'''
#Exemplo de input

favSerie = input("Qual sua série favorita ?:")
favPersonagem = input(f"Qual o seu personagem favorito de {favSerie} ?")
frase = f"O melhor personagem de {favSerie} é {favPersonagem}!"

print(frase)
'''

'''
#Exemplo de slicing

filme = 'Scarface'
index   01234567

print(filme[0])
print(filme[0:8])


valor = 46.77
Index 01234
valor = str(valor)

print(valor[3:5])
print(valor[2:])
'''

'''
#Exemplo de metodos de stirng

frase = '  Lupin é Uma Otima Série'

#Letra minuscula
print(frase.lower())

#Letra Maiuscula
print(frase.upper())

#Primeira letra em maiúsculo
print(frase.capitalize())

#Procurar index de uma letra - Case sensitive
print(frase.find('u')) 
#Serve para palavras, entrega o index inicial
print(frase.find('Uma')) 

#Substituir uma letra - Case sensitive
print(frase.replace('u', 'y'))
#Substituir uma palavra
print(frase.replace('Lupin', 'The Boys'))

#Remover espaço antes da primeira letra
print(frase.strip())
'''

'''
#Exemplo de if

question = int(input("Quantos filmes a franquia tem ?"))

if question == 8:
    print ("Provavelmente e Harry Potter")
else:
    print ("Não é Harry Potter")
'''

'''
#Exemplo de for
for numero in range(1, 20, 2 ):
#              Inicio, fim, step (de quanto em quanto)    
    print(numero)
'''

