cont = 1
num2 = 0
while cont <= 10:
    num = int(input(f"Digite o {cont}° numero"))
    cont = cont + 1
    if num2 < num:
        num2 = num
print (f"O maior numero foi {num2}.") 

