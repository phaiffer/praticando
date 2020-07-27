import datetime

#=======================================================================================================================
#                                      Inicio o codigo aqui coletando informações
#=======================================================================================================================
nome = str(input("Qual o seu nome? "))
# aqui temos o dia atual e o dia que o usuario vai informar
dia_atual = datetime.date.today().day
dia_informado = int(input("Qual o dia do seu nascimento: "))

# aqui temos o mes atual e o mes que o usuario vai informar
mes_atual = datetime.date.today().month
mes_informado = int(input("Qual o mes do seu nascimento: "))

# aqui temos o ano atual e o ano que o usuario vai informar
ano_atual = datetime.date.today().year
ano_informado = int(input("Qual o ano do seu nascimento: "))
#=======================================================================================================================
#                                       Aqui faço a validação das informações
#=======================================================================================================================
# Verifica se o mes atual é menor que o mes informado pelo usuario
if mes_atual < mes_informado:
    idade: int = (ano_atual - ano_informado)-1
# Verifica se o mes atual é o mesmo que o informado pelo usario
elif mes_atual == mes_informado:
    # Verificando se a data atual é maior que a data informada pelo usuario
    if dia_atual >= dia_informado:
        idade = (ano_atual - ano_informado)
# Verificando se a data atual é menor que a data informada pelo usuario
    else:
        idade = (ano_atual - ano_informado)-1
# Caso o mes atual for maior que o mes informado pelo usuario ele entra nessa condição
else:
    idade = (ano_atual - ano_informado)
#=======================================================================================================================
#                                           Aqui imprimo as informações 
#=======================================================================================================================

# Aqui foi utilizado para mostrar se o codigo funcionou corretamente
print(f"Ola {nome}, voce nasceu {dia_informado}/{mes_informado}/{ano_informado} e tem {idade} anos")
