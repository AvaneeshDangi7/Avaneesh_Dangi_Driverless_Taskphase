n= int(input("Enter the number of strings (n): "))

string_list = []

print(f"Enter {n} strings:")
for _ in range(n):
    string_list.append(input())

char_counts = {}

for string in string_list:
    for char in string.lower():

        if char.isalpha():

            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

print("\nAlphabet frequencies across all strings:")
print(char_counts)