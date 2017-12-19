#! /usr/bin/env python
b = input(int())
result = 0
while b >= 3500:
        b -= 3500
        if b <= 0:
                result =0
        elif 0 < b and b<=1500:
                result = b * 0.03
        elif 1500 < b <= 4500:
                result = b * 0.1 - 105
        elif 4500 < b <= 9000:
                result = b * 0.2 - 555
        elif 9000 < b <= 35000:
                result = b * 0.25 - 1005
        elif 35000 < b <= 55000:
                result = b * 0.3 - 2755
        elif 55000 < b <= 80000:
                result = b * 0.35 -5505
        else  :
                result = b * 0.45 -13505
        print (result)

	
