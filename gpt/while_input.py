# i=2
# num = int(input("Enter a number: "))
# while i <= num:
#    if i % 2 == 0:
#       print(i)
#       i += 2

# total = 0
# i = 1
# while i <= 10:
#     total = total + i
#     i += 1
# print(total)

# numbers = [2, 5, 8, 11, 14, 3]
# print(numbers[::-1])

# numbers = [4, 7, 1, 3, 9]
# sum = 0
# for number in numbers:
#     sum += number
# print(sum)

numbers = [-3, 5, -1, 8, -2, 10]
even_num = []
for number in numbers:
    if number > 0:
        even_num.append(number)
print(len(even_num))