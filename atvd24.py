# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.
n = 0
contador = 0
while True:
    numero = float(input('digite os números que deseja calcular a média (digite -1 quando quiser parar): '))
    if numero == -1:
        break
    n += numero
    contador += 1
    mediaCalculada = n/contador
print(f"a média dos números digitados é: {mediaCalculada}")
