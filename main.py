import re

def lineRead(line, contenido_html):
    if line == "\n":
        contenido_html += "<br>"
        return contenido_html
    spaces = countSpaces(line)
    if re.search(r'\#', line):
        contenido_html = comentarioEncontrado(line, contenido_html, spaces)
    elif re.search(r'\bdef\b', line):
        contenido_html = funcionEncontrada(line, contenido_html)
    elif re.search(r'\bif\b', line):
        contenido_html = ifEncontrado(line, contenido_html)
    elif re.search(r'\belse\b', line):
        contenido_html = elseEncontrado(line, contenido_html)
    elif re.search(r'\+|\-|\*|\^|\/|\%|\&\&|\|{2}|\!', line):
        contenido_html = operadorEncontrado(line, contenido_html, spaces)
    else:
        if spaces > 0:
            contenido_html += f"<p>{addSpaces(line, spaces)}</p>"
        else:
            contenido_html += f"<p>{line, spaces}</p>"
        return contenido_html
    return contenido_html

def countSpaces(line):
    count = 0
    index = 0
    while line[index] == " ":
        count+=1
        index+=1
    return count

def addSpaces(line, spaces):
    result = ""
    for i in range(0, int(spaces)):
        result += "&nbsp;"
    result += line
    return result

def comentarioEncontrado(line, contenido_html, spaces):
    if spaces > 0:
        contenido_html += f"<p>{addSpaces(line, spaces)}</p>"
    else:
        contenido_html += f'<p><span class="comment">{line}</span></p>'
    return contenido_html

def funcionEncontrada(line, contenido_html):
    prueba = re.findall(r'\((.*?)\)', line)
    if prueba == [""]:
        resultado = re.sub(r'\bdef\b', '<span class="function">def</span>', line)
        contenido_html += f"<p>{resultado}</p>"
        return contenido_html
    resultado = re.sub(rf'{prueba[0]}', f'<span class="param">{prueba[0]}</span>', line)
    resultado = re.sub(r'\bdef\b', '<span class="function">def</span>', resultado)
    contenido_html += f"<p>{resultado}</p>"
    return contenido_html

def ifEncontrado(line, contenido_html):
    resultado = re.sub(r'\bif\b', '<span class="ifelse">if</span>', line)
    contenido_html += f"<p>{resultado}</p>"
    return contenido_html

def elseEncontrado(line, contenido_html):
    resultado = re.sub(r'\belse\b', '<span class="ifelse">else</span>', line)
    contenido_html += f"<p>{resultado}</p>"
    return contenido_html

def operadorEncontrado(line, contenido_html, spaces):
    resultado = line
    if re.search(r'\/', line):
        resultado = re.sub(r'\/', f'<span class="operator">/</span>', resultado)
    if re.search(r'\+', line):
        resultado = re.sub(r'\+', f'<span class="operator">+</span>', resultado)
    if re.search(r'\-', line):
        resultado = re.sub(r'\-', f'<span class="operator">-</span>', resultado)
    if re.search(r'\*', line):
        resultado = re.sub(r'\*', f'<span class="operator">*</span>', resultado)
    if re.search(r'\^', line):
        resultado = re.sub(r'\^', f'<span class="operator">^</span>', resultado)
    if re.search(r'\%', line):
        resultado = re.sub(r'\%', f'<span class="operator">%</span>', resultado)
    if re.search(r'\&\&', line):
        resultado = re.sub(r'\&\&', f'<span class="operator">&&</span>', resultado)
    if re.search(r'\|{2}', line):
        resultado = re.sub(r'\|{2}', f'<span class="operator">||</span>', resultado)
    if re.search(r'\!', line):
        resultado = re.sub(r'\!', f'<span class="operator">!</span>', resultado)
    if spaces > 0:
        contenido_html += f"<p>{addSpaces(resultado, spaces)}</p>"
    else:
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
        .param {
            color: #1129ff;
        }
        .comment {
            color: #008206;
        }
        .function {
            color: #ff6e00;
        }
        .ifelse {
            color: #ff5bbd;
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