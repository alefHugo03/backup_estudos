import mapa
import grafrico
import conversao

while True:
    
    print("""
        1 - Mapa
        2 - Gráfico
        3 - Tabela
        4 - Sair
    """)
    match int(input("Escolha uma opção: ")):
        case 1:
            mapa.mapa()
                
        case 2:
            grafrico.grafico()
        case 3:
            print(conversao.dados_saida())
        case 4:
            print("Saindo...")
            break
        case _: 
            print("Opção inválida. Tente novamente.")
