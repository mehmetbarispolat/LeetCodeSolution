def nearest_palindromic(n):
    l = len(n)
    num = int(n)
    i = 0
    while True:
        if is_palindrome(num-i):
            return num - i
        if is_palindrome(num+i):
            return num + i
        i += 1

def is_palindrome(n):
    str_n = str(n)
    result = True if str_n == str_n[::-1] else False
    return result
    
if __name__ == "__main__":    
    print(nearest_palindromic("17"))