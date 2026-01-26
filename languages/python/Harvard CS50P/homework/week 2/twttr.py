str = input("Input: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in range(10):
    str = str.replace(vowels[i], '')
print(str)