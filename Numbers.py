desyatki = ["", "надцать", "двадцать", "тридцать", "сорок", "пятьдесят", 
            "шестьдесят" ,"семьдесят", "восемьдесят", "девяносто"]
yedinitsy = ["ноль", "один", "два", "три", "четыре", "пять", 
            "шесть" ,"семь", "восемь", "девять"]
while True:
    
    tsyfra = input("Назовите число")
    
    try:
        tsyfra = int(tsyfra)
    except ValueError:
        print("Вы должны ввести число от 0 до 99")
        continue
        
    if 0 <= tsyfra <= 99:
        tsyfra = [int(i) for i in (list(str(tsyfra)))]
        if len(tsyfra) == 1:
            print(yedinitsy[tsyfra[0]])
        elif tsyfra[0] == 1 and tsyfra[1] == 2:
            print("двенадцать")
        elif tsyfra[0] == 1 and tsyfra[1] == 0:
            print("десять") 
        elif tsyfra[0] == 1 and 3 < tsyfra[1] <= 9 :
            print("".join((list(yedinitsy[tsyfra[1]]))[:(len(yedinitsy[tsyfra[1]]))-1]) + desyatki[tsyfra[0]])
        elif tsyfra[0] == 1:
            print(yedinitsy[tsyfra[1]] + desyatki[tsyfra[0]])
        elif tsyfra[1] == 0:
            print( desyatki[tsyfra[0]])
        else:
            print( desyatki[tsyfra[0]] + " " + yedinitsy[tsyfra[1]])
            
    else:
        print("Вы должны ввести число от 0 до 99")
        continue
        
        