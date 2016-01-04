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
csv_file=[]
data_total=[]
location_total=[]
#location_by_country=[]
location=[]
#location=[]
cnt = 0
with codecs.open('Seoul_foreigners_citizenship_status.csv','r') as f:
	reader = csv.reader(f)
	for i in reader:
		csv_file.append(i)
	for j in range(len(csv_file)):	
		data= []
		data.append(csv_file[j][1])
		data.append(csv_file[j][2])
		data.append(csv_file[j][4])
		data_total.append(data)
		#print(data[j])

#list.sort(data_total)
	data_total.sort()
	#print(data_total)

	
	for csv_i in range(len(data_total)):
		#
		writer=csv.writer(open('final_data_seoul_'+data_total[csv_i-1][0]+'.csv','w'))
		if(csv_i == 0):
			#location=[]
			#location.append(data_total[csv_i])
			cnt = 1
			#print('first',data_total[csv_i][1],cnt)
		elif(csv_i > 0): 
			if(data_total[csv_i-1][0]==data_total[csv_i][0]):	
				
				
				#location=[]
				#location.append(data_total[csv_i])
				if(data_total[csv_i-1][1]==data_total[csv_i][1]):
					cnt += 1
				elif(data_total[csv_i-1][1]!=data_total[csv_i][1]):	
					location_by_country=[]
					location_by_country.append(data_total[csv_i-1][0])
					location_by_country.append(data_total[csv_i-1][1])
					location_by_country.append(cnt)
					location.append(location_by_country)
					
					
					cnt = 1
					
					print(location_by_country)
				#print(cnt)

			elif(data_total[csv_i-1][0]!=data_total[csv_i][0]):
				writer.writerow(location)
				location=[]
				#location.append(location_by_country)
				#location.append(data_total[csv_i-1][0])
				#location.append(cnt)
				#location_total.append(location)
	
				#location =[]

			elif(csv_i == (len(data_total)-1)):
				print('what the fuck')
				#location=[]
			#cnt = 1
	# Write down the last file
	writer.writerow(location)

	print(location_total)
# print(cnt,len(csv_file))

#print(reader)

