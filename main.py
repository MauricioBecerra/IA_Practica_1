import os

#Funcion para borrar la pantalla detectando primero el SO donde se ejecuto el script
def borrarPantalla(): 
    if os.name == "posix": #La funcion .name obtiene el SO usado y lo compara con el de linux y windows
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
#Funion para poner en pausa el programa
def pausa():
    print("Presione cualquier letra para continuar")
    os.system("pause")

#Practica del capitulo 2
#Ejercicio 1consta en guardar un mensaje en una variable 
#Ejercicio 2 consta en generar 2 variables numericas
#Ejercicio 3 consta en sumar las 2 variables e imprimir el resultado de las variables del ejercicio 2
def capitulo_2():
    capitulo2 = "Primer variable en python :D" 
    cap_2_num1 = 17
    cap_2_num2 = 5
    resultado = cap_2_num1 + cap_2_num2
    print("Ejercicio 1")
    print("Mensaje de la variable 'capitulo2'\n" + capitulo2) #Mostramos ejercicio 1
    print("Ejercicio 2")
    print("Variable 1 = " + cap_2_num1 + "\nVariable 2 = " + cap_2_num2)
    print("Ejercicio 3")
    print("Resultado de la suma de las dos variables: " + resultado) # Mostramos ejercicio 2


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
def capitulo_4():
    cap4_1 = "Un mensaje" + "separado pero unido"









def main():
    print("Practica capitulo #2")
    capitulo_2()
    pausa()
    borrarPantalla()
    print("Practica capitulo #3")
    capitulo_3()
    pausa()
    borrarPantalla()


main()
