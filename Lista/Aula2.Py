# def = função

#--------------------------------------------------

# def boas_vindas(nome):
#     print(f"Bem-vindos {nome} à Ctrl+Play!")
    
# boas_vindas('Amanda')

#---------------------------------------------------

# def titulo(nome):
#     print(f"Meus filmes favoritos são {nome}")
    
# titulo('Edward, mão de tesouras e Jurassic Park.')

#----------------------------------------------------

# def carteirinha(nome,idade):
#     print(f'O {nome} tem {idade} anos.')
    
# carteirinha(nome='Cleiton', idade=64)
# carteirinha(64, "Cleiton")
# carteirinha("Cleiton, 64")

#----------------------------------------------------

# def menor(a,b):
#     if a <= b:
#         return a
#     else:
#         return b 
# a=5
# b=1

# print(f'O menos valor entre {a} e {b}, é {menor(a,b)}')

#------------------------------------------------------

# def prepara_acai(*igredientes, tamanho="medio"):
#     print(f"\nPreparando um Açai [tmanho] e com os seguintes ingredientes: ")
    
#     for ingredientes in ingredientes:
#         print('-', ingredientes)
        
# prepara_acai("confetes", "leite condensado", "frutas tropicais", "chantilly", "leite em pó")

#-------------------------------------------------------

# def dobra(lencol, gaveta):
#     if lencol < gaveta:
#         return 0
#     else:
#         return 1 + dobra(lencol/2, gaveta)

# print(dobra(200,25))

#-------------------------------------------------------
# clientes = {}

# def cadastro():
#     nome = input("Digite o seu nome completo: ")
#     cpf = input("Didite seu CPF (Somente números): ")
#     telefone = input("Digite seu telefone (Somente números): ")
   
# while True:
 
#     if len(cpf) != 11: # type: ignore
#         print("CPF inválido! Deve conter 11 digitos.")
#         continue

#     if len(telefone) < 10: # type: ignore
#         print(f"Número {telefone} inválido! Menos de 10 digitos não é permitido.") # type: ignore
#         continue
    
#     else:
#         clientes[nome] = { # type: ignore
#             'cpf': cpf, # type: ignore
#             'telefone': telefone # type: ignore
#         }
#         print(f"Cadastro do cliente {nome} realizado com sucesso!") # type: ignore
#         break
#     cadastro()
   
#-------------------------------------------------------------------------

livro{}

def cadastro_livro(nome_livro, nome_autor):
    nome_livro = imput(f'Digie o nome do livro: ')
    