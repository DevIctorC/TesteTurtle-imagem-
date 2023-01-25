print("##############LISTA DE COMPRAS###############")
lista  = []
lista_vazia = []
fora_r = 'i','l','d','c' 
conf_del = 'sn'
print("Heloiras! ")
while True:
    print(100 * '-')
    print("Selecione uma opção! ")
    user = input("[I]nserir [D]eletar [L]istar [C]lear: ").lower()

    if len(user) > 1 or user not in fora_r:
        print("Favor digitar SOMENTE a letra marcada!!")
        continue


    if user == 'i':
        user_add = input("Digite um valor: ")
        lista.append(user_add)
        print("Item adicionado!")

    if user =='l':
        if len(lista) >= 1:
            for ind, valor in enumerate(lista):
                print(ind, valor)
        else:
            print("Nenhum item a ser listado! ")

    if user == 'd':
        if len(lista) >= 1:
            try:
                for ind, valor in enumerate(lista):
                    print(ind, valor)

                user_del = int(input("Digite um valor: "))
                fora = lista.pop(user_del)
                print(f"O item {fora}")
            except:
                print("cancelada por índices não correspondentes! ")    
        
        else:
            print("A lista não possui itens pra ser deletada")

    if user == 'c':
        if len(lista) == 0:
            print("A lista esta vazia! ")
        else:
            print("Itens deletados: ")
            for ind, valor in enumerate(lista):
                    print(ind, valor)
            lista.clear()

