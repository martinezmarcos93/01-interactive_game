import time, random

#Definiendo Variables:
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
#Finales
win = "TU PLAN HA TRIUNFADO"
loose = "TU PLAN HA FALLADO"
desenlace= (win,loose)


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
     print(Brujah)
    elif elegir_clan == "b":
     print(Gangrel)
    elif elegir_clan == "c":
     print(Tremere)
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
     
     
def desenlacePlan():
    print(random.choice(desenlace))
     
     
introduccion()
elegir_aventura()
desenlacePlan()


jugarDeNuevo = input()
if jugarDeNuevo == 'sí' or jugarDeNuevo == 's':

    introduccion()

    elegir_aventura()
    
    desenlacePlan()

    print('¿Quieres jugar de nuevo? (sí o no):  ')
    jugarDeNuevo = input()
else : 
    print('Hasta la proxima')
    
    

    
