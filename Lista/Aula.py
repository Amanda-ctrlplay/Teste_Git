# #Estruturas condicionais

# #Igualdade

# numero1 = 10
# numero2 = 50

# texto1 = 'Ctrl'
# texto2 = 'Play'

# print(numero1 * 5 ==numero2)
# print(texto1 == texto2)

# #Desigualdade

# print(numero1 != numero2)
# print(texto1 != texto2)

# #Maior ou menor ou igual

# print(numero1 > numero2)
# print(numero1 >= numero2)
# print(texto1 > texto2)

# #And e or

# print(6 < 3 < 7)
# print(19 < 5 or 28 < 9)

# #If e else
# #If: se
# #else: senão

# nota = 5

# if nota >= 10:
#     print("Aprovado!")
    
# elif 4 <= nota <=6:
#     print("Recuperação!")
        
# else:
#     print("Reprovou!")
    
# #Desafio
# nome = input("Digite o nome do aluno: \n")
# nota = int(input("Digite a nota do aluno: \n"))

# if nota >= 7:
#     print(f"O aluno {nome} foi aprovado com a nota {nota}.")
    
# elif nota >= 5:
#     print(f"O aluno {nome} está de recuperação coma a nota {nota}.")

# else:
#     print(f"O aluno {nome} está reprovado com a nota {nota}.")    
    
#Desafio 2

#lista que armazena os meses
#Criar um input que recebe o numero do mês
#if e else
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

numerodomes = int(input("Digite o número do mês (1 a 12)"))

if 1 <= numerodomes <= 12:
    print(f'Seu mês é {meses[numerodomes -1]}')
else:
    print("Número inválido. Digite um número entre 1 e 12.")