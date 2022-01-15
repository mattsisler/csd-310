#Sisler - Module 5.3 Assignment
#pytech_insert.py
#Insert New Student Documents
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.h1wgd.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

matt = {
    "student_id": "1007",
    "first_name": "Matt",
    "last_name": "Sisler",
    "enrollments": [
        {
            "term": "Fall",
            "gpa": "3.9",
            "start_date": "October 10, 2020",
            "end_date": "November 26, 2022",
            "courses": [
                {
                    "course_id": "CIS 245",
                    "description": "Introduction to Python",
                    "instructor": "Robert Kumar",
                    "grade": "A"
                },
                {
                    "course_id": "CYBR 250",
                    "description": "Introduction to Cyber Threats",
                    "instructor": "Mike Woodall",
                    "grade": "A+"
                }
            ]
        }
    ]

}

jim = {
    "student_id": "1008",
    "first_name": "Jim",
    "last_name": "Smith",
    "enrollments": [
        {
            "term": "Fall",
            "gpa": "3.1",
            "start_date": "October 10, 2020",
            "end_date": "November 26, 2022",
            "courses": [
                {
                    "course_id": "CIS 245",
                    "description": "Introduction to Python",
                    "instructor": "Robert Kumar",
                    "grade": "A"
                },
                {
                    "course_id": "CYBR 250",
                    "description": "Introduction to Cyber Threats",
                    "instructor": "Mike Woodall",
                    "grade": "A"
                }
            ]
        }
    ]

}

susan = {
    "student_id": "1009",
    "first_name": "Susan",
    "last_name": "Brown",
    "enrollments": [
        {
            "term": "Fall",
            "gpa": "3.9",
            "start_date": "October 10, 2020",
            "end_date": "November 26, 2022",
            "courses": [
                {
                    "course_id": "CIS 245",
                    "description": "Introduction to Python",
                    "instructor": "Robert Kumar",
                    "grade": "B"
                },
                {
                    "course_id": "CYBR 250",
                    "description": "Introduction to Cyber Threats",
                    "instructor": "Mike Woodall",
                    "grade": "A"
                }
            ]
        }
    ]

}

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
matt_student_id = students.insert_one(matt).inserted_id
print("  Inserted student record Matt Sisler into the students collection with document_id " + str(matt_student_id))

jim_student_id = students.insert_one(jim).inserted_id
print("  Inserted student record Jim Smith into the students collection with document_id " + str(jim_student_id))

susan_student_id = students.insert_one(susan).inserted_id
print("  Inserted student record Susan Brown into the students collection with document_id " + str(susan_student_id))
input("End of Program. Press any key to continue")
