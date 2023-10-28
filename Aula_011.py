# Funções Lambda é uma função anônima e que não tem nome
# condicionais ternárias
# utiliza-se: map(), filter() e reduce()
# map() vai mapear 
# filter() vai filtrar 
# reduce() vai acumular o valor 
# quadrado = lambda x: x ** 2 
# print(quadrado(5))

# # Exemplo de uma função normal
# def soma(a,b):
#     print(a+b)

# # Exemplo com lambda
# soma2 = lambda a,b: a+b 
# soma(1,2)
# print(soma2(3,6))

# # Exemplo com map(): 
# numeros = [1, 2, 3, 4, 5]
# quadrados = list(map(lambda x: x ** 2, numeros))
# print(quadrados)  # Saída: [1, 4, 9, 16, 25]

# # Exemplo com filter():
# numeros01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = list(filter(lambda x: x % 2 == 0, numeros01))
# print(pares)  # Saída: [2, 4, 6, 8, 10]

# # Exemplo com reduce():
# from functools import reduce

# numeros02 = [1, 2, 3, 4, 5]
# soma = reduce(lambda x, y: x + y, numeros02)
# print(soma)  # Saída: 15

# Exercício 01: Crie uma função lambda que retorne o dobro de um número.
# dobro = lambda a: a*2
# a = int(input("Digite um número:\n"))
# print(dobro(a))

# Exercício 02: Crie uma função lambda que calcule a soma de dois números.
# soma = lambda x,y: x+y 
# x = int(input("Digite um número:\n"))
# y = int(input("Digite outro número:\n"))
# print(soma(x,y))

# Exercício 03: Crie uma função lambda que verifique se um número é par.
numero_par = lambda x: x % 2 == 0 
x = int(input("Digite um número:\n"))
numero_par(x)
if numero_par(x) is True:
   print( "é um número par")
else:
   print("É um número ímpar")

# Exercício 04: Crie uma função lambda que converta uma string em maiúsculas.
maiuscula = lambda palavra: palavra.upper()
palavra = str(input("Digite uma palavra:\n"))
print(maiuscula(palavra))

# Exercício 05: Crie uma função lambda que calcule o produto de três números.
produto = lambda: 10*1*5
print("o produto é:", produto())

