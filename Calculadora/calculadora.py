# Este é um exemplo basico de uma calculadora feita em Python 3, não possui parte grafica, para executar é necessario ter o Python 3 Instalado e rodar no console 
# 
def calcular():
    operador = input('''
/ Digite a operação matemática que deseja realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')
    number_1 = int(input("Digite o primeiro número: "))
    number_2 = int(input("Digite o segundo número: "))

    if operador == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operador == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operador == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operador == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print(" 😡 Você não digitou um operador válido, execute o programa novamente. ")

# https://github.com/thiagowilliamp/


calcular()


for i in range(0, 2):
    calcular()

print(" Obrigado!!!")