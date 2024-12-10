#cadastro de usuário e senha
saldo = 0.0 #varialvel que guardará o saldo do usuário
while True:
    #menu principal
    print("Bem vindo! \n  Digite 1. cadastrar 2.login 3.encerrar:")
    #ler a escolha do usuário 
    escolha_menu = int(input()) #lê a escolha como um número inteiro

    #se usuário escolher cadastro
    if escolha_menu == 1:
        #criar um usuário e uma senha com o tipo  string
        usuario = input("crie um nome de usuário:")
        senha = input("Crie uma senha:")
    elif escolha_menu == 2: #se usuário escolher login 
        #comprar as inf. cadastradas com leitura
        login_usuario = input ("digite seu usuário:")
        login_senha =  input("digite sua senha:")
        if login_usuario == usuario and login_senha == senha:
             print("LOGIN REALIZADO COM SUCESSO:")
             #se login correto , entra no
             #menu principal do app
             while True: #enquanto que exibirá o menu principal
                print("1.deposito 2.sacar 3.pix 4.extrato 5.encerrar:")
                escolha_principal = int(input())
                if escolha_principal == 1:
                       #lê o valor a ser depositado
                    valor_deposito = float(input("DIGITE O VALOR DO DEPOSITO:"))
                    saldo = saldo + valor_deposito #atualiza o valor 
               
                elif escolha_principal == 2: #saque
                    valor_saque = float(("digite o valor do saque:"))   
                    senha_saque = input("digite sua senha:")
                    if senha_saque == senha: #se a senha correta
                        saldo = saldo - valor_saque #subtrai o valor do saldo 
                    else:   
                        print("senha incorreta")
                elif escolha_principal == 3 #se usuario escolher pix
                    valor_pix = float(input("digite o valor do pix:"))
                    senha_pix = input("digite sua senha:")
                    if senha_pix == senha:
                       saldo = saldo - valor_pix
                    else:
                       print("senha incorreta:")
                elif escolha_principal == 4: #se usuario escolher visualizar o extrato
                     senha_extrato = input("digite sua senha:")
                     if senha_extrato == senha:
                         print("extrato",saldo)
                elif escolha_principal == 5 #encerrar
                      senha_encerrar = input("digite sua senha:") 
                      if senha_encerrar == senha:  
                            break           
        
        else:
               print("usuário ou senha incorretos")  