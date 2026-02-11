# EXERCÍCIO 1

n = int(input("Digite um valor"))
if n %2 == 0:
    print(0)
else:
    print(1)

# EXERCÍCIO 2

import math

def distancia_origem(x, y):
    return math.sqrt(x**2 + y**2)

def main():
    print("Testes da função distancia_origem:\n")
    
    print("Ponto (3, 4):", distancia_origem(3, 4))
    print("Ponto (0, 0):", distancia_origem(0, 0))
    print("Ponto (1, 1):", distancia_origem(1, 1))
    print("Ponto (-5, 12):", distancia_origem(-5, 12))
    print("Ponto (2.5, -3.1):", distancia_origem(2.5, -3.1))

main()

# EXERCÍCIO 3

# EXERCÍCIO 4

# EXERCÍCIO 5

base = 0
altura = 0
area = 0

def calcula_area():
    global base, altura, area
    area = base * altura

def calcula_base():
    global base, altura, area
    if altura != 0:
        base = area / altura
    else:
        print("Erro: altura não pode ser zero.")

def calcula_altura():
    global base, altura, area
    if base != 0:
        altura = area / base
    else:
        print("Erro: base não pode ser zero.")

def main():
    global base, altura, area
    
    print("Teste 1 - Calcular área")
    base = 5
    altura = 4
    calcula_area()
    print(f"Base = {base}, Altura = {altura}, Área = {area}\n")

    print("Teste 2 - Calcular base")
    altura = 10
    area = 200
    calcula_base()
    print(f"Base = {base}, Altura = {altura}, Área = {area}\n")

    print("Teste 3 - Calcular altura")
    base = 8
    area = 96
    calcula_altura()
    print(f"Base = {base}, Altura = {altura}, Área = {area}\n")

    print("Teste 4 - Outro cálculo de área")
    base = 7.5
    altura = 3.2
    calcula_area()
    print(f"Base = {base}, Altura = {altura}, Área = {area}\n")

main()
