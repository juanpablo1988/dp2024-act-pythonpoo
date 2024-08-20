def solicitudTextos():
    textos = []
    for i in range(3):
        texto = input(f"Ingrese un texto {i + 1}: ")
        textos.append(texto)
    return textos
def promedioLongitud(textos):
    total_longitud = sum(len(texto) for texto in textos)
    promedio = total_longitud / len(textos)
    return promedio
def concatTextos(textos):
    concatenados = ''.join(textos)
    longitud = len(concatenados)
    if longitud > 15:
        comparacion = "mayor que"
    elif longitud < 15:
        comparacion = "menor que"
    else:
        comparacion = "igual a"
    return concatenados, comparacion
def texto_mas_largo(textos):
    texto_max = max(textos, key=len)
    return texto_max
def contar_caracteres_numericos(texto):
    return sum(c.isdigit() for c in texto)
textos = solicitudTextos()
promedio = promedioLongitud(textos)
print(f"el promedio es de : {promedio:.2f}")
texto_concatenado, comparacion = concatTextos(textos)
print(f"la concatenación es : '{texto_concatenado}' y la longitud es {comparacion} 15.")
texto_mayor = texto_mas_largo(textos)
print(f"su texto con mas caracteres es: '{texto_mayor}'")
numericos = contar_caracteres_numericos(texto_concatenado)
print(f"la cantidad de texto concatenado es : {numericos}")
