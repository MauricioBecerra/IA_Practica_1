import ast

archivo_original = "main.py"
archivo_nuevo = "mainconcomentarios.py"

with open(archivo_original, "r") as f:
    codigo = f.read()

arbol_org = ast.parse(codigo)

class AgregarComentarios(ast.NodeTransformer):

    def visit(self, node):
        if isinstance(node, ast.If) or (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "print"):
            comentario = ast.Expr(value=ast.Str(s=f"# Se hace un {node.__class__.__name__.lower()}"))
            # Creamos un nodo que contenga el nodo original y el comentario como una tupla
            nodo = ast.Expr(value=ast.Tuple(elts=[node, comentario], ctx=ast.Load()))
            # No llamamos a self.generic_visit(nodo) dentro del bloque if
            return nodo

        # Si no estamos en un nodo que necesita comentarios, se llama a generic_visit
        return self.generic_visit(node)

# Se crea una instancia de la clase AgregarComentarios
transformador = AgregarComentarios()

# Se aplica el transformador al árbol sintáctico
arbol_modificado = transformador.visit(arbol_org)

# Convertimos el árbol modificado a código python
codigo_modificado = ast.unparse(arbol_modificado)

# Abre el nuevo archivo para escribir el código con los comentarios
with open(archivo_nuevo, "w") as f:
    f.write(codigo_modificado)

print(f"Se ha creado el archivo {archivo_nuevo} con los comentarios.")
