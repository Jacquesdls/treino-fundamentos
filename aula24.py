#Operadores in e not in
# Strings são iteráveis
#{   INDICE    } 
#{ 0 1 2 3 4 5 }
#  j a c q u e s
#  7 6 5 4 3 2 1

nome = 'jacques'

print('Hello world')

print(nome[2]) #Informa qual índice foi selecionada
print(nome[-1]) #Informa qual índice foi selecionada ao contrário

print('á' in nome)
print('z' in nome)
print('ues' in nome)
print(30 * '-')
print('ues' not in nome)

print(30 * '-')
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    
