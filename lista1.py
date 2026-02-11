# EXERCÍCIO 2

valor1 = int(input())
valor2 = float(input())
valor3 = float(input())

print(f"Primeiro numero = {valor1:.0f}")
print(f"{valor2:.2f} eh o segundo numero")
print(f"Finalmente {valor3:.3f} eh o terceiro numero")

# EXERCÍCIO 3

import math

Ax = float(input())
Ay = float(input())
Bx = float(input())
By = float(input())

dAB = math.sqrt((Bx - Ax)**2 + (By - Ay)**2)

print(f"{dAB:.2f}")

# EXERCÍCIO 5
salario = float(input())
vendas = float(input())

comissao = vendas * 0.20

print(f"{comissao:.2f}")

if comissao >= salario * 0.5:
    print("Atingiu meta de vendas")
else:
    print("Nao atingiu meta de vendas")

# EXERPICIO 6

a1 = int(input())
r = int(input())
n = int(input())

an = a1 + (n - 1) * r
S = n * (a1 + an) // 2

print(S)

# EXERCÍCIO 7

valor = float(input())

valor = valor * 0.9
valor = valor * 0.9

print(f"{valor:.2f}")

# EXERCÍCIO 8

numero = input()

resultado = ""

for digito in numero:
    novo = (int(digito) + 1) % 10
    resultado += str(novo)

print(resultado)

# EXERCÍCIO 9

capacidade = int(input())

q500 = capacidade // 500
capacidade %= 500

q100 = capacidade // 100
capacidade %= 100

q25 = capacidade // 25
capacidade %= 25

q1 = capacidade // 1

print(q500)
print(q100)
print(q25)
print(q1)

# EXERCÍCIO 10

VP = int(input())
FN = int(input())
FP = int(input())
VN = int(input())

acuracia = (VP + VN) / (VP + VN + FP + FN)
precisao = VP / (VP + FP)
sensibilidade = VP / (VP + FN)

print(f"{acuracia:.2f}")
print(f"{precisao:.2f}")
print(f"{sensibilidade:.2f}")



