# Ares Dragonas, Sorting Algorithms Analysis, a program that lets a user sort data sets in 4 different algorithms in ascending or descending order.
import random as r
sort_algos = ['Selection Sort','Bubble Sort','Insertion Sort','Quick Sort','End']

def run_algo(n,d,c,v):
    '''This main function holds all of the sorting algorithms upon user selection.'''
    x = d.copy()
    def quick(mem_1,l,h):
        '''Recursion part of the quicksort function.'''
        if l < h:
            split = partitioner(mem_1,l,h)
            quick(mem_1,l,split-1)
            quick(mem_1,split+1,h)
    
    def partitioner(mem_2,f1,f2):
        '''Partioner function that return the split value into the Quicksort recursion function, also has ascending and descending options.'''
        pivot, left, right, z = mem_2[f1], f1+1, f2, False
        while not z:
            if v == 1:
                while left <= right and mem_2[left] >= pivot:
                    left += 1
                while mem_2[right] <= pivot and right >= left:
                    right -= 1
                if right < left:
                    z = True
                else:
                    mem_2[left], mem_2[right] = mem_2[right], mem_2[left]
            elif v == 2:
                while left <= right and mem_2[left] <= pivot:
                    left += 1
                while mem_2[right] >= pivot and right >= left:
                    right -= 1
                if right < left:
                    z = True
                else:
                    mem_2[left], mem_2[right] = mem_2[right], mem_2[left]                
        mem_2[f1], mem_2[right] = mem_2[right], mem_2[f1]
        return right
    if n == 0:
        '''Selection sort algorithm with descending and ascending options.'''
        for i in range(0,len(x)-1):
            for u in range(i+1,len(x)):
                if v == 2:
                    if x[u] < x[i]:
                        x[i], x[u] = x[u], x[i]
                elif v == 1:
                    if x[u] > x[i]:
                        x[i], x[u] = x[u], x[i]
    elif n == 1:
        '''Bubble sort algorithm with descending and ascending options.'''
        for i in range(0, len(x)):
            for u in range(0,len(x)-1):
                if v == 2:
                    if x[u] > x[u+1]:
                        x[u], x[u+1] = x[u+1], x[u]
                elif v == 1:
                    if x[u] < x[u+1]:
                        x[u], x[u+1] = x[u+1], x[u]
    elif n == 2:
        '''Insertion sort algorithm with descending and ascending options.'''
        for i in range(0,len(x)):
            counter, comparator = i, x[i]
            if v == 2:
                while counter > 0 and x[counter-1] > comparator:
                    x[counter] = x[counter-1]
                    counter -= 1
                x[counter] = comparator
            elif v == 1:
                while counter > 0 and x[counter-1] < comparator:
                    x[counter] = x[counter-1]
                    counter -= 1
                x[counter] = comparator
    elif n == 3:
        '''Calls upon the Quicksort's recursive algorithm thus initiating Quicksort.'''
        quick(x,0,len(x)-1)
    else:
        '''Quits the program.'''
        raise Exception("You have chosen to exit.")
    if v == 1:
        '''This is the option that allows the user to sort in descending order.'''
        return ("\nYour sorted data using " + sort_algos[c] + " in descending order is:\n" + str(x)[1:-1])
    elif v == 2:
        '''This is the option that allows the user to sort in ascending order.'''
        return ("\nYour sorted data using " + sort_algos[c] + " in ascending order is:\n" + str(x)[1:-1])

def selection():
    '''This is the main while loop for the user to select descending or ascending order as well as type of sorting algorithm.'''
    while True:
        print("")
        data = []
        for i in range(len(sort_algos)):
            print(str(sort_algos.index(sort_algos[i])) + ": " + str(sort_algos[i]))
        for y in range(int(input("\nHow many numbers would you like to sort? "))):
            data.append(r.randint(0,1000)) # Creates elements of data set to be sorted
        print("\nYour new data set is:\n\n" + str(data)[1:-1] + "\n")
        choice = int(input("Choose a selection: 0, 1, 2, 3, 4:\n ")) # Choice of algorithm
        print(run_algo((sort_algos.index(sort_algos[choice])),data,choice,int(input("Sort in descending (1) or ascending? (2) ")))) # Choice to sort in descending or ascending order
selection()
