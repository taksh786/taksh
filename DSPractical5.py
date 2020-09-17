#Write a program to search an element from a list. Give user the option to perform Linear or Binary search.
def linear_search(lst,n):
        for i in range(len(lst)):
            if lst[i] == n:
                return print('Position:',i)
        return print("Number not found")

def binary_search(lst,n,start,end):
        if start <= end:
            mid = (end + start) // 2
            if lst[mid] == n:
                return print('Position:',mid)
            elif lst[mid] > n:
                return binary_search(lst,n,start,mid-1)
            else:
                return binary_search(lst,n,mid + 1,end)
        else:
            return print("Number not found")

def run():
	while True:
		print("Press 1 for linear search")
		print("Press 2 for binary search")
		print("Press 3 to exit")
		c = int(input())
		if c == 1:
			n = int(input("Enter number to search:"))
			linear_search(lst,n)
			break
		elif c == 2:
			s_lst = sorted(lst)
			n = int(input("Enter number to search:"))
			binary_search(s_lst,n,0,len(s_lst)-1)
			break
		else:
			break


lst = [26,74,12,3,48,2,37,15]
run()
