
import json
import codecs
#with codecs.open(filename,'r',encoding='utf8') as f:
#Va = u'\u221220'
#float(a.replace(u'\N{MINUS SIGN}', '-'))
#a = u'\u221220'
#float(a.replace(u'\N{MINUS SIGN}', '-'))

#f = open('_Installation.json','r+b')
with codecs.open('_Installation.json','r',encoding ='utf8') as f:
	x = json.load(f)
x_values  = x.values()[0]
x_list = []
final_dict = {}
value1 = 0

print(type(x_list))

print(x_values[0]["appVersion"])

for cnt in range(len(x_values)):
	#x_temp = x_values[cnt]["appVersion"]
	# float(x_temp.replace(x_temp,'-'))
	#print(float(x_temp))

	#x_list.append(x_values[cnt]["appVersion"])
	#float(x_list[cnt])
	x_list.append(float(x_values[cnt]["appVersion"]))
	#print(x_list[cnt])
	# print(type(x_list[cnt]),x_list[cnt],cnt+1)

	#print(x_values[cnt]["appVersion"])
	#x_list[cnt] = x_list.insert(len(x_values),x_values[cnt]["appVersion"])
	x_list.sort()
for cnt_list in range(len(x_list)):
	if(cnt_list == 0):
		value1 = 1
		print(value1,x_list[cnt_list],final_dict)
	elif(x_list[cnt_list] == x_list[cnt_list+1]):
		value1 += 1
		print(value1,x_list[cnt_list],final_dict)
	elif((x_list[cnt_list]<x_list[cnt_list+1]) or (x_list[cnt_list]>x_list[cnt_list+1])):
		value1 += 1
		final_dict = {x_list[cnt_list] : value1}
		value1 = 0
		print(value1,x_list[cnt_list],final_dict)
	elif(cnt_list == len(x_list)):
		value1 += 1
		final_dict = {x_list[cnt_list] : value1}
		value1 = 0
		print(value1,x_list[cnt_list],final_dict)
#print(type(x_list),final_dict)


