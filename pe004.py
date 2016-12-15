def findPalindrome(exp):
    big_palindrome = -1

    for i in range(10**exp, 10**(exp-1), -1):
        for j in range(i, 10**(exp-1), -1):
            num = i * j
            rnum = int(str(num)[::-1])

            if num==rnum and num > big_palindrome:
                big_palindrome = num

    return big_palindrome

if __name__=="__main__":
    palindrome = findPalindrome(3)
    print(palindrome) #906609
