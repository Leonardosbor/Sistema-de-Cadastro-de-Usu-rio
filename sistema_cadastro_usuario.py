usuarios = []
contador = 1


while True:
    print('1 - Cadastrar usuário')
    print('2 - Listar usuário')
    print('3 - Sair')

    opcao = input('Digite uma opção:')

    
    if opcao == '1':
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

        
    
    elif opcao == '2':
        print('Listar Usuário')
    
    elif opcao == '3':
        print('Saindo...')
        break

    else:
        print('Opção inválida. Tente novamente com uma opção válida!')



