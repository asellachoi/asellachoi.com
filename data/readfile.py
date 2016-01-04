# -*- coding: utf8 -*-
import json
import codecs
import sys
import csv
#with codecs.open(filename,'r',encoding='utf8') as f:
#Va = u'\u221220'
#float(a.replace(u'\N{MINUS SIGN}', '-'))
#a = u'\u221220'
#float(a.replace(u'\N{MINUS SIGN}', '-'))
#writer = csv.writer(open("/path/to/my/csv/file", 'w'))
#f = open('_Installation.json','r+b')

with codecs.open('2014_internet_shopping_eval.json','r') as f:
	x = json.load(f)
#print(x)
actual_list = x["DATA"]

final_data=[]
final_data.append('shop')
final_data.append('total')
final_data.append("{ role: 'style' }")

#print(actual_list, len(actual_list))
writer=csv.writer(open('final_data.csv','w'))
writer.writerow(final_data)
for i in range(len(actual_list)):
	final_list=[]
	shop_name=actual_list[i]["SHOP_NAME"]
	avr_total=actual_list[i]["AVR_TOTAL"]
	print(type(avr_total), avr_total)
	final_list.append(shop_name)
	final_list.append(avr_total)
	if(float(actual_list[i]["AVR_TOTAL"])<=75):
		final_list.append('color:#FF0000')
	else:
		final_list.append('color:green')
	final_data.append(final_list)
	print(final_list)
	writer.writerow(final_list)
#print(final_data)


