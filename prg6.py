def findindex(sublist, target):

    low = 0
    high = len(sublist) - 1

    while low <= high:
        mid = (low + high) // 2
        if sublist[mid] == target:
            return mid  # Insert  at the spot
        elif sublist[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low  #  first index


def insertht(hash_table, num):

    index = num % 10


    targetsublist = hash_table[index]
    idx = findindex(targetsublist, num)

    targetsublist.insert(idx, num)


#


hash_table = [[] for _ in range(10)]
numbers=[]

n = int(input("Enter the number of numbers (n): "))
for i in range(n):
    numbers.append(int(input("Enter the number (n): ")))


print(f"Inserting numbers: {numbers}\n")
for num in numbers:
    insertht(hash_table, num)


print("--- Final Hash Table ---")
i = 0
for sublist in hash_table:
    print(f"Sublist {i}: {sublist}")
    i += 1
