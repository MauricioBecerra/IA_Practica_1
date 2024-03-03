import os

#Funcion para borrar la pantalla detectando primero el SO donde se ejecuto el script
def borrarPantalla(): 
    if os.name == "posix": #La funcion .name obtiene el SO usado y lo comparamos con el de linux y windows
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
#Funion para poner en pausa el programa
def pausa():
    print("\nPresione Enter para continuar")
    input()
    borrarPantalla()

#Practica del capitulo 2
#Ejercicio 1consta en guardar un mensaje en una variable 
#Ejercicio 2 consta en generar 2 variables numericas
#Ejercicio 3 y 4 consta en sumar las 2 variables e imprimir el resultado de las variables del ejercicio 2
def capitulo_2():
    capitulo2 = "Primer variable en python :D" 
    cap_2_num1 = 17
    cap_2_num2 = 5
    resultado = cap_2_num1 + cap_2_num2
    print("Ejercicio 1:")
    print("Mensaje de la variable 'capitulo2'\n" + capitulo2) #Mostramos ejercicio 1
    print("Ejercicio 2:")
    print("Variable 1 = " + str(cap_2_num1) + "\nVariable 2 = " + str(cap_2_num2))
    print("Ejercicio 3 y 4:")
    print("Resultado de la suma de las dos variables: " + str(resultado)) # Mostramos ejercicio 2

#Practica del capitulo 3
#Ejercicio 5 consta en generar 2 variables y guardar un mensaje en ellas usando commilas simples y en otro comillas dobles
#Ejercicio 6 consta en generar una variable con un msg definido e imprimirla
def capitulo_3():
    capitulo3_1 = "Mensaje con comillas dobles"
    capitulo3_2 = 'Mensaje con comillas simples'
    print("Ejercicio 5: "+capitulo3_1)
    print("Ejercicio 5: "+capitulo3_2)
    capitulo3_3 = '"print()" se utiliza para imprimir valores en la consola.'
    print("Ejercicio 6: "+capitulo3_3)


#Practica del capitulo 4
#Ejercicio 7 consta en generar una variable y concatenar 2 strings
#Ejercicio 8 consta en generar dos variables, sumarlas e imprimirlas
def capitulo_4():
    cap4_1 = "Un mensaje " + "separado pero unido" #concatena 2 strings
    print("Ejercicio 7: "+ cap4_1)
    cap4_2 = "Otro mesaje "
    cap4_3 = "que esta separado pero unido"
    cap4_4 = cap4_2 + cap4_3
    print("Ejercicio 8: "+ cap4_4)
    cap4_5 = "Viva "
    print("Ejercicio 9: \n" + "Mensaje: " + cap4_5 + "Mariachis!!")
    cap4_6_nombre = "Mauricio"
    cap4_7_apellido1 = "Becerra"
    cap4_8_apellido2 = "Guzman"
    cap4_9_fullname = cap4_6_nombre + " " + cap4_7_apellido1 + " " + cap4_8_apellido2
    print("Ejercicio 10: \nNombre: "+ cap4_9_fullname)
    print("Ejercicio 11:\n")
    print("Mensaje: "+"80"+"120")
    
#Practica capitulo 5
#Ejercicio 12 consta de convertir la oracion la primera letra de cada palabra en mayusculas "enrique barros fernández" 
#Ejercicio 13 consta de convertir la oracion la primera letra de cada palabra en minusculas "Esta Es Una Frase Para Ser Formateada."
#Ejercicio 14 consta de convertir la oracion en mayusculas.
def capitulo_5():
    cap5 = "enrique barros fernández".title() #.title() convierte las letras iniciales en mayusculas
    print("Ejercicio 12:")
    print("Mensaje: " + cap5)
    cap5_1 = "Esta Es Una Frase Para Ser Formateada.".lower()#.lower() convierte las letras iniciales en minusculas
    print("Ejercicio 13:")
    print("Mensaje: " + cap5_1)
    cap5_2 = "Esta Es Una Frase Para Ser Formateada.".upper()#.upper() convierte las letras en mayusculas
    print("Ejercicio 14:")
    print("Mensaje: " + cap5_2)

