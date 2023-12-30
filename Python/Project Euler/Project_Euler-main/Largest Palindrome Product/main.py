marcador = 0

for i in range(100, 999):
    for m in range(100, 999):
        conta = i * m
        if conta == int(str(conta)[::-1]) and conta > marcador:
                marcador = conta
print(marcador)