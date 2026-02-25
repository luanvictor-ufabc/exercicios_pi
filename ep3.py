# EX1

def obter_valor_funcao(a, b, c):
    return a + c * (b * (b + 1) // 2)

# EX2

t1 = float(input())
t2 = float(input())
t3 = float(input())
p1 = float(input())
p2 = float(input())

T = (t1 + t2 + t3) / 3

NF = 0.2 * T + 0.4 * p1 + 0.4 * p2

if NF >= 9.0:
    CF = "A"
elif NF >= 7.5:
    CF = "B"
elif NF >= 6.0:
    CF = "C"
elif NF >= 5.0:
    CF = "D"
else:
    CF = "F"

print(f"{NF:.2f}")
print(CF)

# EX3

n = int(input())

soma = 0

valor = int(input())
soma += valor
minimo = valor
maximo = valor

for _ in range(n - 1):
    valor = int(input())
    soma += valor

    if valor < minimo:
        minimo = valor
    if valor > maximo:
        maximo = valor

media = soma / n

print(soma)
print(f"{media:.2f}")
print(minimo)
print(maximo)

# EX4

n = int(input())

contA = contB = contC = contD = contF = 0
soma = 0

for _ in range(n):
    nota = float(input())
    soma += nota

    if 9 <= nota <= 10:
        contA += 1
    elif 8 <= nota < 9:
        contB += 1
    elif 7 <= nota < 8:
        contC += 1
    elif 5 <= nota < 7:
        contD += 1
    else:
        contF += 1

media = soma / n

print(f"A: {contA}")
print(f"B: {contB}")
print(f"C: {contC}")
print(f"D: {contD}")
print(f"F: {contF}")
print(f"Media: {media:.2f}")

# EX5

soma = 0
quantidade = 0

while True:
    num = int(input())

    if num == 0:
        break

    soma += num
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

print(f"{media:.2f}")

# EX6

n = int(input())

for i in range(1, n + 1):
    print(str(i) * i)

# EX7 

n = int(input())

resultado = 36 * (n * (n + 1) // 2 + n)

print(resultado)

# EX8

n = int(input())

qtd = 0
num = 2

while qtd < n:
    divisores = 0

    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1

    if divisores == 2:
        print(num)
        qtd += 1

    num += 1

# EX9

def calcular_pi(n):
    soma = 0.0

    for i in range(n):
        termo = 1 / (2 * i + 1)

        if i % 2 == 0:
            soma += termo
        else:
            soma -= termo

    return 4 * soma

# EX10 

n = int(input())

n = abs(n) 
if n == 0:
    print(0)

while n > 0:
    print(n % 10)
    n //= 10

# EX11

n = int(input())

for i in range(1, n + 1):

    for _ in range(n - i):
        print("-", end="")

    for _ in range(2 * i - 1):
        print("1", end="")

    for _ in range(n - i):
        print("-", end="")

    print()
