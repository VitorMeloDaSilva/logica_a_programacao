   #EXERCICIO 2

#2) Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. A fórmula
#de conversão é C ← (F - 32) * (5/9) , sendo F a temperatura em Fahrenheit e C a temperatura em
#Celsius.
Fahrenheit = float(input("qual a temperatura que você quer transformar?"))
Celsius = ( Fahrenheit - 32 )*( 5 / 9 )
print(f"o valor do Celsius é {Celsius}:")
