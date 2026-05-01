catalogo = {
    "Accion": 3,
    "Comedia": 2,
    "Terror": 4
}

total = 0

while True:
    print("-Menú de Alquiler-")
    print("1. Ver catálogo de películas")
    print("2. Alquilar película")
    print("3. Ver total a pagar")
    print("4. Salir")

    opcion = input("Seleccione una opción : ")

    if opcion == "1":
        print("-Catálogo disponible: ")
        for genero, precio in catalogo.items():
            print(f"{genero}: ${precio}")

    elif opcion == "2":
        print("-Seleccione el género de la película: ")
        for genero in catalogo.keys():
            print("-", genero)
        pelicula = input("Ingrese el género: ").capitalize()

        if pelicula in catalogo:
            total += catalogo[pelicula]
            print(f"Has alquilado una película de {pelicula}. Total acumulado: ${total}")
        else:
            print("Error el género no es válido.")

    elif opcion == "3":
        print(f"El total a pagar es: ${total}")

    elif opcion == "4":
        print("-Gracias por usar el sistema de alquiler de peliculas-")
        break

    else:
        print("Opción inválida. Intente nuevamente.")

