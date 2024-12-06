#ler entrada de usuário
while True:
    menu_escolha = int(input("escolha opção: 1. cadastro: -2:relatorio: -3 para encerrar:")) # variavel que guarda qual opção do menu o usuário vai escolha
    if menu_escolha == 1: # se escolha for para realizar um cadastro
            situacao = ""

            alunos = []
            cont = 0 #variavel que controla a repetição
            escolha_usuario = int(input("digite quantos alunos voce deseja cadastrar:"))
            while cont < escolha_usuario:#infinita
                nome = input("digite nome do aluno:") #ARMAZENAR o nome do aluno
                nota1 = float(input("digite nota 1:"))# 4 notas do aluno
                nota2 = float(input("digite nota 2:"))# 4 notas do aluno
                nota3 = float(input("digite nota 3:"))# 4 notas do aluno
                nota4 = float(input("digite nota 4:"))# 4 notas do aluno


                faltas = int(input("digite a quantidade de faltas:"))
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
    elif menu_escolha ==2: #relatorio
            print(alunos)
    elif menu_escolha == 3:# se o usuario escolheu 3 irá encerrar o programa
        break #quebra a execução do enquanto
        
    
   


