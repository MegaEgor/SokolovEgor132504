numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
while True:
    #ввод градусов
    gradus = list(input("введите градусы"))
    i = 0
    
    while i < (len(gradus)-1):
        if gradus[i] in numbers:
            print(i)
            i += 1
            
        else:
            print("Неверный ввод (Примеры правильного ввода: 23F, 65C)")
            i = -1
            break
        
    if i == -1:
        i = 0
        continue
    
    razdel = ["".join(gradus[:(len(gradus)-1)]), "".join(gradus[(len(gradus)-1):])]
    print(razdel)
    #проверка на корректность
    #перевод шкалы
    if razdel[1] == "F":
        print(str((float(razdel[0])-32.0)*(5/9))+"C")
    elif razdel[1] == "C":
        print(str((float(razdel[0])*(9/5))+32.0)+"F")
    else:
        print("Неверный ввод (Примеры правильного ввода: 23F, 65C)")
        continue