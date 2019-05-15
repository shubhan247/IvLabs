largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num=="done":break
        n=int(num)
    except:
        print("Invalid input")
        continue
    if smallest==None:
        smallest=n
    largest=max(largest,n)
    smallest=min(smallest,n)

print("Maximum is", largest)
print("Minimum is", smallest)
