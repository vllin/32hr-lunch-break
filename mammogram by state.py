import csv
with open('Diagnosed chronic obstructive pulmonary .csv') as filecsv:
	reader = csv.reader(filecsv, delimiter=',')
	d={}
	d2={}
	i = 0
	for row in reader:
		if row[2] == 'DC' or row[3] == 'United States' or row[3] == 'Guam' or row[3] == 'Virgin Islands' or row[3] == 'Puerto Rico' or row[10] == '':
			continue
		if i == 0:
			i+=1
			continue
		check = False
		for key in d.keys():
			if key == row[3]:
				d2[key] += 1
				d[key] += float(row[10])
				check = True
		if check == False:
			d2[row[3]] = 1
			d[row[3]] = float(row[10])
	with open('Diagnosed chronic obstructive pulmonary  by State.csv', 'w') as edi:
		reader2 = csv.writer(edi)
		for key in d.keys():
			reader2.writerow([key, d[key]/d2[key]])
