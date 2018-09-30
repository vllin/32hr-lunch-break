import csv, requests
api_key = "AIzaSyDUXIaiOOfkoIVk5tWIBKV_FmndAj_hfOs"
with open('College and Population.csv') as Cpop:
	reader = csv.reader(Cpop, delimiter=',')
	d = {}
	j = 0
	for row in reader:
		print(j)
		j += 1
		payload = {'key': api_key, 'input': row[0], 'inputtype': 'textquery'}
		r = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json', params = payload)
		if(len(r.json()["candidates"]) == 0):
			continue
		payload2 = {'key': api_key, 'placeid': r.json()["candidates"][0]["place_id"]}
		r2 = requests.get('https://maps.googleapis.com/maps/api/place/details/json', params = payload2)
		i = 0
		while(r2.json()["result"]["address_components"][i]["types"][0] != "administrative_area_level_1"):
			i+=1
			if len(r2.json()["result"]["address_components"]) <= i:
				break
		if len(r2.json()["result"]["address_components"]) <= i:
			continue
		check = False
		for key in d.keys():
			if key == r2.json()["result"]["address_components"][i]["long_name"]:
				d[r2.json()["result"]["address_components"][i]["long_name"]] += row[1]	
				check = True
		if(check == False):
			d[r2.json()["result"]["address_components"][i]["long_name"]] = row[1]
	with open('Edited College and Population.csv', 'w') as edi:
		reader2 = csv.writer(edi)
		for key in d.keys():
			reader2.writerow([key, d[key]])
		