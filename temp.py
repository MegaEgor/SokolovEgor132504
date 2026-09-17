# first_side = as.numeric(readline("введите первую сторону: "))
# second_side = as.numeric(readline("введите первую сторону: "))
# angle = as.numeric(readline("введите угол между ними: "))
# third_side = sqrt(first_side**2 + second_side**2 - 2*first_side*second_side*cos(angle * pi/180))
# cat("Третья сторона — ",third_side)

# вводим необходимые функции и константы из модуля math
from math import sqrt, pi, cos
# просим пользователя вписать 2 стороны и угол между ними
first_side = float(input("введите первую сторону: "))
second_side = float(input("введите вторую сторону: "))
angle = float(input("введите угол между ними: "))
# по теореме косинусов высчитываем третью сторону
third_side = sqrt(first_side**2 + second_side**2 - 2*first_side*second_side*cos(angle * pi/180))
# выводим третью сторону
print("Третья сторона — ",third_side)
