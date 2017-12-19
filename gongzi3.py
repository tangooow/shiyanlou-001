#! /usr/bin/env python3

import sys

class Config(object):
	def __init__(self,configfile):
		self._config = {}
		with open(configfile) as file:
			for line in file:
				key,value = line.strip().split('=')
				key = key.strip()
				value = value.strip()
				self._config[key] =float(value)
	def get_config(self,key):
		return self._config[key]

class UserData(object):
	def __init__(self,userdatafile, config):
		self._userdata = {}
		self._result = []
		self.config = config
		with open(userdatafile) as file:
			for line in file:
				number,salary=line.strip().split(',')
				number = number.strip()
				salary = salary.strip()
				self._userdata[number] = float(salary)


		
	def calculator(self):
		jishuh = self.config.get_config('JiShuH')
		jishul = self.config.get_config('JiShuL')
		shuilv =self.config.get_config('YangLao') + self.config.get_config('YiLiao') +self.config.get_config('ShiYe') + self.config.get_config('GongShang') + self.config.get_config('ShengYu') + self.config.get_config('GongJiJin')

		for number in self._userdata:
			if self._userdata[number] < jishul:
				shebao = shuilv * jishul
			elif self._userdata[number] > jishuh:
				shebao = shuilv * jishuh
			else :
				shebao = self._userdata[number] * shuilv
			
			yingjiao = self._userdata[number] - shebao -3500
			if yingjiao <= 0:
				yingna = 0
			elif yingjiao <= 1500:
				yingna = yingjiao * 0.03
			elif yingjiao <= 4500:
				yingna = yingjiao * 0.10 -105.00
			elif yingjiao <= 9000:
				yingna = yingjiao * 0.20 -555.00
			elif yingjiao <= 35000:
				yingna = yingjiao * 0.25 -1005.00
			elif yingjiao <= 55000:
				yingna = yingjiao * 0.30 -2755.00
			elif yingjiao <= 80000:
				yingna = yingjiao * 0.35 -5505.00
			else: 
				yingna = yingjiao * 0.45 -13505.00

			shuihou =self._userdata[number] - shebao -yingna

			self._result.append([str(number),format(self._userdata[number],'.2f'),format(shebao,'.2f'),format(yingna,'.2f'),format(shuihou,'.2f')])




	def dumptofile(self,outputfile):
		with open(outputfile,'w') as file:
			for result in self._result:
				file.write(','.join(result)+'\n')	

if __name__ == '__main__':
	try:
		args=sys.argv[1:]
		index1 = args.index('-c')
		configfile = args[index1 + 1]
		index2 = args.index('-d')
		userdatafile = args[index2 + 1]
		index3 = args.index('-o')
		outputfile = args[index3 + 1]
		config = Config(configfile)
		userdata = UserData(userdatafile, config)
		userdata.calculator()
		userdata.dumptofile(outputfile)
	except ValueError:
		print('Parameter error')
