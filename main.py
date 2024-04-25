import re

# Función que lee una línea y la procesa
def lineRead(line, contenido_html):
    if re.search(r'\#', line):
        contenido_html = comentarioEncontrado(line, contenido_html)
    elif re.search(r'\bdef\b', line):
        contenido_html = funcionEncontrada(line, contenido_html)
    elif re.search(r'\+|\-|\*', line):
        print("ENCONTRADO")
        contenido_html = operadorEncontrado(line, contenido_html)
    else:
        contenido_html += f"<p>{line}</p>"
        return contenido_html
    return contenido_html

# Función que procesa un comentario
def comentarioEncontrado(line, contenido_html):
    contenido_html += f'<p><span class="comment">{line}</span></p>'
    return contenido_html

def funcionEncontrada(line, contenido_html):
    resultado = re.sub(r'\bdef\b', '<span class="function">def</span>', line)
    contenido_html += f"<p>{resultado}</p>"
    return contenido_html

def operadorEncontrado(line, contenido_html):
    operador = re.search(r'\+', line)
    resultado = re.sub(r'\+', f'<span class="operator">{operador.group(0)}</span>', line)
    contenido_html += f"<p>{resultado}</p>"
    return contenido_html


contenido_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lexical Highlighter</title>
    <style>
        /* Estilos CSS aquí */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
        }
        .comment {
            color: #008206;
        }
        .function {
            color: #ff6e00;
        }
        .operator {
            color: #9600aa;
        }
    </style>
</head>
<body>
"""

final_html = """
</body>
</html>
"""

# Leer archivo de texto
with open("input.txt", "r") as file:
    lines = file.readlines()

# Iterar sobre el arreglo de lineas
for line in lines:
    contenido_html = lineRead(line, contenido_html)

# Poner final del html en el contenido_html
contenido_html += final_html

# Escribir archivo html
with open("out.html", "w") as html:
    html.write(contenido_html)