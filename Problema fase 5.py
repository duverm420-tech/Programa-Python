# Problema 4 fase 5
# Videoteca digital

# Matriz de videoteca digital
#[titulo, año, calificación, género] 

videoteca = [
    ["Avatar", 2022, 9,"ciencia ficción"],
    ["Avengers endgame", 2019, 10,"acción"],
    ["El señor de los anillos", 2001, 8,"fantasía"],
    ["El código Da Vinci", 2006, 6,"misterio"],
    ["Batman: el caballero de la noche", 2008, 9,"superhéroes"],
    ["Mario bros", 2023, 7,"Animación"],
    ["Titanic", 1997, 8,"romance"]
]

# Funcion para contar titulos de videoteca

def contar_titulos(matriz, umbral, año_limite):
    contador = 0
    for titulo in matriz:
        if titulo[2] >= umbral and titulo[1] >= año_limite:
            contador += 1
    return contador

# Solicitar al usuario el umbral de calificación y el año límite

print("===================================")
print(" Bienvenido a la Videoteca Digital")
print("===================================")

Calificacion_minima = int(input("Ingrese el umbral de calificación (0-10): "))
Año_limite = int(input("Ingrese el año límite: "))

# Llamar a la función para contar los títulos que cumplen con los criterios

resultado = contar_titulos(videoteca, Calificacion_minima, Año_limite)