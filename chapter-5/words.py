from urllib.request import urlopen
from time import sleep
from os import system
from modulos import potencias_y_ordinales as po


def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()    # Como la salida HTTP regresa bytes el resultado llega en binario por eso se decodifica a utf8
        #line_words = line.split()                  # Si no se decodifica se imprime mas delante como su representacion en bytes
        for word in line_words:
            story_words.append(word)

    story.close()
    secs = 5
    system('clear')
    print("Wait until",secs,"seconds", end='', flush=True)
    for second in range(secs+1):
        sleep(1)
        print(' .', end=' ', flush=True)
        
    print('\n')
    for word in story_words:
        print(word)  
    print('\n')

if __name__ == '__main__':
    fetch_words()
    po.display_nht_root(25,2)
