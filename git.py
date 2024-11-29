quantidadealuno = int (input("quantidade de aluno"))
alunos = []
cont=1
situacao = ""
while cont <= quantidadealuno:
    nome = input("nome")
    alunos.append
    #LER AS NOTAS E FALTAS
    fsltas= int(input("quantidade de faltas"))
    nota = float(input("nota1 "))
    nota2 = float(input("nota2 "))
    nota3 = float(input("nota3 "))
    nota4 = float(input("nota4 "))
    media = (nota+nota2+nota3+nota4)/4
    #APROVADO,RECUPERAÇÃO E REPROVADO
if media >= 8 and faltas <=30:
    situacao = "aprovado"
elif media >= 5 and faltas <=30:
    situacao = "recuperacao"
    recuperacao = float(input("nota da recuperação"))
    calculadarecuperacao = (10-media )
    if recuperacao > calculodarecuperacao:
        situacao = "aprovado na recuperaçao"
    else:
          situacao = "reprovado na recuperação"
else:
      situacao = "reprovado"
cont += 1
#nome
print ("nome: ", nome)
#media
print("media:" , media)
#faltas
print("faltas" , faltas)
