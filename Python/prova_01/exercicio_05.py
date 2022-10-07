print("Responda com sim ou nao:")
q1 = input("Esteve no local do crime? ")
q2 = input("Conhece a vítima? ")
q3 = input("Devia dinheiro à vítima? ")
q4 = input("Já praticou algum crime antes? ")
q5 = input("Possui arma de fogo?")
r = [q1,q2,q3,q4,q5]
sus = 0
for x in r:
    if x == 'sim':
        sus = sus+1
    else:
        pass
if sus == 2:
    print("suspeito")
elif sus == 3:
    print("muito suspeito")
elif sus == 4:
    print("Cúmplice")
elif sus == 5:
    print("Culpado")
else:
    print("Inocência presumida")