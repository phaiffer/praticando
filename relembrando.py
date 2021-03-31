from datetime import date
today = date.today()

nome = str(input("Digite o seu nome: "))
print(f"-------------------------------------Bem vindo {nome}-------------------------------------")
idade = int(input("Digite sua idade: "))
sex = str(input("Digite seu genero (M/F):  ")).upper()
#dia = int(input("Digite o dia do seu aniversario: "))
#mes = int(input("Digite o mes do seu aniversario: "))
#ano = int(input("Digite o ano do seu aniversario: "))
print("-------------------------------------------------------------------------------------------")
#print(f"Seu nome é {nome}, voce nasceu {dia}/{mes}/{ano}, voce é do genero {sex}, e tem {idade} anos")
print(f"Seu nome é {nome}, voce é do genero {sex}, e tem {idade} anos")

#Verificando se a pessoa que passou as informações é obrigado a votar
print(f"-----------------------------Verificando se {nome} pode votar-----------------------------")
if idade < 16:
    print(f"{nome} você nao tem idade para votar")
elif (idade > 16) and (idade < 18):
    print(f"{nome} você nao é obrigado a votar")
elif idade >= 60:
    print(f"{nome} seu voto é opicional agora")
else:
    print(f"{nome} você é obrigado a votar")

#Verificando se a pessoa que passou as informações tem idade para servir
if sex != 'M':
    print(f"{nome}, voce nao é obrigada a servir!")
else:
    if idade < 17:
        print(f"{nome} ainda nao tem idade para se alistar")
        if idade == 17:
            print(f"{nome} voce deve se alistar ano que vem")
    elif idade == 18:
        print(f"{nome} voce deve se alistar, caso contrario vai pagar uma multa")
    else:
        if idade > 18:
            resp = str(input("Voce ja se apresentou no quartel? [S/N]")).upper()
            if resp == 'N':
                print(f"{nome} deveria ter se apresentado com 18 anos, agora que tem {idade} anos vai pagar uma multa")

#Finalizando codigo
print(f"----------------------------Obrigado por participar {nome}--------------------------------")
print(f"-------------------------------------Volte sempre-------------------------------------")
