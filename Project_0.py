# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 11:02:03 2022

@author: fuque
"""

x = "(if (blocked-p) (move 1) (skip)) (defvar rotate 3)"
y = x.split()
#print(y)
#Revisa si una cadena puede ser convertida a un str
def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False

def check_skip(lista: list)-> bool:
    check= False
    if "(skip" in lista[0]:
        check= True
    return check

def check_functions(lista, x):
    check = False
    for element in lista:
        if x == element:
            check = True
    return check

valid = ["(defvar", "(=", "(move", "(turn", "(face", "(put", "(pick", "(move-dir","(run-dirs","(move-face","(skip","(if","(loop","(repeat", "(defun"]
conditions = ["(facing-p","(can-put-p","(can-pick-p","(can-move-p", "(not"]

#Funcion para revisar si un elemento esta en una lista. Se implementa al revisar instrucciones que incluyen variables creadas anteriormente.
def rev_lista(x, lista):
    v = False
    if x in lista:
        v = True
    return v


#Revisa si defvar esta bien.
def check_defvar(lista: list):
    c = False
    if len(lista) >= 3:
        if lista[0] == "(defvar":
            if type(lista[1]) == str:
                cadena = lista[2]
                cadena = cadena.replace(")","")
                if cadena != lista[2]: 
                    c = check_float(cadena)
    return c, lista[1]
#Revisa si el = esta bien
def check_equal(lista):
    c = False
    if len(lista) == 3:
        if lista[0] == "(=":
            if type(lista[1]) == str:
                cadena = lista[2]
                cadena = cadena.replace(")","")
                if cadena != lista[2]:   
                    c = check_float(cadena)
    return c #, lista[1] (creo que no hace falta ponerla en la nueva lista de variables aceptadas, porque ya estaba inicializada)

#Revisa move, se arreglo el uso de variables
def check_move(lista, var):
    c = False
    if len(lista) ==2:
        if lista[0] == "(move":
            cadena = lista[1]
            cadena = cadena.replace(")","")
            if cadena != lista[1]:
                d = check_float(cadena)
                e = False
                if rev_lista(cadena, var):
                    e = True
                if d == True or e == True:
                    c = True
    return c



#Revisa turn
def check_turn(lista):
    c = False
    if len(lista) ==2:
        if lista[0] == "(turn":
            if (":left)" in lista[1]) or (":right)" in lista[1]) or (":around)" in lista[1]):
                c = True
    return c

#Revisa face
def check_face(lista):
    c = False
    if len(lista) ==2:
        if lista[0] == "(face":
            if (":north)" in lista[1]) or (":south)" in lista[1]) or (":east)" in lista[1]) or (":west)" in lista[1]):
                c = True
    return c

#Revisa put, arreglo variables

def check_put(lista, var):
    c = False
    if len(lista) == 3:
        if "(put" in lista[0]:
            if lista[1] == ":balloons" or lista[1] == ":chips":
                cadena = lista[2]
                cadena = cadena.replace(")","")
                if cadena != lista[2]:
                    d = check_float(cadena)
                    e = False
                if rev_lista(cadena, var):
                    e = True
                if d == True or e == True:
                    c = True
    return c

#Revisa pick, arreglo variables
def check_pick(lista, var):
    c = False
    if len(lista) == 3:
        if lista[0] == "(pick":
            if lista[1] == ":balloons" or lista[1] == ":chips":
                cadena = lista[2]
                cadena = cadena.replace(")","")
                if cadena != lista[2]:
                    d = check_float(cadena)
                    e = False
                if rev_lista(cadena, var):
                    e = True
                if d == True or e == True:
                    c = True
    return c

#Revisa move-dir, arreglo variables
def check_move_dir(lista, var):
    c = False
    if len(lista) == 3:
        if lista[0] == "(move-dir":
            cadena = lista[1]
            cadena = cadena.replace(")","")
            if cadena != lista[1]:
                d = check_float(cadena)
                e = False
                f = False
                if rev_lista(cadena, var):
                    e = True
                if d == True or e == True:
                    f = True
                if f == True:
                    if (":left)" in lista[2]) or (":right)" in lista[2]) or (":front)" in lista[2]) or (":back)" in lista[2]):
                        c = True
    return c


#Revisa run-dirs

def check_run_dirs(lista):
    c = False
    if lista[0] == "(run-dirs":
        if (lista[1] == "(:left") or (lista[1] == "(:right") or (lista[1] == "(:up") or (lista[1] == "(:down"):
            z = 0
            for i in range(2,len(lista)-2):
                lista1 = []
                x = 0
                if (lista[i] == ":left") or (lista[i] == ":right") or (lista[i] == ":up") or (lista[i] == ":down"):
                    x = 1
                    z += x
                lista1.append(x)
                if z == len(lista1):
                    w = len(lista)-1
                    if (lista[w] == ":left))") or (lista[w] == ":right))") or (lista[w] == ":up))") or (lista[w] == ":down))"):
                        c = True
    return c

#Revisa move-face, arreglo variables

def check_move_face(lista, lista_variables):
    c = False
    if lista[0] == "(move-face":
        if lista[1] in lista_variables or check_float(lista[1]):
            if (":north)" in lista[2]) or (":south)" in lista[2]) or (":east)" in lista[2]) or (":west)" in lista[2]):
                    c = True
    return c

def check_parenthesis(lista: list):
    x=0
    contador_izquierdos= 0
    contador_derechos= 0
    procesamiento= []
    check= True
    indices= []
    respuesta = ""
    while(x < len(lista)) and check:
        indices.append(x)
        palabra= lista[x]
        lista_letras= list(palabra)

        for y in range(len(lista_letras)):
            letra= lista_letras[y]

            if(letra == "("):
                contador_izquierdos+=1
            elif(letra == ")"):
                contador_derechos+=1

            if(contador_derechos == contador_izquierdos) and (contador_izquierdos != 0):
                procesamiento.append(palabra)
                check= False
                break

            elif(y == (len(lista_letras)-1)):
                procesamiento.append(palabra)
        x+=1

    del lista[indices[0]: indices[-1]+1]

    for palabras in procesamiento:
        if(palabras[0] == "("):
            respuesta += palabras
        elif(palabras[0] != "(") and (palabras[-1] != ") "):
            respuesta += " " + palabras + " "
        elif(palabras[-1] == ")"):
            respuesta+= palabras

    return respuesta

#Caso 1 variable
def checkvar_facing(lista):
    c = False
    if len(lista)==2:
        if lista[0] == "(facing-p":
            if (":north)" in lista[1]) or (":south)" in lista[1]) or (":east)" in lista[1]) or (":west)" in lista[1]):
                    c = True
    return c

#Caso 2 variable
def checkvar_can_put(lista, var):
    c = False
    if len(lista) == 3:
        if lista[0] == "(can-put-p":
            if lista[1] == ":balloons" or lista[1] == ":chips":
                cadena = lista[2].replace(")","")
                if cadena != lista[2]:
                    if cadena in var or check_float(cadena):
                        c = True
    return c

#Caso 3 variable
def checkvar_can_pick(lista, var):
    c = False
    if len(lista) == 3:
        if lista[0] == "(can-pick-p":
            if lista[1] == ":balloons" or lista[1] == ":chips":
                cadena = lista[2].replace(")","")
                if cadena != lista[2]:
                    if cadena in var or check_float(cadena):
                        c = True
    return c

#Caso 4 variable
def checkvar_can_move(lista):
    c = False
    if len(lista) == 2:
        if lista[0] == "(can-move-p":
            if (":north)" in lista[1]) or (":south)" in lista[1]) or (":east)" in lista[1]) or (":west)" in lista[1]):
                    c = True
    return c

#Revisa todos los casos 1-4 de variables:
def checkvar_1_4(lista, var):
    c = False
    w = checkvar_facing(lista)
    x = checkvar_can_put(lista, var)
    y = checkvar_can_pick(lista, var)
    z = checkvar_can_move(lista)
    if x == True or w == True or y == True or z == True:
        c = True
    return c

#Revisa el caso 5, el not

def checkvar_not(lista, var):
    c = False
    if lista[0] == "(not":
        nueva_lista = lista[1:len(lista)]
        cadena = nueva_lista[-1]
        lista_cambio = list(cadena)
        del lista_cambio[-1]
        cadena1 = "".join(lista_cambio)
        nueva_lista[-1] = cadena1
        print(nueva_lista)
        if checkvar_1_4(nueva_lista, var) == True:
            c = True
    return c

#Revisa todas las condiciones posibles

def checkvar_todas(lista, var):
    c = False
    a = checkvar_not(lista, var)
    b = checkvar_1_4(lista, var)
    if a == True or b == True:
        c = True
    return c


var = ["hola", "uno", "dos"]
cadena = "(not (can-pick-p :balloons uno))"
print(checkvar_todas(cadena.split(), var))


#Revisa todos los casos a excepcion de crear funciones y definir variables
def check_all_cases_1(lista, var):
    c = False
    a1 = check_defvar(lista)
    a2 = check_equal(lista)
    a3 = check_move(lista, var)
    a4 = check_move_dir(lista, var)
    a5 =check_turn(lista)
    a6 = check_face(lista)
    a7 = check_put(lista, var)
    a8 = check_pick(lista, var)
    a9 = check_move_dir(lista, var)
    a10 = check_run_dirs(lista)
    a11 = check_move_face(lista, var)
    if a1 == True or a2 == True or a3 == True or a4 == True or a5 == True or a6 == True or a7 == True or a8 == True or a9 == True or a10 == True or a11 == True:
        c = True
    return c

def check_repeat(lista: list, var_list: list)-> bool:
    check= False

    if(lista[0] == "(loop"):
        condicional= lista[1].split()

        if checkvar_todas(condicional, var_list):
            existe_funcion= buscar_funcion(lista[2].split(), var_list)

            if(existe_funcion[0]==True):
                check= True
    
    return check

def check_n_parameters(var: str)->int:
    x=0

    if("(put" in var) or ("(pick" in var) or ("(move-dir" in var) or ("(move-face" in var):
        x=3
    elif("(move" in var) or ("(turn" in var) or ("(face" in var):
        x=2
    return x
        
def sub_list_creator(lista: list, posicion1: int)->list:
    x= 0
    counter= posicion1
    respuestas= []

    while counter < len(lista):
        x= check_n_parameters(lista[counter])
        sub_list= lista[counter: counter+x]
        respuestas.append(sub_list)
        counter= x + counter
        if x == 0:
            break

    return respuestas

def check_repeat_times(lista: list, var_list: list)-> bool:
    check= False

    if(lista[0] == "(repeat"):

        if check_float(lista[1]) or rev_lista(lista[1], var_list):
            listas = sub_list_creator(lista, 2)
            print(listas)
            contador= 0
            for n in range(0, len(listas)):
                if(buscar_funcion(listas[n], var_list)):
                    contador+=1
            if contador == len(listas):
                check= True

    return check

def check_conditional(lista: list, var_list: list)-> bool:
    check= False
    if(lista[0] == "(if"):
        condicional= lista[1].split()
        if(checkvar_todas(condicional, var_list)):
            existe_funcion1=  buscar_funcion(lista[2].split(), var_list)
            existe_funcion2=  buscar_funcion(lista[3].split(), var_list)
            if (existe_funcion1[0]==True) and (existe_funcion2[0]==True):
                check= True

    return check

def check_function_def(lista: list, var_list: list)-> bool:
    pass

#Esta función se encarga de revisar el texto para encontrarle una función a analizar
def buscar_funcion(lista: list, list_var: list)->list:
    string= ""
    check= False

    if(lista[0] == "(defvar"):
        check, string = check_defvar(lista)

    elif(lista[0] == "(move"):
        check= check_move(lista, list_var)

    elif(lista[0] == "(turn"):
        check= check_turn(lista)

    elif(lista[0] == "(face"):
        check= check_face(lista)

    elif("(put" in lista[0]):
        check= check_put(lista, list_var)

    elif(lista[0] == "(pick"):
        check= check_pick(lista, list_var)

    elif(lista[0] == "(move_dir"):
        check= check_move_dir(lista, list_var)

    elif(lista[0] == "(run-dirs"):
        check= check_run_dirs(lista)

    elif(lista[0] == "(move-face"):
        check= check_move_face(lista, list_var)

    elif(lista[0] == "(not"):
        check= checkvar_not(lista, list_var)

    elif(lista[0] == "(repeat"):
        check= check_repeat_times(lista, list_var)

    elif(lista[0] == "(if"):
        check= check_conditional(lista, list_var)

    elif(lista[0] == "(loop"):
        check= check_repeat(lista, list_var)

    elif("skip" in lista[0]):
        check= check_skip(lista)

    respuestas= []
    respuestas.append(check)
    respuestas.append(string)
    return respuestas

#Funcion que convierte un .txt a una cadena con todas las lineas concatenadas.
def cargar_datos(nombre: str):
    file = open(nombre, "r")
    cadena = ""
    nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
    for element in nonempty_lines:
        cadena = cadena + " "+element
    file.close()
    return cadena


#Función que corre la app con un ciclo hasta que la lista separada por el .split se acabe
def correr_app()-> None:

    txt_list= cargar_datos("data.txt").split()
    list_var= []
    while len(txt_list) != 0:

        procesar= check_parenthesis(txt_list)
        procesar_list= procesar.split()
        print(procesar)
        print(procesar_list)
        var_procesada= buscar_funcion(procesar_list, list_var)

        if(var_procesada[1] == ""):
            print(var_procesada[0])
        else:
            list_var.append(var_procesada[1])
            print(var_procesada[0])


        
correr_app()
        
        
