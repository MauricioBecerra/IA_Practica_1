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
    colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]
    cap9_newlist = ['tres', 'dos', 'cinco', 'cuatro', 'uno']
    print(f"Ejercicio 23: \nDe la siguiente lista 'colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa']', 
          \n¿Que color esta en la posision3?:\nRespuesta: {colores[3]} ")
    print(f"Ejercicio 24: \n¿En qué posición se encuentra el color 'rojo'? ¿y el 'rosa'?\nRespuesta: Rojo en la posicion 0 y rosa en la posision 7")
    print(f"Ejercicio 25: \nCrea una lista que contenga los siguientes valores en las posiciones indicadas.
            \n'uno' en la posición 4.
            \n'dos' en la posición 1.
            \n'tres' en la posición 0.
            \n'cuatro' en la posición 3.
            \n'cinco' en la posición 2.
            \nResultado: 'cap9_newlist = ['tres', 'dos', 'cinco', 'cuatro', 'uno']'")

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
    
main()
