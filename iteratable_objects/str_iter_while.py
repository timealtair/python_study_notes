import time

string = 'some text'

it = iter(string)

while True:
    print(next(it))
    time.sleep(0.2)
