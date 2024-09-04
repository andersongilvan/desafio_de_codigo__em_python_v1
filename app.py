from banco import *
import os
import time
from menu import exibe_menu
from exibe_logo import exibe_logo

def visualizar_menu():
     time.sleep(3)
     os.system("cls")
     exibe_menu()


def main():
    

    exibe_menu()

    while True:
            
            opcao = str(input("\nDigite uma opção: "))
            
            if opcao == "d":
                os.system("cls")
                try:
                    exibe_logo()
                    valor = float(input("Digite o valor do depósito: "))
                    os.system("cls")
                    depositar(valor=valor)
                    
                    visualizar_menu()
                except:
                    print("Vlor inválido")
                    visualizar_menu()

            elif opcao == "s":
                os.system("cls")
                try:
                    valor = float(input("Digite o valor do saque: "))
                    os.system("cls")
                    sacar(valor=valor)
                    visualizar_menu()
                except:
                    print("Vlor inválido")
                    visualizar_menu()

            elif opcao == "e":
                os.system("cls")
                exibir_extrato()
                print("\ndigite qualquer tacla para voltar ao menu principal\n")
                input()
                visualizar_menu()
                
            elif opcao == "q":
                os.system("cls")
                
                print("Encerrando...")
                time.sleep(3)
                os.system("cls")
               
                break

            else:
                os.system("cls")
                print("Opção inválida")
                visualizar_menu()


if __name__ == "__main__":
    main()