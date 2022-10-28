from numpy import True_
from flask_server import db


class Teacher(db.Model):
    Teacher_id = db.Column('Teacher_id',db.Integer(), primary_key=True)
    First_name=db.Column(db.String(length=123),nullable=False)
    Last_name=db.Column(db.String(length=123),nullable=False)
    Department = db.Column(db.String(length=123),nullable=False)
    def __repr__(self):
        return f"Teacher Id : {self.Teacher_id} \n Name : {self.first_name} {self.last_name}"
        
class Courses(db.Model):
    Course_id = db.Column('Course_id',db.Integer(),primary_key=True)
    Name = db.Column(db.String(length=123),nullable=False)
    Syllabus = db.Column(db.LargeBinary())
    Duration = db.Column(db.String(length=123),nullable=False)
    def __repr__(self):
        return f"Course Id : {self.Course_id} \n Name : {self.Name} "

class Student(db.Model):
    Student_id =db.Column('Student_id',db.Integer(),primary_key=True)
    Student_name =db.Column(db.String(length=123),nullable=False)
    Course = db.Column(db.Foreignkey())
    CGPA = db.Column(db.String(length=123))
    def __repr_(self):
        return f"Student Id :{self.Student_id} \n Name : {self.Student_name} "

class Holidays(db.Model):
    id = db.Column('holiday_id',db.Integer(), primary_key=True)
    year=db.Column(db.Integer(),nullable=False)
    file_name=db.Column(db.String(length=123),nullable=False)
    data=db.Column(db.LargeBinary())

    def __repr__(self):
        return f"Holidays ID : {self.id} for year : {self.year}"


