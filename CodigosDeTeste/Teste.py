# #           0       1           2           3
# lista = ["AAAAA", "BBBBBB", "CCCCCCC", "DDDDDD"]
# x = lista.clear()
# print(x)

# user = 'ildc'
# dig = input("Digite: ")

# if dig in user:
#     print("Aceitei o Range!".upper())

# else:
#     print("To aqui".upper())


#     while conf_user not in conf_del:
                
#                 try:
#                     if conf_user == 's':
#                         lista.clear()
#                 except:
#                     print("Favor digite S ou N")

lista = ["arroz", "feijao", "carne"]
user = input("Digite uma letra! ")
conf_del = 'sn'


if user == 'c':
        if len(lista) == 0:
            print("A lista esta vazia! ")
        else:
            print("Itens deletados: ")
            for ind, valor in enumerate(lista):
                    print(ind, valor)
            conf_user = input("Deseja realmente excluir: [S]im ou [N]ão: ").lower()
            while not conf_user.isalpha() and len(conf_user) > 1:
                conf_user = input("Favor digitar S ou N: ").lower()
                if conf_user is 's':
                    print("Itens deletados com sucesso!")
                    lista.clear()
                else:
                    print("Operação cancelada!".upper())
                    continue