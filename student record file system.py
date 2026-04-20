#student record system using file handling
import csv

'''
#creating the csv file

with open("student record file.csv","w",newline='')as csvfile:
 write=csv.writer(csvfile)
 write.writerow(["Name","Roll no","class"])
 write.writerow(["abhi",1,"Data analytics"])
'''
'''
# adding the new content to the file
fieldnames = ["Name","Roll no","class"]
new_row=[
    {'Name':"mohith", 'Roll no':2,'class': "Engineering"},
    {'Name':"gayan",'Roll no': 3,'class': "MBA"}

]
try:
 with open("student record file.csv","a",newline="") as csvfile:
  writer =csv.DictWriter(csvfile,fieldnames=fieldnames)
  writer.writerows(new_row)

 print(f"file successfully appended!!{len(new_row)}rows")

except Exception as e:
 print(e)
'''

'''
#reading the file
try:
 with open("student record file.csv","r") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
   print(row)

except FileNotFoundError:
 print("csv file not found")

except Exception as e:
 print(e)
'''







