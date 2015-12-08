#!/usr/bin/env python

'''

Simple PIN code generator.
It works with list of exclusions of most commonly used PINs,
that based on leaked passwords reviews.
links of reviews:
http://www.jbonneau.com/doc/BPA12-FC-banking_pin_security.pdf
http://datagenetics.com/blog/september32012/index.html 

'''


import random

thousands = list(range(1000,10000))
hundreds = list(range(100,1000)) 
tens = list(range(10,100)) 
ones = list(range(1,10))
zeroes = ['0000']


# convert to str and add zeroes
full_thousands = []
full_hundreds = []
full_tens = []
full_ones = []

for i in thousands:
	i = str(i)
	full_thousands.append(i)

for i in hundreds:
	i = '0' + str(i)
	full_hundreds.append(i)


for i in tens:
	i = '00' + str(i)
	full_tens.append(i)


for i in ones:
	i = '000' + str(i)
	full_ones.append(i)


All_PIN = zeroes + full_ones + full_tens + full_hundreds + full_thousands


exclusions = [
	# same numbers:
	'0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999',

	# increasing and decreasing sequences:
	'0123', '3210', '1234', '4321', '2345', '5432', '3456', '6543', '4567', '7654', '5678', '8765', '6789', '9876', '7890', '0987',
	'0234', '4320', '0345', '5430', '0456', '6540', '0567', '7650', '0678', '8760', '0789', '9870', '1230', '0321',	'2340', '0432',
	'3450', '0543', '4560', '0654', '5670', '0765', '6780', '0876',

	# same pairs of numbers:
	'1212', '1313', '1414', '1515', '1616', '1717', '1818', '1919', '2020', '2121', '2323', '2424', '2525', '2626', '2727', '2828',
	'2929', '3030', '3131', '3232', '3434', '3535', '3636', '3737', '3838', '3939', '4040', '4141', '4242', '4343', '4545', '4646', 
	'4747', '4848', '4949', '5050', '5151', '5252', '5353', '5454', '5656', '5757', '5858', '5959', '6060', '6161', '6262', '6363', 
	'6464', '6565', '6767', '6868', '6969', '7070', '7171', '7272', '7373', '7474', '7575', '7676', '7878', '7979', '8080', '8181', 
	'8282', '8383', '8484', '8585', '8686', '8787', '8989', '9090', '9191', '9292', '9393', '9494', '9595', '9696', '9797', '9898',

	# top 19 least popular 4-digit passwords:
	'7637', '6835', '9629', '8093', '8398', '0738', '9480', '6793', '8557', '9047', '8438', '0439', '9539', '8196', '7063', '6093',		 
	'6827', '7394', '0859',

	# the least commonly used password and it mirror:
	'8068', '8608',																														
	
	# corners:
	'1397', '3971', '7139', '9713', '3179', '9317', '1793', '7931',

	# vertical:
	'1470', '2580', '3690', '0963', '0852', '0741', '0147', '0258','0369', '9630', '8520', '7410',

	# diagonal:  
	'1590', '3570', '0753', '0951', '0159', '0357', '7530', '9510', 

	# square:
	'1254', '2541', '5412', '4125', '5214', '2145', '1452', '4521', '1245', '5421', '2154', '4512',
	'2365', '3652', '6523', '5236', '6325', '3256', '2563', '5632', '2356', '6532', '3265', '5623', 
	'4587', '5874', '8745', '7458', '8547', '5478', '4785', '7854', '4578', '8754', '7845', '5487', 
	'5698', '6985', '9856', '8569', '9658', '6589', '5896', '8965', '5689', '9865', '6598', '8956',
	
	# cross:
	'2684', '6842', '8426', '4268', '8624', '6248', '2486', '4862', 
	'5907', '9075', '0759', '7590', '0957', '9570', '5709', '7095', 

	# zigzag:
	'4780', '0874', '6980', '0896', '2547', '2569', '7452', '9652', '3254', '4523', '9854', '4589', '8563', '3658', '1458', '8541',
	'7856', '6587', '1256', '6521', 

	# perimeter:
	'1236', '2369', '3698', '6987', '9874', '8741', '7412', '4123', '3214', '2147', '1478', '4789', '7896', '8963', '9632', '6321',

	# closely-related:
	'1584', '5841', '8415', '4158', '8514', '5148', '1485', '4851', '2695', '6952', '9526', '5269', '9625', '6259', '2596', '5962',
	'3586', '5863', '8635', '6358', '8536', '5368', '3685', '6853', '2475', '4752', '7524', '5247', '7425', '4257', '2574', '5742',
	'1562', '5621', '6215', '2156', '6512', '5126', '1265', '2615', '2453', '4532', '5324', '3245', '5423', '4235', '2354', '3542',

	'3695', '6953', '9536', '5369', '9635', '6359', '3596', '5963',
	'1475', '4751', '7514', '5147', '7415', '4157', '1574', '5741',
	'1235', '2351', '3512', '5123', '3215', '2153', '1532', '5321', 
	'7895', '8957', '9578', '5789', '9875', '8759', '7598', '5987',
	'8907', '9078', '8709', '7098',  
	
	'1258', '3258', '8521', '8523', '1456', '6541', '0854', '4580', '6580', '0856', '3654', '4563', '7852', '2587', '9852', '2589', 
	'4569', '9654', '7580', '0857', '9580',
	
	# James-Bond:
	'0070', '0007',

	# words (that, this, your, know, what, have, love, hate, Angel (Korean), Pi[:4], Pi[1:5], pink):
	'8428', '8447', '9678', '5669', '9428', '5683', '4283', '8627', '1004', '3141', '1415', '7465',

	# year of birth with overlap:
	'1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', 
	'1916', '1917', '1918', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932',
	'1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', 
	'1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', 
	'1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', 
	'1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', 
	'1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', 
	'2013', '2014', '2015', '2016', '2017', '2018', '2019', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', 
	'2030',
	
	# commonly used pattern:
	'1122', '2233', '3344', '4455', '5566', '6677', '7788', '8899', '9900', '0099', '9988', '8877', '7766', '6655', '5544', '4433',
	'3322', '2211', '0101', '0102', '0103', '0111', '0202', '0303', '0404', '0505', '0606', '0707', '0808', '0909', '1010', '1101',
	'1102', '1103', '1112', '1123', '1201', '1202', '1203', '1210', '1211', '2229', 

	# mirrors:
	'0110', '3003', '4004', '5005', '6006', '7007', '8008', '9009', '1001', '1221', '1331', '1441', '1551', '1661', '1771', '1881',
	'2112', '2332', '2442', '2552', '2662', '2772', '2882', '2992', '3113', '3223', '3443', '3553', '3663', '3773', '3883', '3993',
	'4114', '4224', '4334', '4554', '4664', '4774', '4884', '4994', '5115', '5225', '5335', '5445', '5665', '5775', '5885', '5995',
	'6116', '6226', '6336', '6446', '6556', '6776',	'6886', '6996', '7117', '7227', '7337', '7447', '7557', '7667', '7887', '7997',
	'8118', '8228', '8338', '8448', '8558', '8668', '8778', '8998', '9119', '9229', '9339', '9449', '9559', '9669', '9779', '9889',
	 
	]


