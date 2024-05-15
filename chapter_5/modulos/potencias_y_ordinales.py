import os
import time

def nth_root(radicand, n):
    return radicand ** (1/n)

def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'

def ordinal(value):
    return str(value) + ordinal_suffix(value)

def display_nht_root(radicand, n):
    root = nth_root(radicand, n)
    message = "The " + ordinal(n) + " root of " \
              + str(radicand) + " is " + str(root)
    print(message)
    print('__name__ = ', __name__)



# Si quiero probar mi archivo pero que no se ejecute lo que esta despues del if
# cuando importamos este archivo como modulo en otro archivo se hace lo siguiente:
if __name__ == "__main__":      # __name__ conteendra el nombre que se le asigna al modulo al momento de ejecutarse.
    os.system('clear')          # Si recibe main, es que se se esta ejecutando de forma directa, y si recibe su propio
    print('\n\n')               # nombre significa que esta siendo llamado mediante import en otro modulo o archivo.
    time.sleep(5)
    x = display_nht_root(27,4)  # Esto nos demuestra que una funcion que no devuelve un valor
    print('x es igual a: ', x)  # siempre nos va a regresar None.
    print('\n\n')
    print('__name__ = ', __name__)
    print('\n\n')
else:
    print('__name__ =', __name__) # Esto es solo pára probar que si se imprima el nombre del archivo desde otro modulo
                                  # Si lo importo desde REPL se imprimira una sola o unica vez
                                  # Si lo importo desde otro modulo se imprimira tantas veces como llame al modulo