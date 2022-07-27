with open('file1.txt') as file1:
    file1_numbers = file1.readlines()

with open('file2.txt') as file2:
    file2_numbers = file2.readlines()
        
result = [int(num) for num in file1_numbers if num in file2_numbers ]
# Write your code above 👆
print(result)