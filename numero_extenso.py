#valor por extenso
while True:
  try:
    num = input('De um a 999: ')
    if int(num) < 0:
      print('Digite um número inteiro de 0 a 999')
    else:
      break
  except:
    print('Digite um número inteiro de 0 a 999')

dicionario = {}
dicionario['0 a 9'] =['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dicionario['10 a 19'] = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dicionario['20 a 99'] = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
dicionario['100 a 900'] = ['cem', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

if int(num) in range(0, 10):
  valor = int(num[0])
  print(dicionario['0 a 9'][valor])

if int(num) in range(10, 20):
  valor = int(num[1])
  print(dicionario['10 a 19'][valor])

if int(num) in range(20, 100):
  valor1 = int(num[0]) - 2
  print(f"{dicionario['20 a 99'][valor1]}", end=' ')
  valor2 = int(num[1])
  if valor2 > 0:
    print(f"e {dicionario['0 a 9'][valor2]}")

if int(num) in range(100, 1000):
  if int(num) == 100:
    print('cem')
  else:
    valor1 = int(num[0])
    print(f"{dicionario['100 a 900'][valor1]}", end=' ')
    valor2 = int(num[1]) -2
    if valor2 > 0:
      print(f"e {dicionario['20 a 99'][valor2]}", end=' ')
    valor3 = int(num[2])
    if valor3 > 0:
      print(f"e {dicionario['0 a 9'][valor3]}")








