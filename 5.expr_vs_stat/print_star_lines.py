separator = '-' * 32

print(separator)

print('Enter how many lines with stars to print:')
lines_with_stars = int(input())

print(separator)

counter = 0
while counter < lines_with_stars:
    counter = counter + 1
    print('*' * counter)

print(separator)