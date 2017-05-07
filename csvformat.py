import csv


 #gives coords of school
def locatecoords(school):
	return {

		"Stanford" : [0,0],
		"Harvard" : [1,2],
		"UCLA" : [5,6]
	}.get(school,"null")

#checks if schools are in list
def checklist(school, list):
	counter = 0
	for i in list:
		if i.keys()[0] == school:
			return counter
		counter+=1
	
	return -1


print("var SchoolData = [")
colleges = []

with open('form.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	
	for row in spamreader:	
		# organizes people by college
		numoflist=checklist(row[5], colleges)
		if numoflist != -1:
			colleges[numoflist][row[5]].append(row[1]+" "+row[2])
		else:
			colleges.append({row[5]:[row[1]+" "+row[2]]})
		#coordinates of people
 	for college in colleges:
 		strcollege = college.keys()[0]
 		college['coordinates'] = locatecoords(strcollege)
 		print("{'coordinate': "+str(college['coordinates'])
 			+", 'collegeName': '"+strcollege
 			+"', 'students': "+str(college[strcollege])+"},")
 	
print("];")
	 		# for col in row:
