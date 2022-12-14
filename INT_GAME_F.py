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
    print("Pero recuerda, debes mantener y cuidar siempre....LA MASCARADA!!")
    time.sleep(2)
   
    
def elegirNombre():
    time.sleep(2)
    nombre = input("Buenas noches, ¿cual es su nombre?:  ")
    print("Un enorme placer", nombre)
    time.sleep(2)
  
   
def elegir_aventura():
    elegir_clan=input("A que Clan perteneces,?: a)Brujah, b) Gangrel, c)Tremere   :         ")
    time.sleep(2)
    if elegir_clan == "a":
        time.sleep(2)
        print(Brujah)
        time.sleep(2)
    elif elegir_clan == "b":
        time.sleep(2)
        print(Gangrel)
        time.sleep(2)
    elif elegir_clan == "c":
        time.sleep(2)
        print(Tremere)
        time.sleep(2)
    elegir_enemigo=input("Quienes son tus enemigos?: a)Los Ventrue,  b)Los Giovanni, c) El Sabath   :    ")
    time.sleep(2)
    if elegir_enemigo == "a":
        time.sleep(2)
        print(ant1_v)
        time.sleep(2)
    elif elegir_enemigo == "b":
        time.sleep(2)
        print(ant_g)
        time.sleep(2)
    elif elegir_enemigo == "c":
        time.sleep(2)
        print(ant_S)
        time.sleep(2)
    elegir_plan=input("Como vamos a derrotarlos?: a)Con toda nuestra furia,  b) Silenciosamente y con astucia, c) Cara a cara  :    ")
    time.sleep(2)
    if elegir_plan == "a":
        time.sleep(2)
        print(plan_1)
        time.sleep(2) 
    elif elegir_plan == "b":
        time.sleep(2)
        print(plan_2)
        time.sleep(2)
    elif elegir_plan == "c":
        time.sleep(2)
        print(plan_3)
        time.sleep(2)
     
     
def desenlacePlan():
    time.sleep(2)
    print(random.choice(desenlace))
    time.sleep(2)
          

def repetirJuego():
    jugarDeNuevo = input('¿Quieres jugar de nuevo? (sí o no):  ')
    print(jugarDeNuevo)
    if jugarDeNuevo == 'sí' or jugarDeNuevo == 's':
        introduccion()
        elegirNombre()
        elegir_aventura()
        desenlacePlan()
        repetirJuego()
    else :
        print('Hasta la proxima')
        pass
    
    
