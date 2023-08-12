class cliente:

    #inicializo los datos
    def __init__(self,nomb_usu,clav_usu):
   
        self.nomb_usu = nomb_usu
        self.clav_usu = clav_usu
   


        #creo la funcion atributos para mostrar los datos
    def perfil(self):
        #print(f'Nombre: {self.nombre}')
        #print(f'Apellido: {self.apellido}')
        #print(f'Edad: {self.edad}')
        #print(f'Ciudadania: {self.ciudadania}')
        #print(f'Celular: {self.celular}')
        #print(f'Email: {self.email}')
        print(f'Nombre de usuario: {self.nomb_usu}')
        print(f'Contraseña: {self.clav_usu}')


    def iniciar_sesion(self,n_u,v_u):
        
        self.n_u = n_u
        self.v_u = v_u

        if (self.nomb_usu == self.n_u) and (self.clav_usu == self.v_u):
            print(f'Inicio exitoso, bienvenido señor {self.nomb_usu}')
            print("--------------------------------------------------")
            print(f'Por favor, ingrese su conjunto de vuelo')
            print()
            print("1. VUELO DIRECTO\n2. VUELO TRANSVORDO\n3. Salir")
            print()
            opcion = 0
        
            while(opcion != 2):
                opcion = int(input("Seleccione una opción (1/2/3)==> "))

                if opcion == 1:
                    print("AH ELEGIDO EL VUELO DIRECTO")
              
                    
                elif opcion == 2:
                    print("AH ELEGIDO EL VUELO TRANSVORDO")

                elif opcion ==3:
                    salir = input("¿Está seguro que desea salir? (s/n): ")
                    if salir.lower() == "s":
                        print("Saliendo...")
                    else:
                        print(f'Por favor, ingrese su conjunto de vuelo')
                        print()
                        print("1. VUELO DIRECTO\n2. VUELO TRANSVORDO\nSalir")
                        print()
                    
              
                    
                else:
                    print("OPCION INVALIDA")
             
            

        else:
            print(f'Usuario o contraseña incorrecta')

#pido al usuario dichos datos
#nom = input("Ingrese el nombre: ")
#ape = input("Ingrese el apellido: ")
#edad = int(input("Ingrese el edad: "))
#ciuda = input("Ingrese el ciudadania: ")
#cel = int(input("Ingrese numero de celular: "))
#email = input("Ingrese el email: ")
nomb_u = input("Ingrese el nombre de usuario: ")
clav_u = input("Ingrese el contraseña: ")
#envio por parametros a la clase padre
#mi_cli = cliente(nom,ape,edad,ciuda,cel,email,nomb_u,clav_u)
#llamo  a la funcion atributos para visualizar los datos ingresados

mi_cli=cliente(nomb_u,clav_u)
mi_cli.iniciar_sesion('Srojas','123')


        