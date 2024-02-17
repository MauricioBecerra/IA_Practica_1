import os

#Funcion para borrar la pantalla detectando primero el SO donde se ejecuto el script
def borrarPantalla(): 
    if os.name == "posix": #La funcion .name obtiene el SO usado y lo compara con el de linux y windows
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

def capitulo_6():
    cap6 = "-Python.\n-JavaScript.\n-Java.\n-PHP.\n-TypeScript.\n-SQL.\n-COBOL.\n-C++.\n-Ruby"
    print("Ejercicio 15: \n" + cap6)

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

main()
