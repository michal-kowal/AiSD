import random
import time

# generatory danych

# losowe liczby
rund_num_list = [] #to dodałem i w środku funkcji tab wymieniłem na to i jeszcze do insertion sort dałem to
def losowe(minimum, maximum, length):
    #tab = []
    for i in range(length):
        rund_num_list.append(random.randint(minimum, maximum))
    return rund_num_list


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
    print("INSERTION SORT:") #dodałem to
    print("czas operacji: ", (end - start))
    print("ilosc zamian: ", zamian)
    print("ilosc porownan: ", porownan)
    print(array)
    return array
ins_list = rund_num_list[::]

print(losowe(1, 10000, n))
print(rosnaca(10))
print(malejaca(10))
print(a_ksztaltna(8))
print(v_ksztaltna(9))
insertion_sort(ins_list)

# MERGE SORT
def merge_sort(array):
    porownan = 0
    if len(array) > 1:
        srodek = len(array)//2
        prawa = array[:srodek]
        lewa = array[srodek:]
        l = merge_sort(lewa)
        p = merge_sort(prawa)
        i = 0
        j = 0
        k = 0
        porownan += l[1] + p[1]
        while i < len(lewa) and j < len(prawa):
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
            porownan += 1
        while j < len(prawa):
            array[k] = prawa[j]
            j += 1
            k += 1
            porownan +=1
    return array, porownan
def pomiary_merge_sort():
    start = time.time()
    sort_list = merge_sort(mer_list)
    end = time.time()
    porownan = sort_list[-1]
    print("MERGE SORT:")
    print("czas operacji: ", (end - start))
    print("liczba porównań: " + str(porownan))
    # dodać liczbę scaleń
mer_list = rund_num_list[::]
pomiary_merge_sort()
print(mer_list)

#SHELL SORT KNUTH SEQUENCE
def shell_sort(array):
    start = time.time()
    porownan = 0
    zamian = 0
    gap = 1
    while gap <= len(array)//3:
        gap = gap*3 + 1
    print("SHELL SORT:")
    while gap > 0:
        print("przeskok: ", gap)
        for i in range(gap, n):
            temp = array[i]
            j = i
            while  j >= gap and array[j - gap] < temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap = (gap - 1)//3
    end = time.time()
    print("czas operacji", end - start)
    print(array)
    # dodać liczbę porównań i zamian
she_list = rund_num_list[::]
shell_sort(she_list)

#QUICK SORT RECURSION
print("QUICK SORT:")
qui_list = rund_num_list[::]
def quick_sort(array):
    if len(array) <= 1: return array
    smaller, equal, larger = [],[],[]
    pivot = array[-1]
    print("pivot: ", pivot)
    porownan = 0
    for i in array:
        if i > pivot: larger.append(i)
        elif i == pivot: equal.append(i)
        else: smaller.append(i)
        porownan +=1
    return quick_sort(larger)+equal+quick_sort(smaller)
def pomiar_quick_sort():
    start = time.time()
    sort_list = quick_sort(qui_list)
    end = time.time()
    print("ilość porównan: ")
    print("czas operacji: ", end - start)
    print(sort_list)
pomiar_quick_sort()