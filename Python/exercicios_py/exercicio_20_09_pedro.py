salario=int(input("digite o valor do salário: "))
if salario <= 280:
    aumento=salario/20*100
    percentual="20%"
elif salario >= 280 and salario <= 700:
        aumento=salario/15*100
        percentual="15%"
elif  salario >= 700 and salario <= 1500:
            aumento=salario/10*100
            percentual="10%"
elif salario >= 1500:
                aumento=salario/5*100
                percentual:"5%"
print("O Salário inicial é:"salario)
print("o percentual de aumento é:"percentual)
print("O valor do aumento foi:"aumento - salario)
print("o novo salário é:"aumento)