"""Al final este codigo no se uso por la debida falta de dedicacion para su funcionalidad definitiva se lograron dos version
la primera version comentaba pero dejaba el codigo con errores de sintaxys asi que se procedio a una solucion mas basica que era
editar el archivo.py como sifuera un archivo txt, identificando las funcniones usadas en python y agregar su mensaje correspondiente, lo cual no se termino de 
desarrollar y quedo en un proyecto en desarrollo"""
archivo_original = "main.py"
archivo_nuevo = "mainconcomentarios.py"

with open(archivo_original, "r") as f:
    lineas = f.readlines()
# Agregar comentarios después de las llamadas a la función print
for i, linea in enumerate(lineas):
    if "print(" in linea:
        lineas[i] = linea.rstrip() + " # Se imprime un texto con un print\n"
# Guardar las líneas modificadas en el nuevo archivo
with open(archivo_nuevo, "w") as f:
    f.writelines(lineas)

print(f"Se ha creado el archivo {archivo_nuevo} con comentarios después de las llamadas a la función print.")
