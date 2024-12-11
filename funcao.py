#Declarar uma funçãO
def saudacoes(hora_do_dia): #exebir a saudação correspondente a hora do dia
     #condição para  DAR BOM DIA
    if (hora_do_dia >= 0) and (hora_do_dia <= 12):
         print("BOM DIA!!!")
    #condição para DAR BOA TARDE     
    elif  (hora_do_dia) >= 13 and (hora_do_dia) <= 18:
         print("Boa tarde!")
    else:
         print("boa noite")     
#fora da função
#peço para usuário dizer a hora atual 
resposta = int(input("digite que horas são"))
#chamo a função passando para ela o paramento obrigatorio

saudacoes(resposta)