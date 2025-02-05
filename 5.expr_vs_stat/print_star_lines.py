separator = '-' * 32

print(separator)

print('Enter how many lines with stars to print:')
count_to = int(input())

print(separator)

counter = 0
while counter < count_to:
    counter = counter + 1
    print('*' * counter)

print(separator)