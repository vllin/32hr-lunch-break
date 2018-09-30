import csv
d = {}
with open('alcohol.csv') as alc:
	reader = csv.reader(alc, delimiter=',')
	for row in reader:
		if d[row[0]] > 0:
			d[row[0]] += row[5]
		else:
			d[row[0]] = row[5]
		
