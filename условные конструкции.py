x=int(input('x='))
if 0<x<7:
    print('Значение в диапазоне,продолжим')
    y=2*x-5
    if y<0:
        print('y отрицательный')
    else:
        if y>0:
            print('y пололжительный')
        else:
            print('y=0')