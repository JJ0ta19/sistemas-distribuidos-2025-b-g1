def es_palindromo(texto):
    texto_limpio = ''.join(
        c.lower() for c in texto if c.isalnum()
    )
    return texto_limpio == texto_limpio[::-1]

if __name__ == "__main__":
    frase = input("Ingresa una palabra o frase: ")
    if es_palindromo(frase):
        print("¡Es un palíndromo!")
    else:
        print("No es un palíndromo.")