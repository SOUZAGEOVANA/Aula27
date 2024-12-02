#ler entrada de usuário
nome = input() #ARMAZENAR o nome do aluno
nota1 = float(input())# 4 notas do aluno
nota2 = float(input())# 4 notas do aluno
nota3 = float(input())# 4 notas do aluno
nota4 = float(input())# 4 notas do aluno

faltas = int(input())

#caculo da média
media = (nota1+nota2+nota3+nota4)/4

#logica da situaçao
if faltas > 31:
    situacao = "Reprovado por faltas"
elif media >= 8 :
    situacao = "aprovado"
elif media >= 5: #recuperação
      recuperacao= float(input())#ler a nota da prova de recuperaçaõ
      if recuperacao >= (10-media):
      
      else:

      situacao = "reprovado na recuperaçõ"
else:
      situacao = "reprovado por media"

#relatorio
print("nome", nome)
print("notas", nota1,nota2,nota3,nota4)
print("faltas", faltas)
print("média",media)
print("situação",situacao)

