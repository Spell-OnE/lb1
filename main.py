import math
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x1,2 = %.2f" % x)
else:
    print("Корней нет")

# disc > 0: a = 14; b = -5; c = -1; disc = 81; x1 = 0,5; x2 = -0.14;

# disc = 0: a = 9; b = -30; c = 25; disc = 0; x1,2 = 1.67

# disc < 0: a = 2; b = 1; c = 67; disc = -535;
