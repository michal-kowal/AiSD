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


#tablica malejaca
def malejaca(length):
    tab = []
    for i in range(length - 1, -1, -1):
        tab.append(i)
    return tab


#tablica A-ksztaltna
def a_ksztaltna(length):
    tab = []
    for i in range(0, int(length / 2)):
        tab.append(2 * i + 1)
    for i in range(int(length / 2), length):
        tab.append(2 * (length - i))
    return tab


#tablica V-ksztaltna
def v_ksztaltna(length):
    tab = []
    for i in range(0, int(length / 2)):
        tab.append(2 * (int(length / 2) - i))
    for i in range(int(length / 2), length):
        tab.append(2 * (i - int(length / 2)) + 1)
    return tab



# insertion sort
def insertion_sort(array):
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
            if j>=0:
                porownan += 1
    end = time.time()
    print("czas operacji: ", (end - start))
    print("ilosc zamian: ", zamian)
    print("ilosc porownan: ", porownan)
    print(array)
    return array


print(losowe(100, 1000, 10))
print(rosnaca(10))
print(malejaca(10))
print(a_ksztaltna(8))
print(v_ksztaltna(9))
insertion_sort([2,9,3])
