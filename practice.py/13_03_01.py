numbers = [3,7,2,9,4,7,1]
count = 0
largest_number = numbers[0]
second_largest = numbers[0]

for number in numbers:
    if number > largest_number:
        second_largest = largest_number
        largest_number = number
    if number == 7:
        count += 1


print("Largest number: ", largest_number)
print("Second largest number: ",second_largest)
print(count, "Apperances of 7")
