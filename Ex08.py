media = 0
nome = str(input("Digite seu nome: "))
nota = int(input(f"Digite nota 1: "))
nota2 = int(input(f"Digite nota 2: "))
nota3 = int(input(f"Digite nota 3: "))
media = (nota + nota2 + nota3)/ 3
if media >= 7:
    print(f"Parabéns {nome}! Você foi aprovado")
elif 5 <= media < 7:
    print(f"Você ficou com média {media} e está de recuperação.")
elif media < 5:
    print(f"{nome}, você está reprovado")