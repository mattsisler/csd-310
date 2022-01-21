#Sisler - Module 6.2 Assignment
#pytech_update.py
#Updating Student Documents
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.h1wgd.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# get the students collection 
students = db.students

student_list=students.find({})
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#update_one method for 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Davidson"}})

#find_one method for 1007
matt = students.find_one({"student_id": "1007"})

print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

#display the updated document for 1007
print("  Student ID: " + matt["student_id"] + "\n  First Name: " + matt["first_name"] + "\n  Last Name: " + matt["last_name"] + "\n")

input("End of Program. Press any key to continue")

