```python

_______________________________________________

            Логический тип bool:


True --> link to bool obj | True
False --> link to bool obj | False


_______________________________________________

            Преобразование в bool:


bool("any text") --> link to bool obj | True
bool("") --> link to bool obj | False

bool(123) --> link to bool obj | True
bool(0) --> link to bool obj | False


_______________________________________________

            Условный оператор if / else:


Условие - это выражение между if и :
Тело - это 1 (или более) строчка с выражениями,
    выделенные отступом (TAB)


1. Вычисляет условие

2. Если type(результат_вычисления) не bool:

    результат_вычисления = bool(результат_вычисления)

3. Вычисляет тело после if, только если:
        результат_вычисления --> True

4. Вычисляет тело после else, только если:
        результат_вычисления --> False


if True:
    num = 1 + 2
    print("Evals if True")
else:
    num = 3 + 4
    print("Evals if False")

num --> 3


if False:
    num = 1 + 2
    print("Evals if True")
else:
    num = 3 + 4
    print("Evals if False")

num --> 7