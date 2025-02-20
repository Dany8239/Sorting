import time as t
import random as r
import os
from collections import Counter
import matplotlib.pyplot as plt

def wait(s):
    t.sleep(s)

def bubble_sort(arr, visualize=False):
    n = len(arr)
    if visualize:
        pass
        fig, ax = plt.subplots()
    
        bars = ax.bar(range(len(arr)), arr, color="skyblue")
        plt.ion()
    
    for i in range(n - 1):
        swapped = False
        rmng = n - i
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                if visualize:
                    pass
                    ax.clear()
                    bars = ax.bar(range(len(arr)), arr, color="skyblue")
                    bars[j+1].set_color("red")
                    bars[j].set_color("red")
                
                    plt.pause(0.000000000000001)
                swapped = True
        if n >= 1000 and rmng % 1000 == 0:
            print(f"Zbývá {n-i} čísel")
        if not swapped:
            break
        plt.ioff()
    plt.show(block=False)
    wait(1)
    plt.close("all")

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        rmng = n - i
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if n >= 1000 and rmng % 1000 == 0:
            print(f"Zbývá {n-i} čísel")

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


print("Number sorter\nStiskni Ctrl+c pro ukončení\n----------")
while True:
    try:
        visualise = False
        method = input("Chceš zadat [s]voje čísla, nebo si je nechat vy[g]enerovat? ([s]/[g]): ")
        visualise = input("Chceš vizualizovat průběh třídění? Při číslech větších než 100 je funkce vypnuta. ([a]no/[n]e): ")
        if visualise.lower() == "a":
            visualise = True
        else:
            visualise = False
        if method.lower() == "s":
            numbers = input("Zadej čísla oddělená mezerou: ")
            if len(numbers) > 100:
                visualise = False
            if not numbers:
                print("Nezadal jsi žádná čísla")
                continue
            numbers = list(map(int, numbers.split()))
            print("Neseřazená čísla:", numbers)
            sort = input("Chceš seřadit čísla? ([a]no/[n]e): ")                
            if sort.lower() == "n":
                continue
        else:
            numbercount = input("Kolik čísel chceš vygenerovat?: ")
            if int(numbercount) > 100:
                visualise = False
            start = 1
            end = 100
            rng = input("Zadej rozmezí čísel oddělené mezerou (default: 1-100): ")
            if rng:
                start, end = map(int, rng.split())
            numbers = []
            for i in range (1, int(numbercount)+1):
                numbers.append(r.randint(start, end))
            print("Neseřazená čísla:", numbers)
            sort = input("Chceš seřadit čísla? ([a]no/[n]e): ")
            if sort.lower() == "n":
                continue
        alg = input("Vyber algoritmus: [B]ubble sort, [S]election sort: ")
        if alg.lower() == "s":
            wait(0.5)
            print("Vybrán alroritmus selection sort")
            wait(0.5)
            selection_sort(numbers)
        elif alg.lower() == "b":
            wait(0.5)
            print("Vybrán algoritmus bubble sort")
            wait(0.5)
            bubble_sort(numbers, visualise)
        # Naprosto zbytečné, ale je to pro efekt
        if len(numbers) <= 5000 and not visualise:
            wait(0.5)
            print("Seřazuji čísla pomocí pokročilých algoritmů.")
            wait(0.8)
            print("Seřazuji čísla pomocí pokročilých algoritmů..")
            wait(0.8)
            print("Seřazuji čísla pomocí pokročilých algoritmů...")
            wait(0.8)
        print("Seřazená čísla:", numbers)
        count = Counter(numbers)
        most_common = count.most_common()
        max_count = most_common[0][1]
        most_frequent_numbers = [num for num, freq in most_common if freq == max_count]
        if len(most_frequent_numbers) > 1:
            print(f"Nejčastější čísla: {', '.join(map(str, most_frequent_numbers))}, objevila se celkem {max_count}x")
        else:
            print(f"Nejčastější číslo: {most_frequent_numbers[0]}, objevilo se celkem {max_count}x")
        most_common = count.most_common(1)
    except KeyboardInterrupt:
        print(f"\n\nVypínám program")
        wait(0.8)
        os._exit(0)
    except ValueError:
        print("Zadal jsi neplatné hodnoty")
    except Exception as e:
        print(f"\nDošlo k chybě: {e}")
