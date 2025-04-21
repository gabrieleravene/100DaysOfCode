# sequência de fibonacci

# escreva um programa que leia um número n qualquer e mostre na tela os n primeiros elementos de um sequência de fibonacci

# A regra básica da sequência é: do terceiro termo em diante, cada novo é a soma dos dois anteriores

# fórmula para sequência de fibonacci: f(n) = f(n-1) + f(n-2)

# os primeiros números são: 0 e 1

numero = int(input('Digite um número: '))
sequencia_de_fibonacci = [0, 1]

numero_atual = 1
numero_anterior = 0

for i in range(numero - 2):
    proximo_numero = numero_atual + numero_anterior
    sequencia_de_fibonacci.append(proximo_numero)
    numero_anterior = numero_atual
    numero_atual = proximo_numero
print(sequencia_de_fibonacci)
    
    