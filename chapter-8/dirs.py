
import os
import sys

def make_at(path, dir_name):
    actual_path = os.getcwd()
    
    try:
        os.chdir(path)
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        #Borramos el directorio que es solo de prueba
        os.rmdir(dir_name)
    except Exception as e:
        print(e, file=sys.stderr)
        #raise
    finally:
        os.chdir(actual_path)
        print("Estamos en: ", os.getcwd())

if __name__ == '__main__':
    make_at('/Users/federicomartinezescamilla/cursos/python/plural-python-core','verga')