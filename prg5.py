def createtable():

    hash_table = [[] for _ in range(10)]
    #only 10 possibilities


    n = int(input("Enter the number of integers to insert: "))


    print(f"Enter {n} integers: ")
    for _ in range(n):
        num = int(input())
        key = num % 10
        hash_table[key].append(num)


    print("\n--- Hash Table ---")
    for index, sublist in enumerate(hash_table):

        print(f"Sublist {index}: {sublist}")


# Run the function
createtable()