   #EXERCICIO 10

#10) Elaborar um programa que efetue a apresentação do valor da conversão em real de um valor
#lido emdólar. O programa deve solicitar o valor da cotação do dólar e também a quantidade de
#dólares disponível com o usuário, para que seja apresentado o valor em moeda brasileira.
cotacao = float(input('informe a cotação do dólar:\n'))
dolar = float(input('informe a quantidade de dólar que você tem:\n'))
reais = dolar * cotacao
print(f'o seu valor na moeda brasileira é:\nR$ {reais}')
