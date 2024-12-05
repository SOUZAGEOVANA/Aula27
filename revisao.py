#ler entrada de usuário
menu_escolha = int(input()) # variavel que guarda qual opção do menu o usuário vai escolha
if menu_escolha == 1: # se escolha for para realizar um cadastro
   situacao = ""
   alunos = []
   cont = 0 #variavel que controla a repetição
   escolha_usuario = int(input("digite quanos alunos voce deseja cadastrar"))
  

   while cont < escolha_usuario: 
    nome = input() #ARMAZENAR o nome do aluno
    nota1 = float(input())# 4 notas do aluno
    nota2 = float(input())# 4 notas do aluno
    nota3 = float(input())# 4 notas do aluno
    nota4 = float(input())# 4 notas do aluno


    faltas = int(input("digite a quantidade de faltas"))
        #calculo de media
    media = (nota1+nota2+nota3+nota4)/4
        #logica da situaçao
    if faltas > 31 :
   situacao ="reprovado por faltas"
   elif media >= 8:
  situacao = "aprovado"
        
   elif media >= 5: #recuperação
            recuperacao= float(input("digite a nota da recuperacao"))#ler a nota da prova de recuperaçaõ
      if recuperacao >= (10-media):
                situacao = "reprovado na recuperaçõ"
       else:
            situacao = "reprovado por media"
    #enviar os dados do aluno para a lista alunos
    alunos.append([nome,faltas,media,situacao])
    cont += 1
    #relatorio
print(alunos)
   


