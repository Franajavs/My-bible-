import random

options = ('piedra', 'papel', 'tijera')

usted_gano = 0
computer_gano = 0

rounds = 1

while True:

  print("*" * 10)
  print('ROUND', rounds)
  print("*" * 10)

  print('computer_gano:', computer_gano)
  print('usted_gano:', usted_gano)

  usted_option = input('piedra, papel o tijera => ')
  usted_option = usted_option.lower()

  rounds += 1

  if not usted_option in options:
    print('esa opcion no es valida')
    continue
  computer_option = random.choice(options)

  if usted_option == computer_option:
    print('Empate!')
  elif usted_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('usted gano!')
      usted_gano += 1
    else:
      print('papel gana a piedra')
      print('computer gano!')
      computer_gano += 1
  elif usted_option == 'papel':
    if computer_option == 'piedra':
      print("papel gana a piedra")
      print("usted gano!")
      usted_gano += 1
    else:
      print("tijera gana a papel")
      print("computer gano!")
      computer_gano += 1
  elif usted_option == 'tijera':
    if computer_option == 'papel':
      print("tijera gana a papel")
      print("usted gano!")
      usted_gano += 1
    else:
      print("piedra gana a tijera")
      print("computer gano!")
      computer_gano += 1

  if computer_gano == 2:
    print('El ganador is computer')
    break

  if usted_gano == 2:
    print('El ganador is usted')
    break
