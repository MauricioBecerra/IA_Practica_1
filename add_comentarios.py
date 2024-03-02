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
