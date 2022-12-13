prizes = [20, 100, 200, 500, 1000]

dbl_prizes = []

for prize in prizes:
    dbl_prizes.append(prize * 2)
    ##print(dbl_prizes)


## Comprehension method
dbl_prizes = [prize * 2 for prize in prizes]
##print(dbl_prizes)


##squaring

nums = [2, 3, 4, 5, 6]

squared_even_nums = [num**2 for num in nums if (num**2) % 2 == 0]
print(squared_even_nums)
