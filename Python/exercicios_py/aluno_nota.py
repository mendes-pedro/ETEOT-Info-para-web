n1 = -1
while not n1 in range(0,11):
    n1 = int(input("Digite um valor entre 0 e 10 para a nota 1: "))
n2 = -1
while not n2 in range(0,11):
    n2 = int(input("Digite um valor entre 0 e 10 para a nota 2: "))
fq = -1
while not fq in range(0,101):
    fq = int(input("Digite um valor entre 0 e 100 para a frequência: "))
media=int((n1+n2)/2)
if media == 10 and fq > 95:
    print("aprovado com distinção!")
elif media >= 7 and fq >= 75:
    print("Aprovado!")
elif media < 7 or fq < 75:
    print("Reprovado!")