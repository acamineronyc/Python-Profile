
fizzbuzz = []

start = int(input("Enter Start Value:"))
end = int(input("Enter End Value:"))

for i in range(start, end+1):
    entry = ''
    if i % 3 == 0:
        entry += "Fizz"
    if i % 5 == 0:
        entry += "Buzz"
    if i % 3 == 0 and 5 % i == 0:
        entry += "Fizz and Buzz"
    elif i % 3 != 0 and i % 5 != 0:
        entry = i

    fizzbuzz.append(entry)

for i in fizzbuzz:
    print(i)