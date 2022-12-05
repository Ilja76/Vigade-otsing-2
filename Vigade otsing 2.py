print("*** ИГРЫ С ЧИСЛАМИ/NUMBER MÄNGU ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a=(abs(int(input("Введите целое число =>/Sisestage täisarv => "))))
        break
    except ValueError:
         print("Это не целое число/See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём/Nulliga pole mõtet midagi teha")
else:
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр/Määrake, kui palju on paaris ja mitu paaritu numbrit")
    print()
    c=b=a
    paaris =0
    paaritu = 0
    while b > 0:
        if b % 2 == 0:
            paaris += 1
        else:
            paaritu += 1
        b = b // 10
    
    print("Чётных цифр:/Isegi numbrid:", paaris)
    print("Нечётных цифр:/Kummalised numbrid:", paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число/Pöörake * sisestatud number ümber")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    print("*Перевёрнутое* число/* Pööratud * number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз/Syracuse hüpoteesi testimine")
    print()
    if c % 2 == 0:
        print("с - чётное число. Делим на 2./s on paarisarv. Jagage 2 -ga.")
    else:
        print("с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2./s on paaritu arv. Korrutage 3 -ga, lisage 1 ja jagage 2 -ga.")
    while c > 1:
        if c%2:
            c = 3*c+1
        c //= 2
        print(c)
    print()
    print("Гипотеза верна/Hüpotees on õige")