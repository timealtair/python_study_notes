```python

_______________________________________________

    Expression (Выражение) vs Statement (Утверждение)


_______________________________________________

        Expressions Evals (Выражения Вычисляются)


eval('expression') --> link to object

Можно воспринимать как поток информации: (вход --> выход)

Может содержать в себе другие выражения (expressions)

(!) Результатом вычисления выражений всегда является ссылка на объект

_______________________________________________


1 == 10 --> link to bool object | False

1 + 2 + 3 --> 3 + 3 --> link to int object | 6

'any ' + 'text' --> link to str object | 'any text'

input() --> link to str object | 'user input example'

print('Hello') --> link to NoneType object | None


Извлечение ссылки на объект из связанной переменной
            тоже является вычислением выражения:

print --> link to Function object | Function

__name__ --> link to str object | '__main__'

_______________________________________________

        Statements Executes (Утверждения Исполняются)


exec('statement')

Является набором инструкций для интерпретатора

Может содержать в себе другие выражения (expressions)
                            и/или утверждения (statements)

Все исполняемые строки можно считать утвержениями (statements)

(!) Результат вычисления утверждений отсутвует

_______________________________________________

                    = statement:


имя_переменной = выражение

num_name_example = 3 * 4 

| Инструкции: 1. Вычислить результат выражения справа от =
              2. Полученную ссылку на объект связать с именем
                 переменной

_______________________________________________

                    if/else statement:


if выражение:
    утверждение
else:
    утверждение

if 1:
    num_name_example = 1
    print('Executes if True')
else:
    num_name_example = 2
    print('Executes if False')

| Инструкции: 1. Вычислить результат bool(выражение) в условии
              2. Если результат это ссылка на True,
                        то исполнить утверждение после if ...:
                 В ином случае (ссылка на False) -
                        исполнить утверждение после else:

_______________________________________________

                    while statement:


while выражение:
    утверждение

i = 0
while i < 10:
    i = i + 1
    print(i)

| Инструкции: 1. Вычислить результат bool(выражение) в условии
              2. Если результат это ссылка на True,
                        2.1 то исполнить утверждение после while ...:
                        2.2 Перейти к исполнению шага 1.
                 В ином случае (ссылка на False) -
                        ничего не делать
