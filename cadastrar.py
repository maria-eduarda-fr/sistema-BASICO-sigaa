flag = True
while flag:
    opcao = True
    while opcao:
        menu = int(input(
            'Escolha uma das opções a seguir:\n' \
            '1 - Cadastrar novo curso\n' \
            '2 - Cadastrar nova disciplina\n' \
            '3 - Listar cursos\n' \
            '4 - Listar disciplinas\n' \
            '0 - Parar operações | sair'
        ))
        if menu >= 0 and menu <= 4:
            opcao = False
    
    if menu == 0:
        print('Operações finalizadas')
        flag = False
    elif menu == 1:
        print('OPÇÃO SELECIONADA: ')
        pass
    elif menu == 2:
        print('OPÇÃO SELECIONADA: ')
        pass
    elif menu == 3:
        print('OPÇÃO SELECIONADA: ')
        pass
    elif menu == 4:
        print('OPÇÃO SELECIONADA: ')
        pass
