#! /usr/bin/env python3
import sys
b = sys.argv[1:]
def cal_result(b):
	result = 0
	if b <= 3500:
		result = b*0.835
	elif b <= 5000:
		result = (b*0.835-3500) * 0.97+3500
	elif b <= 8000:
		result = (b*0.835-3500)*0.9 +105+3500
	elif b <= 12500:
		result = (b*0.835-3500)*0.8 + 555+3500
	elif b <= 38500:
		result = (b*0.835-3500)*0.75+1005+3500
	elif b <= 58500:
		result = (b*0.835-3500)*0.7 +2755+3500
	elif b <= 83500:
		result = (b*0.835-3500)*0.65+5505+3500
	else :
		result = (b*0.835-3500)*0.55+13505+3500
	return result

for arg in sys.argv[1:]:
	b = arg.split(':')
	print(b[0]+':',end=' ')
	print(format(cal_result(int(b[1])),".2f"))
