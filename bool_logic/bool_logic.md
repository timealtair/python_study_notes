```python

_______________________________________________

            Отрицание not (инверсия):


1. Вычисляет выражение после not

2. Если type(результат_вычисления) не bool:

    результат_вычисления = bool(результат_вычисления)

3. Возвращает противоположное значение для результат_вычисления


not True --> bool obj | False
not False --> bool obj | True


not 'abc' --> not bool('abc') --> not True --> bool obj | False

not '' --> not bool('') --> not False --> bool obj | True


not 123 --> not bool(123) --> not True --> bool obj | False

not 0 --> not bool(0) --> not False --> bool obj | True


_______________________________________________

            ???:


???