num1=int(input("insira o primeiro número: "))
num2=int(input("insira o segundo número: "))

if (num1 == num2):
    print(num1, "é igual a", num2)
else:
    if (num1 > num2):
        print(num1, "é maior que", num2)
    else:
        print(num1, "é menor que", num2)