selection = set(All_PIN)-set(exclusions)

YOUR_PIN = random.choice(list(selection))

print ('------------------------')
print ('your secure PIN is: ' + YOUR_PIN)
print ('------------------------')



prompt = 'more personalized PIN, that will excludes patterns of your day of birth? Yes / No ? '

prompt_day = 'please, enter your day of birth in numbers (from 1 to 31 only): '
prompt_day_error = 'Invalid Data, ' + prompt_day[:-2]

prompt_month = 'please, enter your month of birth in numbers (from 1 to 12 only): '
prompt_month_error = 'Invalid Data, ' + prompt_month[:-2]

prompt_year = 'please, enter your year of birth in numbers (ex. 1990): '
prompt_year_error = 'Invalid Data, ' + prompt_year[:-2]



"""
Next exception is for Python 2 and Python 3 compatibility.

"""

try:
	input = raw_input
except NameError:
	pass


birth_day_range = list(range(1,32))
birth_month_range = list(range(1,13))
birth_year_range = list(range(1900,2017))

"""
Next functions check the input data, 
that returns its only if data in appropriate view and range.
"""

def check_day(number):
	number = None
	global prompt_day, prompt_day_error
	while not number:
		try:
			number = int(input(prompt_day))
		except ValueError:
			print (prompt_day_error)
	if number in birth_day_range:
		prompt_day = number
		return prompt_day
	else:
		check_day(number)

def check_month(number):
	number = None
	global prompt_month, prompt_month_error
	while not number:
		try:
			number = int(input(prompt_month))
		except ValueError:
			print (prompt_month_error)
	if number in birth_month_range:
		prompt_month = number
		return prompt_month
	else:
		check_month(number)

def check_year(number):
	number = None
	global prompt_year, prompt_year_error
	while not number:
		try:
			number = int(input(prompt_year))
		except ValueError:
			print (prompt_year_error)
	if number in birth_year_range:
		prompt_year = number
		return prompt_year
	else:
		check_year(number)



def pin_constructor(day, month, year):
	"""
	This function construct the PIN on base of user input.
	"""
	if len(day) and len(month) == 2:
		return  day+month, month+day, day+(year)[2:], month+(year)[2:], year, year[::-1], (year)[2:]+day,(year)[2:]+month
	elif len(day) and len(month) == 1:
		return '0'+day+'0'+month, '0'+month+"0"+day, "0"+day+(year)[2:], "0"+month+(year)[2:], year, year[::-1], (year)[2:]+"0"+day, (year)[2:]+'0'+month, day+month+(year)[2:], month+day+(year)[2:], (year)[2:]+month+day, (year)[2:]+day+month
	elif len(day) == 1 and len(month) == 2:
		return '0'+day+month, month+"0"+day, "0"+day+(year)[2:], month+(year)[2:], year, year[::-1], (year)[2:]+"0"+day, (year)[2:]+month
	else:
		return day+'0'+month, '0'+month+day, day+(year)[2:], "0"+month+(year)[2:], year, year[::-1], (year)[2:]+day, (year)[2:]+'0'+month



def personal_pin(answer):
	answer = input(prompt)
	if answer in ['y', 'Y', 'yes', 'YES', 'Yes', 'ye']:
		check_day(prompt_day)
		check_month(prompt_month)
		check_year(prompt_year)
		day = str(prompt_day)
		month = str(prompt_month)
		year = str(prompt_year)
		pin_user = pin_constructor(day, month, year)
		personalized_selection = selection - set(pin_user)
		YOUR_PERSONAL_PIN = random.choice(list(personalized_selection))
		print ('------------------------')
		print 'your personal secure PIN is: ' + str(YOUR_PERSONAL_PIN)
		print ('------------------------')
	else:
		print ('------------------------')
		print 'your secure PIN is: ' + str(YOUR_PIN)
		print ('------------------------')

personal_pin(prompt)
