print("Module users is imported successfully")

class Human:
    def __init__(self,name=None,familyname=None,age=None,gender=None,nationality=None):
        self.name=name
        self.familyname=familyname
        self.age=age
        self.gender=gender
        self.nationality=nationality

    def set_name(self,name):
        self.name=name
    def set_family(self,familyname):
        self.familyname=familyname
    def set_age(self,age):
        self.age=age
    def set_gender(self,gender):
        self.gender=gender
    def set_nationality(self,nationality):
        self.nationality=nationality
    
    
class Student(Human):
    def __init__(self,name=None,familyname=None,age=None,gender=None,nationality=None,classroom=None,subject=None):
        Human.__init__(self,name=name,familyname=familyname,age=age,gender=gender,nationality=nationality)
        self.classroom=classroom
        self.subject=[]
        if subject and type(subject)==list:
            self.subject+=subject
        if subject and type(subject)==str:
            self.subject.append(subject)

    def set_classroom(self,classroom):
        self.classroom=classroom
    def add_subject(self,*args):
        for s in args:
            self.subject.append(s)
    
    def get_info(self):
        return {'name':self.name,'familyname':self.familyname,'age':self.age,'gender':self.gender,'nationality':self.nationality,'classroom':self.classroom,'subject':self.subject}


class Teacher(Human):
    def __init__(self,name=None,familyname=None,age=None,gender=None,nationality=None,classroom=None,subject=None):
        Human.__init__(self, name=name, familyname=familyname, age=age, gender=gender, nationality=nationality)
        self.classroom=classroom
        self.subject=subject

    def set_classroom(self,classroom):
        self.classroom=classroom
    def add_subject(self,subject):
        self.subject=subject
    
    def get_info(self):
        return {'name':self.name,'familyname':self.familyname,'age':self.age,'gender':self.gender,'nationality':self.nationality,'classroom':self.classroom,'subject':self.subject}


