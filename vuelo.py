class cliente:

    #inicializo los datos
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        #creo la funcion atributos para mostrar los datos
    def atributos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Edad: {self.edad}')
#pido al usuario dichos datos
nom = input("Ingrese el nombre: ")
ape = input("Ingrese el apellido: ")
edad = int(input("Ingrese el edad: "))
#envio por parametros a la clase padre
mi_hotel = cliente(nom,ape,edad)
#llamo  a la funcion atributos para visualizar los datos ingresados
mi_hotel.atributos()


        