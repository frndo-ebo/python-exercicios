# Análise de nome: todas maisuculas, minusculos, len sem espaços e quantas letras tem o primeiro nome

nome=input('Insira seu nome completo: ')
print('Analisando seu nome...')
print(f'Nome em maíusculas: {nome.upper()}')
print(f'Nome em minúsculas: {nome.lower()}')
print(f'Quantidade de letras sem espaços: {len(nome.strip())}')
print(f'Quantidade de letras do primeiro nome: {len(nome.split()[0])}')

print('Aqui está a sua análise completa, caso tenha gostado de nossos serviços, contate-nos novamente!') 
