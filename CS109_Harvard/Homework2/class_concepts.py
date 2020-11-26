#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:23:23 2020

@author: shadrack
"""


class Student:
    """ class instance contains names, age, grades, count_students, display """
    count_students = 0 # class attribute
    def __init__(self,name,age,grades):
        self.name = name # instance attributes
        self.age = age
        self.grades = grades
        Student.count_students += 1
    def display(self): # instance function
        print("{}. Student {}, is {} years young, secured {} in science".format(Student.count_students,self.name,self.age,self.grades))

class Courses:
    """ class contains name, max_students, add_students, get_grades """
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_students(self,student):
        if (len(self.students) < self.max_students):
            self.students.append(student) # courses class interacts with students class
        return False
    def get_grades(self,student): 
        print(student.grades) # courses class interacts with students class but not vice versa
        
s1=Student("jabes",35,60)
s1.display()
s2=Student("manu",29,90)
s2.display()
c=Courses("science",2)
c.add_students(s1)
c.add_students(s2)
c.get_grades(s1)

class Animals:
    nanimals = []
    def __init__(self,name,age,typ): 
        self.name = name
        self.age = age
        self.typ = typ
        Animals.add_animals(name)
        
    @classmethod
    def add_animals(cls,name):
        cls.nanimals.append(name)
        
    def display(self):
        print("{}. the name of the {} is {}, aged {}".format(len(Animals.nanimals),self.typ,self.name,self.age) )

class Cats(Animals): # inheritance from parent class Animals
    def speak(self):
        print("Meow")

class Dogs(Animals):
    def speak(self):
        print("Bark")

a1=Animals("dudu",4,"dog")
a1.display()
a2=Animals("jillu",5,"cat")
a2.display()
a3=Animals("cheeta",2,"cat")
a3.display()
a4=Animals("tinka",5,"cat")
a4.display()
a5=Animals("tally",7,"cat")
a5.display()

d1 = Dogs("dudu",4,"dog")
d1.speak()
d2 = Cats("jillu",5,"cat")
d2.speak()

