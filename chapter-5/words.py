from urllib.request import urlopen
from time import sleep
from os import system
import sys


def fetch_words(url):        
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()    # Como la salida HTTP regresa bytes el resultado llega en binario por eso se decodifica a utf8
        #line_words = line.split()                  # Si no se decodifica se imprime mas delante como su representacion en bytes
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    for item in items:
        print(item)  

def main(url):
    # try:
    #     if len(sys.argv) <= 1:
    #         #print(sys.argv[0])  # El primer elemento de argv contiene el nombre del archivo
    #         print('ARGUMENTOS INVALIDOS')
    #         system('sleep 5')
    #         url = 
    #     else:
    #         url = sys.argv[1]
    # except Exception as ex:
    #     print("Ha habido una excepción", type(ex))
    #     return

    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1])