while True:
    #ввод градусов
    gradus = list(input("введите градусы"))
    razdel = ["".join(gradus[:(len(gradus)-1)]), "".join(gradus[(len(gradus)-1):])]
    #проверка на корректность
    try:
        razdel[0] = float(razdel[0])
    except TypeError:
        print("Неверный ввод (Примеры правильного ввода: 23F, 65C)")
        continue
    #перевод шкалы
    if razdel[1] == "F":
        print(str((razdel[0]-32.0)*(5/9))+"C")
    elif razdel[1] == "C":
        print(str((razdel[0]*(9/5))+32.0)+"F")
    else:
        print("Неверный ввод (Примеры правильного ввода: 23F, 65C)")
        continue