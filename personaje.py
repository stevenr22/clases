class personaje:
   
    
    #para edirar creo  una clase init
    def __init__(self,nombre,edad,estatura):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        
    def atributos(self):
        print(f'Nombre: {self.nombre}')
        print(f'edad: {self.edad}')
        print(f'Estatura: {self.estatura}')
        
    def año_actual(self,edadDespues):
        self.edad = self.edad+edadDespues
        
    def estatura_comprobacion(self):
        if(self.estatura>0):
            print(f'Tiene estatura')
        elif (self.estatura<0):
            print(f'No tiene estatura')
        else:
            print('No existe')
        
        


#mando los valores q imprimo
mi_personaje = personaje('Galo',22,23)
#llamo los datos con la funcion atributos
mi_personaje.atributos()
print()
#actualizo la edad
mi_personaje.año_actual(56)
#muestro la edad despues del tiempo establecido
mi_personaje.atributos()
print()
print(mi_personaje.estatura_comprobacion())
