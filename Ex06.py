val = float(input("Escreva valor do primeiro produto: "))
val2 = float(input("Escreva valor do segundo produto: "))
media1 = (val / 100) * 8
media2 = (val / 100) * 11
final = (val - media1) + (val2 - media2)
print(f"Valor final: {final}")