#Practica capitulo 6
#Ejercicio 15 consta de generar una variable string con varios nombres de lenguajes de programacion con un salto de linea y un '-' al inicio de cada lenguaje
def capitulo_6():
    cap6 = "-Python.\n-JavaScript.\n-Java.\n-PHP.\n-TypeScript.\n-SQL.\n-COBOL.\n-C++.\n-Ruby"
    print("Ejercicio 15: \n" + cap6)

#Practica capitulo 7
#Ejercicio 16 consta de guardar una suma en una variable con 3 valores, usando 2 numeros predeterminados y se cumpla la condicion 20+23+x=87
#Ejercicio 17 consta de guardar una resta en una variable con 3 valores, usando 2 numeros predeterminados y se cumpla la condicion x-20-23=-87
#Ejercicio 18 consta de guardar una multiplicacion en una variable con 3 valores, usando 2 numeros predeterminados y se cumpla la condicion 20*23*x=870
#Ejercicio 19 consta de guardar una division en una variable con 3 valores, usando 2 numeros predeterminados y se cumpla la condicion 10 <= 5000/230/x < 11
#Ejercicio 20 consta de solucionar una operacion de 3 valores, usando 3 operadores sin repetir, para que el resultado sea 0
def capitulo_7():
    cap7_suma = 20 + 23 + 45
    cap7_resta = -20 - 23 - 45
    cap7_mult = 20 * 23 * ((870)/(20*23))
    cap7_div = 5000 / 230 / 2
    cap7_operacion = 10 / 5 + 15 - 17
    print("Ejercicio 16: \nSuma: '20 + 23 + 45' = ", cap7_suma,)
    print("Ejercicio 17: \nResta: '-20 - 23 - 45' = ", cap7_resta,)
    print("Ejercicio 18: \nMultiplicacion: '20 * 23 * ((870)/(20*23))' = ", cap7_mult,)
    print("Ejercicio 19: \nDivision: '5000 / 230 / 2' = ", cap7_div,)
    print("Ejercicio 20: \nOperacion con resultado 0: '10 / 5 + 15 - 17' = ",cap7_operacion)

#Practica capitulo 8
#Ejercicio 21 consta de utilizar solo el número 2 (cuantas veces necesites) y sin utilizar exponentes, para obtener el resultado 1024
def capitulo_8():
    cap8_exponencial = 2*2*2*2*2*2*2*2*2*2
    print("Ejercicio 21: \nOperacion: '2*2*2*2*2*2*2*2*2*2' = ",cap8_exponencial)

#Practica capitulo 9
#Ejercicio 22 consta de redondear con 5 decimales el numero '17.567383292929200234' usando la funcion round()
def capitulo_9():
    cap9_redondear = 17.567383292929200234
    print(f"Ejercicio 22: \nRedondear {cap9_redondear} con 5 decimales, resultado: {round(cap9_redondear,5)} ")
    
#Practica capitulo 10
#Ejercicio 23 consta de conocer que color esta en la posicion 3 de la lista colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]
#Ejercicio 24 consta de conocer enn qué posición se encuentra el color 'rojo' y el 'rosa' en la lista del anterior comentario
#Ejercicio 25 consta de Crea una lista que contenga los siguientes valores en las posiciones indicadas.'uno' en la posición 4.'dos' en la posición 1.'tres' en la posición 0.'cuatro' en la posición 3.'cinco' en la posición 2.
def capitulo_10():
    colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa'] #se creo un arreglo
    cap9_newlist = ['tres', 'dos', 'cinco', 'cuatro', 'uno'] #se creo un arreglo
    print(f"""Ejercicio 23: \nDe la siguiente lista "colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa']", 
        \n¿Que color esta en la posision3?:\nRespuesta: {colores[3]} """)    
    print(f"Ejercicio 24: \n¿En qué posición se encuentra el color 'rojo'? ¿y el 'rosa'?\nRespuesta: Rojo en la posicion 0 y rosa en la posision 7")
    print("""Ejercicio 25: \nCrea una lista que contenga los siguientes valores en las posiciones indicadas.
            \n"uno" en la posición 4.
            \n"dos" en la posición 1.
            \n"tres" en la posición 0.
            \n"cuatro" en la posición 3.
            \n"cinco" en la posición 2.
            \nResultado: "cap9_newlist = ['tres', 'dos', 'cinco', 'cuatro', 'uno']" """)
    
