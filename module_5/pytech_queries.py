#Sisler - Module 5.3 Assignment
#pytech_queries.py
#Query Student Documents
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.h1wgd.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list=students.find({})
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
matt = students.find_one({"student_id": "1007"})    
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + matt["student_id"] + "\n  First Name: " + matt["first_name"] + "\n  Last Name: " + matt["last_name"] + "\n")
input("End of Program. Press any key to continue")