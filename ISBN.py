ISBN = int(input())  
l = len(str(ISBN))  

if l == 10:  
    sum = 0  
    i = 10  
    while ISBN > 0:
        r = ISBN % 10  # Extracts the rightmost digit of ISBN
        sum += r * i   # Calculates weighted sum
        i -= 1         # Decrements weight
        ISBN = ISBN // 10  # Removes the rightmost digit from ISBN

    if sum % 11 == 0:
        print("Legal ISBN")  
    else:
        print("Illegal ISBN - not divisible by 11")  
else:
    print("Illegal ISBN")  
