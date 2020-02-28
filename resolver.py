import json
import random

student = []
classes = []

def students(_, info, student_id):
    studs = [stu for stu in student if stu["student_id"] == int(student_id)]    
    return studs[0]

def classess(_, info, class_id):
    clas = [clas for clas in classes if clas["class_id"] == int(class_id)]    
    return clas[0]

def create_student(_, info, name):
    student_id = random.randint(1,10000)
    student.append({'student_id' : student_id, 'name': name})
    return student

def create_class(_, info, course_name):
    class_id = random.randint(200,1000)
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
    students = [st for st in student if st["student_id"] == int(student_id)]
    for j in classes:
        if j["class_id"] == int(class_id):
            clas = j
            break
    clas["students"].append(students[0])
    return clas