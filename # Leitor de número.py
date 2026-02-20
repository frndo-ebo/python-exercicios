# Leitor de número

num = input('Insira um número de 0 a 9999: ')
while True:
    if num.isdigit() and 0 <= int(num) <= 9999:
        break
    print('Entrada inválida. Insira um número de 0 a 9999')
    num = input('Insira um número de 0 a 9999: ')

print(f'O número informado foi: {num}\nUnidade: {num[-1]}\nDezena: {num[-2]}\nCentena: {num[-3]}\nMilhar: {num[-4]}')
