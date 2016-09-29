largest = None
smallest = None
x = []
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done":
            break
        else:
            x.append(int(num))
    except:
        print "Invalid input"

for i in x:
    if smallest is None:
        smallest = i
    elif i<smallest:
        smallest = i

    if largest is None:
        largest = i
    elif i>largest:
        largest = i


print "Maximum is", largest
print "Minimum is", smallest