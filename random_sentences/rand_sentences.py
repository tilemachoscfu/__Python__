import random

def random_sent():
	str1 = ['the', 'a', 'an', 'their']
	str2 = ['enthusiastic', 'efficient', 'active', 'archaic']
	str3 = ['boy', 'dog', 'cat', 'girl']
	str4 = ['eats', 'chases', 'makes', 'produces']
	str5 = ['mice', 'tools', 'chocolate', 'calculations']
	num = random.randrange(0,4)
	print(str1[num] + ' ' + str2[num] + ' ' + str3[num] + ' ' + str4[num] + ' ' + str5[num] + ' ')

random_sent()	

