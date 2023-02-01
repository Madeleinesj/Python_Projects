# Parent class instance
class Human():
    name = ''
    species = ''
    legs = 2
    arms = 2
    origin = "Earth"

    def information(self):
        msg = "\nName: {},\nSpecies: {}\nLegs: {}\nArms: {}\nOrigin: {}".format(self.name,self.species,self.legs,self.arms,self.origin)
        return msg

   

# Child class instance
class Teacher(Human):
    name = 'Tom'
    species = 'Homosapien'
    age = 30
    specialty = 'German'
    
  
    
    def teaching(self):
        msg = "\nSpends most of the day teaching their students about the world and how to succeed in it."
        return msg
        
# Child class instance
class Student(Human):
    name = 'Fred'
    species = 'Homosapien'
    major = 'Biology'
    minor = 'History'

    
    def study(self):
        msg = "\nWorks day and night on homework to ace final exam!"
        print(msg)


if __name__ == "__main__":
    
     teacher = Teacher()
     
     print(teacher.information())
     print(teacher.teaching())
    
     

     student = Student()
     
     print(student.information())
     print(student.study())
