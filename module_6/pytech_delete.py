#Sisler - Module 6.3 Assignment
#pytech_delete.py
#Deleting Student Documents
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

clint = {
    "student_id": "1010",
    "first_name": "Clint",
    "last_name": "Eastwood"
}

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
clint_student_id = students.insert_one(clint).inserted_id
print("  Inserted student record Clint Eastwood into the students collection with document_id " + str(clint_student_id))


# find_one() method for 1010
student_clint = students.find_one({"student_id": "1010"})

print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_clint["student_id"] + "\n  First Name: " + student_clint["first_name"] + "\n  Last Name: " + student_clint["last_name"] + "\n")

#delete_one method 
delete_clint = students.delete_one({"student_id": "1010"})

# find() method to display students in the collection 
student_list=students.find({})
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
