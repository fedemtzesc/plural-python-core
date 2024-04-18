from urllib.request import urlopen
from time import sleep
from os import system


def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()    # Como la salida HTTP regresa bytes el resultado llega en binario por eso se decodifica a utf8
        #line_words = line.split()                  # Si no se decodifica se imprime mas delante como su representacion en bytes
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_words(story_words):
    for word in story_words:
        print(word)  

def main():
    words = fetch_words()
    print_words(words)

if __name__ == '__main__':
    main()
