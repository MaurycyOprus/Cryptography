import sympy
import math
from termcolor import colored
import random


def generateBigPrime():
    while True:
        prime = sympy.randprime(1000000, 10000000)
        if prime % 4 == 3:
            break
    return prime


def generateN():
    p = generateBigPrime()
    q = generateBigPrime()
    # p = 1000003
    # q = 2001911
    while p == q:
        q = generateBigPrime()
    return p * q


def nwd(n):
    while True:
        x = random.randint(1,10)
        if math.gcd(n, x) == 1:
            break
    return x


def generateNumber():
    N = generateN()
    x = nwd(N)

    x_ = ["{0:b}".format(x)[-1]]
    for i in range(20000 - 1):
        x = (x ** 2) % N
        x_.append("{0:b}".format(x)[-1])

    # print generowanej liczby
    last_num = ""
    for i in x_:
        last_num += i
    print("Wygenerowana liczba: ")
    print(int(last_num, 2))

    return x_


def test_pojedynczych_bitów(x_):
    last_num = ""
    for i in x_:
        last_num += i

    count = last_num.count("1")
    if 9725 < count < 10275:
        colour = "green"
    else:
        colour = "red"
    print("Liczba jedynek: " + colored(count, colour))


def test_serii(x_):
    count = 0
    temp = ""
    dictionary_1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    dictionary_0 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in x_:
        if count == 0:
            temp = i
            count += 1
        else:
            if i == temp:
                count += 1
            else:
                if temp == '1':
                    if count >= 6:
                        dictionary_1[6] += 1
                    else:
                        dictionary_1[count] += 1
                else:
                    if count >= 6:
                        dictionary_0[6] += 1
                    else:
                        dictionary_0[count] += 1
                count = 1
                temp = i

    # sprawdzanie przedziałów
    print("Serie zer: ")
    if 2315 < dictionary_0[1] < 2685:
        colour_1 = "green"
    else:
        colour_1 = "red"
    if 1114 < dictionary_0[2] < 1386:
        colour_2 = "green"
    else:
        colour_2 = "red"
    if 527 < dictionary_0[3] < 723:
        colour_3 = "green"
    else:
        colour_3 = "red"
    if 240 < dictionary_0[4] < 384:
        colour_4 = "green"
    else:
        colour_4 = "red"
    if 103 < dictionary_0[5] < 209:
        colour_5 = "green"
    else:
        colour_5 = "red"
    if 103 < dictionary_0[6] < 209:
        colour_6 = "green"
    else:
        colour_6 = "red"
    print("1: "+colored(dictionary_0[1], colour_1)+ ", 2: "+colored(dictionary_0[2], colour_2)+", 3: "+colored(dictionary_0[3], colour_3)+", 4: "+colored(dictionary_0[4], colour_4)+", 5: "+colored(dictionary_0[5], colour_5)+", 6 i więcej: "+colored(dictionary_0[6], colour_6))
    print("Serie jedynek: ")
    if 2315 < dictionary_1[1] < 2685:
        colour_1 = "green"
    else:
        colour_1 = "red"
    if 1114 < dictionary_1[2] < 1386:
        colour_2 = "green"
    else:
        colour_2 = "red"
    if 527 < dictionary_1[3] < 723:
        colour_3 = "green"
    else:
        colour_3 = "red"
    if 240 < dictionary_1[4] < 384:
        colour_4 = "green"
    else:
        colour_4 = "red"
    if 103 < dictionary_1[5] < 209:
        colour_5 = "green"
    else:
        colour_5 = "red"
    if 103 < dictionary_1[6] < 209:
        colour_6 = "green"
    else:
        colour_6 = "red"
    print("1: " + colored(dictionary_1[1], colour_1) + ", 2: " + colored(dictionary_1[2], colour_2) + ", 3: " + colored(dictionary_1[3], colour_3) + ", 4: " + colored(dictionary_1[4], colour_4) + ", 5: " + colored(dictionary_1[5],colour_5) + ", 6 i więcej: " + colored(dictionary_1[6], colour_6))


def test_długiej_serii(x_):
    last_num = ""
    for i in x_:
        last_num += i

    count_1 = last_num.count("11111111111111111111111111")
    count_0 = last_num.count("00000000000000000000000000")
    if count_0 == 0:
        colour_0 = "green"
    else:
        colour_0 = "red"
    if count_1 == 0:
        colour_1 = "green"
    else:
        colour_1 = "red"
    print("Liczba serii zer >= 26: " + colored(count_0, colour_0))
    print("Liczba serii jedynek >= 26: " + colored(count_1, colour_1))


def test_pokerowy(x_):
    dictionary_4_bit = {}
    for i in range(5000):
        bits = x_[i] + x_[i + 1] + x_[i + 2] + x_[i + 3]
        i += 3
        if bits not in dictionary_4_bit:
            dictionary_4_bit[bits] = 1
        else:
            dictionary_4_bit[bits] += 1

    value = 0
    for i in dictionary_4_bit:
        value += dictionary_4_bit[i]**2
    x = 16/5000 * value - 5000

    if 2.16 < x < 46.17:
        colour = "green"
    else:
        colour = "red"
    print("Wartość X: " + colored(x, colour))


if __name__ == '__main__':
    number = generateNumber()
    test_pojedynczych_bitów(number)
    test_serii(number)
    test_długiej_serii(number)
    test_pokerowy(number)
