def mostrar_menu():
    print("Menú de opciones:")
    print("1. Saludar")
    print("2. Realizar cálculo")
    print("3. Salir")

def saludar():
    nombre = input("Ingrese su nombre: ")
    print("¡Hola, " + nombre + "!")

def realizar_calculo():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)

mostrar_menu()
opcion = 0

while opcion != 3:
    opcion = int(input("Seleccione una opción (1/2/3): "))

    if opcion == 1:
        saludar()
    elif opcion == 2:
        realizar_calculo()
    elif opcion == 3:
        print("Saliendo...")
    else:
        print("Opción no válida. Intente nuevamente.")
