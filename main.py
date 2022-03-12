import random
import time


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
    for i in range(0, length):
        tab.append(i)
    return tab


# tablica malejaca
def malejaca(length):
    tab = []
    for i in range(length - 1, -1, -1):
        tab.append(i)
    return tab


# tablica A-ksztaltna
def a_ksztaltna(length):
    tab = []
    for i in range(0, int(length / 2)):
        tab.append(2 * i + 1)
    for i in range(int(length / 2), length):
        tab.append(2 * (length - i))
    return tab


# tablica V-ksztaltna
def v_ksztaltna(length):
    tab = []
    for i in range(0, int(length / 2)):
        tab.append(2 * (int(length / 2) - i))
    for i in range(int(length / 2), length):
        tab.append(2 * (i - int(length / 2)) + 1)
    return tab


# insertion sort
def insertion_sort(array, tryb):
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
    global porownan_merge, scalen_merge
    start = time.time()
    sort_list = merge_sort(mer_list)
    end = time.time()
    print("czas operacji: ", (end - start))
    print("liczba porownan: ", porownan_merge)
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
    global zamian_heap, porownan_heap
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
    if tryb == 't':
        print('Ciag wyjsciowy: ', *array)
    zamian_heap = 0
    porownan_heap = 0


# SHELL SORT KNUTH SEQUENCE
def shell_sort(array, tryb):
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
    if tryb == 't':
        print('Ciag wyjsciowy: ', *array)


# QUICK SORT RECURSION:
def quick_sort(array, tryb):
    if len(array) <= 1: return array
    smaller, equal, larger = [], [], []
    pivot = array[-1]
    if tryb == 't':  # warunek zostal dodany poniewaz tylko gdy wprowadzamy dane recznie mamy wyswietlac pivota, gdy generujemy dane jest on niepotrzebny
        print("pivot: ", pivot)
    porownan = 0
    for i in array:
        if i > pivot:
            larger.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            smaller.append(i)
        porownan += 1
    return quick_sort(larger, tryb) + equal + quick_sort(smaller, tryb)


def pomiar_quick_sort(qui_list, tryb):
    start = time.time()
    sort_list = quick_sort(qui_list, tryb)
    end = time.time()
    print("ilość porównan: ")
    print("czas operacji: ", end - start)
    if tryb == 't':
        print(sort_list)
    #dodać zamiany


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
        return pomiar_quick_sort(tablica, tryb)


# program pyta uzytkownika czy chce wprowadzac dane recznie czy chce korzystac z generatora danych
print("Czy chcesz wprowadzic dane recznie? (t/n)")
ans = input()
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