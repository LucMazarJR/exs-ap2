'''
Crie um algoritimo que, ao receber as informações de início e término de um evento, 
calcule e apresente sua duração total. A entrada consiste em quatro linhas: "Dia DD" para o dia de início, 
seguido por "HH:MM:SS" para a hora de início; e repetindo o mesmo formato para o término do evento. 
A saída deve exibir a duração em dias, horas, minutos e segundos, respectivamente, conforme o padrão 
"W dia(s)", "X hora(s)", "Y minuto(s)", "Z segundo(s)
Considere que os dias são do mesmo mês
'''

# Receber dados
diaI = int(input("Digite o dia de início: "))
horasI = input("Digite o horário de início do evento (HH:MM:SS): ").split(":")
diaF = int(input("Digite o dia de término: "))
horasF = input("Digite o horário de término do evento (HH:MM:SS): ").split(":")

# Tratar dados
# Converter strings para inteiros
for i in range(3):
    horasI[i] = int(horasI[i])
    horasF[i] = int(horasF[i])

# Converter tudo para segundos
segundos_inicio = diaI * 86400 + horasI[0] * 3600 + horasI[1] * 60 + horasI[2] #86400 = segundos em um dia, 3600 = segundos em uma hora
segundos_fim = diaF * 86400 + horasF[0] * 3600 + horasF[1] * 60 + horasF[2]

# Calcular duração total em segundos
duracao_total = segundos_fim - segundos_inicio

# Converter de volta para dias, horas, minutos e segundos
dias = duracao_total // 86400 # Divisão inteira (//) mostra os dias
duracao_total %= 86400  # Mostra quantos segundos ainda restam no periodo, e usando a mesma lógica no resto descobre o valor de cada um
horas = duracao_total // 3600
duracao_total %= 3600
minutos = duracao_total // 60
segundos = duracao_total % 60

# Exibir resultado
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")