#Practica capitulo 11
def capitulo_11():
    cap11_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']#Se crea arreglo de una lista de colores
    print("Ejercicio 26: \nUtiliza las posiciones negativas para acceder e imprimir algunos de los colores de esta lista.\nLos colores a los que tienes que acceder son 'naranja', 'amarillo', 'lila', 'blanco' y 'rojo'.\n")
    print(f"Para el color naranja usamos '-1': {cap11_colores[-1]}")
    print(f"Para el color amarillo usamos '-7': {cap11_colores[-7]}")
    print(f"Para el color lila usamos '-5': {cap11_colores[-5]}")
    print(f"Para el color blanco usamos '-2': {cap11_colores[-2]}")
    print(f"Para el color rojo usamos '-10': {cap11_colores[-10]}")

#Practica capitulo 12
def capitulo_12():
    cap12_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']#Se crea lista de colores
    del cap12_colores[1]#Elimina el dato alojado en la posision indicada
    del cap12_colores[3]#Elimina el dato alojado en la posision indicada
    del cap12_colores[4]#Elimina el dato alojado en la posision indicada
    del cap12_colores[-3]#Elimina el dato alojado en la posision indicada
    print("Ejercicio 27: \nElimina los colores 'azul', 'marrón', 'negro' y 'rosa' de la lista:\ncap12_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']")
    print("Resultado del arreglo: " + "[" + ",".join(cap12_colores) + "]") #Se unen los datos del arreglo o lista con join y separados con una ,

#Practica capitulo 13
def capitulo_13():
    cap13_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
    cap13_colores.remove('amarillo')#usa la funcion remove para eliminar un elemento especifico del arreglo
    cap13_colores.remove('rojo')#usa la funcion remove para eliminar un elemento especifico
    print("Ejercicio 28: \nElimina los elementos 'amarillo' y 'rojo' de la siguiente lista\ncap13_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']")
    print("Resultado del arreglo: "+"[" + ",".join(cap13_colores) + "]") #Se unen los datos del arreglo o lista con join y separados con una ,

#Practica capitulo 14 
def capitulo_14():
    cap14_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
    cap14_colorsgd = [cap14_colores.pop(1), cap14_colores.pop(7)]
    print("Ejercico 29: \n-Elimina los elementos 'azul' y 'blanco' de la lista \n- cap14_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']\n-Utiliza el metodo .pop()")
    print("Los datos almacenados son: " + " y ".join(cap14_colorsgd)) #Se unen los datos del arreglo o lista con join y separados con una ,

#Practica capitulo 15
def capitulo_15():
    cap15_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
    cap15_colores.append('fuxia')
    cap15_colores.append('celeste')
    print("Ejercicio 30: \n-Agrega a la lista: \n- cap15_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] \n-Los colores 'fuxia' y 'celeste'")
    print("Lista con los nuevos colores: [" + ",".join(cap15_colores) + "]" ) #Se unen los datos del arreglo o lista con join y separados con una ,

#Practica capitulo 16  
def capitulo_16():
    cap16_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
    cap16_colores.insert(-4,'magenta')
    cap16_colores.insert(-1,'turquesa')
    print("Ejercicio 31: \n-Agrega a la lista: \n- cap16_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] \n-Los colores 'magenta' y 'turquesa' usando la funcion .insert() con posision negativa.")
    print("Lista con los nuevos colores: [" + ",".join(cap16_colores) + "]" ) #Se unen los datos del arreglo o lista con join y separados con una ,
    
#practica capitulo 17
def capitulo_17():
    cap17_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón','lila', 'negro', 'rosa', 'blanco', 'naranja']
    cap17_colores.sort(reverse=True)
    print("Ejercicio 32: \n-Ordenar la lista: \n- cap17_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón','lila', 'negro', 'rosa', 'blanco', 'naranja'] \n-En orden alfabetico.")
    print("Lista con los nuevos colores: [" + ",".join(cap17_colores) + "]" ) #Se unen los datos del arreglo o lista con join y separados con una ,
    
