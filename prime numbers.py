print("This program prints the list of prime numbers till a given number")
n = int(input("Enter the last number \n"))
prime_nos = []
for i in range(2, n+1):
    count = 0
    for j in range(2, i+1):
        if i % j == 0:
            count += 1
        if count > 1:
            break
    if count <= 1:
        prime_nos.append(i)
print(prime_nos)

