   #EXERCICIO 4


#4) Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um
#automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto
#(TEMPO) e a velocidade média (VELOCIDADE) durante a viagem. Desta forma, será possível obter
#a distância percorrida com a fórmula DISTANCIA ← TEMPO * VELOCIDADE. Possuindo o valor da
#distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula
#LITROS_USADOS ← DISTANCIA / 12. Ao final, o programa deve apresentar os valores da
#velocidade média (VELOCIDADE), tempo gasto na viagem (TEMPO), a distancia percorrida
#(DISTANCIA) e a quantidade de litros (LITROS_USADOS) utilizada na viaga
velocidade = float(input("informe a velocidade em que viajou:\n"))
tempo = float(input("informe o tempo que gastou na viagem:\n"))
distancia = tempo * velocidade
litros_usados = distancia / 12 
print("abaixo estão os dados:\n")
print(f"a velocida foi: {velocidade}\no tempo foi: {tempo}\na distancia foi: {distancia}\nos litros usados: {litros_usados}")
