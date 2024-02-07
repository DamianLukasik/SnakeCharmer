#-*- coding: utf8 -*-

import sys

# Wzór na ciag liczb Pella:
# P(n) = 2 * P(n-1) + P(n-2)
def pell(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        pell_sequence = [0, 1]
        for i in range(2, n):
            pell_sequence.append(2 * pell_sequence[-1] + pell_sequence[-2])
        return pell_sequence

if __name__ == "__main__":
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        if sys.argv[1] == "--range":
            try:
                num = int(sys.argv[2])
                pell_sequence = pell(num)
                if len(sys.argv) == 4 and (sys.argv[3] == "--onlyresult" or sys.argv[3] == "--or"):
                    print("{}".format(pell_sequence))
                else:
                    print("Ciag liczb Pella do numeru {}: {}".format(num, pell_sequence))                
            except ValueError:
                print("Błędny numer. Podaj liczbę całkowitą dodatnią.")
        elif sys.argv[1] == "--get":
            try:
                num = int(sys.argv[2])
                last_pell_num = pell(num)[-1]
                if len(sys.argv) == 4 and (sys.argv[3] == "--onlyresult" or sys.argv[3] == "--or"):
                    print("{}".format(last_pell_num))
                else:
                    print("Ostatnia liczba z ciagu liczb Pella do numeru {}: {}".format(num, last_pell_num))
            except ValueError:
                print("Błędny numer. Podaj liczbę całkowitą dodatnią.")
        else:
            print("Niepoprawna opcja. Dostępne opcje: --range, --get")
    else:
        print("Podaj opcję --range lub --get oraz numer.")
