import os

#Funcion para borrar la pantalla detectando primero el SO donde se ejecuto el script
def borrarPantalla(): 
    if os.name == "posix": #La funcion .name obtiene el SO usado y lo compara con el de linux y windows
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
#Funion para 
def pausa():
    print("Presione cualquier letra para continuar")
    os.system("pause")


def capitulo_2():
    capitulo2 = "Primer variable en python :D"
    print(capitulo2)


def capitulo_3():
    capitulo3_1 = "Mensaje con comillas dobles"
    capitulo3_2 = 'Mensaje con comillas simples'
    print(capitulo3_1)
    print(capitulo3_2)










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
