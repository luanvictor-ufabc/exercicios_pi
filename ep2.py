# EX4

import math
a = int(input())
b = int(input())
c = int(input())

delta = b**2 - 4*a*c

if a == 0:
    print("Sem solucao real!")
    print(f"{delta:.2f}")

else:
    if delta < 0:
        print("Sem solucao real!")
        print(f"{delta:.2f}")

    elif delta == 0:
        x = -b / (2*a)
        print(f"{x:.2f}")

    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)

        
        menor = min(x1, x2)
        maior = max(x1, x2)

        print(f"{menor:.2f}")
        print(f"{maior:.2f}")

# EX 5

t = float(input())

if t < -20:
    print("Muito Baixa")

elif t < 30:
    print("Baixa")

elif t < 200:
    print("Normal")

elif t < 250:
    print("Alta")

else:
    print("Muito Alta")

# EX 6

def comparar_datas(d1, m1, a1, d2, m2, a2):

    if a1 < a2:
        return -1
    elif a1 > a2:
        return 1

    if m1 < m2:
        return -1
    elif m1 > m2:
        return 1

    if d1 < d2:
        return -1
    elif d1 > d2:
        return 1
      
    return 0

# EX 7

ano = int(input())
motor = int(input())
distancia = float(input())

revisao = False

if 1901 <= ano <= 2000:
    if motor == 100 or motor == 101:
        revisao = True

elif 2001 <= ano <= 2020:
    if distancia > 5000:
        revisao = True

elif ano == 2021:
    if (motor == 200 or motor == 201) and distancia > 200:
        revisao = True

if revisao:
    print("SIM")
else:
    print("NAO")

# EX 8

x = float(input())
y = float(input())

if -800 <= x <= 22 and -20 <= y <= 35:
    print("SIM")
else:
    print("NAO")

# EX 9

n = int(input())

n = abs(n)

if n == 0:
    print(0)

while n > 0:
    digito = n % 10
    print(digito)
    n = n // 10

# EX 10

n = int(input())
vetor = list(map(int, input().split()))

vistos = []

for num in vetor:
    if num not in vistos:
        print(num, end=" ")
        vistos.append(num)
