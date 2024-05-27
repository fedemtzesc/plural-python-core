import os
import time

class Animal:
    _nombre=''
    
    def __init__(self, nombre):
        self._nombre = nombre
        
    def __repr__(self):
        return f"El nombre del animal es {self._nombre}"
    
    def moverse(self):
        print("El animal generico se mueve...")


class Perro(Animal):
    def moverse(self):
        print(f"Hola! soy un perro {self._nombre}, y estoy caminando!")
        
    
class Pez(Animal):
    def moverse(self):
        print(f"Hola! soy un pez {self._nombre}, y estoy nadando!")
        
 
class Ave(Animal):
    def moverse(self):
        print(f"Hola! soy un ave {self._nombre}, y estoy volando!")
    
class Reptil(Animal):
    def moverse(self):
        print(f"Hola! soy un reptil {self._nombre}, y me estoy arrastrando!")
    
def mover_animal(animal):
    print(animal)
    animal.moverse()

if __name__== "__main__":
    opcion = -1 
    while opcion!=0:
        os.system("clear")
        print("Que mascota quieres?")
        lst = ['1.Perro','2.Pez','3.Ave','4.Reptil', '0.Salir']
        print('\n', '\n'.join(lst), sep='')
        #print("\t1. Perro \n\t2. Pez \n\t3. Ave \n\t4. Reptil \n\t0. Salir")
        opcion = int(input("\n*** Opcion: "))
        if opcion<0 or opcion > 4:
            print("Valor equivocado!")
            time.sleep(2)
            continue
        
        if opcion != 0:
            nombre = input("Que nombre tiene?:  ")
            if opcion == 1:
                mi_mascota = Perro(nombre)
            elif opcion == 2:
                mi_mascota = Pez(nombre)
            elif opcion == 3:
                mi_mascota = Ave(nombre)
            else:
                mi_mascota = Reptil(nombre)
            # Invocamos a mover_animal() que funciona de forma polimorfica
            mover_animal(mi_mascota)
            print("-------------------------")
            y = input("presione cualquier teclar para continuar...")
        else:
            print("Adios!")
            break
        

