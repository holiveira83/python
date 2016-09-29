def digit_sum(n):
    total = 0
    num = n
    for i in range(len(str(n))):
        num = n%10
        total+=num
        n = n//10
    return total

print digit_sum(573)