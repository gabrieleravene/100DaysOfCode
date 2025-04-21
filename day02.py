# faça um programa que calcule e imprima a o salário a ser transferido para o usuário
# para realizar o cálculo receba o valor bruto do salário e o adicional dos benefícios
# o salário a ser transferido é calculado da seguinte maneira:
# (valor bruto do salário - percentual de imposto mediante ao salário) + adicional dos benefícios

# cálculo do percentual do imposto:
# - 0 1100 = 5%
# 1100 - 2500 = 10%
# >2500 = 15%

def calcular_salario_transferido(valor_bruto, beneficios):
    percentual_imposto = 0
    if valor_bruto <= 1100:
        percentual_imposto = valor_bruto * 0.05
    elif 1100 <= valor_bruto < 2500:
        percentual_imposto = valor_bruto  * 0.1
    else:
        percentual_imposto = valor_bruto * 0.15
    
    salario_transferido = (valor_bruto - percentual_imposto) + beneficios
    return salario_transferido

valor_bruto = float(input('Digite o valor bruto do salário: '))
beneficios = float(input('Digite o valor adicional dos benefícios: '))

print('O salário a ser recebido é: R$', calcular_salario_transferido(valor_bruto, beneficios))