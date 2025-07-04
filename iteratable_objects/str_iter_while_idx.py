import time

string = 'some text'

i = 0
while i < len(string):
    print(string[i])
    i = i + 1
    time.sleep(0.2)
