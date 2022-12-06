import time, random


# clanes
Brujah="Bienvenido al clan Brujah"
Gangrel="Bienvenido al clan Gangrel"
Tremere="Bienvenido al clan Tremere"  
# enemigos       
ant1_v="Los Ventrue han comprado terrenos cerca de tus dominios, debemos darles una leccion!"   
ant_g="Los Giovanni han robado un poderoso artefacto necromantico, debemos detenerlos!"
ant_S="El Sabath va a atacar la ciudad, debemos alertar a la Camarilla y prepararnos!"
# plan
plan_1="Con todo el armamento posible, nos dedicamos a expulsar a esa escoria de nuestro dominio, a costa de la vida de algunos neo natos"
plan_2="Astutamente hemos doblegado todos sus intentos de intromision en nuestro dominio y ahora estan subyugados por nuestra jugada"
plan_3="Esos cobardes nisiquiera se presentaron a la batalla, los buscaremos donde quiera que se escondan"

def introduccion():
    time.sleep(2)
    print("En este momento de inquietudes, la ciudad es un caos de crimen y corrupcion")
    time.sleep(2)
    print("Como neo-nato, es tu deber plantar tu influencia en la ciudad")
    time.sleep(2)
    print("Pero revcuerda, debes mantener y cuidar siempre....LA MASCARADA!!")
    
   
def elegir_aventura():
    elegir_clan=input("A que Clan perteneces?: a)Brujah, b) Gangrel, c)Tremere   :         ")
    time.sleep(2)
    if elegir_clan == "a":
     print("Bienvenido al clan Brujah")
    elif elegir_clan == "b":
     print("Bienvenido al clan Gangrel")
    elif elegir_clan == "c":
     print("Bienvenido al clan Tremere")
    elegir_enemigo=input("Quienes son tus enemigos?: a)Los Ventrue,  b)Los Giovanni, c) El Sabath   :    ")
    time.sleep(2)
    if elegir_enemigo == "a":
     print(ant1_v)
    elif elegir_enemigo == "b":
     print(ant_g)
    elif elegir_enemigo == "c":
     print(ant_S)
    elegir_plan=input("Como vamos a derrotarlos?: a)Con toda nuestra furia,  b) Silenciosamente y con astucia, c) Cara a cara  :    ")
    time.sleep(2)
    if elegir_plan == "a":
       print(plan_1) 
    elif elegir_plan == "b":
     print(plan_2)
    elif elegir_plan == "c":
     print(plan_3)
     
# def desenlace():
#     desenlacePlan = random.randint("a", "b", "c")
#     if elegir_plan == str(desenlacePlan):
#        print("TU PLAN HA FRACASADO")
#     else:
#          print("TU PLAN HA TRIUNFADO")
     
introduccion()
elegir_aventura()
# desenlace()

# print('¿Quieres jugar de nuevo? (sí o no)')
# jugarDeNuevo = input()
# while jugarDeNuevo == 'sí' or jugarDeNuevo == 's':
#     introduccion()
#     aventura= elegir_aventura()

# class jugarDeNuevo():
#   volver_a_empezar=input('¿Quieres jugar de nuevo? (sí o no):  ')
#   while volver_a_empezar == "si" or volver_a_empezar == "s":
#    introduccion()
#    elegir_aventura()
#   volver_a_empezar= ''
   

jugarDeNuevo = input()
if jugarDeNuevo == 'sí' or jugarDeNuevo == 's':

    introduccion()

    elegir_aventura()
    
    # desenlace()

    print('¿Quieres jugar de nuevo? (sí o no):  ')
    jugarDeNuevo = input()
else : 
    print('Hasta la proxima')
    
    

    
