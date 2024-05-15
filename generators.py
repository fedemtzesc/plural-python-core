'''
    En este ejemplo se muestra como se hace una tuberia (pipelining) entre 
    dos funciones generadoras de iteradores:
    La primera se llama take y sirve para tomar los primeros n numeros del
    iterator que se la pasa como parametro.
    En el ejemplo se le pasa como iterator la funcion distinct que genera 
    un iterador con numeros que no se repiten y que obtiene de un iterable
    que se le pasa como argumento a su vez.
    Conforme se va generando cada yield de distinct estos se pasan a take
    que a su vez conforme genera un nuevo yield lo va subiendo hacia arriba.
'''

from os import system

def take(n, iterator):
    counter = 0
    #print("Funcion Generadora: Iterador: ", next(iterator))
    for item in iterator:
        if counter == n:
            return
        counter += 1
        yield item

def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_pipeline():
    items = [3,6,6,2,1,1,]
    for item in take(3, list(distinct(items))): # List provoca que primero se genere la lista completa del iterador
        print(item)                             # dentro de distinc en vez de usar el valor yield inmediatamente 
                                                # generado como se hace en take
if __name__ == '__main__':
    system('clear')
    run_pipeline()
    print("")

