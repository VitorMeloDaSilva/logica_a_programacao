   #EXERCICIO 7

#7) Ler quatro números inteiros e apresentar o resultado da adição e multiplicação, baseando-se
#nautilização do conceito da propriedade distributiva. Ou seja, se forem lidas as variáveis A, B, C, e
#D, devem ser somadas e multiplicadas A com B, A com C e A com D. Depois B com C, B com D e
#por fim C com D. Perceba que será necessário efetuar seis operações de adição e seis operações
#de multiplicação e apresentar doze resultados de saída.
a = int(input("digite o valo de a:\n"))
b = int(input("digite o valo de b:\n"))
c = int(input("digite o valo de c:\n"))
d = int(input("digite o valo de d:\n"))
ab = a + b 
ab1 = a * b
ac = a + c 
ac1 = a * c
ad = a + d 
ad1 = a * d
bc = b + c 
bc1 = b * c
bd = b + d 
bd1 = b * d
cd = c + d 
cd1 = c * d
print(f"o valor da soma de ab é:\n{ab}")
print(f"o valor da multiplicação de ab é:\n{ab1}")
print(f"o valor da soma de ac é:\n{ac}")
print(f"o valor da multiplicação de ac é:\n{ac1}")
print(f"o valor da soma de ad é:\n{ad}")
print(f"o valor da multiplicação de ad é:\n{ad1}")
print(f"o valor da soma de bc é:\n{bc}")
print(f"o valor da multiplicação de bc é:\n{bc1}")
print(f"o valor da soma e de bd é:\n{bd}")
print(f"o valor da multiplicação de bd é:\n{bd1}")
print(f"o valor da soma de cd é:\n{cd}")
print(f"o valor da multiplicação de cd é:\n{cd1}")
