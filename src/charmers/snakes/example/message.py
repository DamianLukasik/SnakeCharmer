#-*- coding: utf8 -*-

import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        if sys.argv[1] == "--text":
            try:
                text = sys.argv[2]
                print("{}".format(text))                
            except ValueError:
                print("Błąd")
        else:
            print("Niepoprawna opcja. Dostępne opcje: --text")
    else:
        print("Podaj opcję --text oraz tekst.")