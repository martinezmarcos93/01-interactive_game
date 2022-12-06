import time

def  elegir_clan():
    elegir_clan=input("A que Clan perteneces?: a)Brujah, b) Gangrel, c)Tremere   :         ")
    print(elegir_clan)    
    if elegir_clan == "a":
     print("Bienvenido al clan Brujah")
    elif elegir_clan == "b":
     print("Bienvenido al clan Gangrel")
    elif elegir_clan == "c":
     print("Bienvenido al clan Tremere")   
   
# enemigos       
ant1_v="Los Ventrue han comprado terrenos cerca de tus dominios, debemos darles una leccion!"   
ant_g="Los Giovanni han robado un poderoso artefacto necromantico, debemos detenerlos!"
ant_S="El Sabath va a atacar la ciudad, debemos alertar a la Camarilla y prepararnos!"

def  elegir_enemigo():
    elegir_enemigo=print(input("Quienes son tus enemigos?: a)Los Ventrue,  b)Los Giovanni, c) El Sabath   :    "))
    print(elegir_enemigo)
    if elegir_enemigo == "a":
     print(ant1_v)
    elif elegir_enemigo == "b":
     print(ant_g)
    elif elegir_enemigo == "c":
     print(ant_S)

# plan
plan_1="Con todo el armamento posible, nos dedicamos a expulsar a esa escoria de nuestro dominio, a costa de la vida de algunos neo natos"
plan_2="Astutamente hemos doblegado todos sus intentos de intromision en nuestro dominio y ahora estan subyugados por nuestra jugada"
plan_3="Esos cobardes nisiquiera se presentaron a la batalla, los buscaremos donde quiera que se escondan"

def  plan_de_ataque():
    plan_de_ataque=input("Como vamos a derrotarlos?: a)Con toda nuestra furia,  b) Silenciosamente y con astucia, c) Cara a cara  :    ")
    print (plan_de_ataque)
    if plan_de_ataque == "a":
       print(plan_1) 
    elif plan_de_ataque == "b":
     print(plan_2)
    elif plan_de_ataque == "c":
     print(plan_3)
    
def  jugarDeNuevo():
    jugarDeNuevo = input('¿Quieres jugar de nuevo? (sí o no):    ')
    if jugarDeNuevo == 'si':
     elegir_clan
     elegir_enemigo
     plan_de_ataque
    else:
        pass
    
elegir_clan
elegir_enemigo
plan_de_ataque

# una funcion con prints para hacer introduccion

# una funcion con inputs para hacer las selecciones

# una funcion que muestre los resultados

# un bucle whhile para jugar de nuevo


# utilizar el import time


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

# def desenlace():
#     desenlacePlan = random.randint("a", "b", "c")
#     if elegir_plan == str(desenlacePlan):
#        print("TU PLAN HA FRACASADO")
#     else:
#          print("TU PLAN HA TRIUNFADO")