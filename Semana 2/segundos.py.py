texto = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos = int(texto)

dias = segundos // 86400
diferença_seg1 = segundos % 86400
horas = diferença_seg1 // 3600
diferença_seg2 = diferença_seg1 % 3600
minutos = diferença_seg2 // 60
segundos_finais = diferença_seg2 % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos_finais, "segundos.")