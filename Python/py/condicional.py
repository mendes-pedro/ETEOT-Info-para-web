# Exercício:
#  Inserir dois valores e depois determinar se o primeiro é maior ou menor que o segundo valor.

num1 = int(input("Digite um número: "))# A primeira variável recebe o nome de "num1" e tem seu valor determinado no tempo de execução pelo usuário através da função "input()" sendo feito um casting para converter o tipo de variável de "string" para "int"
num2 = int(input("Digite outro número: "))# Repete-se o mesmo processo para a segunda variável.


if (num1 == num2):# Inicia-se o processo condicional com "if():". Aonde é retornado um valor booleano de "False" ou "True"
    print(num1, "é igual a ", num2)# A tabulação determina o aninhamento e indica a ação em caso de sucesso no processo.

else:# Em caso de retorno falso "False", o processo segue e inicia-se a condicional "else:", que engloba tudo o que não consta na "if" anterior.
    if (num1 > num2):# Novamente a identação determina o aninhamento nesta segunda fase da condicional
        print(num1, "é maior que ", num2)
    else:# A condicional else não requer parâmetros para funcionar sendo necessário apenas determinar a ação a seguir.
        print(num1, "é menor que", num2)