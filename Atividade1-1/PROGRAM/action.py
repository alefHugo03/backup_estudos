import lista 
import sys
 
def menu():
 
    print('''        
    #############################################
           Lista da empresa AtmosFeras S.A
    #############################################
    ''' )
    while  True:
        print("Bem-Vindo ao Menu da AtmosFeras S.A")
        print()    
        print("Digite o número que deseja:")
        print("1 - Listar colaboradores da empresa")
        print("2 - Listar colaboradores por ordem alfabética")
        print("3 - Listar colaboradores por salário")
        print("4 - Listar colaboradores de cada cargo")
        print("5 - Sair")
         
        try:
            caso = int(input('Digite o número: '))
            match caso: 
                case 1: 
                    print()
                    lista.pessoass()
                    print()
                case 2: 
                    print()
                    lista.pessoas_Alfabetica()
                    print()
                case 3:
                    print()
                    lista.pessoas_Salario()
                    print()
                case 4:
                    print()
                    lista.cargos_Filter()
                    print()
                case 5:
                    print()
                    print("Saindo do programa...")
                    print()
                    sys.exit()
                case _:
                    print()
                    print("Número inválido")
                    print()
                    continue
        except ValueError:
            print('''############################
        Opção inválida
                  
############################''')