#Practica capitulo 19
def capitulo_19():
    cap19_colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
    print("Ejercicio 33: \n-Imprimir la segunda posicion de esta tupla: \n- cap18_colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')")
    print("El dato guardado en la segunda posicion es: " + cap19_colores[1])
    cap19_numeros = (10, 1, 5, 11)
    cap19_operacion = cap19_numeros[0] + cap19_numeros[2] + cap19_numeros[3] - cap19_numeros[1] #Se hace una suma
    print("\nEjercicio 34: \n-Utiliza simbolos de suma y resta para obtener el resultado 25, \nla matriz a usar es: cap19_numeros = (10, 1, 5, 11)")
    print("El orden es: cap19_operacion = cap19_numeros[0] + cap19_numeros[2] + cap19_numeros[3] - cap19_numeros[1]")
    print(f"El resultado es: {cap19_operacion}")

#Practica capitulo 20
def capitulo_20():
    cap20_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
    cap20_tuple = tuple(cap20_colores)#Transformamos la lista a tuple
    print("Ejercicio 35: \nUtiliza tuple para convertir una lista e imprime el tipo de lista que es. \nLa lista es: cap20_colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']")
    print("Resultado: " + str(type(cap20_tuple)))

#Practica capitulo 21
def capitulo_21():
    cap21_num1 = 15
    cap21_num2 = 20
    print("Ejercicio 36: \nModifica el operador del condicional para que sea True las variables valen:\n'cap21_num1 = 15' y 'cap21_num2 = 20', el condicional es if cap21_num1 == cap21_num2:")
    if cap21_num1 != cap21_num2: #iniciamos condicional donde cap21_num1 debe ser diferente a cap21_num2
        print('Resultado: Se ejecuta el if con el siguiente orden "cap21_num1 != cap21_num2".')
        
    print("\nEjercicio 37: \nModifica el operador del condicional para que sea True las variables valen:\n'cap21_num1 = 1450' y 'cap21_num2 = 60', el condicional es if cap21_num1 < cap21_num2:")
    if cap21_num1 > cap21_num2: #iniciamos condicional donde cap21_num1 debe ser mayor a cap21_num2
        print('Resultado: Se ejecuta el if con el siguiente orden "cap21_num1 > cap21_num2".')
    
    print("\nEjercicio 38: \nModifica el condicional para que sea False sin modificar el operador las variables valen:\n'cap21_num1 = 1450' y 'cap21_num2 = 60', el condicional es if cap21_num1 != cap21_num2:")
    if cap21_num1 == cap21_num2:#iniciamos condicional donde cap21_num1 debe ser igual a cap21_num2
        print('Hola')
    else: #si no se cumple el condicional donde cap21_num1 debe ser igual a cap21_num2 ejecuta esta accion
        print('Resultado: No se ejecuta el if con el siguiente orden "cap21_num1 = 60" y "cap21_num2 = 60".')    
    
#Practica capitulo 22
def capitulo_22():
    print("Ejercicio 39:")
    print("Arregla el siguiente tramo de codigo:\n----------- \ncolor = rojo\n\nelse color == rojo\nPrint \"El color es rojo.\"\nif color != rojo\nPrint \"El color no es rojo.\"\n-----------\n")
    color = "rojo"
    if color == "rojo":
        print("Resultado: El color es rojo.")
        print("El codigo quedo asi: \n")
        print("if color == \"rojo\":\n\tprint(\"El color es rojo.\")\nelse:\n\tprint(\"El color no es rojo.\")\n-----------")
    else:
        print("El color no es rojo.")
        
def capitulo_23():
    print("Ejercicio 40:")
    band = False #Se crea una bandera
    while band != True:#Se repite el ciclo hasta la bandera sea True
        estatura = input('Ingresa tu estatura en cm: ')
        if estatura.isdigit(): #Comprueba que el valor ingresado sea numerico
            band=True
            estatura=int(estatura)
            if (estatura > 160 ):#Condicional
                print('Eres una persona alta.')
            elif ( estatura <= 160 and estatura > 80): #Condicional si no es puede ser
                print('Eres una persona bajita.')
            elif (estatura < 80):#Condicional si no es puede ser
                print('No puedes ser tan bajito.')
        else:
            print('Ingresa una edad valida.')
        
        
def capitulo_24():
    print("Ejercicio 41:")
    cap24_materia = input('Introduce nombre de una materia: ')
    cap24_materias = ['Matematicas', 'Español', 'Historia', 'Ciencias Naturales']
    if cap24_materia in cap24_materias: #Condicional donde se encarga de ver si la materia ingresada esta en la lista
        print('La materia ingresada se encuentra en la lista.')
    else: #En caso que la materia ingresada no este arroja el siguiente mensaje
        print('La materia ingresada no esta en la lista.')

