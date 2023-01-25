"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# user_digt = input("Digite uma número inteiro: ")

# try:
#     user_digt = float(user_digt)
#     if user_digt % 2 == 0:
#         print("O valor digitado é PAR! ")
#     else:
#         print("Valor digitado é IMPAR!")

# except:
#     print(f"Valor digitado: '{user_digt.upper()}' não é um número inteiro!")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 

Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# tempo_dig = input("Digite o horário: ")

# try:
#     tempo_dig = float(tempo_dig)
    
#     if tempo_dig >= 0 and tempo_dig < 11:
#         print("Bom dia")

#     elif tempo_dig >= 12 and tempo_dig <= 18:
#         print("Boa tarde")

#     else:
#         print("Boa notie!")

# except:
#     print("Erro causado por você! ")
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome_user = input("Digite seu nome: ")

# if len(nome_user) <= 4:
#     print("Seu nome é CURTO")

    
# if len(nome_user) > 4 and len(nome_user) <= 6:
#     print("Seu nome é NORMAL")

    
# if len(nome_user) > 6:
#     print("Seu nome é LONGO")

"""Exercício do While"""
# nome = 'COLINDO'
# nova_str = ''
# ind = 0

# while ind < len(nome):
#         nova_str += f'{nome[ind]}*'
#         # print(nova_str)
#         ind += 1
# print(nova_str)

"""Calculadora com while (TEM QUE TERMINAR)"""

"""Calculadora com while"""
# while True:
#         n1 = input("Digite um número: ")
#         n2 = input("Digite um número: ")
#         op = input("Digite um operador +-*/")

#         n1_f = 0
#         n2_f = 0
#         n1_va = None

#         try:
#                 n1_f = float(n1)
#                 n2_f = float(n2)
#                 n1_va = True

#         except:
#                 n1_va = None
               
#         if n1_va is None:
#                 print("Favor digitar um valor válido! ")
#                 continue

        





#         sair = input("Deseja sair? [s]im ou [n]ao: ").lower()
#         if sair.startswith('s'):
#                 print("Saindo da calc")
#                 break

"""Jogo da forca """

# import os

# palavra_secreta = input("Digite uma palavra para iniciar o jogo da forca: ")
# letras_acertadas = ''
# tentativas = len(palavra_secreta) - 1

# while tentativas > 0:
    

#     print(f"Você tem {tentativas} tentativas! ")
#     letra_digitada = input("Digite uma letra: ")

#     if len(letra_digitada) > 1:
#         print("Digite apenas UMA letra!!")
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     elif letra_digitada != palavra_secreta:
#         tentativas -= 1

#     palavra_formada = ''

#     for letra_secreta in palavra_secreta:
#             if letra_secreta in letras_acertadas:
#                 palavra_formada += letra_secreta
                
#             else:
#                 palavra_formada += "*"
    
#     print(palavra_formada)
#     print(100 *"-")

#     if palavra_formada == palavra_secreta:
#         os.system('cls')
#         print("Parabéns você acertou a palavra!".upper())
#         break


# if tentativas == 0:
#     print(f'Infelizmente você errou a plavra era: {palavra_secreta.upper()}')

"""Enumerar valores da lista com seus indices"""

# lista = ['Maria', 'Helena', 'Luiz', 'Marcos']
# indices = range(len(lista))

# for indice in indices:
#     print(indice, lista[indice])

# """Exercicios criando lista com ações"""

# print("##############LISTA DE COMPRAS###############")
# lista  = []
# lista_vazia = []

# while True:
#     print(100 * '-')
#     print("Selecione uma opção! ")
#     user = input("[I]nserir [D]eletar [L]istar [C]lear: ").lower()

#     if len(user) > 1:
#         print("Favor digitar SOMENTE a letra marcada!!")
#         continue


#     if user == 'i':
#         user_add = input("Digite um valor: ")
#         lista.append(user_add)
#         print("Item adicionado!")

#     if user =='l':
#         if len(lista) >= 1:
#             for ind, valor in enumerate(lista):
#                 print(ind, valor)
#         else:
#             print("Nenhum item a ser listado! ")

#     if user == 'd':
#         if len(lista) >= 1:
#             try:
#                 for ind, valor in enumerate(lista):
#                     print(ind, valor)

#                 user_del = int(input("Digite um valor: "))
#                 fora = lista.pop(user_del)
#                 print(f"O item {fora}")
#             except:
#                 print("cancelada por índices não correspondentes! ")    
        
#         else:
#             print("A lista não possui itens pra ser deletada")

    # if user == 'c':
    #     if len(lista) == 0:
    #         print("A lista esta vazia! ")
    #     else:
    #         print("Itens deletados: ")
    #         for ind, valor in enumerate(lista):
    #                 print(ind, valor)
    #         lista.clear()
            
