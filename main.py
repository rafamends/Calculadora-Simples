import math
 
def divisao(num1,num2):
    try:
        return f'{num1}/{num2}={num1/num2}'
    except ZeroDivisionError:
        return 'O denominador deve ser diferente de zero!'
    except TypeError:
        return 'Digite um valor válido.'
 
def menu():
    print("Calculadora".center(65,'='))
    opcao()
    print('='*65)
 
def opcao():
    print("1 - Operações aritiméticas")
    print("2 - Funções Logarítimicas e Potência")
    print("3 - Funções trigonométricas")
    print("4 - Outras opções")
    print("5 - Sair")
    
def opcao1():
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Voltar")
    
    
def opcao2():
    print("1 - Quadrado")
    print("2 - Cubo")
    print("3 - Potência")
    print("4- Log10")
    print("5 - Log")
    print("6 - Voltar")
 
def opcao3():
    print("1 - Seno")
    print("2 - Cosseno")
    print("3 - Tangente")
    print("4 - Voltar")
 
def opcao4():
    print("1 - Fatorial")
    print("2 - Voltar")
 
def menu1():
    opcao=0
    while opcao!=5:
        opcao=int(input(">> "))
        if opcao in range(1,5):
            num1=float(input("Número 1: "))
            num2=float(input("Número 2: "))
            if opcao==1:
                print(f'{num1}+{num2}={num1+num2}')
            elif opcao==2:
                print(f'{num1}-{num2}={num1-num2}')
            elif opcao==3:
                print(f'{num1} x {num2}={num1*num2}')
            else:
                print(divisao(num1,num2))
                
        else:
            if opcao!=5:
                print('Opção inválida.')
 
                
def menu2():
    opcao=0
    while opcao!=6:
        opcao=int(input(">> "))
        if opcao in range(1,6):
            
            if opcao==1 or opcao==2 or opcao==4:
                num1=float(input('Número: '))
                
                if opcao==1:
                    print(f'{num1}²={num1**2}')
                elif opcao==2:
                    print(f'{num1}³={num1**3}')
                else:
                    print(f'O log de {num1} na base 10 é: {math.log10(num1)}')
            else:
                if opcao==3:
                    base=float(input("Base da potência: "))
                    exp=float(input("Expoente: "))
                    print(f'{base}^{exp}={base**exp}')
                if opcao==5:
                    base=float(input("Base do Log: "))
                    num=float(input("Número: "))
                    print(f'O Log de {num} na base {base} é :{math.log(num,base)}')
 
        else:
            if opcao!=6:
                print('Opção inválida.')
                
def menu3():
    opcao=0
    while opcao!=4:
        opcao=int(input(">> "))
        if opcao in range(1,4):
            num=float(input("Número: "))
            if opcao==1:
                print(f"sen({num})={math.sin(num)}")
            elif opcao==2:
                print(f"cos({num})={math.cos(num)}")
            else:
                print(f"tan({num})={math.tan(num)}")
        else:
            if opcao!=4:
                print('Opção inválida.')
 
def menu4():
    opcao=0
    while opcao!=2:
        opcao=int(input(">> "))
        if opcao==1:
            num=int(input("Digite o número inteiro: "))
            print(f"{num}!={math.factorial(num)}")
        else:
            if opcao!=2:
                print('Opção inválida.')
 
def main():
    escolha=''
    
    while escolha!='5':
        
        menu()
        
        escolha=input(">> ")
        
        if escolha in list('1234'):
            
            if escolha=='1':
                opcao1()
                menu1()
 
            elif escolha=='2':
                opcao2()
                menu2()
                
            
            elif escolha=='3':
                opcao3()
                menu3()
                
            elif escolha=='4':
                opcao4()
                menu4()
                
        elif escolha=='5':
            print("Fim do programa")
            
        else:
            print("Opção inválida!")
            
 
main()