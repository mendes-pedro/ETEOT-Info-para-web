salarioAnterior = 0
percentualAplicado = 0
valorAumento = 0
novoSalario = 0

salario = int(input('Digite o salario do colaborador'))
salarioAnterior = salario

if salario <= 280:
    #aumento de 20%
    percentualAplicado = 20
    valorAumento = (salario * percentualAplicado)/100
    novoSalario = salario + valorAumento
elif salario >= 280 and salario <= 700:
    #aumento de 15%
    percentualAplicado = 15
    valorAumento = (salario * percentualAplicado)/100
    novoSalario = salario + valorAumento
elif salario >= 700 and salario <= 1500:
    #aumento de 10%
    percentualAplicado = 10
    valorAumento = (salario * percentualAplicado)/100
    novoSalario = salario + valorAumento
else:
    #salario acima de 1500 = aumento de 5%
    percentualAplicado = 5
    valorAumento = (salario * percentualAplicado)/100
    novoSalario = salario + valorAumento

print("Salario antes do reajuste: ", salarioAnterior)
print("Percentual de aumento: ", percentualAplicado)
print("Valor do aumento: ", valorAumento)
print("Novo salário: ", novoSalario)