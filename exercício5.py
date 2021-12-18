   #EXERCICIO 5

#5) Efetuar o cálculo e a apresentação do valor de uma prestação em atraso, utilizando a fórmula
#PRESTACAO ← VALOR + (VALOR * TAXA/100) * TEMPO).
valor = float(input("olá cliente, infrome o valor do seu debito conosco:"))
tempo = float(input("certo agora nos fale a quanto tempo tem esse debito:"))
prestacao = valor + (valor * 5 / 100) * tempo
print(f"o valor do seu debito è:R$ {prestacao}")
