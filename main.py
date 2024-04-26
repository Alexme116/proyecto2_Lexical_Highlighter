import re

# Función que lee una línea y la procesa con las expresiones regulares 
def lineRead(line, contenido_html):

    if line == "\n":
        contenido_html += "<br>"
        return contenido_html
    
    spaces = countSpaces(line)
    if re.search(r'\#', line):
        newLine = comentarioEncontrado(line, spaces)
    elif re.search(r'\bdef\b', line):
        newLine = funcionEncontrada(line)
    elif re.search(r'\bif\b', line):
        newLine = ifEncontrado(line, spaces)
    elif re.search(r'\belse\b', line):
        newLine = elseEncontrado(line, spaces)
    elif re.search(r'\+|\-|\*|\^|\/|\%|\&\&|\|{2}|\!', line):
        newLine = operadorEncontrado(line, spaces)
    elif re.search(r'\bfor|\bin|\brange\b',line):
        newLine = forEncontrado(line, spaces)
    elif re.search(r'\bwhile|\bbreak\b|\<|\>',line):
        newLine = whileEncontrado(line, spaces)
    else:
        if spaces > 0:
            contenido_html += f"<p>{addSpaces(line, spaces)}</p>"
        else:
            contenido_html += f"<p>{line}</p>"
        return contenido_html
    contenido_html += f"<p>{newLine}</p>"
    return contenido_html

# Funcion del FOR
def forEncontrado(line, spaces):

    resultado = line
    #condicion para palabra reservada de for
    if re.search(r'\bfor\b',resultado):
        resultado = re.sub(r'\bfor\b','<span class="for">for</span>',resultado)
    #condicion para palabra reservada de in
    if re.search(r'\bin\b',resultado):
        resultado = re.sub(r'\bin\b','<span class="for">in</span>',resultado)
    #condicion para palabra reservada de range
    if re.search(r'\brange\b',resultado):
        resultado = re.sub(r'\brange\b','<span class="range">range</span>',resultado)
    #concantenamos todo
    if spaces > 0:
        resultado = addSpaces(resultado, spaces)
    return resultado

def whileEncontrado(line, spaces):
    
    resultado = line
    if re.search(r'\>',resultado):
        resultado = re.sub(r'\>','<span>&gt</span>',resultado)
    if re.search(r'\<',resultado):
        resultado = re.sub(r'\<','<span >&lt</span>',resultado)

    if re.search(r'\bwhile\b',resultado):
        resultado = re.sub(r'\bwhile\b','<span class="while">while</span>',resultado)

    if re.search(r'\bbreak\b',resultado):
        resultado = re.sub(r'\bbreak\b','<span class="while">break</span>',resultado)

    if spaces > 0:
        resultado = addSpaces(resultado, spaces)
    return resultado

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

def comentarioEncontrado(line, spaces):
    if re.match(r'^\s*#', line):
        resultado_busqueda = re.search(r'#[^\n]*', line)
        resultado = re.sub(r'#[^\n]*', f'<span class="comment">{resultado_busqueda.group(0)}</span>', line)
        if spaces > 0:
            resultado = addSpaces(resultado, spaces)
        return resultado
    else:
        if re.search(r'\bdef\b', line):
            newLine = funcionEncontrada(line)
        elif re.search(r'\bif\b', line):
            newLine = ifEncontrado(line, spaces)
        elif re.search(r'\belse\b', line):
            newLine = elseEncontrado(line, spaces)
        elif re.search(r'\+|\-|\*|\^|\/|\%|\&\&|\|{2}|\!', line):
            newLine = operadorEncontrado(line, spaces)
        elif re.search(r'\bfor|\bin|\brange\b', line):
            newLine = forEncontrado(line, spaces)
        elif re.search(r'\bwhile|\bbreak\b|\<|\>', line):
            newLine = whileEncontrado(line, spaces)
        resultado_busqueda = re.search(r'#[^<]*', newLine)
        resultado = re.sub(r'#[^\n]*', f'<span class="comment">{resultado_busqueda.group(0)}</span>', newLine)
        return resultado

def funcionEncontrada(line):
    prueba = re.findall(r'\((.*?)\)', line)
    if prueba == [""]:
        resultado = re.sub(r'\bdef\b', '<span class="function">def</span>', line)
        return resultado
    
    resultado = re.sub(rf'{prueba[0]}', f'<span class="param">{prueba[0]}</span>', line)
    resultado = re.sub(r'\bdef\b', '<span class="function">def</span>', resultado)
    return resultado

def ifEncontrado(line, spaces):
    if re.search(r'\+|\-|\*|\^|\/|\%|\&\&|\|{2}|\!', line):
        newLine = operadorEncontrado(line, spaces=0)
        resultado = re.sub(r'\bif\b', '<span class="ifelse">if</span>', newLine)
    else:
        resultado = re.sub(r'\bif\b', '<span class="ifelse">if</span>', line)
    if spaces > 0:
        resultado = addSpaces(resultado, spaces)
    return resultado

def elseEncontrado(line, spaces):
    resultado = line
    resultado = re.sub(r'\belse\b', '<span class="ifelse">else</span>', line)
    if spaces > 0:
        resultado = addSpaces(resultado, spaces)
    return resultado

def operadorEncontrado(line, spaces):
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
        resultado = addSpaces(resultado, spaces)
    return resultado


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
        .for {
            color: #ff5bbd;
        }
        .range {
            color: #ff6e00;
        }
        .while {
            color: #1129ff;
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