def capitulo_25():
    print("Ejercicio capitulo 25:")
    band2 = False
    while band2 != True: #Se repite el ciclo hasta la bandera sea True
        cap25_edad = input('Ingresa una edad: ')
        if cap25_edad.isdigit(): #Comprueba que el valor ingresado sea numerico
            band2 = True
            cap25_edad = int(cap25_edad)
            if cap25_edad == 18: #Se crea un condicional
                print('Ingresaste la edad equivalente a ' + str(cap25_edad) + ' años')
            if cap25_edad == 19: #Se crea un condicional
                print('Ingresaste la edad equivalente a ' + str(cap25_edad) + ' años')
            if cap25_edad == 20: #Se crea un condicional
                print('Ingresaste la edad equivalente a ' + str(cap25_edad) + ' años')
            if cap25_edad == 21: #Se crea un condicional
                print('Ingresaste la edad equivalente a ' + str(cap25_edad) + ' años')
            if cap25_edad != 18 or cap25_edad != 21 or cap25_edad != 20 or cap25_edad != 19:
                print('La edad no esta registra en los condicionales.')
        else:
            print('Ingresa una edad valida.')

def capitulo_26():
    cap26_num1 = 50
    cap26_num2 = 200
    print("Ejercicio capitulo 26:")
    print('El numero 1 es mayor que el numero 2') if cap26_num1 > cap26_num2 else print('El numero 1 es mayor que el numero 2') #Condicional con else en una sola linea de codigo.

def capitulo_27():
    print("Ejercicio 42:")
    cap27_x = 0
    while cap27_x <= 15: #Se crea un ciclo while
        print('El valor es: ' + str(cap27_x)) #Imprime de valor de la variable
        cap27_x += 5 #Suma 5 al valor anterior de la variable
    print("Ejercicio 43:")
    cap27_y = 0
    while cap27_y >= -100: #Se crea un ciclo while
        print('El valor es: ' + str(cap27_y)) #Imprime de valor de la variable
        cap27_y -= 20 #Resta 20 al valor anterior de la variable
    print("Ejercicio 44:")
    cap27_z = 10
    while cap27_z >= 0: #Se crea un ciclo while
        print('El valor es: ' + str(cap27_z)) #Imprime de valor de la variable
        cap27_z -= 1 #Resta 1 al valor anterior de la variable
    
def capitulo_28():
    print("Ejercicio 45:")
    cap28_num1 = 0
    while cap28_num1 <= 30:
        cap28_num1 += 1#Incrementa 1 al valor anterior
        if cap28_num1 == 4 or cap28_num1 == 6 or cap28_num1 == 10:#Condicional que se ejecuta cuando la variable toma el valor de 4 o 6 o 10, en cualquiera de esoos 3 casos
            print('Se saltó el valor ' + str(cap28_num1) + ' de cap28_num1') #Imprime el mensaje se salto el valor e imprime el valor de la variable
            continue#hace salto del ciclo
        if cap28_num1 == 15:#ocndicional que comprueba ssi el valor es igual a 15
            print('Se rompió la ejecución del bucle cuando cap28_num1 tomo el valor de: '+ str(cap28_num1))#Imprime el mensaje se rompio el bucle en el valor e imprime el valor de la variable
            break#rompe el ciclo
        print(cap28_num1)

def capitulo_29():
    print("Ejercicio 46:")
    print("Consiste en un ciclo for para mostrar el contenido de un for:")
    cap_29_nombres = ['Mauricio', 'Manuel', 'Diego', 'Edgar', 'Martha', 'Montse', 'Fernando'] #Lista con nombres
    for z in cap_29_nombres: #Se crea un ciclo for de z hasta la longitud del arreglo o lista
        print('El nombre es: ' + z)#Imprime el nombre en la lista en el valor tomado en el ciclo for hasta terminar con el arreglo

def capitulo_30():
    print("Ejercicio 47:")
    print('Crear ciclo for que vaya desde 7 hasta 700 con saltos de 100.')
    for cap36_num1 in range(7, 700 , 100): #Ciclo for que inicia en 7 hasta 700 con incrementos de 100 en 100
        print(cap36_num1)#Imprime el valor de cap36_num1

