'''
    Este ejemplo se utiliza para explicar mejor como se crean, y se utilizan las
    Comprehensions y las funciones como filtros para generar otros iterables.
    La sintaxis para este tipo de Comprehensions es la siguiente:
    
    [ EXPR(item) for item in items if FILTER(item) ] # List Comprehension
    ó:
    { EXPR(item) for item in items if FILTER(item) } # Dict Comprehension
    
    Donde FILTER es una funcion que creamos para poder hacer que el item cumpla 
    con la loginca de dicha funcion la cual debe regresar solo dos valores:
    True o False
'''

from math import sqrt
from pprint import pp

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x))+ 1):
        #print(i)
        if x % i == 0:
            return False
    return True

def get_primes(limit):
    lst_primes = []
    for i in range(limit):
        if is_prime(i):
            lst_primes.append(i)
    return lst_primes


if __name__ == '__main__':
    print("primos: ",get_primes(101))
    # Aqui generamos la misma lista usando una List Comprehension
    # y como filtro la funcion is_prime(x) para condicionar cuales
    # numeros iran en la lista, que en este caso deben ser solo los
    # numeros primos
    p = [ x for x in range(101) if is_prime(x) ]
    print("primos: ", p)
    # Tambien podemos crear un diccionario con los primeros numeros
    # primos dentro del rango de 1 a 20 como claves y como valor una
    # tupla que contenga 3 de sus multiplos. Para esto usamos una
    # dict Comprehension y una funcion como filtro
    m = { x*x : (1, x, x*x) for x in range(20) if is_prime(x) }
    pp(m)