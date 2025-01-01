```python

_______________________________________________

            Логический тип bool:


True --> bool obj | True
False --> bool obj | False


_______________________________________________

            Преобразование в bool:


bool('any text') --> bool obj | True
bool('') --> bool obj | False

bool(123) --> bool obj | True
bool(0) --> bool obj | False


_______________________________________________

            Условный оператор if / else:


Условие - это выражение между if и :
Тело - это 1 (или более) строчка с выражениями, выделенные отступом (TAB)


1. Вычисляет условие

2. Если type(результат_вычисления) не bool:

    результат_вычисления = bool(результат_вычисления)

3. Вычисляет тело после if, только если: результат_вычисления --> True

4. Вычисляет тело после else, только если: результат_вычисления --> False


if True:
    print('Will be printed')
else:
    print('Will NOT be printed')


if False:
    print('Will NOT be printed')
else:
    print('Will be printed')

