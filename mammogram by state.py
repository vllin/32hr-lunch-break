import csv
with open('highblood.csv') as filecsv:
	reader = csv.reader(filecsv, delimiter=',')
	d={}
	d2={}
	i = 0
	for row in reader:
		if row[1] == 'DC' or row[2] == 'United States':
			continue
		if i == 0:
			i+=1
			continue
		check = False
		for key in d.keys():
			if key == row[2]:
				d2[key] += 1
				d[key] += float(row[12])
				check = True
		if check == False:
			d2[row[2]] = 1
			d[row[2]] = float(row[12])
	with open('highblood by State.csv', 'w') as edi:
		reader2 = csv.writer(edi)
		for key in d.keys():
			reader2.writerow([key, d[key]/d2[key]])
