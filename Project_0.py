# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 11:02:03 2022

@author: fuque
"""

x = "(if (blocked-p) (move 1) (skip)) (defvar rotate 3)"
y = x.split()
print(y)
#Revisa si una cadena puede ser convertida a un str
def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False
    

def check_functions(lista, x):
    check = False
    for element in lista:
        if x == element:
            check = True
    return check

valid = ["(defvar", "(=", "(move", "(turn", "(face", "(put", "(pick", "(move-dir","(run-dirs","(move-face","(skip)","(if","(loop","(repeat", "(defun"]
conditions = ["(facing-p","(can-put-p","(can-pick-p","(can-move-p", "(not"]

#Revisa si defvar esta bien.
def check_defvar(lista: list):
    c = False
    if len(lista) == 3:
        if lista[0] == "(defvar":
            if type(lista[1]) == str:
                cadena = lista[2]
                cadena = cadena.replace(")","")
                c = check_float(cadena)
    return c, lista[1]
print(check_defvar(y))
#Revisa si el = esta bien
def check_equal(lista):
    c = False
    if len(lista) == 3:
        if lista[0] == "(=":
            if type(lista[1]) == str:
                cadena = lista[2]
                cadena = cadena.replace(")","")
                c = check_float(cadena)
    return c #, lista[1] (creo que no hace falta ponerla en la nueva lista de variables aceptadas, porque ya estaba inicializada)

#Revisa move
def check_move(lista):
    c = False
    if len(lista) ==2:
        if lista[0] == "(move":
            cadena = lista[1]
            cadena = cadena.replace(")","")
            c = check_float(cadena)
    return c

#Revisa turn
def check_turn(lista):
    c = False
    if len(lista) ==2:
        if lista[0] == "(turn":
            if (lista[1] == ":left)") or (lista[1] == ":right)") or (lista[1] == ":around)"):
                c = True
    return c

#Revisa face
def check_face(lista):
    c = False
    if len(lista) ==2:
        if lista[0] == "(face":
            if (lista[1] == ":north)") or (lista[1] == ":south)") or (lista[1] == ":east)") or (lista[1] == ":west)"):
                c = True
    return c

#Revisa put

def check_put(lista):
    c = False
    if len(lista) == 3:
        if lista[0] == "(put":
            if lista[1] == ":balloons" or lista[1] == ":chips":
                cadena = lista[2]
                cadena = cadena.replace(")","")
                c = check_float(cadena)
    return c

#Revisa pick
def check_pick(lista):
    c = False
    if len(lista) == 3:
        if lista[0] == "(pick":
            if lista[1] == ":balloons" or lista[1] == ":chips":
                cadena = lista[2]
                cadena = cadena.replace(")","")
                c = check_float(cadena)
    return c

#Revisa move-dir
def check_move_dir(lista):
    c = False
    if len(lista) == 3:
        if lista[0] == "(move-dir":
            cadena = lista[1]
            cadena = cadena.replace(")","")
            d = check_float(cadena)
            if d == True:
                if (lista[2] == ":left)") or (lista[2] == ":right)") or (lista[2] == ":front)") or (lista[2] == ":back)"):
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

#Revisa move-face

def check_move_face(lista, lista_variables):
    c = False
    if lista[0] == "(move-face":
        if lista[1] in lista_variables or check_float(lista[1]):
            if (lista[2] == ":north)") or (lista[2] == ":south)") or (lista[2] == ":east)") or (lista[2] == ":west)"):
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
        elif(palabras[0] != "(") and (palabras[-1] != ")"):
            respuesta += " " + palabras + " "
        elif(palabras[-1] == ")"):
            respuesta+= palabras

    return respuesta

def check_ifs(lista: list, condition: list)->bool:
    pass

def start_app(y:list)->None:

    while len(y)!= 0:
        procesar= check_parenthesis(y)
        print(procesar)
            
            
    

                

    
                
            
    

        
        
