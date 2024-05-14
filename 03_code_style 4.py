x, y = 10, 29
if x < 0:
    print('Меньше нуля\n')
    z = x ** 2 + y
else:
    print('Больше нуля\n')
    z = x - y
print('Получается\n', z)

name = input('Enter your name >>>')
if name == 'Ola':
    opponent = 'Ola'
    print('Hi, Ola!')
else:
    if name == 'Sofi':
        opponent = 'Sofi'
        print('Hi, Sofi!')
    else:
        if name == 'Katy':
            opponent = 'Katy'
            print('Hi, Katy!')
        else:
            opponent = 'anonymous'
            print('Hi, anonymous!')

pass
if x < 0:
    if y > 0:
        z = -x + y
        pass
    else:
        z = -x - y
        pass
else:
    z = x + y
    pass

if x < 0:
    if y > 0:
        pass
    else:
        print('направо!')
else:
    print('стой!')

my_poem = ['Варкалось,хливкие шорьки пырялись по наве',
           'И хрюкотали зелюки как мюмзики в мове',
           'О бойся Бармаглота, сын!Он так свиреп и дик',
           'А в глуше рымит исполин-Злопастный Брандашмыг!']

x = 2
y = x * x + 1
is_big = x >= 3000
x = my_poem[-1]
print(x)
my_list = [2, 3, 4, 5, 6]

x = 3
if x == 3:
    print(42)
    if y < 0:
        print('налево!')
    else:
        print('направо!')
else:
    print('Стой!')

# названия переменных

count_of_my_pets = 34
if count_of_my_pets > 10:
    print('I need more space for my pets!')
my_favorite_pets_and_bird = ['cat', 'wolf', 'ostrich']
if 'lion' in my_favorite_pets_and_bird:
    print('Wow!')
my_favorite_pets_and_bird = ['cat', 'wolf', 'ostrich']

i = 34
j = 43
if i > j:
    print()
k = 9
if k > 0:
    print()

# lowercase (слово в нижнем регистре)
# lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
# UPPERCASE (заглавные буквы)
# UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)

# CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase).
#   Замечание: когда вы используете аббревиатуры в таком стиле, пишите все буквы аббревиатуры заглавными —
#   HTTPServerError лучше, чем HttpServerError.

# mixedCase (отличается от CapitalizedWords тем, что первое слово начинается с маленькой буквы)
# Capitalized_Words_With_Underscores (слова с заглавными буквами и подчеркиваниями — уродливо!)


# автоматическое переименование в PyCharm и подсказки - вам не нужно набирать длинные названия переменных

animals = ['cat', 'wolf', 'ostrich']
if 'lion' in animals:
    print('Wow!')

# В каждой уважающей себя компании есть style guide (стайл-гайд) - руководство по стилю написания кода.
# Практически все они основываются на PEP8, с небольшими исключениями, принятыми в этой команде.
# Как пример стайл-гайда небольшой компании рекомендую почитать
# https://github.com/best-doctor/guides/blob/master/guides/python_styleguide.md
