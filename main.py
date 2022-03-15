import math
import random
import time
import sys
import statistics

sys.setrecursionlimit(10000000)


# generatory danych
# losowe liczby
def losowe(minimum, maximum, length):
    tab = []
    for i in range(length):
        tab.append(random.randint(minimum, maximum))
    return tab


# tablica rosnaca
def rosnaca(length):
    tab = []
    element = random.randint(1, length * 10 - length + 1)
    for i in range(0, length):
        tab.append(element)
        element = random.randint(element + 1, length * 10 - length + 2 + i)
    return tab


# tablica malejaca
def malejaca(length):
    tab = []
    element = random.randint(length, length * 10)
    for i in range(length):
        tab.append(element)
        element = random.randint(length - 1 - i, element - 1)
    return tab


# tablica A-ksztaltna
def a_ksztaltna(length):
    tab = []
    element = random.randint(1, length * 10 - math.floor(length / 2) + 1)
    for i in range(math.floor(length / 2)):
        tab.append(element)
        if j != math.floor(length / 2) - 1:
            element = random.randint(element + 1, length * 10 - math.floor(length / 2) + i + 2)
    element = random.randint(length // 2, element - 1)
    for i in range(length // 2):
        tab.append(element)
        element = random.randint(length // 2 - i - 1, element - 1)
    return tab


# tablica V-ksztaltna
def v_ksztaltna(length):
    tab = []
    element = random.randint(math.floor(length/2), length * 10)
    for i in range(math.floor(length / 2)):
        tab.append(element)
        if j != math.floor(length / 2) - 1:
            element = random.randint(math.floor(length / 2) - i - 1, element - 1)
    element = random.randint(element + 1, length * 10 - length // 2 + 1)
    for i in range(length // 2):
        tab.append(element)
        element = random.randint(element + 1, length * 10 - length // 2 + i + 2)
    return tab


# insertion sort
def insertion_sort(array, tryb):
    global czasy, operacje
    zamian = 0
    porownan = 0
    start = time.time()
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        porownan += 1
        while j >= 0 and key > array[j]:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key
            zamian += 1
            if j >= 0:
                porownan += 1
    end = time.time()
    print("czas operacji: ", (end - start))
    print("ilosc zamian: ", zamian)
    print("ilosc porownan: ", porownan)
    czasy.append(end - start)
    operacje.append(zamian + porownan)
    if tryb == 't':
        print(*array)
    return array


# MERGE SORT
porownan_merge = 0
scalen_merge = 0
def merge_sort(array):
    if len(array) > 1:
        srodek = len(array) // 2
        lewa = array[:srodek]
        prawa = array[srodek:]
        merge_sort(lewa)
        merge_sort(prawa)
        i = 0
        j = 0
        k = 0
        while i < len(lewa) and j < len(prawa):
            global porownan_merge
            porownan_merge += 1
            if lewa[i] >= prawa[j]:
                array[k] = lewa[i]
                i += 1
            else:
                array[k] = prawa[j]
                j += 1
            k += 1
        while i < len(lewa):
            array[k] = lewa[i]
            i += 1
            k += 1
        while j < len(prawa):
            array[k] = prawa[j]
            j += 1
            k += 1
        global scalen_merge
        scalen_merge += 1
    return array


def pomiary_merge_sort(mer_list, tryb):
    global porownan_merge, scalen_merge, czasy, operacje
    start = time.time()
    sort_list = merge_sort(mer_list)
    end = time.time()
    print("czas operacji: ", (end - start))
    print("liczba porownan: ", porownan_merge)
    czasy.append(end - start)
    operacje.append(porownan_merge)
    if tryb == 't':
        print("liczba scalen: ", scalen_merge)
        print('Ciag wyjsciowy: ', *sort_list)
    porownan_merge = 0
    scalen_merge = 0


# HEAP SORT
porownan_heap = 0
zamian_heap = 0
def heap(array, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    global porownan_heap, zamian_heap
    if l < n:
        porownan_heap += 1
        if array[l] < array[smallest]:
            smallest = l
    if r < n:
        porownan_heap += 1
        if array[r] < array[smallest]:
            smallest = r
    if smallest != i:
        zamian_heap += 1
        array[i], array[smallest] = array[smallest], array[i]
        heap(array, n, smallest)


def heap_sort(array, tryb):
    global zamian_heap, porownan_heap, czasy, operacje
    n = len(array)
    start = time.time()
    for i in range(int(n / 2) - 1, -1, -1):
        heap(array, n, i)
    for i in range(n - 1, -1, -1):
        zamian_heap += 1
        array[0], array[i] = array[i], array[0]
        heap(array, i, 0)
    end = time.time()
    print('Czas operacji: ', end - start)
    print('Porownan: ', porownan_heap)
    print('Zamian: ', zamian_heap)
    czasy.append(end - start)
    operacje.append(porownan_heap + zamian_heap)
    if tryb == 't':
        print('Ciag wyjsciowy: ', *array)
    zamian_heap = 0
    porownan_heap = 0


# SHELL SORT KNUTH SEQUENCE
def shell_sort(array, tryb):
    global czasy, operacje
    porownan_shell = 0
    zamian_shell = 0
    start = time.time()
    gap = 1
    while gap <= len(array) // 3:
        gap = gap * 3 + 1
    while gap > 0:
        if tryb == 't':
            print("przeskok: ", gap)
        for i in range(gap, n):
            temp = array[i]
            j = i
            porownan_shell += 1
            while j >= gap and array[j - gap] < temp:
                array[j] = array[j - gap]
                j -= gap
                zamian_shell += 1
                if j >= gap:
                    porownan_shell += 1
            array[j] = temp
        gap = (gap - 1) // 3
    end = time.time()
    print("czas operacji: ", end - start)
    print("porownan: ", porownan_shell)
    print("zamian: ", zamian_shell)
    czasy.append(end - start)
    operacje.append(porownan_shell + zamian_shell)
    if tryb == 't':
        print('Ciag wyjsciowy: ', *array)


# QUICK SORT RECURSION:
qsort_porownan = 0
qsort_zamian = 0
def partition(array, low, high, tryb):
    global qsort_zamian, qsort_porownan
    pivot = array[high]
    if tryb == 't':  # warunek zostal dodany poniewaz tylko gdy wprowadzamy dane recznie mamy wyswietlac pivota, gdy generujemy dane jest on niepotrzebny
        print("pivot: ", pivot)
    i = low - 1
    for j in range(low, high):
        qsort_porownan += 1
        if array[j] > pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
            qsort_zamian += 1
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    qsort_zamian += 1
    return i + 1


def quick_sort(array, low, high, tryb):
    if low < high:
        pi = partition(array, low, high, tryb)
        quick_sort(array, low, pi - 1, tryb)
        quick_sort(array, pi + 1, high, tryb)


def pomiary_quick_sort(array, low, high, tryb):
    global qsort_zamian, qsort_porownan, czasy, operacje
    start = time.time()
    quick_sort(array, low,  high, tryb)
    end = time.time()
    print("Porownan: ", qsort_porownan)
    print("Zamian: ", qsort_zamian)
    print("czas operacji: ", end - start)
    czasy.append(end - start)
    operacje.append(qsort_porownan + qsort_zamian)
    if tryb == 't':
        print('Ciag wyjsciowy: ', *array)
    qsort_porownan = 0
    qsort_zamian = 0


# Czesc sterujaca programem
def rodzaj_sortowania(ciag, tryb, tablica):  # tryb okresla czy program ma dane wprowadzane recznie czy generuje je sam
    if ciag == 1:
        return pomiary_merge_sort(tablica, tryb)
    elif ciag == 2:
        return heap_sort(tablica, tryb)
    elif ciag == 3:
        return insertion_sort(tablica, tryb)
    elif ciag == 4:
        return shell_sort(tablica, tryb)
    elif ciag == 5:
        return pomiary_quick_sort(tablica, 0, len(tablica) - 1, tryb)


# program pyta uzytkownika czy chce wprowadzac dane recznie czy chce korzystac z generatora danych
print("Czy chcesz wprowadzic dane recznie? (t/n)")
ans = input()
czasy = []
operacje = []
if ans == 't':
    print('Wprowadz dane uzywajac spacji')
    tab = list(map(int, input().split()))

    n = len(tab)

    print('Wybierz rodzaj sortowania: 1) Merge sort 2) Heap sort 3) Insertion sort 4) Shell sort 5) Quick sort')
    rodzaj = int(input())

    print('Ciag wejsciowy: ', *tab)
    rodzaj_sortowania(rodzaj, ans, tab)

elif ans == 'n':
    print('Podaj dlugosc ciagu: ')
    n = int(input())

    print("Wybierz rodzaj ciagu: 1) losowy 2) rosnacy 3) malejacy 4) A-ksztaltny 5) V-ksztaltny")
    ciag = int(input())

    print('Wybierz rodzaj sortowania: 1) Merge sort 2) Heap sort 3) Insertion sort 4) Shell sort 5) Quick sort')
    rodzaj = int(input())
    print('_______________________________________________________________________')

    for j in range(1):  # petla dodana aby wygenerowac 10 roznych dlugosci ciagow - wystarczy zmienic range
        #n += j * 250
        #print('n: ', n)
        for i in range(10):
            print("Pomiar nr: ", i + 1)
            if ciag == 1:
                tab = losowe(1, 10 * n, n)
                rodzaj_sortowania(rodzaj, ans, tab)
            elif ciag == 2:
                tab = rosnaca(n)
                rodzaj_sortowania(rodzaj, ans, tab)
            elif ciag == 3:
                tab = malejaca(n)
                rodzaj_sortowania(rodzaj, ans, tab)
            elif ciag == 4:
                tab = a_ksztaltna(n)
                rodzaj_sortowania(rodzaj, ans, tab)
            elif ciag == 5:
                tab = v_ksztaltna(n)
                rodzaj_sortowania(rodzaj, ans, tab)
            print('______________________________')
        print('Srednia czasu: ', statistics.mean(czasy))
        print('Odchylenie stardardowe: ', statistics.stdev(czasy))
        print('______________________________')
        print('Srednia liczba operacji: ', statistics.mean(operacje))
        print('Odchylenie stardardowe: ', statistics.stdev(operacje))
        print('______________________________')
        #n = 250
        czasy = []
        operacje = []