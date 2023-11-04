for x in range(0, 1000):
    x=""
    a=float(input("Напишите 1 коэффициент"))
    b=float(input("Напишите 2 коэффицент"))
    c=float(input("Напишите 3 коэффицент"))
    d=b**2-4*a*c
    if a!=0:
        if d>0:
            print((-b+d**0.5)/(2*a))
            print((-b-d**0.5)/(2*a))
        elif d==0:
            print(-b/2*a)
        else:
            print("Нету корней")
    else:
        x=-(c/b)
        print(x)
