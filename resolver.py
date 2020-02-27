import json

student = [
    {
        "student_id": "1",
        "name": "Jack",
        "course_name": "CMPE202"
    },
    {
        "student_id": "2",
        "name": "Mark",
        "course_name": "CMPE272"
    }
]

classes = [
    {
        "class_id": 202,
        "course_name": "CMPE202",
        "students": [
        {
            "student_id": 1,
            "name": "Tom",
            "course_name": "CMPE202"
        }
        ]
    }
] 

def get_student(_, info, student_id):
    print("Students",student)
    studs = [stu for stu in student if stu["student_id"] == student_id]    
    return studs[0]

def get_class(_, info, class_id):
    clas = [clas for clas in classes if clas["class_id"] == int(class_id)]    
    return clas[0]

def create_student(_, info, student_id, name, course_name):
    global student
    student.append({'student_id' : student_id, 'name': name, 'course_name':course_name})
    return student

def create_class(_, info, class_id, course_name):
    global classes 
    classes.append({"class_id":class_id, "course_name":course_name, "students": []})
    return classes

def update_class(_, info, class_id, course_name):
    for j in classes:
        print("Class_id",class_id)
        print("Class_id inttt",int(class_id))
        if j["class_id"] == class_id:
            print("Inside ")
            j["course_name"] = course_name
            clas = j
            break
    return clas

def update_student_class(_, info, class_id, student_id):
    students = [st for st in student if st["student_id"] == student_id]
    for j in classes:
        if j["class_id"] == int(class_id):
            clas = j
            break
    clas["students"].append(students[0])
    return clas