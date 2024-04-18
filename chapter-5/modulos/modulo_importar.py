'''
    Este modulo fue creado para poder probar que si trae cosas ejecutables,
    al momento de hacer la imortacion las partes ejecutables se mostraran
    una unica vez desde el REPL, con o sin el if de validacion de __name__
'''

def saluda():
    print('Hola Mundo!')

if __name__ != '__main__':
    print(__name__,'cargado!')