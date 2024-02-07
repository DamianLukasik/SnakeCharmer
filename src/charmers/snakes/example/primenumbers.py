#-*- coding: utf8 -*-

import sys

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        if sys.argv[1] == "--range":
            try:
                num = int(sys.argv[2])
                prime_nums = prime_numbers(num)
                if len(sys.argv) == 4 and (sys.argv[3] == "--onlyresult" or sys.argv[3] == "--or"):
                    print("{}".format(prime_nums))
                else:
                    print("Liczby pierwsze w zakresie od 2 do {}: {}".format(num, prime_nums))                
            except ValueError:
                print("Błędny zakres. Podaj liczbę całkowitą większą niż 1.")
        elif sys.argv[1] == "--get":
            try:
                num = int(sys.argv[2])
                last_prime_nums = prime_numbers(num)[-1]
                if len(sys.argv) == 4 and (sys.argv[3] == "--onlyresult" or sys.argv[3] == "--or"):
                    print("{}".format(last_prime_nums))
                else:
                    print("Liczba pierwsza z pozycji {}: {}".format(num, last_prime_nums))
            except ValueError:
                print("Błędny numer. Podaj liczbę całkowitą dodatnią.")
        else:
            print("Niepoprawna opcja. Dostępne opcje: --range, --get")
    else:
        print("Podaj opcję --range lub --get oraz numer.")
