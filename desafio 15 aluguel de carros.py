KM = float(input('Qual foi a quantidade de kms percorridos:'))
dia = float(input('qual a quantidade de dias que o carro foi alugado: '))
VKM = KM*0.15
vdia = dia*60
Preço = dia + KM
print('O valor por km rodado foi R${}\nO valor por dia foi R${}\nO valor total ficou em R${}'.format(VKM, vdia, Preço))