# EX4

import math
a = int(input())
b = int(input())
c = int(input())

delta = b**2 - 4*a*c

if delta < 0:
        print("Sem solucao real!")
        print(f"Delta = {delta:.2f}")

elif delta == 0:
        x = -b / (2*a)
        print(f"x = {x:.2f}")

else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)

        
        menor = min(x1, x2)
        maior = max(x1, x2)

        print(f"x1 = {menor:.2f}")
        print(f"x2 = {maior:.2f}")

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

from os import error
# funcao_origem: 
def funcao_origem():
  origem = int(input("Digite o código do planeta de origem"))
  marte = 80
  saturno = 81
  netuno = 90

  if origem == marte or saturno or netuno:
    return marte, saturno, netuno;
  else:
    return error

# funcao_destino:
def funcao_destino(): 
  destino = input("Digite o código do destino")
  HD21749b = 91

  if destino == 91:
    return HD21749b
  else:
    return error

# funcao_modelo:
def funcao_modelo():
  modelo = input("Digite o código do modelo")
  A6000 = 60
  B7500 = 61
  C9000 = 62

  if modelo == 60


  return A6000, B7500, C9000;

# EX 10

import math

carga = int(input())
Ax = float(input())
Ay = float(input())
Bx = float(input())
By = float(input())

if carga <= 50000:
    autonomia = 18000
elif carga <= 200000:
    autonomia = 9000
else:
    autonomia = 3000

distancia = math.sqrt((Bx - Ax)**2 + (By - Ay)**2)
limite = autonomia * 1.1

print(f"{distancia:.2f}")

if distancia <= autonomia:
    print("SIM")
elif distancia <= limite:
    print("TALVEZ")
else:
    print("NAO")
