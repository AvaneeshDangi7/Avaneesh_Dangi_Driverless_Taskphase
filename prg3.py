class SortSearch:
    def selection_sort(self, string_list):
        n = len(string_list)
        for i in range(n):
            min = i
            for j in range(i + 1, n):
                if string_list[j] < string_list[min]:
                    min = j
            string_list[i], string_list[min] = string_list[min], string_list[i]
        return string_list

    def binsearch(self,sorted_list,strg):

        left = 0
        right = len(sorted_list) - 1

        while left <= right:
            mid = left + (right - left) // 2 #rounding to int


            if sorted_list[mid] == strg:
                return mid
            elif sorted_list[mid] < strg:
                left = mid + 1
            else:
                right = mid - 1

        return -1


n = int(input("Enter the number of strings (n): "))
string_list = []
print(f"Enter {n} strings:")
for _ in range(n):
    string_list.append(input())
sorter=SortSearch()
sorted_list = sorter.selection_sort(string_list)
print(sorted_list)

strg=(input("Enter the string to be sorted: "))

searcher=SortSearch()
flag=searcher.binsearch(sorted_list,strg)
if flag==-1:
    print("String not found")
else:
    print("String found at position ",(flag+1))