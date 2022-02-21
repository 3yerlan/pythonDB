print(" Module organizations is imported successfully")
import csv
import os.path
try:
    from education.users import * # при запуске на прямую выдает ошибку
except:
    from users import *


class School:
    def __init__(self,name=None,address=None,phone=None,email=None,num_stud=0,num_teachers=0):
        self.name=name
        self.address=address
        self.phone=phone
        self.email=email
        self.num_stud=num_stud
        self.num_teachers=num_teachers
        self.list_of_stud=[]
        self.list_of_teachers=[]
        self.unique=set()
        self.load_data()


    def load_data(self):
        if not os.path.exists('{}.csv'.format(self.name)):
            return
        file=open('{}.csv'.format(self.name),'r')
        data=list(csv.reader(file,delimiter="|",skipinitialspace=True))
        
        nt=int(data[1][5])
        for i in range(3,nt+3):
            self.unique.add((data[i][0],data[i][1]))
            self.list_of_teachers.append(Teacher(name=data[i][0],familyname=data[i][1],age=data[i][2],gender=data[i][3],nationality=data[i][4],classroom=data[i][5],subject=data[i][6]))
            self.num_teachers+=1
            print("teacher %s %s loaded" % (data[i][0],data[i][1]))
        
        beg=nt+3
        end=beg+int(data[1][4])
        for i in range(beg,end):
            nm=data[i][0]
            fnm=data[i][1]
            self.unique.add((nm,fnm))
            
            sj=data[i][6] # при загрузке список становится строкой
            if '[' in sj:
                sj=eval(sj)
            
            self.list_of_stud.append(Student(name=nm,familyname=fnm,age=data[i][2],gender=data[i][3],nationality=data[i][4],classroom=data[i][5],subject=sj))
            self.num_stud+=1
            print("student %s %s loaded" % (data[i][0],data[i][1]))


    def set_name(self,name):
        self.name=name
    def set_address(self,address):
        self.address=address
    def set_phone(self,phone):
        self.phone=phone
    def set_email(self,email):
        self.email=email
    def set_num_stud(self,num_stud):
        self.num_stud=num_stud
    def set_num_teachers(self,num_teachers):
        self.num_teachers=num_teachers


    def add_student(self,name=None,familyname=None,age=None,gender=None,nationality=None,classroom=None,subject=None):
        nf=(name,familyname)
        if nf in self.unique:
            print("student %s %s not added" % nf)
        else:
            print("student %s %s added" % nf)
            self.unique.add((name,familyname))
            self.list_of_stud.append(Student(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality, classroom=classroom, subject=subject))
            self.num_stud+=1
        
    def add_teacher(self,name=None,familyname=None,age=None,gender=None,nationality=None,classroom=None,subject=None):
        nf=(name,familyname)
        if nf in self.unique:
            print("teacher %s %s not added" % nf)
        else:
            print("teacher %s %s added" % nf)
            self.unique.add((name,familyname))
            self.list_of_teachers.append(Teacher(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality, classroom=classroom, subject=subject))
            self.num_teachers+=1


    def get_info(self):
        return {'name':self.name,'address':self.address,'phone':self.phone,'email':self.email,'num_stud':self.num_stud,'num_teachers':self.num_teachers}


    def get_report(self):
        filename = f'{self.name}.csv'
        fields1 = ['name','address','phone','email','num_stud','num_teachers'] 
        fields2 = ['name','familyname','age','gender','nationality','classroom','subject']

        with open(filename, 'w', newline='') as csvfile:         
            writers = csv.DictWriter(csvfile, fieldnames = fields1, delimiter="|") 
            writers.writeheader() 
            writers.writerow(self.get_info()) 
            
            writerh = csv.DictWriter(csvfile, fieldnames = fields2, delimiter="|")
            writerh.writeheader()
            for i in self.list_of_teachers:
                writerh.writerow(i.get_info())
            for i in self.list_of_stud:
                writerh.writerow(i.get_info())
        print('Done')



