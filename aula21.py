#Operadores lógicos 
# and or not

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitada = '123456'

if entrada =='E' and senha_digitada == senha_permitada:
    print('Entrando...')
else: print('Sair')

#Avaliação de curto circuito
print(False and True)