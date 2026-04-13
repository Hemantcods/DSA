def fabonaci(n):
    if n==1 or n==0:
        return 1
    else:
        return fabonaci(n-1)+fabonaci(n-2)
print(fabonaci(2))    