import random


# generowanie danych
# losowe liczby
import time


def losowe(minimum, maximum, length):
    tab = []
    for i in range(length):
        tab.append(random.randint(minimum, maximum))
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


insertion_sort([2,9,3])
