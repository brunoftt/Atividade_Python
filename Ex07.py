num = int(input("Escreva primeiro número: "))
num2 = int(input("Escreva segundo número: "))
if num > num2:
    cont = num2 + 1
    while cont < num:
        print(cont)
        cont = cont + 1
else:
    cont = num + 1
    while cont < num2:
        print(cont)
        cont = cont + 1 