def capitulo_31():
    cap31_teclado_2 = {#Creamos un diccionario  con datos de categoria, modelo y precio, en este caso de un teclado
        'Categoría': 'Teclados', #Parte del diccionario que contiene la categoria
        'Modelo': 'Corsair K55 RGB', #Parte del diccionario que contiene el modelo
        'Precio': '59,99'#Parte del diccionario que contiene el precio
    }
    print("Ejercicio 48:")
    print('El modelo ', cap31_teclado_2['Modelo'] + ' cuesta ' + ' $ ' +cap31_teclado_2['Precio'])#Imprime los valores del diccionario en el apartado correspondiente.
    
def capitulo_32():
    cap32_teclado_2 = {#Creamos un diccionario  con datos de categoria, modelo y precio, en este caso de un teclado
        'Categoría': 'Teclados', #Parte del diccionario que contiene la categoria
        'Modelo': 'HyperX Alloy FPS Pro', #Parte del diccionario que contiene el modelo
        'Precio': '89,99'#Parte del diccionario que contiene el precio
    }
    print("Ejercicio 49:")
    print('Consiste en imprimir los valores del diccionario con un ciclo for ')
    for z in cap32_teclado_2: #Generamos un for que se repetira la longitud del diccionario
        print(z + ' = ' + cap32_teclado_2[z]) #Imprime el valor de z que sera la key y luego cap32_teclado_2[z] sera el valor en esa key
    
def capitulo_33():
    cap33_1 = {#Creamos un diccionario  con datos de categoria, modelo y precio, en este caso de un teclado
        'Categoría': 'Teclados', #Parte del diccionario que contiene la categoria
        'Modelo': 'HyperX Alloy FPS Pro', #Parte del diccionario que contiene el modelo
        'Precio': '89,99'#Parte del diccionario que contiene el precio
    }
    cap33_2 = {#Creamos un diccionario  con datos de categoria, modelo y precio, en este caso de un teclado
        'Categoría': 'Teclados',#Parte del diccionario que contiene la categoria
        'Modelo': 'Corsair K55 RGB',#Parte del diccionario que contiene el modelo
        'Precio': '59,99'#Parte del diccionario que contiene el precio
    }
    print("Ejercicio 50:")
    del cap33_1 #Se borra el diccionario por completo
    del cap33_2['Categoría']#Se elimina la key junto con su valor del diccionario por completo
    del cap33_2['Precio']#Se elimina la key junto con su valor del diccionario por completo
    print(cap33_2['Modelo'])#Se imprime el diccionario por completo

def capitulo_34():
    def cap_34suma(cap34_numero1, cap34_numero2): #Declaramos una funcion con parametros sin retorno
        print('El resultado de la suma es: ',cap34_numero1 + cap34_numero2)#Hacemos una suma con los dos parametros recibidos y los imprimimos

    print("Ejercicio 51:")
    cap_34suma(10, 20)#llamamos a la funcion y mandamos dos numeros como parametros
    cap_34suma(20, 30)#llamamos a la funcion y mandamos dos numeros como parametros
    cap_34suma(50000, 7000)#llamamos a la funcion y mandamos dos numeros como parametros
    
def capitulo_35():
    print("Ejercicio 52:")
    """
    Este codigo es proporcionado por el curso de aqui debemos reconocer cuantos argumentos existen en cada una de las lineas en la que se llama a la funcion
    def colores(*args):
        pass

    colores('rojo', 'azul', 'verde', 'amarillo')
    colores('lila', 'negro', 'rojo')
    colores('rosa')
    colores('marrón', 'naranja')
    """
    print('Codigo proporcionado: ')
    print("def colores(*args):\n\tpass\ncolores('rojo', 'azul', 'verde', 'amarillo')\ncolores('lila', 'negro', 'rojo')\ncolores('rosa')\ncolores('marrón', 'naranja')")
    print('Los argumentos por linea son: \nLinea 4: 4 argumentps \nLinea 5: 3 argumentos \nLinea 6: 1 argumento \nLinea 7: 2 argumentos')
    print("Ejercicio 53:")
    def cap35_colors(*args):#Creamos una funcion con parametro de args
        print('El color ' + args[1] + ' es mi favorito. El color ' + args[0] + ' tampoco está mal.')#Imprimimos los argumentos ingresados en este caso solamente el argumento 0 y 1

    cap35_colors('Azul', 'Negro')#Llamamos a la funcion mandando los dos colores como parametros
    print("Ejercicio 54:")
    def cap35_suma(*args):#definimos la funcion con parametros args
        cap35_result = args[0] + args[1] + args[2] + args[3] + args[4]#sumamos todos los argumentos
        print('El resultado de la suma de los argumentos es:', cap35_result)#imprimimos la suma

    cap35_suma(14,15,30,85,94)#Llamamos a nuestra funcion

