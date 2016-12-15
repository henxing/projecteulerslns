big_palindrome = -1

for i in range(100, 1000):
    for j in range(100, 1000):
        num = i * j
        rnum = int(str(num)[::-1])

        if num==rnum and num > big_palindrome:
            big_palindrome = num

print(big_palindrome) #906609
