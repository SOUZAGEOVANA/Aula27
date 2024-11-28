cont= int(input("quantidade de alunos: "))
nome= input("nome do aluno: ")
nota1= float(input("nota 1: "))
nota2= float(input("nota 2: "))
nota3= float(input("nota 3:"))
nota4= float(input("nota 4: "))
faltas= int(input("numeros de faltas: "))
soma= (nota1+nota2+nota3+nota4)/4
if soma >=8 and faltas <30:
   print(f"{nome} esta aprovado/a") 
elif soma<5 and faltas <30:
    print(f"{nome} esta de recuperação")
    calculo= (10 - soma)
else:
    print(f"{nome} esta de recuperação")
