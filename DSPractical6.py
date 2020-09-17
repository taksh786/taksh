#WAP to sort a list of elements. Give user the option to perform sorting using Insertion sort, Bubble sort or Selection sort.
def bubble_sort(lst):
	for i in range(len(lst)):
           for j in range(len(lst)):
               if lst[i] < lst[j]:
                   lst[i],lst[j] = lst[j],lst[i]
	return lst

def insertion_sort(lst): 
        for i in range(1, len(lst)): 
            index = lst[i] 
            j = i-1
            while j >= 0 and index < lst[j] : 
                    lst[j + 1] = lst[j] 
                    j -= 1
            lst[j + 1] = index 
        return lst

def selection_sort(lst):
        for i in range(len(lst)):
            smallest_element = i
            for j in range(i+1,len(lst)):
                if lst[smallest_element] > lst[j]:
                    smallest_element = j
            lst[i],lst[smallest_element] = lst[smallest_element],lst[i]
        return lst

def run():
	while True:
		print("Press 1 for bubble sort")
		print("Press 2 for insertion sort")
		print("Press 3 for selection sort")
		print("Press 4 to exit")
		print("List:",lst)
		c = int(input())
		if c == 1:
			print("Sorted list",bubble_sort(lst))
		elif c == 2:
			print("Sorted list",insertion_sort(lst))
		elif c == 3:
			print("Sorted list",selection_sort(lst))
		else:
			break

lst = [26,74,12,3,48,2,37,15]
run()