def capitulo_36():
    def cap36_colores (**kwargs):
        print("Este es el color 1 " + kwargs['color_1'] + ' Este es el color 2 ' + kwargs['color_2'])

    print("Ejercicio capitulo 36:")
    cap36_colores(color_1='Negro', color_2='Verde')
    
def capitulo_37():
    class Correo:#Se crea una clase
        name = ''#Se crea un atributo
        password = ''#Se crea un atributo

        def cap37_imprime(self):#Se crea un metodo de la clase
            print('Name: ', self.name, '\nPassword: ', self.password)#Imprime los atributos

    key = Correo()#Creamos un objeto
    print('Ejercicio capitulo 37')
    key.name = 'Mauricio'#Usamos el objeto para llenar los atributos
    key.password = '123456789M'#Usamos el objeto para llenar los atributos
    key.cap37_imprime()#Llama el metodo de la clase

def main():
    print("Practica capitulo #2\n")
    capitulo_2()
    pausa()
    print("Practica capitulo #3\n")
    capitulo_3()
    pausa()
    print("Practica capitulo #4\n")
    capitulo_4()
    pausa()
    print("Practica capitulo #5\n")
    capitulo_5()
    pausa()
    print("Practica capitulo #6\n")
    capitulo_6()
    pausa()
    print("Practica capitulo #7\n")
    capitulo_7()
    pausa()
    print("Practica capitulo #8\n")
    capitulo_8()
    pausa()
    print("Practica capitulo #9\n")
    capitulo_9()
    pausa()
    print("Practica capitulo #10\n")
    capitulo_10()
    pausa()
    print("Practica capitulo #11\n")
    capitulo_11()
    pausa()
    print("Practica capitulo #12\n")
    capitulo_12()
    pausa()
    print("Practica capitulo #13\n")
    capitulo_13()
    pausa()
    print("Practica capitulo #14\n")
    capitulo_14()
    pausa()
    print("Practica capitulo #15\n")
    capitulo_15()
    pausa()
    print("Practica capitulo #16\n")
    capitulo_16()
    pausa()
    print("Practica capitulo #17\n")
    capitulo_17()
    pausa()
    print("Practica capitulo #19\n")
    capitulo_19()
    pausa()
    print("Practica capitulo #20\n")
    capitulo_20()
    pausa()
    print("Practica capitulo #21\n")
    capitulo_21()
    pausa()
    print("Practica capitulo #22\n")
    capitulo_22()
    pausa()
    print("Practica capitulo #23\n")
    capitulo_23()
    pausa()
    print("Practica capitulo #24\n")
    capitulo_24()
    pausa()
    print("Practica capitulo #25\n")
    capitulo_25()
    pausa()
    print("Practica capitulo #26\n")
    capitulo_26()
    pausa()
    print("Practica capitulo #27\n")
    capitulo_27()
    pausa()
    print("Practica capitulo #28\n")
    capitulo_28()
    pausa()
    print("Practica capitulo #29\n")
    capitulo_29()
    pausa()
    print("Practica capitulo #30\n")
    capitulo_30()
    pausa()
    print("Practica capitulo #31\n")
    capitulo_31()
    pausa()
    print("Practica capitulo #32\n")
    capitulo_32()
    pausa()
    print("Practica capitulo #33\n")
    capitulo_33()
    pausa()
    print("Practica capitulo #34\n")
    capitulo_34()
    pausa()
    print("Practica capitulo #35\n")
    capitulo_35()
    pausa()
    print("Practica capitulo #36\n")
    capitulo_36()
    pausa()
    print("Practica capitulo #37\n")
    capitulo_37()
    pausa()
    
main()

#print("Ejercicio 45:")