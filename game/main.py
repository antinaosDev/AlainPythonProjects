#La funcion define la seleccion de las opciones del usuario y del pc
def selections():
  import random
  
  #Se definen las alternativas disponibles para el pc
  options = {
    1:'Piedra',
    2:'Papel',
    3:'Tijera'
  }
  
  #Se recibe la opción del usuario
  user_option = int(input('Ingrese su opcion:\n\t1.Piedra\n\t2.Papel\n\t3.Tijera\nTu opción aquí--> '))
    
  #Se evalua que la opción del usuario se válida
  while user_option not in (1,2,3):
    print('Ingresa una opción válida\n')
    user_option = int(input('Ingrese su opcion:\n\t1.Piedra\n\t2.Papel\n\t3.Tijera\nTu opción aquí--> '))
  else:
    computer_option = random.choice(list(options.values()))
    return options[user_option],computer_option

#La funcion define el ganador de cada partida
def match():
  #Titulo del Juego
  print('/'*60)
  print('\nEste es el juego de Piedra,Papel o Tijera.Prueba Tu suerte,\ngana el mejor de 3!\n')
  print('/'*60)
  
  #Combinaciónes de la partida
  partida = {
    'Piedra':{
    'Papel':'Perdiste',
    'Tijera':'Ganaste'
    },
    'Papel':{
      'Tijera':'Perdiste',
      'Piedra':'Ganaste'
    },
    'Tijera':{
      'Papel':'Ganaste',
      'Piedra':'Perdiste'
    }
  }

  #Inicio contador de Victorias Usuario/PC
  wins_user = 0
  wins_computer = 0

  #Inicio contador de Partidas
  count = 0
  
 
  #Definición del ganador mediante acumulación de Victorias
  while wins_user < 3 and wins_computer < 3:
    #Se obtienen las opciones del usuario y pc
    while True:
      try:
        user_select, computer_select = selections()
        break
      except ValueError:
        print('\nPor favor, ingrese un valor numérico.\n')
      
      
    #Se suma una partida al contador
    if user_select not in(list(partida.keys())) and computer_select not in(list(partida.keys())):
      count += 0
    else:
      count += 1
      
    #Se define encabezado de las partidas
    print('\n')
    print('*'*40)
    print('RONDA',count)
    print('*'*40)
      
    #Se define empate
    if user_select == computer_select:
      wins_user += 0
      wins_computer += 0
      print(f'\nLa ronda N°{count} es un empate! {user_select} vs {computer_select}\n')
    #Se acumula victoria del usuario
    elif partida[user_select][computer_select] == 'Ganaste':
      wins_user += 1
      print(f'\nGanaste la ronda N°{count}: {user_select} vs {computer_select}. Vas:{wins_user}|{wins_computer}\n')
    #Se acumula la victoria del computador
    else:
      wins_computer += 1
      print(f'\nPerdiste la ronda: {user_select} vs {computer_select}. Vas:{wins_user}|{wins_computer}\n')
       
  else:
    #Usuario Gana la Partida
    if wins_user == 3:
      print('-'*40)
      print(f'\nGanaste la partida, tu tablero: {wins_user}|{wins_computer}.\n\t\tN°Total de rondas:{count}\n')
      print('-'*40)
    #PC gana la partida  
    else:
      print('-'*40)
      print(f'\nPerdiste la partida, tu tablero: {wins_user}|{wins_computer}\n\t\tN°Total de rondas:{count}\n')
      print('-'*40)


#La funcion consulta al usuario si quiere volver a jugar, luego de terminada la partida
def repet():
  #Se Inicia el Juego
  match()
  #Se consulta al usuario si quiere volver a jugar
  question = input('\n¿Desea continuar? (Y/N): ').upper().strip()

  #Loop de desicion para continuar o no, la partida
  while True:
    #Se evalua que el usuario ingrese una opción válida
    while question not in ('Y','N'):
      print('\nIngresa una opción válida.\n')
      question = input('¿Desea continuar? (Y/N): ').upper().strip()
    else:
      #Si la respuesta es 'Y', se vuelve a iniciar una partida
      if question == 'Y':
        match()
        question = input('¿Desea continuar? (Y/N): ').upper().strip()
      #Si la respuesta es 'N', se termina la partida
      else:
        print('\nGracias por jugar!')
        break
    
    
print(repet())