class StringSorter:
    def selection_sort( self, string_list):
        n = len(string_list)
        for i in range(n):
            min = i
            for j in range(i + 1, n):
                if string_list[j] < string_list[min]:
                    min = j
            string_list[i], string_list[min] = string_list[min], string_list[i] #sw
        return string_list



n = int(input("Enter the number of strings (n): "))
string_list = []
print(f"Enter {n} strings:")
for i in range(n):
    string_list.append(input())

a1 = ["banana", "apple", "cherry", "date", "apricot"]


sorter = StringSorter()


sorted_list = sorter.selection_sort(string_list)
print(sorted_list)
