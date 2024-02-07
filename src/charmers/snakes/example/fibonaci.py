#-*- coding: utf8 -*-

import sys

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

if __name__ == "__main__":
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        if sys.argv[1] == "--range":
            try:
                num = int(sys.argv[2])
                fib_sequence = fibonacci(num)
                if len(sys.argv) == 4 and (sys.argv[3] == "--onlyresult" or sys.argv[3] == "--or"):
                    print("{}".format(fib_sequence))
                else:
                    print("Ciag Fibonacciego do numeru {}: {}".format(num, fib_sequence))                
            except ValueError:
                print("Błędny numer. Podaj liczbę całkowitą dodatnią.")
        elif sys.argv[1] == "--get":
            try:
                num = int(sys.argv[2])
                last_fib_num = fibonacci(num)[-1]
                if len(sys.argv) == 4 and (sys.argv[3] == "--onlyresult" or sys.argv[3] == "--or"):
                    print("{}".format(last_fib_num))
                else:
                    print("Ostatnia liczba z ciagu Fibonacciego do numeru {}: {}".format(num, last_fib_num))
            except ValueError:
                print("Błędny numer. Podaj liczbę całkowitą dodatnią.")
        else:
            print("Niepoprawna opcja. Dostępne opcje: --range, --get")
    else:
        print("Podaj opcję --range lub --get oraz numer.")
