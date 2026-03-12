usuarios = []
contador = 1


# Opção 1
def cadastrar_usuario():
    global contador

    nome = input('Digite seu nome: ')
    email = input('Digite seu e-mail: ')
    idade = int(input('digite sua idade: '))

    usuario = {
        'Id': contador,
        'Nome': nome,
        'E-mail': email,
        'Idade': idade
    }

    usuarios.append(usuario)
    contador += 1

    print(('Usuário cadastrado com sucesso!'))


# Opção 2
def listar_usuarios():
    if len(usuarios) == 0:
        print('Nenhum usuário cadastrado')
    else:
        for usuario in usuarios:
            print(f"ID: {usuario['Id']} | Nome: {usuario['Nome']} | Email: {usuario['E-mail']} | Idade: {usuario['Idade']}")


# Opção 3
def buscar_usuario():
    id_digitado = int(input('Digite o ID: '))

    encontrado = False

    for usuario in usuarios:
        if usuario['Id'] == id_digitado:
            print(f"ID: {usuario['Id']} | Nome: {usuario['Nome']} | Email: {usuario['E-mail']} | Idade: {usuario['Idade']}")
            encontrado = True
            break
        
    if not encontrado:
        print('Usuário não encontrado!')


# Opção 4
def atualizar_usuario():
    id_solicitado = int(input('Digite um ID: '))

    usuario_encontrado = False

    for usuario in usuarios:
        if usuario['Id'] == id_solicitado:
            novo_nome = input('Atualize o nome: ')
            novo_email = input('Atualize o email: ')
            nova_idade = int(input('Atualize a idade: '))

            usuario['Nome'] = novo_nome
            usuario['E-mail'] = novo_email
            usuario['Idade'] = nova_idade

            print('Usuário atualizado com sucesso!')
            usuario_encontrado = True
            break
            
            
    if  not usuario_encontrado:
        print('Usuário não encontrado!') 


# Opção 5
def deletar_usuario():
    id_requerido = int(input('Digite o ID: '))

    id_encontrado = False

    for usuario in usuarios:
        if usuario['Id'] == id_requerido:
            usuarios.remove(usuario)
            print('Usuário removido com sucesso!')
            id_encontrado = True
            break
        
    if not id_encontrado:
        print('ID não encontrado!')


while True:
    print('1 - Cadastrar usuário')
    print('2 - Listar usuário')
    print('3 - Buscar Usuário por ID')
    print('4 - Atualizar usuário')
    print('5 - Deletar usuário')
    print('6 - Sair...')

    opcao = input('Digite uma opção:')

    
    if opcao == '1':
        cadastrar_usuario()
  
    elif opcao == '2':
        listar_usuarios()
  
    elif opcao == '3':
        buscar_usuario()


    elif opcao == '4':
        atualizar_usuario() 

    
    elif opcao == '5':
        deletar_usuario()

    
    elif opcao == '6':
        print('Saindo...')
        break

    else:
        print('Opção inválida. Tente novamente com uma opção válida!')



