class cliente:

    #inicializo los datos
    def __init__(self,nombre,apellido,edad,ciudadania,celular,email,nomb_usu,clav_usu):
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudadania = ciudadania
        self.celular = celular
        self.email = email
        self.nomb_usu = nomb_usu
        self.clav_usu = clav_usu
   


        #creo la funcion atributos para mostrar los datos
    def atributos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Edad: {self.edad}')
        print(f'Ciudadania: {self.ciudadania}')
        print(f'Celular: {self.celular}')
        print(f'Email: {self.email}')
        print(f'Nombre de usuario: {self.nomb_usu}')
        print(f'Contraseña: {self.clav_usu}')

    def iniciar_sesion(self,n_u,v_u):
        self.n_u = n_u
        self.v_u = v_u

        if (self.nomb_usu == self.n_u) and (self.clav_usu == self.v_u):
            print(f'Inicio exitoso, bienvenido señor {self.nombre}+{self.apellido}')
        else:
            print(f'Usuario o contraseña incorrecta')

#pido al usuario dichos datos
nom = input("Ingrese el nombre: ")
ape = input("Ingrese el apellido: ")
edad = int(input("Ingrese el edad: "))
ciuda = input("Ingrese el ciudadania: ")
cel = int(input("Ingrese numero de celular: "))
email = input("Ingrese el email: ")
nomb_u = input("Ingrese el nombre de usuario: ")
clav_u = input("Ingrese el contraseña: ")
#envio por parametros a la clase padre
mi_cli = cliente(nom,ape,edad,ciuda,cel,email,nomb_u,clav_u)
#llamo  a la funcion atributos para visualizar los datos ingresados
mi_cli.iniciar_sesion('Srojas','123')


        